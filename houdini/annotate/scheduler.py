"""Decide when the annotation workflow should run, from the clock and the live plan usage.

    scheduler.py wait     exits (printing START) once the workflow should start, in the next window
    scheduler.py watch [TRANSCRIPT_DIR [SHARE]]
                          exits (printing STOP) once the running workflow should pause; SHARE
                          overrides tonight's share, in percent of the week, the budget line
                          and the window

The workflow runs overnight, between WINDOW_START and WINDOW_END, while weekly usage stays
below a budget line that reserves RESERVE_PER_DAY percent of the week for each day left before
the weekly reset, plus SAFETY percent. What is left above that line is shared equally between
the nights before the reset, so one night cannot spend the whole week's allowance.

The status line only receives new rate limits when its own session makes a request, so while
that session sits idle the usage file can repeat an old reading. Given the workflow's transcript
directory, `watch` also estimates the night's usage from its agents' token counts, and goes by
whichever figure is higher. Usage is read from ~/.claude/usage-latest.json, which
the status line script (~/.claude/statusline-usage.sh) refreshes every minute.
"""

import datetime
import json
import pathlib
import sys
import time

USAGE_FILE = pathlib.Path.home() / ".claude" / "usage-latest.json"
WINDOW_START = datetime.time(22, 0)
WINDOW_END = datetime.time(7, 0)
RESERVE_PER_DAY = 6.0
SAFETY = 5.0
POLL_SECONDS = 60
STALE_SECONDS = 15 * 60
# Weighted token units (input 1, output 5, cache write 1.25, cache read 0.1) per percent of the
# weekly limit, as measured on this plan; on the low side, so the estimate errs towards pausing.
UNITS_PER_PERCENT = 3.0e6
# Don't start a night with less than this to spend: an agent cut off mid-batch is wasted.
MIN_NIGHT = 1.0


def in_window(now: datetime.datetime) -> bool:
    t = now.time()
    return t >= WINDOW_START or t < WINDOW_END


def usage() -> tuple[float, float, float]:
    """Weekly percent used, the budget line, and the age of the usage data in seconds."""
    data = json.loads(USAGE_FILE.read_text())["rate_limits"]["seven_day"]
    days_left = max(0.0, (data["resets_at"] - time.time()) / 86400)
    limit = 100 - SAFETY - RESERVE_PER_DAY * days_left
    age = time.time() - USAGE_FILE.stat().st_mtime
    return float(data["used_percentage"]), limit, age


def nights_left(now: datetime.datetime, resets_at: float) -> int:
    """Overnight windows that start before the weekly reset, counting the current one."""
    start = datetime.datetime.combine(now.date(), WINDOW_START)
    if now.time() < WINDOW_END:
        start -= datetime.timedelta(days=1)
    count = 0
    while start.timestamp() < resets_at:
        count += 1
        start += datetime.timedelta(days=1)
    return max(1, count)


def night_limit(now: datetime.datetime) -> float:
    """The usage at which tonight's share of the week's allowance is spent."""
    data = json.loads(USAGE_FILE.read_text())["rate_limits"]["seven_day"]
    used, limit, _ = usage()
    return used + max(0.0, limit - used) / nights_left(now, data["resets_at"])


def agent_units(transcripts: pathlib.Path, since: float) -> float:
    """Weighted tokens the workflow's agents have used since `since`."""
    usages = {}
    for path in transcripts.glob("agent-*.jsonl"):
        if path.stat().st_mtime < since:
            continue
        with path.open() as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    message = entry.get("message") or {}
                    when = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                except (ValueError, KeyError, AttributeError):
                    continue
                # A message's usage is repeated on each of its content blocks' entries.
                if message.get("usage") and when.timestamp() >= since:
                    usages[message.get("id") or entry.get("uuid")] = message["usage"]
    return sum(
        u.get("input_tokens", 0)
        + 5 * u.get("output_tokens", 0)
        + 1.25 * u.get("cache_creation_input_tokens", 0)
        + 0.1 * u.get("cache_read_input_tokens", 0)
        for u in usages.values()
    )


def status() -> str:
    try:
        used, limit, age = usage()
    except (OSError, KeyError, ValueError) as exc:
        return f"usage unreadable ({exc})"
    return f"week {used:.0f}% (budget line {limit:.0f}%), usage data {age:.0f}s old"


def wait() -> None:
    # Started inside a window means tonight's run was just paused; wait for the next window.
    while in_window(datetime.datetime.now()):
        time.sleep(POLL_SECONDS)
    while True:
        now = datetime.datetime.now()
        if in_window(now):
            try:
                used, limit, age = usage()
            except (OSError, KeyError, ValueError):
                used = limit = age = None
            if used is not None and age < STALE_SECONDS and used + MIN_NIGHT <= limit:
                print(f"START at {now:%a %H:%M}: {status()}", flush=True)
                return
        time.sleep(POLL_SECONDS)


def watch(transcripts: pathlib.Path | None, share: float | None = None) -> None:
    started = time.time()
    try:
        start_used = usage()[0]
        tonight = start_used + share if share is not None else night_limit(datetime.datetime.now())
    except (OSError, KeyError, ValueError) as exc:
        print(f"STOP: cannot read usage ({exc})", flush=True)
        return
    print(f"watching: tonight's share ends at {tonight:.0f}%; {status()}", flush=True)
    last_read = time.time()
    last_good = start_used, usage()[1]
    while True:
        now = datetime.datetime.now()
        if not in_window(now) and share is None:
            print(f"STOP at {now:%a %H:%M}: overnight window over; {status()}", flush=True)
            return
        try:
            used, limit, age = usage()
            last_read = time.time()
            last_good = used, limit
        except (OSError, KeyError, ValueError) as exc:
            if transcripts is not None:
                # The token estimate still tracks the run; go on from the last good reading.
                (used, limit), age = last_good, 0.0
            # A read can catch the file mid-update; only give up once it has failed for a while.
            elif time.time() - last_read > STALE_SECONDS:
                print(f"STOP at {now:%a %H:%M}: cannot read usage ({exc})", flush=True)
                return
            else:
                time.sleep(POLL_SECONDS)
                continue
        if transcripts is not None:
            estimate = start_used + agent_units(transcripts, started) / UNITS_PER_PERCENT
            if estimate > used:
                used = estimate
        if used >= limit and share is None:
            print(f"STOP at {now:%a %H:%M}: budget reached; {status()}", flush=True)
            return
        if used >= tonight:
            print(f"STOP at {now:%a %H:%M}: tonight's share ({tonight:.0f}%) spent (at {used:.0f}%); {status()}", flush=True)
            return
        if age > STALE_SECONDS:
            print(f"STOP at {now:%a %H:%M}: usage data is stale; {status()}", flush=True)
            return
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    if sys.argv[1] == "wait":
        wait()
    else:
        watch(
            pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else None,
            float(sys.argv[3]) if len(sys.argv) > 3 else None,
        )

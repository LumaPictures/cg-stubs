#! /bin/bash

set -e

if [[ -z $@ ]]
then
    echo "$(basename $0): Missing arguments"
    exit 1
fi

if [[ ! -x $(which $1) ]]
then
    echo "$(basename $0): Argument $1 is not a valid executable"
    exit 1
fi

# Allow an explicit display to be specified with an environment
# variable, otherwise default to `:2`.
if [[ -n $XINITRUNNER_DEFAULT_DISPLAY ]]
then
    display=$XINITRUNNER_DEFAULT_DISPLAY
else
    display=:2
fi

# Only start a new X server if $DISPLAY is not already set. This way,
# we can use this script in an environment with a running X server
# without worrying about display collisions or unnecessary processes.
if [[ -z $DISPLAY ]]
then
    # Default to killing all children of this bash shell on the way out
    sigterm_kill_parent=$BASHPID


    _cleanup_kill_xserver() {
        # SIGTERM the children of the `xinit` process, which will be
        # the X server process and the blocking `sleep` spawned below.
        pkill -P $sigterm_kill_parent

        # Wait 5 seconds for the children to exit, and then SIGKILL
        # them if they don't.
        for i in {1..5}
        do
            sleep 1
            if ! pgrep -P $sigterm_kill_parent
            then
                # All child processes have exited
                return 0
            fi
        done

        pkill -KILL -P $sigterm_kill_parent
    }

    trap _cleanup_kill_xserver EXIT

    echo "[$(basename $0)] Launching X using DISPLAY $display"

    # Look for Xvfb and use it if it's available.
    if [[ -x /usr/bin/Xvfb ]]
    then
        /usr/bin/Xvfb $display &
    else
        # Start an X server in the background on our alternate display,
        # with a target command that will run indefinitely. This will spawn
        # two child processes: the X server (`/usr/bin/X`), and the
        # `/usr/bin/sleep` process passed to `xinit`.
        xinit /usr/bin/sleep infinity -- /usr/bin/X $display &
        sigterm_kill_parent=$!
    fi

    # XXX: We could try polling the children of the `xinit` process to
    # better detect when the X server is up and running, but it's
    # simpler (and seemingly reliable enough) to just snooze briefly.
    sleep 2
else
    echo "[$(basename $0)] Preserving DISPLAY $DISPLAY from environment"
    display=$DISPLAY
fi

# Run the real command with the appropriate DISPLAY.
DISPLAY=$display "$@"
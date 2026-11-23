import optparse

options: optparse.Values
args: list[str]
parser: optparse.OptionParser

def progress_callback(tag: str, dlnow: int, dltotal: int, msg: str) -> None: ...
def debug_callback(tag: str, mtype: int, message: bytes) -> None: ...
async def main() -> int: ...

result: int

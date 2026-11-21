import hou
from nodesearch.matchers import Matcher

def parse_query(qstring: str) -> Matcher: ...
def select(
    querystring: str | None = ...,
    query: Matcher | None = ...,
    network: hou.Node | None = ...,
    editor: hou.NetworkEditor | None = ...,
    frame: bool = ...,
) -> None: ...

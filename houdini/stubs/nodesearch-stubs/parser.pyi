import hou
from bookish.parser.builder import Builder as Builder
from nodesearch import matchers as matchers
from nodesearch.matchers import Matcher as Matcher

def parse_query(qstring: str) -> Matcher: ...
def select(querystring: str | None = None, query: Matcher | None = None, network: hou.Node | None = None, editor: hou.NetworkEditor | None = None, frame: bool = False) -> None: ...

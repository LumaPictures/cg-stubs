from nodesearch.matchers import *
import hou
from nodesearch.parser import parse_query as parse_query, select as select

def node_types(category: hou.NodeTypeCategory | None) -> list[str]: ...

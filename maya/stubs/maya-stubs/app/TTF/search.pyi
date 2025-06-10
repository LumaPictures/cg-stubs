from _typeshed import Incomplete

class ClosestMatchNode:
    text: Incomplete
    subnodes: Incomplete
    def __init__(self) -> None: ...
    def add(self, text) -> None: ...

class ClosestMatch:
    maxErr: Incomplete
    root: Incomplete
    def __init__(self, values, maxErr: int = 2) -> None: ...
    results: Incomplete
    searchStr: Incomplete
    def search(self, text): ...
    def searchRecursive(self, node, x, prevErrors) -> None: ...
    def searchChildren(self, node, errors) -> None: ...

class TTFSearch:
    wordSplitter: Incomplete
    labelLookupTable: Incomplete
    labelRankingTable: Incomplete
    labelClosestTable: Incomplete
    descriptionLookupTable: Incomplete
    descriptionRankingTable: Incomplete
    descriptionClosestTable: Incomplete
    keywordLookupTable: Incomplete
    keywordRankingTable: Incomplete
    keywordClosestTable: Incomplete
    commandLookupTable: Incomplete
    commandRankingTable: Incomplete
    commandClosestMatch: Incomplete
    lastSearchStringWords: Incomplete
    lastSearchResults: Incomplete
    def __init__(self) -> None: ...
    def addItem(self, item) -> None: ...
    def addKeyToLookupTable(self, key, item, lookupTable) -> None: ...
    def find(self, searchString): ...

import re as re
import types
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager

__all__ = ['__version__', '__versionTime__', '__author__', '__compat__', '__diag__', 'And', 'CaselessKeyword', 'CaselessLiteral', 'CharsNotIn', 'Combine', 'Dict', 'Each', 'Empty', 'FollowedBy', 'Forward', 'GoToColumn', 'Group', 'Keyword', 'LineEnd', 'LineStart', 'Literal', 'PrecededBy', 'MatchFirst', 'NoMatch', 'NotAny', 'OneOrMore', 'OnlyOnce', 'Optional', 'Or', 'ParseBaseException', 'ParseElementEnhance', 'ParseException', 'ParseExpression', 'ParseFatalException', 'ParseResults', 'ParseSyntaxException', 'ParserElement', 'QuotedString', 'RecursiveGrammarException', 'Regex', 'SkipTo', 'StringEnd', 'StringStart', 'Suppress', 'Token', 'TokenConverter', 'White', 'Word', 'WordEnd', 'WordStart', 'ZeroOrMore', 'Char', 'alphanums', 'alphas', 'alphas8bit', 'anyCloseTag', 'anyOpenTag', 'cStyleComment', 'col', 'commaSeparatedList', 'commonHTMLEntity', 'countedArray', 'cppStyleComment', 'dblQuotedString', 'dblSlashComment', 'delimitedList', 'dictOf', 'downcaseTokens', 'empty', 'hexnums', 'htmlComment', 'javaStyleComment', 'line', 'lineEnd', 'lineStart', 'lineno', 'makeHTMLTags', 'makeXMLTags', 'matchOnlyAtCol', 'matchPreviousExpr', 'matchPreviousLiteral', 'nestedExpr', 'nullDebugAction', 'nums', 'oneOf', 'opAssoc', 'operatorPrecedence', 'printables', 'punc8bit', 'pythonStyleComment', 'quotedString', 'removeQuotes', 'replaceHTMLEntity', 'replaceWith', 'restOfLine', 'sglQuotedString', 'srange', 'stringEnd', 'stringStart', 'traceParseAction', 'unicodeString', 'upcaseTokens', 'withAttribute', 'indentedBlock', 'originalTextFor', 'ungroup', 'infixNotation', 'locatedExpr', 'withClass', 'CloseMatch', 'tokenMap', 'pyparsing_common', 'pyparsing_unicode', 'unicode_set', 'conditionAsParseAction', 're']

__version__: str
__versionTime__: str
__author__: str

class SimpleNamespace: ...

__compat__: Incomplete
__diag__: Incomplete
basestring = str
unichr = chr
unicode = str
_ustr = str
range = xrange  # type: ignore[name-defined]
alphas: Incomplete
nums: str
hexnums: Incomplete
alphanums: Incomplete
printables: Incomplete

def conditionAsParseAction(fn, message=None, fatal: bool = False): ...

class ParseBaseException(Exception):
    """base exception class for all parsing runtime exceptions"""
    loc: Incomplete
    msg: Incomplete
    pstr: str
    parserElement: Incomplete
    args: Incomplete
    def __init__(self, pstr, loc: int = 0, msg=None, elem=None) -> None: ...
    @classmethod
    def _from_exception(cls, pe):
        """
        internal factory method to simplify creating one type of ParseException
        from another - avoids having __init__ signature conflicts among subclasses
        """
    def __getattr__(self, aname):
        """supported attributes by name are:
           - lineno - returns the line number of the exception text
           - col - returns the column number of the exception text
           - line - returns the line containing the exception text
        """
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def markInputline(self, markerString: str = '>!<'):
        """Extracts the exception line from the input string, and marks
           the location of the exception with a special symbol.
        """
    def __dir__(self): ...

class ParseException(ParseBaseException):
    '''
    Exception thrown when parse expressions don\'t match class;
    supported attributes by name are:
    - lineno - returns the line number of the exception text
    - col - returns the column number of the exception text
    - line - returns the line containing the exception text

    Example::

        try:
            Word(nums).setName("integer").parseString("ABC")
        except ParseException as pe:
            print(pe)
            print("column: {}".format(pe.col))

    prints::

       Expected integer (at char 0), (line:1, col:1)
        column: 1

    '''
    @staticmethod
    def explain(exc, depth: int = 16):
        """
        Method to take an exception and translate the Python internal traceback into a list
        of the pyparsing expressions that caused the exception to be raised.

        Parameters:

         - exc - exception raised during parsing (need not be a ParseException, in support
           of Python exceptions that might be raised in a parse action)
         - depth (default=16) - number of levels back in the stack trace to list expression
           and function names; if None, the full stack trace names will be listed; if 0, only
           the failing input line, marker, and exception string will be shown

        Returns a multi-line string listing the ParserElements and/or function names in the
        exception's stack trace.

        Note: the diagnostic output will include string representations of the expressions
        that failed to parse. These representations will be more helpful if you use `setName` to
        give identifiable names to your expressions. Otherwise they will use the default string
        forms, which may be cryptic to read.

        explain() is only supported under Python 3.
        """

class ParseFatalException(ParseBaseException):
    """user-throwable exception thrown when inconsistent parse content
       is found; stops all parsing immediately"""
class ParseSyntaxException(ParseFatalException):
    """just like :class:`ParseFatalException`, but thrown internally
    when an :class:`ErrorStop<And._ErrorStop>` ('-' operator) indicates
    that parsing is to stop immediately because an unbacktrackable
    syntax error has been found.
    """

class RecursiveGrammarException(Exception):
    """exception thrown by :class:`ParserElement.validate` if the
    grammar could be improperly recursive
    """
    parseElementTrace: Incomplete
    def __init__(self, parseElementList) -> None: ...
    def __str__(self) -> str: ...

class _ParseResultsWithOffset:
    tup: Incomplete
    def __init__(self, p1, p2) -> None: ...
    def __getitem__(self, i): ...
    def __repr__(self) -> str: ...
    def setOffset(self, i) -> None: ...

class ParseResults:
    '''Structured parse results, to provide multiple means of access to
    the parsed data:

       - as a list (``len(results)``)
       - by list index (``results[0], results[1]``, etc.)
       - by attribute (``results.<resultsName>`` - see :class:`ParserElement.setResultsName`)

    Example::

        integer = Word(nums)
        date_str = (integer.setResultsName("year") + \'/\'
                        + integer.setResultsName("month") + \'/\'
                        + integer.setResultsName("day"))
        # equivalent form:
        # date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

        # parseString returns a ParseResults object
        result = date_str.parseString("1999/12/31")

        def test(s, fn=repr):
            print("%s -> %s" % (s, fn(eval(s))))
        test("list(result)")
        test("result[0]")
        test("result[\'month\']")
        test("result.day")
        test("\'month\' in result")
        test("\'minutes\' in result")
        test("result.dump()", str)

    prints::

        list(result) -> [\'1999\', \'/\', \'12\', \'/\', \'31\']
        result[0] -> \'1999\'
        result[\'month\'] -> \'12\'
        result.day -> \'31\'
        \'month\' in result -> True
        \'minutes\' in result -> False
        result.dump() -> [\'1999\', \'/\', \'12\', \'/\', \'31\']
        - day: 31
        - month: 12
        - year: 1999
    '''
    def __new__(cls, toklist=None, name=None, asList: bool = True, modal: bool = True): ...
    __doinit: bool
    __name: Incomplete
    __parent: Incomplete
    __accumNames: Incomplete
    __asList: Incomplete
    __modal: Incomplete
    __toklist: Incomplete
    __tokdict: Incomplete
    def __init__(self, toklist=None, name=None, asList: bool = True, modal: bool = True, isinstance=...) -> None: ...
    def __getitem__(self, i): ...
    def __setitem__(self, k, v, isinstance=...) -> None: ...
    def __delitem__(self, i) -> None: ...
    def __contains__(self, k) -> bool: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def __iter__(self): ...
    def __reversed__(self): ...
    def _iterkeys(self): ...
    def _itervalues(self): ...
    def _iteritems(self): ...
    keys = _iterkeys
    values = _itervalues
    items = _iteritems
    iterkeys = _iterkeys
    itervalues = _itervalues
    iteritems = _iteritems
    def keys(self):  # type: ignore[no-redef]
        """Returns all named result keys (as a list in Python 2.x, as an iterator in Python 3.x)."""
    def values(self):  # type: ignore[no-redef]
        """Returns all named result values (as a list in Python 2.x, as an iterator in Python 3.x)."""
    def items(self):  # type: ignore[no-redef]
        """Returns all named result key-values (as a list of tuples in Python 2.x, as an iterator in Python 3.x)."""
    def haskeys(self):
        """Since keys() returns an iterator, this method is helpful in bypassing
           code that looks for the existence of any defined results names."""
    def pop(self, *args, **kwargs):
        '''
        Removes and returns item at specified index (default= ``last``).
        Supports both ``list`` and ``dict`` semantics for ``pop()``. If
        passed no argument or an integer argument, it will use ``list``
        semantics and pop tokens from the list of parsed tokens. If passed
        a non-integer argument (most likely a string), it will use ``dict``
        semantics and pop the corresponding value from any defined results
        names. A second default return value argument is supported, just as in
        ``dict.pop()``.

        Example::

            def remove_first(tokens):
                tokens.pop(0)
            print(OneOrMore(Word(nums)).parseString("0 123 321")) # -> [\'0\', \'123\', \'321\']
            print(OneOrMore(Word(nums)).addParseAction(remove_first).parseString("0 123 321")) # -> [\'123\', \'321\']

            label = Word(alphas)
            patt = label("LABEL") + OneOrMore(Word(nums))
            print(patt.parseString("AAB 123 321").dump())

            # Use pop() in a parse action to remove named result (note that corresponding value is not
            # removed from list form of results)
            def remove_LABEL(tokens):
                tokens.pop("LABEL")
                return tokens
            patt.addParseAction(remove_LABEL)
            print(patt.parseString("AAB 123 321").dump())

        prints::

            [\'AAB\', \'123\', \'321\']
            - LABEL: AAB

            [\'AAB\', \'123\', \'321\']
        '''
    def get(self, key, defaultValue=None):
        '''
        Returns named result matching the given key, or if there is no
        such name, then returns the given ``defaultValue`` or ``None`` if no
        ``defaultValue`` is specified.

        Similar to ``dict.get()``.

        Example::

            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            result = date_str.parseString("1999/12/31")
            print(result.get("year")) # -> \'1999\'
            print(result.get("hour", "not specified")) # -> \'not specified\'
            print(result.get("hour")) # -> None
        '''
    def insert(self, index, insStr) -> None:
        '''
        Inserts new element at location index in the list of parsed tokens.

        Similar to ``list.insert()``.

        Example::

            print(OneOrMore(Word(nums)).parseString("0 123 321")) # -> [\'0\', \'123\', \'321\']

            # use a parse action to insert the parse location in the front of the parsed results
            def insert_locn(locn, tokens):
                tokens.insert(0, locn)
            print(OneOrMore(Word(nums)).addParseAction(insert_locn).parseString("0 123 321")) # -> [0, \'0\', \'123\', \'321\']
        '''
    def append(self, item) -> None:
        '''
        Add single element to end of ParseResults list of elements.

        Example::

            print(OneOrMore(Word(nums)).parseString("0 123 321")) # -> [\'0\', \'123\', \'321\']

            # use a parse action to compute the sum of the parsed integers, and add it to the end
            def append_sum(tokens):
                tokens.append(sum(map(int, tokens)))
            print(OneOrMore(Word(nums)).addParseAction(append_sum).parseString("0 123 321")) # -> [\'0\', \'123\', \'321\', 444]
        '''
    def extend(self, itemseq) -> None:
        '''
        Add sequence of elements to end of ParseResults list of elements.

        Example::

            patt = OneOrMore(Word(alphas))

            # use a parse action to append the reverse of the matched strings, to make a palindrome
            def make_palindrome(tokens):
                tokens.extend(reversed([t[::-1] for t in tokens]))
                return \'\'.join(tokens)
            print(patt.addParseAction(make_palindrome).parseString("lskdj sdlkjf lksd")) # -> \'lskdjsdlkjflksddsklfjkldsjdksl\'
        '''
    def clear(self) -> None:
        """
        Clear all elements and results names.
        """
    def __getattr__(self, name): ...
    def __add__(self, other): ...
    def __iadd__(self, other): ...
    def __radd__(self, other): ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _asStringList(self, sep: str = ''): ...
    def asList(self):
        '''
        Returns the parse results as a nested list of matching tokens, all converted to strings.

        Example::

            patt = OneOrMore(Word(alphas))
            result = patt.parseString("sldkj lsdkj sldkj")
            # even though the result prints in string-like form, it is actually a pyparsing ParseResults
            print(type(result), result) # -> <class \'pyparsing.ParseResults\'> [\'sldkj\', \'lsdkj\', \'sldkj\']

            # Use asList() to create an actual list
            result_list = result.asList()
            print(type(result_list), result_list) # -> <class \'list\'> [\'sldkj\', \'lsdkj\', \'sldkj\']
        '''
    def asDict(self):
        '''
        Returns the named parse results as a nested dictionary.

        Example::

            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            result = date_str.parseString(\'12/31/1999\')
            print(type(result), repr(result)) # -> <class \'pyparsing.ParseResults\'> ([\'12\', \'/\', \'31\', \'/\', \'1999\'], {\'day\': [(\'1999\', 4)], \'year\': [(\'12\', 0)], \'month\': [(\'31\', 2)]})

            result_dict = result.asDict()
            print(type(result_dict), repr(result_dict)) # -> <class \'dict\'> {\'day\': \'1999\', \'year\': \'12\', \'month\': \'31\'}

            # even though a ParseResults supports dict-like access, sometime you just need to have a dict
            import json
            print(json.dumps(result)) # -> Exception: TypeError: ... is not JSON serializable
            print(json.dumps(result.asDict())) # -> {"month": "31", "day": "1999", "year": "12"}
        '''
    def copy(self):
        """
        Returns a new copy of a :class:`ParseResults` object.
        """
    def asXML(self, doctag=None, namedItemsOnly: bool = False, indent: str = '', formatted: bool = True):
        """
        (Deprecated) Returns the parse results as XML. Tags are created for tokens and lists that have defined results names.
        """
    def __lookup(self, sub): ...
    def getName(self):
        '''
        Returns the results name for this token expression. Useful when several
        different expressions might match at a particular location.

        Example::

            integer = Word(nums)
            ssn_expr = Regex(r"\\d\\d\\d-\\d\\d-\\d\\d\\d\\d")
            house_number_expr = Suppress(\'#\') + Word(nums, alphanums)
            user_data = (Group(house_number_expr)("house_number")
                        | Group(ssn_expr)("ssn")
                        | Group(integer)("age"))
            user_info = OneOrMore(user_data)

            result = user_info.parseString("22 111-22-3333 #221B")
            for item in result:
                print(item.getName(), \':\', item[0])

        prints::

            age : 22
            ssn : 111-22-3333
            house_number : 221B
        '''
    def dump(self, indent: str = '', full: bool = True, include_list: bool = True, _depth: int = 0):
        '''
        Diagnostic method for listing out the contents of
        a :class:`ParseResults`. Accepts an optional ``indent`` argument so
        that this string can be embedded in a nested display of other data.

        Example::

            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            result = date_str.parseString(\'12/31/1999\')
            print(result.dump())

        prints::

            [\'12\', \'/\', \'31\', \'/\', \'1999\']
            - day: 1999
            - month: 31
            - year: 12
        '''
    def pprint(self, *args, **kwargs) -> None:
        '''
        Pretty-printer for parsed results as a list, using the
        `pprint <https://docs.python.org/3/library/pprint.html>`_ module.
        Accepts additional positional or keyword args as defined for
        `pprint.pprint <https://docs.python.org/3/library/pprint.html#pprint.pprint>`_ .

        Example::

            ident = Word(alphas, alphanums)
            num = Word(nums)
            func = Forward()
            term = ident | num | Group(\'(\' + func + \')\')
            func <<= ident + Group(Optional(delimitedList(term)))
            result = func.parseString("fna a,b,(fnb c,d,200),100")
            result.pprint(width=40)

        prints::

            [\'fna\',
             [\'a\',
              \'b\',
              [\'(\', \'fnb\', [\'c\', \'d\', \'200\'], \')\'],
              \'100\']]
        '''
    def __getstate__(self): ...
    def __setstate__(self, state) -> None: ...
    def __getnewargs__(self): ...
    def __dir__(self): ...
    @classmethod
    def from_dict(cls, other, name=None):
        """
        Helper classmethod to construct a ParseResults from a dict, preserving the
        name-value relations as results names. If an optional 'name' argument is
        given, a nested ParseResults will be returned
        """

def col(loc, strg):
    """Returns current column within a string, counting newlines as line separators.
   The first column is number 1.

   Note: the default parsing behavior is to expand tabs in the input string
   before starting the parsing process.  See
   :class:`ParserElement.parseString` for more
   information on parsing strings containing ``<TAB>`` s, and suggested
   methods to maintain a consistent view of the parsed string, the parse
   location, and line and column positions within the parsed string.
   """
def lineno(loc, strg):
    """Returns current line number within a string, counting newlines as line separators.
    The first line is number 1.

    Note - the default parsing behavior is to expand tabs in the input string
    before starting the parsing process.  See :class:`ParserElement.parseString`
    for more information on parsing strings containing ``<TAB>`` s, and
    suggested methods to maintain a consistent view of the parsed string, the
    parse location, and line and column positions within the parsed string.
    """
def line(loc, strg):
    """Returns the line of text containing loc within a string, counting newlines as line separators.
       """
def nullDebugAction(*args) -> None:
    """'Do-nothing' debug action, to suppress debugging output during parsing."""

class ParserElement:
    """Abstract base level parser element class."""
    DEFAULT_WHITE_CHARS: str
    verbose_stacktrace: bool
    @staticmethod
    def setDefaultWhitespaceChars(chars) -> None:
        '''
        Overrides the default whitespace chars

        Example::

            # default whitespace chars are space, <TAB> and newline
            OneOrMore(Word(alphas)).parseString("abc def\\nghi jkl")  # -> [\'abc\', \'def\', \'ghi\', \'jkl\']

            # change to just treat newline as significant
            ParserElement.setDefaultWhitespaceChars(" \\t")
            OneOrMore(Word(alphas)).parseString("abc def\\nghi jkl")  # -> [\'abc\', \'def\']
        '''
    @staticmethod
    def inlineLiteralsUsing(cls) -> None:
        '''
        Set class to be used for inclusion of string literals into a parser.

        Example::

            # default literal class used is Literal
            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            date_str.parseString("1999/12/31")  # -> [\'1999\', \'/\', \'12\', \'/\', \'31\']


            # change to Suppress
            ParserElement.inlineLiteralsUsing(Suppress)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            date_str.parseString("1999/12/31")  # -> [\'1999\', \'12\', \'31\']
        '''
    @classmethod
    def _trim_traceback(cls, tb): ...
    parseAction: Incomplete
    failAction: Incomplete
    strRepr: Incomplete
    resultsName: Incomplete
    saveAsList: Incomplete
    skipWhitespace: bool
    whiteChars: Incomplete
    copyDefaultWhiteChars: bool
    mayReturnEmpty: bool
    keepTabs: bool
    ignoreExprs: Incomplete
    debug: bool
    streamlined: bool
    mayIndexError: bool
    errmsg: str
    modalResults: bool
    debugActions: Incomplete
    re: Incomplete
    callPreparse: bool
    callDuringTry: bool
    def __init__(self, savelist: bool = False) -> None: ...
    def copy(self):
        '''
        Make a copy of this :class:`ParserElement`.  Useful for defining
        different parse actions for the same parsing pattern, using copies of
        the original parse element.

        Example::

            integer = Word(nums).setParseAction(lambda toks: int(toks[0]))
            integerK = integer.copy().addParseAction(lambda toks: toks[0] * 1024) + Suppress("K")
            integerM = integer.copy().addParseAction(lambda toks: toks[0] * 1024 * 1024) + Suppress("M")

            print(OneOrMore(integerK | integerM | integer).parseString("5K 100 640K 256M"))

        prints::

            [5120, 100, 655360, 268435456]

        Equivalent form of ``expr.copy()`` is just ``expr()``::

            integerM = integer().addParseAction(lambda toks: toks[0] * 1024 * 1024) + Suppress("M")
        '''
    name: Incomplete
    def setName(self, name):
        '''
        Define name for this expression, makes debugging and exception messages clearer.

        Example::

            Word(nums).parseString("ABC")  # -> Exception: Expected W:(0123...) (at char 0), (line:1, col:1)
            Word(nums).setName("integer").parseString("ABC")  # -> Exception: Expected integer (at char 0), (line:1, col:1)
        '''
    def setResultsName(self, name, listAllMatches: bool = False):
        '''
        Define name for referencing matching tokens as a nested attribute
        of the returned parse results.
        NOTE: this returns a *copy* of the original :class:`ParserElement` object;
        this is so that the client can define a basic element, such as an
        integer, and reference it in multiple places with different names.

        You can also set results names using the abbreviated syntax,
        ``expr("name")`` in place of ``expr.setResultsName("name")``
        - see :class:`__call__`.

        Example::

            date_str = (integer.setResultsName("year") + \'/\'
                        + integer.setResultsName("month") + \'/\'
                        + integer.setResultsName("day"))

            # equivalent form:
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")
        '''
    def _setResultsName(self, name, listAllMatches: bool = False): ...
    _parse: Incomplete
    def setBreak(self, breakFlag: bool = True):
        """Method to invoke the Python pdb debugger when this element is
           about to be parsed. Set ``breakFlag`` to True to enable, False to
           disable.
        """
    def setParseAction(self, *fns, **kwargs):
        '''
        Define one or more actions to perform when successfully matching parse element definition.
        Parse action fn is a callable method with 0-3 arguments, called as ``fn(s, loc, toks)`` ,
        ``fn(loc, toks)`` , ``fn(toks)`` , or just ``fn()`` , where:

        - s   = the original string being parsed (see note below)
        - loc = the location of the matching substring
        - toks = a list of the matched tokens, packaged as a :class:`ParseResults` object

        If the functions in fns modify the tokens, they can return them as the return
        value from fn, and the modified list of tokens will replace the original.
        Otherwise, fn does not need to return any value.

        If None is passed as the parse action, all previously added parse actions for this
        expression are cleared.

        Optional keyword arguments:
        - callDuringTry = (default= ``False``) indicate if parse action should be run during lookaheads and alternate testing

        Note: the default parsing behavior is to expand tabs in the input string
        before starting the parsing process.  See :class:`parseString for more
        information on parsing strings containing ``<TAB>`` s, and suggested
        methods to maintain a consistent view of the parsed string, the parse
        location, and line and column positions within the parsed string.

        Example::

            integer = Word(nums)
            date_str = integer + \'/\' + integer + \'/\' + integer

            date_str.parseString("1999/12/31")  # -> [\'1999\', \'/\', \'12\', \'/\', \'31\']

            # use parse action to convert to ints at parse time
            integer = Word(nums).setParseAction(lambda toks: int(toks[0]))
            date_str = integer + \'/\' + integer + \'/\' + integer

            # note that integer fields are now ints, not strings
            date_str.parseString("1999/12/31")  # -> [1999, \'/\', 12, \'/\', 31]
        '''
    def addParseAction(self, *fns, **kwargs):
        """
        Add one or more parse actions to expression's list of parse actions. See :class:`setParseAction`.

        See examples in :class:`copy`.
        """
    def addCondition(self, *fns, **kwargs):
        '''Add a boolean predicate function to expression\'s list of parse actions. See
        :class:`setParseAction` for function call signatures. Unlike ``setParseAction``,
        functions passed to ``addCondition`` need to return boolean success/fail of the condition.

        Optional keyword arguments:
        - message = define a custom message to be used in the raised exception
        - fatal   = if True, will raise ParseFatalException to stop parsing immediately; otherwise will raise ParseException

        Example::

            integer = Word(nums).setParseAction(lambda toks: int(toks[0]))
            year_int = integer.copy()
            year_int.addCondition(lambda toks: toks[0] >= 2000, message="Only support years 2000 and later")
            date_str = year_int + \'/\' + integer + \'/\' + integer

            result = date_str.parseString("1999/12/31")  # -> Exception: Only support years 2000 and later (at char 0), (line:1, col:1)
        '''
    def setFailAction(self, fn):
        """Define action to perform if parsing fails at this expression.
           Fail acton fn is a callable function that takes the arguments
           ``fn(s, loc, expr, err)`` where:
           - s = string being parsed
           - loc = location where expression match was attempted and failed
           - expr = the parse expression that failed
           - err = the exception thrown
           The function returns no value.  It may throw :class:`ParseFatalException`
           if it is desired to stop parsing immediately."""
    def _skipIgnorables(self, instring, loc): ...
    def preParse(self, instring, loc): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def postParse(self, instring, loc, tokenlist): ...
    def _parseNoCache(self, instring, loc, doActions: bool = True, callPreParse: bool = True): ...
    def tryParse(self, instring, loc): ...
    def canParseNext(self, instring, loc): ...
    class _UnboundedCache:
        not_in_cache: Incomplete
        get: Incomplete
        set: Incomplete
        clear: Incomplete
        __len__: Incomplete
        def __init__(self) -> None: ...
    class _FifoCache:
        not_in_cache: Incomplete
        get: Incomplete
        set: Incomplete
        clear: Incomplete
        __len__: Incomplete
        def __init__(self, size) -> None: ...
    class _FifoCache:  # type: ignore[no-redef]
        not_in_cache: Incomplete
        get: Incomplete
        set: Incomplete
        clear: Incomplete
        __len__: Incomplete
        def __init__(self, size) -> None: ...
    packrat_cache: Incomplete
    packrat_cache_lock: Incomplete
    packrat_cache_stats: Incomplete
    def _parseCache(self, instring, loc, doActions: bool = True, callPreParse: bool = True): ...
    _parse = _parseNoCache
    @staticmethod
    def resetCache() -> None: ...
    _packratEnabled: bool
    @staticmethod
    def enablePackrat(cache_size_limit: int = 128) -> None:
        '''Enables "packrat" parsing, which adds memoizing to the parsing logic.
           Repeated parse attempts at the same string location (which happens
           often in many complex grammars) can immediately return a cached value,
           instead of re-executing parsing/validating code.  Memoizing is done of
           both valid results and parsing exceptions.

           Parameters:

           - cache_size_limit - (default= ``128``) - if an integer value is provided
             will limit the size of the packrat cache; if None is passed, then
             the cache size will be unbounded; if 0 is passed, the cache will
             be effectively disabled.

           This speedup may break existing programs that use parse actions that
           have side-effects.  For this reason, packrat parsing is disabled when
           you first import pyparsing.  To activate the packrat feature, your
           program must call the class method :class:`ParserElement.enablePackrat`.
           For best results, call ``enablePackrat()`` immediately after
           importing pyparsing.

           Example::

               import pyparsing
               pyparsing.ParserElement.enablePackrat()
        '''
    def parseString(self, instring, parseAll: bool = False):
        """
        Execute the parse expression with the given string.
        This is the main interface to the client code, once the complete
        expression has been built.

        Returns the parsed data as a :class:`ParseResults` object, which may be
        accessed as a list, or as a dict or object with attributes if the given parser
        includes results names.

        If you want the grammar to require that the entire input string be
        successfully parsed, then set ``parseAll`` to True (equivalent to ending
        the grammar with ``StringEnd()``).

        Note: ``parseString`` implicitly calls ``expandtabs()`` on the input string,
        in order to report proper column numbers in parse actions.
        If the input string contains tabs and
        the grammar uses parse actions that use the ``loc`` argument to index into the
        string being parsed, you can ensure you have a consistent view of the input
        string by:

        - calling ``parseWithTabs`` on your grammar before calling ``parseString``
          (see :class:`parseWithTabs`)
        - define your parse action using the full ``(s, loc, toks)`` signature, and
          reference the input string using the parse action's ``s`` argument
        - explictly expand the tabs in your input string before calling
          ``parseString``

        Example::

            Word('a').parseString('aaaaabaaa')  # -> ['aaaaa']
            Word('a').parseString('aaaaabaaa', parseAll=True)  # -> Exception: Expected end of text
        """
    def scanString(self, instring, maxMatches=..., overlap: bool = False) -> Generator[Incomplete]:
        '''
        Scan the input string for expression matches.  Each match will return the
        matching tokens, start location, and end location.  May be called with optional
        ``maxMatches`` argument, to clip scanning after \'n\' matches are found.  If
        ``overlap`` is specified, then overlapping matches will be reported.

        Note that the start and end locations are reported relative to the string
        being parsed.  See :class:`parseString` for more information on parsing
        strings with embedded tabs.

        Example::

            source = "sldjf123lsdjjkf345sldkjf879lkjsfd987"
            print(source)
            for tokens, start, end in Word(alphas).scanString(source):
                print(\' \'*start + \'^\'*(end-start))
                print(\' \'*start + tokens[0])

        prints::

            sldjf123lsdjjkf345sldkjf879lkjsfd987
            ^^^^^
            sldjf
                    ^^^^^^^
                    lsdjjkf
                              ^^^^^^
                              sldkjf
                                       ^^^^^^
                                       lkjsfd
        '''
    def transformString(self, instring):
        '''
        Extension to :class:`scanString`, to modify matching text with modified tokens that may
        be returned from a parse action.  To use ``transformString``, define a grammar and
        attach a parse action to it that modifies the returned token list.
        Invoking ``transformString()`` on a target string will then scan for matches,
        and replace the matched text patterns according to the logic in the parse
        action.  ``transformString()`` returns the resulting transformed string.

        Example::

            wd = Word(alphas)
            wd.setParseAction(lambda toks: toks[0].title())

            print(wd.transformString("now is the winter of our discontent made glorious summer by this sun of york."))

        prints::

            Now Is The Winter Of Our Discontent Made Glorious Summer By This Sun Of York.
        '''
    def searchString(self, instring, maxMatches=...):
        '''
        Another extension to :class:`scanString`, simplifying the access to the tokens found
        to match the given parse expression.  May be called with optional
        ``maxMatches`` argument, to clip searching after \'n\' matches are found.

        Example::

            # a capitalized word starts with an uppercase letter, followed by zero or more lowercase letters
            cap_word = Word(alphas.upper(), alphas.lower())

            print(cap_word.searchString("More than Iron, more than Lead, more than Gold I need Electricity"))

            # the sum() builtin can be used to merge results into a single ParseResults object
            print(sum(cap_word.searchString("More than Iron, more than Lead, more than Gold I need Electricity")))

        prints::

            [[\'More\'], [\'Iron\'], [\'Lead\'], [\'Gold\'], [\'I\'], [\'Electricity\']]
            [\'More\', \'Iron\', \'Lead\', \'Gold\', \'I\', \'Electricity\']
        '''
    def split(self, instring, maxsplit=..., includeSeparators: bool = False) -> Generator[Incomplete]:
        '''
        Generator method to split a string using the given expression as a separator.
        May be called with optional ``maxsplit`` argument, to limit the number of splits;
        and the optional ``includeSeparators`` argument (default= ``False``), if the separating
        matching text should be included in the split results.

        Example::

            punc = oneOf(list(".,;:/-!?"))
            print(list(punc.split("This, this?, this sentence, is badly punctuated!")))

        prints::

            [\'This\', \' this\', \'\', \' this sentence\', \' is badly punctuated\', \'\']
        '''
    def __add__(self, other):
        '''
        Implementation of + operator - returns :class:`And`. Adding strings to a ParserElement
        converts them to :class:`Literal`s by default.

        Example::

            greet = Word(alphas) + "," + Word(alphas) + "!"
            hello = "Hello, World!"
            print (hello, "->", greet.parseString(hello))

        prints::

            Hello, World! -> [\'Hello\', \',\', \'World\', \'!\']

        ``...`` may be used as a parse expression as a short form of :class:`SkipTo`.

            Literal(\'start\') + ... + Literal(\'end\')

        is equivalent to:

            Literal(\'start\') + SkipTo(\'end\')("_skipped*") + Literal(\'end\')

        Note that the skipped text is returned with \'_skipped\' as a results name,
        and to support having multiple skips in the same parser, the value returned is
        a list of all skipped text.
        '''
    def __radd__(self, other):
        """
        Implementation of + operator when left operand is not a :class:`ParserElement`
        """
    def __sub__(self, other):
        """
        Implementation of - operator, returns :class:`And` with error stop
        """
    def __rsub__(self, other):
        """
        Implementation of - operator when left operand is not a :class:`ParserElement`
        """
    def __mul__(self, other):
        '''
        Implementation of * operator, allows use of ``expr * 3`` in place of
        ``expr + expr + expr``.  Expressions may also me multiplied by a 2-integer
        tuple, similar to ``{min, max}`` multipliers in regular expressions.  Tuples
        may also include ``None`` as in:
         - ``expr*(n, None)`` or ``expr*(n, )`` is equivalent
              to ``expr*n + ZeroOrMore(expr)``
              (read as "at least n instances of ``expr``")
         - ``expr*(None, n)`` is equivalent to ``expr*(0, n)``
              (read as "0 to n instances of ``expr``")
         - ``expr*(None, None)`` is equivalent to ``ZeroOrMore(expr)``
         - ``expr*(1, None)`` is equivalent to ``OneOrMore(expr)``

        Note that ``expr*(None, n)`` does not raise an exception if
        more than n exprs exist in the input stream; that is,
        ``expr*(None, n)`` does not enforce a maximum number of expr
        occurrences.  If this behavior is desired, then write
        ``expr*(None, n) + ~expr``
        '''
    def __rmul__(self, other): ...
    def __or__(self, other):
        """
        Implementation of | operator - returns :class:`MatchFirst`
        """
    def __ror__(self, other):
        """
        Implementation of | operator when left operand is not a :class:`ParserElement`
        """
    def __xor__(self, other):
        """
        Implementation of ^ operator - returns :class:`Or`
        """
    def __rxor__(self, other):
        """
        Implementation of ^ operator when left operand is not a :class:`ParserElement`
        """
    def __and__(self, other):
        """
        Implementation of & operator - returns :class:`Each`
        """
    def __rand__(self, other):
        """
        Implementation of & operator when left operand is not a :class:`ParserElement`
        """
    def __invert__(self):
        """
        Implementation of ~ operator - returns :class:`NotAny`
        """
    def __iter__(self): ...
    def __getitem__(self, key):
        '''
        use ``[]`` indexing notation as a short form for expression repetition:
         - ``expr[n]`` is equivalent to ``expr*n``
         - ``expr[m, n]`` is equivalent to ``expr*(m, n)``
         - ``expr[n, ...]`` or ``expr[n,]`` is equivalent
              to ``expr*n + ZeroOrMore(expr)``
              (read as "at least n instances of ``expr``")
         - ``expr[..., n]`` is equivalent to ``expr*(0, n)``
              (read as "0 to n instances of ``expr``")
         - ``expr[...]`` and ``expr[0, ...]`` are equivalent to ``ZeroOrMore(expr)``
         - ``expr[1, ...]`` is equivalent to ``OneOrMore(expr)``
         ``None`` may be used in place of ``...``.

        Note that ``expr[..., n]`` and ``expr[m, n]``do not raise an exception
        if more than ``n`` ``expr``s exist in the input stream.  If this behavior is
        desired, then write ``expr[..., n] + ~expr``.
       '''
    def __call__(self, name=None):
        '''
        Shortcut for :class:`setResultsName`, with ``listAllMatches=False``.

        If ``name`` is given with a trailing ``\'*\'`` character, then ``listAllMatches`` will be
        passed as ``True``.

        If ``name` is omitted, same as calling :class:`copy`.

        Example::

            # these are equivalent
            userdata = Word(alphas).setResultsName("name") + Word(nums + "-").setResultsName("socsecno")
            userdata = Word(alphas)("name") + Word(nums + "-")("socsecno")
        '''
    def suppress(self):
        """
        Suppresses the output of this :class:`ParserElement`; useful to keep punctuation from
        cluttering up returned output.
        """
    def leaveWhitespace(self):
        """
        Disables the skipping of whitespace before matching the characters in the
        :class:`ParserElement`'s defined pattern.  This is normally only used internally by
        the pyparsing module, but may be needed in some whitespace-sensitive grammars.
        """
    def setWhitespaceChars(self, chars):
        """
        Overrides the default whitespace chars
        """
    def parseWithTabs(self):
        """
        Overrides default behavior to expand ``<TAB>``s to spaces before parsing the input string.
        Must be called before ``parseString`` when the input grammar contains elements that
        match ``<TAB>`` characters.
        """
    def ignore(self, other):
        """
        Define expression to be ignored (e.g., comments) while doing pattern
        matching; may be called repeatedly, to define multiple comment or other
        ignorable patterns.

        Example::

            patt = OneOrMore(Word(alphas))
            patt.parseString('ablaj /* comment */ lskjd') # -> ['ablaj']

            patt.ignore(cStyleComment)
            patt.parseString('ablaj /* comment */ lskjd') # -> ['ablaj', 'lskjd']
        """
    def setDebugActions(self, startAction, successAction, exceptionAction):
        """
        Enable display of debugging messages while doing pattern matching.
        """
    def setDebug(self, flag: bool = True):
        '''
        Enable display of debugging messages while doing pattern matching.
        Set ``flag`` to True to enable, False to disable.

        Example::

            wd = Word(alphas).setName("alphaword")
            integer = Word(nums).setName("numword")
            term = wd | integer

            # turn on debugging for wd
            wd.setDebug()

            OneOrMore(term).parseString("abc 123 xyz 890")

        prints::

            Match alphaword at loc 0(1,1)
            Matched alphaword -> [\'abc\']
            Match alphaword at loc 3(1,4)
            Exception raised:Expected alphaword (at char 4), (line:1, col:5)
            Match alphaword at loc 7(1,8)
            Matched alphaword -> [\'xyz\']
            Match alphaword at loc 11(1,12)
            Exception raised:Expected alphaword (at char 12), (line:1, col:13)
            Match alphaword at loc 15(1,16)
            Exception raised:Expected alphaword (at char 15), (line:1, col:16)

        The output shown is that produced by the default debug actions - custom debug actions can be
        specified using :class:`setDebugActions`. Prior to attempting
        to match the ``wd`` expression, the debugging message ``"Match <exprname> at loc <n>(<line>,<col>)"``
        is shown. Then if the parse succeeds, a ``"Matched"`` message is shown, or an ``"Exception raised"``
        message is shown. Also note the use of :class:`setName` to assign a human-readable name to the expression,
        which makes debugging and exception messages easier to understand - for instance, the default
        name created for the :class:`Word` expression without calling ``setName`` is ``"W:(ABCD...)"``.
        '''
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def streamline(self): ...
    def checkRecursion(self, parseElementList) -> None: ...
    def validate(self, validateTrace=None) -> None:
        """
        Check defined expressions for valid structure, check for infinite recursive definitions.
        """
    def parseFile(self, file_or_filename, parseAll: bool = False):
        """
        Execute the parse expression on the given file or filename.
        If a filename is specified (instead of a file object),
        the entire file is opened, read, and closed before parsing.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def __req__(self, other): ...
    def __rne__(self, other): ...
    def matches(self, testString, parseAll: bool = True):
        '''
        Method for quick testing of a parser against a test string. Good for simple
        inline microtests of sub expressions while building up larger parser.

        Parameters:
         - testString - to test against this expression for a match
         - parseAll - (default= ``True``) - flag to pass to :class:`parseString` when running tests

        Example::

            expr = Word(nums)
            assert expr.matches("100")
        '''
    def runTests(self, tests, parseAll: bool = True, comment: str = '#', fullDump: bool = True, printResults: bool = True, failureTests: bool = False, postParse=None, file=None):
        '''
        Execute the parse expression on a series of test strings, showing each
        test, the parsed results or where the parse failed. Quick and easy way to
        run a parse expression against a list of sample strings.

        Parameters:
         - tests - a list of separate test strings, or a multiline string of test strings
         - parseAll - (default= ``True``) - flag to pass to :class:`parseString` when running tests
         - comment - (default= ``\'#\'``) - expression for indicating embedded comments in the test
              string; pass None to disable comment filtering
         - fullDump - (default= ``True``) - dump results as list followed by results names in nested outline;
              if False, only dump nested list
         - printResults - (default= ``True``) prints test output to stdout
         - failureTests - (default= ``False``) indicates if these tests are expected to fail parsing
         - postParse - (default= ``None``) optional callback for successful parse results; called as
              `fn(test_string, parse_results)` and returns a string to be added to the test output
         - file - (default=``None``) optional file-like object to which test output will be written;
              if None, will default to ``sys.stdout``

        Returns: a (success, results) tuple, where success indicates that all tests succeeded
        (or failed if ``failureTests`` is True), and the results contain a list of lines of each
        test\'s output

        Example::

            number_expr = pyparsing_common.number.copy()

            result = number_expr.runTests(\'\'\'
                # unsigned integer
                100
                # negative integer
                -100
                # float with scientific notation
                6.02e23
                # integer with scientific notation
                1e-12
                \'\'\')
            print("Success" if result[0] else "Failed!")

            result = number_expr.runTests(\'\'\'
                # stray character
                100Z
                # missing leading digit before \'.\'
                -.100
                # too many \'.\'
                3.14.159
                \'\'\', failureTests=True)
            print("Success" if result[0] else "Failed!")

        prints::

            # unsigned integer
            100
            [100]

            # negative integer
            -100
            [-100]

            # float with scientific notation
            6.02e23
            [6.02e+23]

            # integer with scientific notation
            1e-12
            [1e-12]

            Success

            # stray character
            100Z
               ^
            FAIL: Expected end of text (at char 3), (line:1, col:4)

            # missing leading digit before \'.\'
            -.100
            ^
            FAIL: Expected {real number with scientific notation | real number | signed integer} (at char 0), (line:1, col:1)

            # too many \'.\'
            3.14.159
                ^
            FAIL: Expected end of text (at char 4), (line:1, col:5)

            Success

        Each test string must be on a single line. If you want to test a string that spans multiple
        lines, create a test like this::

            expr.runTest(r"this is a test\\n of strings that spans \\n 3 lines")

        (Note that this is a raw string literal, you must include the leading \'r\'.)
        '''

class _PendingSkip(ParserElement):
    strRepr: Incomplete
    name: Incomplete
    anchor: Incomplete
    must_skip: Incomplete
    def __init__(self, expr, must_skip: bool = False) -> None: ...
    def __add__(self, other): ...
    def __repr__(self) -> str: ...
    def parseImpl(self, *args) -> None: ...

class Token(ParserElement):
    """Abstract :class:`ParserElement` subclass, for defining atomic
    matching patterns.
    """
    def __init__(self) -> None: ...

class Empty(Token):
    """An empty token, will always match.
    """
    name: str
    mayReturnEmpty: bool
    mayIndexError: bool
    def __init__(self) -> None: ...

class NoMatch(Token):
    """A token that will never match.
    """
    name: str
    mayReturnEmpty: bool
    mayIndexError: bool
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True) -> None: ...

class Literal(Token):
    '''Token to exactly match a specified string.

    Example::

        Literal(\'blah\').parseString(\'blah\')  # -> [\'blah\']
        Literal(\'blah\').parseString(\'blahfooblah\')  # -> [\'blah\']
        Literal(\'blah\').parseString(\'bla\')  # -> Exception: Expected "blah"

    For case-insensitive matching, use :class:`CaselessLiteral`.

    For keyword matching (force word break before and after the matched string),
    use :class:`Keyword` or :class:`CaselessKeyword`.
    '''
    match: Incomplete
    matchLen: Incomplete
    firstMatchChar: Incomplete
    __class__: Incomplete
    name: Incomplete
    errmsg: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    def __init__(self, matchString) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class _SingleCharLiteral(Literal):
    def parseImpl(self, instring, loc, doActions: bool = True): ...
_L = Literal

class Keyword(Token):
    '''Token to exactly match a specified string as a keyword, that is,
    it must be immediately followed by a non-keyword character.  Compare
    with :class:`Literal`:

     - ``Literal("if")`` will match the leading ``\'if\'`` in
       ``\'ifAndOnlyIf\'``.
     - ``Keyword("if")`` will not; it will only match the leading
       ``\'if\'`` in ``\'if x=1\'``, or ``\'if(y==2)\'``

    Accepts two optional constructor arguments in addition to the
    keyword string:

     - ``identChars`` is a string of characters that would be valid
       identifier characters, defaulting to all alphanumerics + "_" and
       "$"
     - ``caseless`` allows case-insensitive matching, default is ``False``.

    Example::

        Keyword("start").parseString("start")  # -> [\'start\']
        Keyword("start").parseString("starting")  # -> Exception

    For case-insensitive matching, use :class:`CaselessKeyword`.
    '''
    DEFAULT_KEYWORD_CHARS: Incomplete
    match: Incomplete
    matchLen: Incomplete
    firstMatchChar: Incomplete
    name: Incomplete
    errmsg: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    caseless: Incomplete
    caselessmatch: Incomplete
    identChars: Incomplete
    def __init__(self, matchString, identChars=None, caseless: bool = False) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def copy(self): ...
    @staticmethod
    def setDefaultKeywordChars(chars) -> None:
        """Overrides the default Keyword chars
        """

class CaselessLiteral(Literal):
    '''Token to match a specified string, ignoring case of letters.
    Note: the matched results will always be in the case of the given
    match string, NOT the case of the input text.

    Example::

        OneOrMore(CaselessLiteral("CMD")).parseString("cmd CMD Cmd10") # -> [\'CMD\', \'CMD\', \'CMD\']

    (Contrast with example for :class:`CaselessKeyword`.)
    '''
    returnString: Incomplete
    name: Incomplete
    errmsg: Incomplete
    def __init__(self, matchString) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class CaselessKeyword(Keyword):
    '''
    Caseless version of :class:`Keyword`.

    Example::

        OneOrMore(CaselessKeyword("CMD")).parseString("cmd CMD Cmd10") # -> [\'CMD\', \'CMD\']

    (Contrast with example for :class:`CaselessLiteral`.)
    '''
    def __init__(self, matchString, identChars=None) -> None: ...

class CloseMatch(Token):
    '''A variation on :class:`Literal` which matches "close" matches,
    that is, strings with at most \'n\' mismatching characters.
    :class:`CloseMatch` takes parameters:

     - ``match_string`` - string to be matched
     - ``maxMismatches`` - (``default=1``) maximum number of
       mismatches allowed to count as a match

    The results from a successful parse will contain the matched text
    from the input string and the following named results:

     - ``mismatches`` - a list of the positions within the
       match_string where mismatches were found
     - ``original`` - the original match_string used to compare
       against the input string

    If ``mismatches`` is an empty list, then the match was an exact
    match.

    Example::

        patt = CloseMatch("ATCATCGAATGGA")
        patt.parseString("ATCATCGAAXGGA") # -> ([\'ATCATCGAAXGGA\'], {\'mismatches\': [[9]], \'original\': [\'ATCATCGAATGGA\']})
        patt.parseString("ATCAXCGAAXGGA") # -> Exception: Expected \'ATCATCGAATGGA\' (with up to 1 mismatches) (at char 0), (line:1, col:1)

        # exact match
        patt.parseString("ATCATCGAATGGA") # -> ([\'ATCATCGAATGGA\'], {\'mismatches\': [[]], \'original\': [\'ATCATCGAATGGA\']})

        # close match allowing up to 2 mismatches
        patt = CloseMatch("ATCATCGAATGGA", maxMismatches=2)
        patt.parseString("ATCAXCGAAXGGA") # -> ([\'ATCAXCGAAXGGA\'], {\'mismatches\': [[4, 9]], \'original\': [\'ATCATCGAATGGA\']})
    '''
    name: Incomplete
    match_string: Incomplete
    maxMismatches: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    mayReturnEmpty: bool
    def __init__(self, match_string, maxMismatches: int = 1) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Word(Token):
    '''Token for matching words composed of allowed character sets.
    Defined with string containing all allowed initial characters, an
    optional string containing allowed body characters (if omitted,
    defaults to the initial character set), and an optional minimum,
    maximum, and/or exact length.  The default value for ``min`` is
    1 (a minimum value < 1 is not valid); the default values for
    ``max`` and ``exact`` are 0, meaning no maximum or exact
    length restriction. An optional ``excludeChars`` parameter can
    list characters that might be found in the input ``bodyChars``
    string; useful to define a word of all printables except for one or
    two characters, for instance.

    :class:`srange` is useful for defining custom character set strings
    for defining ``Word`` expressions, using range notation from
    regular expression character sets.

    A common mistake is to use :class:`Word` to match a specific literal
    string, as in ``Word("Address")``. Remember that :class:`Word`
    uses the string argument to define *sets* of matchable characters.
    This expression would match "Add", "AAA", "dAred", or any other word
    made up of the characters \'A\', \'d\', \'r\', \'e\', and \'s\'. To match an
    exact literal string, use :class:`Literal` or :class:`Keyword`.

    pyparsing includes helper strings for building Words:

     - :class:`alphas`
     - :class:`nums`
     - :class:`alphanums`
     - :class:`hexnums`
     - :class:`alphas8bit` (alphabetic characters in ASCII range 128-255
       - accented, tilded, umlauted, etc.)
     - :class:`punc8bit` (non-alphabetic characters in ASCII range
       128-255 - currency, symbols, superscripts, diacriticals, etc.)
     - :class:`printables` (any non-whitespace character)

    Example::

        # a word composed of digits
        integer = Word(nums) # equivalent to Word("0123456789") or Word(srange("0-9"))

        # a word with a leading capital, and zero or more lowercase
        capital_word = Word(alphas.upper(), alphas.lower())

        # hostnames are alphanumeric, with leading alpha, and \'-\'
        hostname = Word(alphas, alphanums + \'-\')

        # roman numeral (not a strict parser, accepts invalid mix of characters)
        roman = Word("IVXLCDM")

        # any string of non-whitespace characters, except for \',\'
        csv_value = Word(printables, excludeChars=",")
    '''
    initCharsOrig: Incomplete
    initChars: Incomplete
    bodyCharsOrig: Incomplete
    bodyChars: Incomplete
    maxSpecified: Incomplete
    minLen: Incomplete
    maxLen: Incomplete
    name: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    asKeyword: Incomplete
    reString: Incomplete
    re: Incomplete
    re_match: Incomplete
    __class__: Incomplete
    def __init__(self, initChars, bodyChars=None, min: int = 1, max: int = 0, exact: int = 0, asKeyword: bool = False, excludeChars=None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class _WordRegex(Word):
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Char(_WordRegex):
    """A short-cut class for defining ``Word(characters, exact=1)``,
    when defining a match of any single character in a string of
    characters.
    """
    reString: Incomplete
    re: Incomplete
    re_match: Incomplete
    def __init__(self, charset, asKeyword: bool = False, excludeChars=None) -> None: ...

class Regex(Token):
    '''Token for matching strings that match a given regular
    expression. Defined with string specifying the regular expression in
    a form recognized by the stdlib Python  `re module <https://docs.python.org/3/library/re.html>`_.
    If the given regex contains named groups (defined using ``(?P<name>...)``),
    these will be preserved as named parse results.

    If instead of the Python stdlib re module you wish to use a different RE module
    (such as the `regex` module), you can replace it by either building your
    Regex object with a compiled RE that was compiled using regex:

    Example::

        realnum = Regex(r"[+-]?\\d+\\.\\d*")
        date = Regex(r\'(?P<year>\\d{4})-(?P<month>\\d\\d?)-(?P<day>\\d\\d?)\')
        # ref: https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
        roman = Regex(r"M{0,4}(CM|CD|D?{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

        # use regex module instead of stdlib re module to construct a Regex using
        # a compiled regular expression
        import regex
        parser = pp.Regex(regex.compile(r\'[0-9]\'))

    '''
    pattern: Incomplete
    flags: Incomplete
    re: Incomplete
    reString: Incomplete
    re_match: Incomplete
    name: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    mayReturnEmpty: Incomplete
    asGroupList: Incomplete
    asMatch: Incomplete
    def __init__(self, pattern, flags: int = 0, asGroupList: bool = False, asMatch: bool = False) -> None:
        """The parameters ``pattern`` and ``flags`` are passed
        to the ``re.compile()`` function as-is. See the Python
        `re module <https://docs.python.org/3/library/re.html>`_ module for an
        explanation of the acceptable patterns and flags.
        """
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def parseImplAsGroupList(self, instring, loc, doActions: bool = True): ...
    def parseImplAsMatch(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...
    def sub(self, repl):
        '''
        Return Regex with an attached parse action to transform the parsed
        result as if called using `re.sub(expr, repl, string) <https://docs.python.org/3/library/re.html#re.sub>`_.

        Example::

            make_html = Regex(r"(\\w+):(.*?):").sub(r"<\\1>\\2</\\1>")
            print(make_html.transformString("h1:main title:"))
            # prints "<h1>main title</h1>"
        '''

class QuotedString(Token):
    '''
    Token for matching strings that are delimited by quoting characters.

    Defined with the following parameters:

        - quoteChar - string of one or more characters defining the
          quote delimiting string
        - escChar - character to escape quotes, typically backslash
          (default= ``None``)
        - escQuote - special quote sequence to escape an embedded quote
          string (such as SQL\'s ``""`` to escape an embedded ``"``)
          (default= ``None``)
        - multiline - boolean indicating whether quotes can span
          multiple lines (default= ``False``)
        - unquoteResults - boolean indicating whether the matched text
          should be unquoted (default= ``True``)
        - endQuoteChar - string of one or more characters defining the
          end of the quote delimited string (default= ``None``  => same as
          quoteChar)
        - convertWhitespaceEscapes - convert escaped whitespace
          (``\'\\t\'``, ``\'\\n\'``, etc.) to actual whitespace
          (default= ``True``)

    Example::

        qs = QuotedString(\'"\')
        print(qs.searchString(\'lsjdf "This is the quote" sldjf\'))
        complex_qs = QuotedString(\'{{\', endQuoteChar=\'}}\')
        print(complex_qs.searchString(\'lsjdf {{This is the "quote"}} sldjf\'))
        sql_qs = QuotedString(\'"\', escQuote=\'""\')
        print(sql_qs.searchString(\'lsjdf "This is the quote with ""embedded"" quotes" sldjf\'))

    prints::

        [[\'This is the quote\']]
        [[\'This is the "quote"\']]
        [[\'This is the quote with "embedded" quotes\']]
    '''
    quoteChar: Incomplete
    quoteCharLen: Incomplete
    firstQuoteChar: Incomplete
    endQuoteChar: Incomplete
    endQuoteCharLen: Incomplete
    escChar: Incomplete
    escQuote: Incomplete
    unquoteResults: Incomplete
    convertWhitespaceEscapes: Incomplete
    flags: Incomplete
    pattern: Incomplete
    escCharReplacePattern: Incomplete
    re: Incomplete
    reString: Incomplete
    re_match: Incomplete
    name: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    mayReturnEmpty: bool
    def __init__(self, quoteChar, escChar=None, escQuote=None, multiline: bool = False, unquoteResults: bool = True, endQuoteChar=None, convertWhitespaceEscapes: bool = True) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class CharsNotIn(Token):
    '''Token for matching words composed of characters *not* in a given
    set (will include whitespace in matched characters if not listed in
    the provided exclusion set - see example). Defined with string
    containing all disallowed characters, and an optional minimum,
    maximum, and/or exact length.  The default value for ``min`` is
    1 (a minimum value < 1 is not valid); the default values for
    ``max`` and ``exact`` are 0, meaning no maximum or exact
    length restriction.

    Example::

        # define a comma-separated-value as anything that is not a \',\'
        csv_value = CharsNotIn(\',\')
        print(delimitedList(csv_value).parseString("dkls,lsdkjf,s12 34,@!#,213"))

    prints::

        [\'dkls\', \'lsdkjf\', \'s12 34\', \'@!#\', \'213\']
    '''
    skipWhitespace: bool
    notChars: Incomplete
    minLen: Incomplete
    maxLen: Incomplete
    name: Incomplete
    errmsg: Incomplete
    mayReturnEmpty: Incomplete
    mayIndexError: bool
    def __init__(self, notChars, min: int = 1, max: int = 0, exact: int = 0) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class White(Token):
    '''Special matching class for matching whitespace.  Normally,
    whitespace is ignored by pyparsing grammars.  This class is included
    when some whitespace structures are significant.  Define with
    a string containing the whitespace characters to be matched; default
    is ``" \\t\\r\\n"``.  Also takes optional ``min``,
    ``max``, and ``exact`` arguments, as defined for the
    :class:`Word` class.
    '''
    whiteStrs: Incomplete
    matchWhite: Incomplete
    name: Incomplete
    mayReturnEmpty: bool
    errmsg: Incomplete
    minLen: Incomplete
    maxLen: Incomplete
    def __init__(self, ws: str = ' \t\r\n', min: int = 1, max: int = 0, exact: int = 0) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class _PositionToken(Token):
    name: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    def __init__(self) -> None: ...

class GoToColumn(_PositionToken):
    """Token to advance to a specific column of input text; useful for
    tabular report scraping.
    """
    col: Incomplete
    def __init__(self, colno) -> None: ...
    def preParse(self, instring, loc): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class LineStart(_PositionToken):
    """Matches if current position is at the beginning of a line within
    the parse string

    Example::

        test = '''\\\n        AAA this line
        AAA and this line
          AAA but not this one
        B AAA and definitely not this one
        '''

        for t in (LineStart() + 'AAA' + restOfLine).searchString(test):
            print(t)

    prints::

        ['AAA', ' this line']
        ['AAA', ' and this line']

    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class LineEnd(_PositionToken):
    """Matches if current position is at the end of a line within the
    parse string
    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class StringStart(_PositionToken):
    """Matches if current position is at the beginning of the parse
    string
    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class StringEnd(_PositionToken):
    """Matches if current position is at the end of the parse string
    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class WordStart(_PositionToken):
    """Matches if the current position is at the beginning of a Word,
    and is not preceded by any character in a given set of
    ``wordChars`` (default= ``printables``). To emulate the
    ``\x08`` behavior of regular expressions, use
    ``WordStart(alphanums)``. ``WordStart`` will also match at
    the beginning of the string being parsed, or at the beginning of
    a line.
    """
    wordChars: Incomplete
    errmsg: str
    def __init__(self, wordChars=...) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class WordEnd(_PositionToken):
    """Matches if the current position is at the end of a Word, and is
    not followed by any character in a given set of ``wordChars``
    (default= ``printables``). To emulate the ``\x08`` behavior of
    regular expressions, use ``WordEnd(alphanums)``. ``WordEnd``
    will also match at the end of the string being parsed, or at the end
    of a line.
    """
    wordChars: Incomplete
    skipWhitespace: bool
    errmsg: str
    def __init__(self, wordChars=...) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class ParseExpression(ParserElement):
    """Abstract subclass of ParserElement, for combining and
    post-processing parsed tokens.
    """
    exprs: Incomplete
    callPreparse: bool
    def __init__(self, exprs, savelist: bool = False) -> None: ...
    strRepr: Incomplete
    def append(self, other): ...
    skipWhitespace: bool
    def leaveWhitespace(self):
        """Extends ``leaveWhitespace`` defined in base class, and also invokes ``leaveWhitespace`` on
           all contained expressions."""
    def ignore(self, other): ...
    def __str__(self) -> str: ...
    errmsg: Incomplete
    def streamline(self): ...
    def validate(self, validateTrace=None) -> None: ...
    def copy(self): ...
    def _setResultsName(self, name, listAllMatches: bool = False): ...

class And(ParseExpression):
    '''
    Requires all given :class:`ParseExpression` s to be found in the given order.
    Expressions may be separated by whitespace.
    May be constructed using the ``\'+\'`` operator.
    May also be constructed using the ``\'-\'`` operator, which will
    suppress backtracking.

    Example::

        integer = Word(nums)
        name_expr = OneOrMore(Word(alphas))

        expr = And([integer("id"), name_expr("name"), integer("age")])
        # more easily written as:
        expr = integer("id") + name_expr("name") + integer("age")
    '''
    class _ErrorStop(Empty):
        name: str
        def __init__(self, *args, **kwargs) -> None: ...
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    callPreparse: bool
    def __init__(self, exprs, savelist: bool = True) -> None: ...
    exprs: Incomplete
    def streamline(self): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def __iadd__(self, other): ...
    def checkRecursion(self, parseElementList) -> None: ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class Or(ParseExpression):
    '''Requires that at least one :class:`ParseExpression` is found. If
    two expressions match, the expression that matches the longest
    string will be used. May be constructed using the ``\'^\'``
    operator.

    Example::

        # construct Or using \'^\' operator

        number = Word(nums) ^ Combine(Word(nums) + \'.\' + Word(nums))
        print(number.searchString("123 3.1416 789"))

    prints::

        [[\'123\'], [\'3.1416\'], [\'789\']]
    '''
    mayReturnEmpty: Incomplete
    def __init__(self, exprs, savelist: bool = False) -> None: ...
    saveAsList: Incomplete
    def streamline(self): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def __ixor__(self, other): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...
    def checkRecursion(self, parseElementList) -> None: ...
    def _setResultsName(self, name, listAllMatches: bool = False): ...

class MatchFirst(ParseExpression):
    '''Requires that at least one :class:`ParseExpression` is found. If
    two expressions match, the first one listed is the one that will
    match. May be constructed using the ``\'|\'`` operator.

    Example::

        # construct MatchFirst using \'|\' operator

        # watch the order of expressions to match
        number = Word(nums) | Combine(Word(nums) + \'.\' + Word(nums))
        print(number.searchString("123 3.1416 789")) #  Fail! -> [[\'123\'], [\'3\'], [\'1416\'], [\'789\']]

        # put more selective expression first
        number = Combine(Word(nums) + \'.\' + Word(nums)) | Word(nums)
        print(number.searchString("123 3.1416 789")) #  Better -> [[\'123\'], [\'3.1416\'], [\'789\']]
    '''
    mayReturnEmpty: Incomplete
    def __init__(self, exprs, savelist: bool = False) -> None: ...
    saveAsList: Incomplete
    def streamline(self): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def __ior__(self, other): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...
    def checkRecursion(self, parseElementList) -> None: ...
    def _setResultsName(self, name, listAllMatches: bool = False): ...

class Each(ParseExpression):
    '''Requires all given :class:`ParseExpression` s to be found, but in
    any order. Expressions may be separated by whitespace.

    May be constructed using the ``\'&\'`` operator.

    Example::

        color = oneOf("RED ORANGE YELLOW GREEN BLUE PURPLE BLACK WHITE BROWN")
        shape_type = oneOf("SQUARE CIRCLE TRIANGLE STAR HEXAGON OCTAGON")
        integer = Word(nums)
        shape_attr = "shape:" + shape_type("shape")
        posn_attr = "posn:" + Group(integer("x") + \',\' + integer("y"))("posn")
        color_attr = "color:" + color("color")
        size_attr = "size:" + integer("size")

        # use Each (using operator \'&\') to accept attributes in any order
        # (shape and posn are required, color and size are optional)
        shape_spec = shape_attr & posn_attr & Optional(color_attr) & Optional(size_attr)

        shape_spec.runTests(\'\'\'
            shape: SQUARE color: BLACK posn: 100, 120
            shape: CIRCLE size: 50 color: BLUE posn: 50,80
            color:GREEN size:20 shape:TRIANGLE posn:20,40
            \'\'\'
            )

    prints::

        shape: SQUARE color: BLACK posn: 100, 120
        [\'shape:\', \'SQUARE\', \'color:\', \'BLACK\', \'posn:\', [\'100\', \',\', \'120\']]
        - color: BLACK
        - posn: [\'100\', \',\', \'120\']
          - x: 100
          - y: 120
        - shape: SQUARE


        shape: CIRCLE size: 50 color: BLUE posn: 50,80
        [\'shape:\', \'CIRCLE\', \'size:\', \'50\', \'color:\', \'BLUE\', \'posn:\', [\'50\', \',\', \'80\']]
        - color: BLUE
        - posn: [\'50\', \',\', \'80\']
          - x: 50
          - y: 80
        - shape: CIRCLE
        - size: 50


        color: GREEN size: 20 shape: TRIANGLE posn: 20,40
        [\'color:\', \'GREEN\', \'size:\', \'20\', \'shape:\', \'TRIANGLE\', \'posn:\', [\'20\', \',\', \'40\']]
        - color: GREEN
        - posn: [\'20\', \',\', \'40\']
          - x: 20
          - y: 40
        - shape: TRIANGLE
        - size: 20
    '''
    mayReturnEmpty: Incomplete
    skipWhitespace: bool
    initExprGroups: bool
    saveAsList: bool
    def __init__(self, exprs, savelist: bool = True) -> None: ...
    def streamline(self): ...
    opt1map: Incomplete
    optionals: Incomplete
    multioptionals: Incomplete
    multirequired: Incomplete
    required: Incomplete
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...
    def checkRecursion(self, parseElementList) -> None: ...

class ParseElementEnhance(ParserElement):
    """Abstract subclass of :class:`ParserElement`, for combining and
    post-processing parsed tokens.
    """
    expr: Incomplete
    strRepr: Incomplete
    mayIndexError: Incomplete
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    saveAsList: Incomplete
    callPreparse: Incomplete
    def __init__(self, expr, savelist: bool = False) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def leaveWhitespace(self): ...
    def ignore(self, other): ...
    def streamline(self): ...
    def checkRecursion(self, parseElementList) -> None: ...
    def validate(self, validateTrace=None) -> None: ...
    def __str__(self) -> str: ...

class FollowedBy(ParseElementEnhance):
    '''Lookahead matching of the given parse expression.
    ``FollowedBy`` does *not* advance the parsing position within
    the input string, it only verifies that the specified parse
    expression matches at the current position.  ``FollowedBy``
    always returns a null token list. If any results names are defined
    in the lookahead expression, those *will* be returned for access by
    name.

    Example::

        # use FollowedBy to match a label only if it is followed by a \':\'
        data_word = Word(alphas)
        label = data_word + FollowedBy(\':\')
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word, stopOn=label).setParseAction(\' \'.join))

        OneOrMore(attr_expr).parseString("shape: SQUARE color: BLACK posn: upper left").pprint()

    prints::

        [[\'shape\', \'SQUARE\'], [\'color\', \'BLACK\'], [\'posn\', \'upper left\']]
    '''
    mayReturnEmpty: bool
    def __init__(self, expr) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class PrecededBy(ParseElementEnhance):
    '''Lookbehind matching of the given parse expression.
    ``PrecededBy`` does not advance the parsing position within the
    input string, it only verifies that the specified parse expression
    matches prior to the current position.  ``PrecededBy`` always
    returns a null token list, but if a results name is defined on the
    given expression, it is returned.

    Parameters:

     - expr - expression that must match prior to the current parse
       location
     - retreat - (default= ``None``) - (int) maximum number of characters
       to lookbehind prior to the current parse location

    If the lookbehind expression is a string, Literal, Keyword, or
    a Word or CharsNotIn with a specified exact or maximum length, then
    the retreat parameter is not required. Otherwise, retreat must be
    specified to give a maximum number of characters to look back from
    the current parse position for a lookbehind match.

    Example::

        # VB-style variable names with type prefixes
        int_var = PrecededBy("#") + pyparsing_common.identifier
        str_var = PrecededBy("$") + pyparsing_common.identifier

    '''
    expr: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    exact: bool
    retreat: Incomplete
    errmsg: Incomplete
    skipWhitespace: bool
    def __init__(self, expr, retreat=None) -> None: ...
    def parseImpl(self, instring, loc: int = 0, doActions: bool = True): ...

class NotAny(ParseElementEnhance):
    '''Lookahead to disallow matching with the given parse expression.
    ``NotAny`` does *not* advance the parsing position within the
    input string, it only verifies that the specified parse expression
    does *not* match at the current position.  Also, ``NotAny`` does
    *not* skip over leading whitespace. ``NotAny`` always returns
    a null token list.  May be constructed using the \'~\' operator.

    Example::

        AND, OR, NOT = map(CaselessKeyword, "AND OR NOT".split())

        # take care not to mistake keywords for identifiers
        ident = ~(AND | OR | NOT) + Word(alphas)
        boolean_term = Optional(NOT) + ident

        # very crude boolean expression - to support parenthesis groups and
        # operation hierarchy, use infixNotation
        boolean_expr = boolean_term + ZeroOrMore((AND | OR) + boolean_term)

        # integers that are followed by "." are actually floats
        integer = Word(nums) + ~Char(".")
    '''
    skipWhitespace: bool
    mayReturnEmpty: bool
    errmsg: Incomplete
    def __init__(self, expr) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class _MultipleMatch(ParseElementEnhance):
    saveAsList: bool
    def __init__(self, expr, stopOn=None) -> None: ...
    not_ender: Incomplete
    def stopOn(self, ender): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def _setResultsName(self, name, listAllMatches: bool = False): ...

class OneOrMore(_MultipleMatch):
    '''Repetition of one or more of the given expression.

    Parameters:
     - expr - expression that must match one or more times
     - stopOn - (default= ``None``) - expression for a terminating sentinel
          (only required if the sentinel would ordinarily match the repetition
          expression)

    Example::

        data_word = Word(alphas)
        label = data_word + FollowedBy(\':\')
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word).setParseAction(\' \'.join))

        text = "shape: SQUARE posn: upper left color: BLACK"
        OneOrMore(attr_expr).parseString(text).pprint()  # Fail! read \'color\' as data instead of next label -> [[\'shape\', \'SQUARE color\']]

        # use stopOn attribute for OneOrMore to avoid reading label string as part of the data
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word, stopOn=label).setParseAction(\' \'.join))
        OneOrMore(attr_expr).parseString(text).pprint() # Better -> [[\'shape\', \'SQUARE\'], [\'posn\', \'upper left\'], [\'color\', \'BLACK\']]

        # could also be written as
        (attr_expr * (1,)).parseString(text).pprint()
    '''
    strRepr: Incomplete
    def __str__(self) -> str: ...

class ZeroOrMore(_MultipleMatch):
    """Optional repetition of zero or more of the given expression.

    Parameters:
     - expr - expression that must match zero or more times
     - stopOn - (default= ``None``) - expression for a terminating sentinel
          (only required if the sentinel would ordinarily match the repetition
          expression)

    Example: similar to :class:`OneOrMore`
    """
    mayReturnEmpty: bool
    def __init__(self, expr, stopOn=None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class _NullToken:
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def __str__(self) -> str: ...

class Optional(ParseElementEnhance):
    """Optional matching of the given expression.

    Parameters:
     - expr - expression that must match zero or more times
     - default (optional) - value to be returned if the optional expression is not found.

    Example::

        # US postal code can be a 5-digit zip, plus optional 4-digit qualifier
        zip = Combine(Word(nums, exact=5) + Optional('-' + Word(nums, exact=4)))
        zip.runTests('''
            # traditional ZIP code
            12345

            # ZIP+4 form
            12101-0001

            # invalid ZIP
            98765-
            ''')

    prints::

        # traditional ZIP code
        12345
        ['12345']

        # ZIP+4 form
        12101-0001
        ['12101-0001']

        # invalid ZIP
        98765-
             ^
        FAIL: Expected end of text (at char 5), (line:1, col:6)
    """
    __optionalNotMatched: Incomplete
    saveAsList: Incomplete
    defaultValue: Incomplete
    mayReturnEmpty: bool
    def __init__(self, expr, default=...) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    strRepr: Incomplete
    def __str__(self) -> str: ...

class SkipTo(ParseElementEnhance):
    '''Token for skipping over all undefined text until the matched
    expression is found.

    Parameters:
     - expr - target expression marking the end of the data to be skipped
     - include - (default= ``False``) if True, the target expression is also parsed
          (the skipped text and target expression are returned as a 2-element list).
     - ignore - (default= ``None``) used to define grammars (typically quoted strings and
          comments) that might contain false matches to the target expression
     - failOn - (default= ``None``) define expressions that are not allowed to be
          included in the skipped test; if found before the target expression is found,
          the SkipTo is not a match

    Example::

        report = \'\'\'
            Outstanding Issues Report - 1 Jan 2000

               # | Severity | Description                               |  Days Open
            -----+----------+-------------------------------------------+-----------
             101 | Critical | Intermittent system crash                 |          6
              94 | Cosmetic | Spelling error on Login (\'log|n\')         |         14
              79 | Minor    | System slow when running too many reports |         47
            \'\'\'
        integer = Word(nums)
        SEP = Suppress(\'|\')
        # use SkipTo to simply match everything up until the next SEP
        # - ignore quoted strings, so that a \'|\' character inside a quoted string does not match
        # - parse action will call token.strip() for each matched token, i.e., the description body
        string_data = SkipTo(SEP, ignore=quotedString)
        string_data.setParseAction(tokenMap(str.strip))
        ticket_expr = (integer("issue_num") + SEP
                      + string_data("sev") + SEP
                      + string_data("desc") + SEP
                      + integer("days_open"))

        for tkt in ticket_expr.searchString(report):
            print tkt.dump()

    prints::

        [\'101\', \'Critical\', \'Intermittent system crash\', \'6\']
        - days_open: 6
        - desc: Intermittent system crash
        - issue_num: 101
        - sev: Critical
        [\'94\', \'Cosmetic\', "Spelling error on Login (\'log|n\')", \'14\']
        - days_open: 14
        - desc: Spelling error on Login (\'log|n\')
        - issue_num: 94
        - sev: Cosmetic
        [\'79\', \'Minor\', \'System slow when running too many reports\', \'47\']
        - days_open: 47
        - desc: System slow when running too many reports
        - issue_num: 79
        - sev: Minor
    '''
    ignoreExpr: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    includeMatch: Incomplete
    saveAsList: bool
    failOn: Incomplete
    errmsg: Incomplete
    def __init__(self, other, include: bool = False, ignore=None, failOn=None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Forward(ParseElementEnhance):
    """Forward declaration of an expression to be defined later -
    used for recursive grammars, such as algebraic infix notation.
    When the expression is known, it is assigned to the ``Forward``
    variable using the '<<' operator.

    Note: take care when assigning to ``Forward`` not to overlook
    precedence of operators.

    Specifically, '|' has a lower precedence than '<<', so that::

        fwdExpr << a | b | c

    will actually be evaluated as::

        (fwdExpr << a) | b | c

    thereby leaving b and c out as parseable alternatives.  It is recommended that you
    explicitly group the values inserted into the ``Forward``::

        fwdExpr << (a | b | c)

    Converting to use the '<<=' operator instead will avoid this problem.

    See :class:`ParseResults.pprint` for an example of a recursive
    parser created using ``Forward``.
    """
    def __init__(self, other=None) -> None: ...
    expr: Incomplete
    strRepr: Incomplete
    mayIndexError: Incomplete
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    saveAsList: Incomplete
    def __lshift__(self, other): ...
    def __ilshift__(self, other): ...
    def leaveWhitespace(self): ...
    streamlined: bool
    def streamline(self): ...
    def validate(self, validateTrace=None) -> None: ...
    def __str__(self) -> str: ...
    def copy(self): ...
    def _setResultsName(self, name, listAllMatches: bool = False): ...

class TokenConverter(ParseElementEnhance):
    """
    Abstract subclass of :class:`ParseExpression`, for converting parsed results.
    """
    saveAsList: bool
    def __init__(self, expr, savelist: bool = False) -> None: ...

class Combine(TokenConverter):
    """Converter to concatenate all matching tokens to a single string.
    By default, the matching patterns must also be contiguous in the
    input string; this can be disabled by specifying
    ``'adjacent=False'`` in the constructor.

    Example::

        real = Word(nums) + '.' + Word(nums)
        print(real.parseString('3.1416')) # -> ['3', '.', '1416']
        # will also erroneously match the following
        print(real.parseString('3. 1416')) # -> ['3', '.', '1416']

        real = Combine(Word(nums) + '.' + Word(nums))
        print(real.parseString('3.1416')) # -> ['3.1416']
        # no match when there are internal spaces
        print(real.parseString('3. 1416')) # -> Exception: Expected W:(0123...)
    """
    adjacent: Incomplete
    skipWhitespace: bool
    joinString: Incomplete
    callPreparse: bool
    def __init__(self, expr, joinString: str = '', adjacent: bool = True) -> None: ...
    def ignore(self, other): ...
    def postParse(self, instring, loc, tokenlist): ...

class Group(TokenConverter):
    '''Converter to return the matched tokens as a list - useful for
    returning tokens of :class:`ZeroOrMore` and :class:`OneOrMore` expressions.

    Example::

        ident = Word(alphas)
        num = Word(nums)
        term = ident | num
        func = ident + Optional(delimitedList(term))
        print(func.parseString("fn a, b, 100"))  # -> [\'fn\', \'a\', \'b\', \'100\']

        func = ident + Group(Optional(delimitedList(term)))
        print(func.parseString("fn a, b, 100"))  # -> [\'fn\', [\'a\', \'b\', \'100\']]
    '''
    saveAsList: bool
    def __init__(self, expr) -> None: ...
    def postParse(self, instring, loc, tokenlist): ...

class Dict(TokenConverter):
    '''Converter to return a repetitive expression as a list, but also
    as a dictionary. Each element can also be referenced using the first
    token in the expression as its key. Useful for tabular report
    scraping when the first column can be used as a item key.

    Example::

        data_word = Word(alphas)
        label = data_word + FollowedBy(\':\')
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word).setParseAction(\' \'.join))

        text = "shape: SQUARE posn: upper left color: light blue texture: burlap"
        attr_expr = (label + Suppress(\':\') + OneOrMore(data_word, stopOn=label).setParseAction(\' \'.join))

        # print attributes as plain groups
        print(OneOrMore(attr_expr).parseString(text).dump())

        # instead of OneOrMore(expr), parse using Dict(OneOrMore(Group(expr))) - Dict will auto-assign names
        result = Dict(OneOrMore(Group(attr_expr))).parseString(text)
        print(result.dump())

        # access named fields as dict entries, or output as dict
        print(result[\'shape\'])
        print(result.asDict())

    prints::

        [\'shape\', \'SQUARE\', \'posn\', \'upper left\', \'color\', \'light blue\', \'texture\', \'burlap\']
        [[\'shape\', \'SQUARE\'], [\'posn\', \'upper left\'], [\'color\', \'light blue\'], [\'texture\', \'burlap\']]
        - color: light blue
        - posn: upper left
        - shape: SQUARE
        - texture: burlap
        SQUARE
        {\'color\': \'light blue\', \'posn\': \'upper left\', \'texture\': \'burlap\', \'shape\': \'SQUARE\'}

    See more examples at :class:`ParseResults` of accessing fields by results name.
    '''
    saveAsList: bool
    def __init__(self, expr) -> None: ...
    def postParse(self, instring, loc, tokenlist): ...

class Suppress(TokenConverter):
    '''Converter for ignoring the results of a parsed expression.

    Example::

        source = "a, b, c,d"
        wd = Word(alphas)
        wd_list1 = wd + ZeroOrMore(\',\' + wd)
        print(wd_list1.parseString(source))

        # often, delimiters that are useful during parsing are just in the
        # way afterward - use Suppress to keep them out of the parsed output
        wd_list2 = wd + ZeroOrMore(Suppress(\',\') + wd)
        print(wd_list2.parseString(source))

    prints::

        [\'a\', \',\', \'b\', \',\', \'c\', \',\', \'d\']
        [\'a\', \'b\', \'c\', \'d\']

    (See also :class:`delimitedList`.)
    '''
    def postParse(self, instring, loc, tokenlist): ...
    def suppress(self): ...

class OnlyOnce:
    """Wrapper for parse actions, to ensure they are only called once.
    """
    callable: Incomplete
    called: bool
    def __init__(self, methodCall) -> None: ...
    def __call__(self, s, l, t): ...
    def reset(self) -> None: ...

def traceParseAction(f):
    '''Decorator for debugging parse actions.

    When the parse action is called, this decorator will print
    ``">> entering method-name(line:<current_source_line>, <parse_location>, <matched_tokens>)"``.
    When the parse action completes, the decorator will print
    ``"<<"`` followed by the returned value, or any exception that the parse action raised.

    Example::

        wd = Word(alphas)

        @traceParseAction
        def remove_duplicate_chars(tokens):
            return \'\'.join(sorted(set(\'\'.join(tokens))))

        wds = OneOrMore(wd).setParseAction(remove_duplicate_chars)
        print(wds.parseString("slkdjs sld sldd sdlf sdljf"))

    prints::

        >>entering remove_duplicate_chars(line: \'slkdjs sld sldd sdlf sdljf\', 0, ([\'slkdjs\', \'sld\', \'sldd\', \'sdlf\', \'sdljf\'], {}))
        <<leaving remove_duplicate_chars (ret: \'dfjkls\')
        [\'dfjkls\']
    '''
def delimitedList(expr, delim: str = ',', combine: bool = False):
    '''Helper to define a delimited list of expressions - the delimiter
    defaults to \',\'. By default, the list elements and delimiters can
    have intervening whitespace, and comments, but this can be
    overridden by passing ``combine=True`` in the constructor. If
    ``combine`` is set to ``True``, the matching tokens are
    returned as a single token string, with the delimiters included;
    otherwise, the matching tokens are returned as a list of tokens,
    with the delimiters suppressed.

    Example::

        delimitedList(Word(alphas)).parseString("aa,bb,cc") # -> [\'aa\', \'bb\', \'cc\']
        delimitedList(Word(hexnums), delim=\':\', combine=True).parseString("AA:BB:CC:DD:EE") # -> [\'AA:BB:CC:DD:EE\']
    '''
def countedArray(expr, intExpr=None):
    """Helper to define a counted list of expressions.

    This helper defines a pattern of the form::

        integer expr expr expr...

    where the leading integer tells how many expr expressions follow.
    The matched tokens returns the array of expr tokens as a list - the
    leading count token is suppressed.

    If ``intExpr`` is specified, it should be a pyparsing expression
    that produces an integer value.

    Example::

        countedArray(Word(alphas)).parseString('2 ab cd ef')  # -> ['ab', 'cd']

        # in this parser, the leading integer value is given in binary,
        # '10' indicating that 2 values are in the array
        binaryConstant = Word('01').setParseAction(lambda t: int(t[0], 2))
        countedArray(Word(alphas), intExpr=binaryConstant).parseString('10 ab cd ef')  # -> ['ab', 'cd']
    """
def matchPreviousLiteral(expr):
    '''Helper to define an expression that is indirectly defined from
    the tokens matched in a previous expression, that is, it looks for
    a \'repeat\' of a previous expression.  For example::

        first = Word(nums)
        second = matchPreviousLiteral(first)
        matchExpr = first + ":" + second

    will match ``"1:1"``, but not ``"1:2"``.  Because this
    matches a previous literal, will also match the leading
    ``"1:1"`` in ``"1:10"``. If this is not desired, use
    :class:`matchPreviousExpr`. Do *not* use with packrat parsing
    enabled.
    '''
def matchPreviousExpr(expr):
    '''Helper to define an expression that is indirectly defined from
    the tokens matched in a previous expression, that is, it looks for
    a \'repeat\' of a previous expression.  For example::

        first = Word(nums)
        second = matchPreviousExpr(first)
        matchExpr = first + ":" + second

    will match ``"1:1"``, but not ``"1:2"``.  Because this
    matches by expressions, will *not* match the leading ``"1:1"``
    in ``"1:10"``; the expressions are evaluated first, and then
    compared, so ``"1"`` is compared with ``"10"``. Do *not* use
    with packrat parsing enabled.
    '''
def oneOf(strs, caseless: bool = False, useRegex: bool = True, asKeyword: bool = False):
    '''Helper to quickly define a set of alternative Literals, and makes
    sure to do longest-first testing when there is a conflict,
    regardless of the input order, but returns
    a :class:`MatchFirst` for best performance.

    Parameters:

     - strs - a string of space-delimited literals, or a collection of
       string literals
     - caseless - (default= ``False``) - treat all literals as
       caseless
     - useRegex - (default= ``True``) - as an optimization, will
       generate a Regex object; otherwise, will generate
       a :class:`MatchFirst` object (if ``caseless=True`` or ``asKeyword=True``, or if
       creating a :class:`Regex` raises an exception)
     - asKeyword - (default=``False``) - enforce Keyword-style matching on the
       generated expressions

    Example::

        comp_oper = oneOf("< = > <= >= !=")
        var = Word(alphas)
        number = Word(nums)
        term = var | number
        comparison_expr = term + comp_oper + term
        print(comparison_expr.searchString("B = 12  AA=23 B<=AA AA>12"))

    prints::

        [[\'B\', \'=\', \'12\'], [\'AA\', \'=\', \'23\'], [\'B\', \'<=\', \'AA\'], [\'AA\', \'>\', \'12\']]
    '''
def dictOf(key, value):
    '''Helper to easily and clearly define a dictionary by specifying
    the respective patterns for the key and value.  Takes care of
    defining the :class:`Dict`, :class:`ZeroOrMore`, and
    :class:`Group` tokens in the proper order.  The key pattern
    can include delimiting markers or punctuation, as long as they are
    suppressed, thereby leaving the significant key text.  The value
    pattern can include named results, so that the :class:`Dict` results
    can include named token fields.

    Example::

        text = "shape: SQUARE posn: upper left color: light blue texture: burlap"
        attr_expr = (label + Suppress(\':\') + OneOrMore(data_word, stopOn=label).setParseAction(\' \'.join))
        print(OneOrMore(attr_expr).parseString(text).dump())

        attr_label = label
        attr_value = Suppress(\':\') + OneOrMore(data_word, stopOn=label).setParseAction(\' \'.join)

        # similar to Dict, but simpler call format
        result = dictOf(attr_label, attr_value).parseString(text)
        print(result.dump())
        print(result[\'shape\'])
        print(result.shape)  # object attribute access works too
        print(result.asDict())

    prints::

        [[\'shape\', \'SQUARE\'], [\'posn\', \'upper left\'], [\'color\', \'light blue\'], [\'texture\', \'burlap\']]
        - color: light blue
        - posn: upper left
        - shape: SQUARE
        - texture: burlap
        SQUARE
        SQUARE
        {\'color\': \'light blue\', \'shape\': \'SQUARE\', \'posn\': \'upper left\', \'texture\': \'burlap\'}
    '''
def originalTextFor(expr, asString: bool = True):
    '''Helper to return the original, untokenized text for a given
    expression.  Useful to restore the parsed fields of an HTML start
    tag into the raw tag text itself, or to revert separate tokens with
    intervening whitespace back to the original matching input text. By
    default, returns astring containing the original parsed text.

    If the optional ``asString`` argument is passed as
    ``False``, then the return value is
    a :class:`ParseResults` containing any results names that
    were originally matched, and a single token containing the original
    matched text from the input string.  So if the expression passed to
    :class:`originalTextFor` contains expressions with defined
    results names, you must set ``asString`` to ``False`` if you
    want to preserve those results name values.

    Example::

        src = "this is test <b> bold <i>text</i> </b> normal text "
        for tag in ("b", "i"):
            opener, closer = makeHTMLTags(tag)
            patt = originalTextFor(opener + SkipTo(closer) + closer)
            print(patt.searchString(src)[0])

    prints::

        [\'<b> bold <i>text</i> </b>\']
        [\'<i>text</i>\']
    '''
def ungroup(expr):
    """Helper to undo pyparsing's default grouping of And expressions,
    even if all but one are non-empty.
    """
def locatedExpr(expr):
    '''Helper to decorate a returned token with its starting and ending
    locations in the input string.

    This helper adds the following results names:

     - locn_start = location where matched expression begins
     - locn_end = location where matched expression ends
     - value = the actual parsed results

    Be careful if the input text contains ``<TAB>`` characters, you
    may want to call :class:`ParserElement.parseWithTabs`

    Example::

        wd = Word(alphas)
        for match in locatedExpr(wd).searchString("ljsdf123lksdjjf123lkkjj1222"):
            print(match)

    prints::

        [[0, \'ljsdf\', 5]]
        [[8, \'lksdjjf\', 15]]
        [[18, \'lkkjj\', 23]]
    '''

empty: Incomplete
lineStart: Incomplete
lineEnd: Incomplete
stringStart: Incomplete
stringEnd: Incomplete

def srange(s):
    '''Helper to easily define string ranges for use in Word
    construction. Borrows syntax from regexp \'[]\' string range
    definitions::

        srange("[0-9]")   -> "0123456789"
        srange("[a-z]")   -> "abcdefghijklmnopqrstuvwxyz"
        srange("[a-z$_]") -> "abcdefghijklmnopqrstuvwxyz$_"

    The input string must be enclosed in []\'s, and the returned string
    is the expanded character set joined into a single string. The
    values enclosed in the []\'s may be:

     - a single character
     - an escaped character with a leading backslash (such as ``\\-``
       or ``\\]``)
     - an escaped hex character with a leading ``\'\\x\'``
       (``\\x21``, which is a ``\'!\'`` character) (``\\0x##``
       is also supported for backwards compatibility)
     - an escaped octal character with a leading ``\'\\0\'``
       (``\\041``, which is a ``\'!\'`` character)
     - a range of any of the above, separated by a dash (``\'a-z\'``,
       etc.)
     - any combination of the above (``\'aeiouy\'``,
       ``\'a-zA-Z0-9_$\'``, etc.)
    '''
def matchOnlyAtCol(n):
    """Helper method for defining parse actions that require matching at
    a specific column in the input text.
    """
def replaceWith(replStr):
    '''Helper method for common parse actions that simply return
    a literal value.  Especially useful when used with
    :class:`transformString<ParserElement.transformString>` ().

    Example::

        num = Word(nums).setParseAction(lambda toks: int(toks[0]))
        na = oneOf("N/A NA").setParseAction(replaceWith(math.nan))
        term = na | num

        OneOrMore(term).parseString("324 234 N/A 234") # -> [324, 234, nan, 234]
    '''
def removeQuotes(s, l, t):
    '''Helper parse action for removing quotation marks from parsed
    quoted strings.

    Example::

        # by default, quotation marks are included in parsed results
        quotedString.parseString("\'Now is the Winter of our Discontent\'") # -> ["\'Now is the Winter of our Discontent\'"]

        # use removeQuotes to strip quotation marks from parsed results
        quotedString.setParseAction(removeQuotes)
        quotedString.parseString("\'Now is the Winter of our Discontent\'") # -> ["Now is the Winter of our Discontent"]
    '''
def tokenMap(func, *args):
    """Helper to define a parse action by mapping a function to all
    elements of a ParseResults list. If any additional args are passed,
    they are forwarded to the given function as additional arguments
    after the token, as in
    ``hex_integer = Word(hexnums).setParseAction(tokenMap(int, 16))``,
    which will convert the parsed data to an integer using base 16.

    Example (compare the last to example in :class:`ParserElement.transformString`::

        hex_ints = OneOrMore(Word(hexnums)).setParseAction(tokenMap(int, 16))
        hex_ints.runTests('''
            00 11 22 aa FF 0a 0d 1a
            ''')

        upperword = Word(alphas).setParseAction(tokenMap(str.upper))
        OneOrMore(upperword).runTests('''
            my kingdom for a horse
            ''')

        wd = Word(alphas).setParseAction(tokenMap(str.title))
        OneOrMore(wd).setParseAction(' '.join).runTests('''
            now is the winter of our discontent made glorious summer by this sun of york
            ''')

    prints::

        00 11 22 aa FF 0a 0d 1a
        [0, 17, 34, 170, 255, 10, 13, 26]

        my kingdom for a horse
        ['MY', 'KINGDOM', 'FOR', 'A', 'HORSE']

        now is the winter of our discontent made glorious summer by this sun of york
        ['Now Is The Winter Of Our Discontent Made Glorious Summer By This Sun Of York']
    """

upcaseTokens: Incomplete
downcaseTokens: Incomplete

def makeHTMLTags(tagStr):
    '''Helper to construct opening and closing tag expressions for HTML,
    given a tag name. Matches tags in either upper or lower case,
    attributes with namespaces and with quoted or unquoted values.

    Example::

        text = \'<td>More info at the <a href="https://github.com/pyparsing/pyparsing/wiki">pyparsing</a> wiki page</td>\'
        # makeHTMLTags returns pyparsing expressions for the opening and
        # closing tags as a 2-tuple
        a, a_end = makeHTMLTags("A")
        link_expr = a + SkipTo(a_end)("link_text") + a_end

        for link in link_expr.searchString(text):
            # attributes in the <A> tag (like "href" shown here) are
            # also accessible as named results
            print(link.link_text, \'->\', link.href)

    prints::

        pyparsing -> https://github.com/pyparsing/pyparsing/wiki
    '''
def makeXMLTags(tagStr):
    """Helper to construct opening and closing tag expressions for XML,
    given a tag name. Matches tags only in the given upper/lower case.

    Example: similar to :class:`makeHTMLTags`
    """
def withAttribute(*args, **attrDict):
    '''Helper to create a validating parse action to be used with start
    tags created with :class:`makeXMLTags` or
    :class:`makeHTMLTags`. Use ``withAttribute`` to qualify
    a starting tag with a required attribute value, to avoid false
    matches on common tags such as ``<TD>`` or ``<DIV>``.

    Call ``withAttribute`` with a series of attribute names and
    values. Specify the list of filter attributes names and values as:

     - keyword arguments, as in ``(align="right")``, or
     - as an explicit dict with ``**`` operator, when an attribute
       name is also a Python reserved word, as in ``**{"class":"Customer", "align":"right"}``
     - a list of name-value tuples, as in ``(("ns1:class", "Customer"), ("ns2:align", "right"))``

    For attribute names with a namespace prefix, you must use the second
    form.  Attribute names are matched insensitive to upper/lower case.

    If just testing for ``class`` (with or without a namespace), use
    :class:`withClass`.

    To verify that the attribute exists, but without specifying a value,
    pass ``withAttribute.ANY_VALUE`` as the value.

    Example::

        html = \'\'\'
            <div>
            Some text
            <div type="grid">1 4 0 1 0</div>
            <div type="graph">1,3 2,3 1,1</div>
            <div>this has no type</div>
            </div>

        \'\'\'
        div,div_end = makeHTMLTags("div")

        # only match div tag having a type attribute with value "grid"
        div_grid = div().setParseAction(withAttribute(type="grid"))
        grid_expr = div_grid + SkipTo(div | div_end)("body")
        for grid_header in grid_expr.searchString(html):
            print(grid_header.body)

        # construct a match with any div tag having a type attribute, regardless of the value
        div_any_type = div().setParseAction(withAttribute(type=withAttribute.ANY_VALUE))
        div_expr = div_any_type + SkipTo(div | div_end)("body")
        for div_header in div_expr.searchString(html):
            print(div_header.body)

    prints::

        1 4 0 1 0

        1 4 0 1 0
        1,3 2,3 1,1
    '''
def withClass(classname, namespace: str = ''):
    '''Simplified version of :class:`withAttribute` when
    matching on a div class - made difficult because ``class`` is
    a reserved word in Python.

    Example::

        html = \'\'\'
            <div>
            Some text
            <div class="grid">1 4 0 1 0</div>
            <div class="graph">1,3 2,3 1,1</div>
            <div>this &lt;div&gt; has no class</div>
            </div>

        \'\'\'
        div,div_end = makeHTMLTags("div")
        div_grid = div().setParseAction(withClass("grid"))

        grid_expr = div_grid + SkipTo(div | div_end)("body")
        for grid_header in grid_expr.searchString(html):
            print(grid_header.body)

        div_any_type = div().setParseAction(withClass(withAttribute.ANY_VALUE))
        div_expr = div_any_type + SkipTo(div | div_end)("body")
        for div_header in div_expr.searchString(html):
            print(div_header.body)

    prints::

        1 4 0 1 0

        1 4 0 1 0
        1,3 2,3 1,1
    '''

opAssoc: Incomplete

def infixNotation(baseExpr, opList, lpar=..., rpar=...):
    """Helper method for constructing grammars of expressions made up of
    operators working in a precedence hierarchy.  Operators may be unary
    or binary, left- or right-associative.  Parse actions can also be
    attached to operator expressions. The generated parser will also
    recognize the use of parentheses to override operator precedences
    (see example below).

    Note: if you define a deep operator list, you may see performance
    issues when using infixNotation. See
    :class:`ParserElement.enablePackrat` for a mechanism to potentially
    improve your parser performance.

    Parameters:
     - baseExpr - expression representing the most basic element for the
       nested
     - opList - list of tuples, one for each operator precedence level
       in the expression grammar; each tuple is of the form ``(opExpr,
       numTerms, rightLeftAssoc, parseAction)``, where:

       - opExpr is the pyparsing expression for the operator; may also
         be a string, which will be converted to a Literal; if numTerms
         is 3, opExpr is a tuple of two expressions, for the two
         operators separating the 3 terms
       - numTerms is the number of terms for this operator (must be 1,
         2, or 3)
       - rightLeftAssoc is the indicator whether the operator is right
         or left associative, using the pyparsing-defined constants
         ``opAssoc.RIGHT`` and ``opAssoc.LEFT``.
       - parseAction is the parse action to be associated with
         expressions matching this operator expression (the parse action
         tuple member may be omitted); if the parse action is passed
         a tuple or list of functions, this is equivalent to calling
         ``setParseAction(*fn)``
         (:class:`ParserElement.setParseAction`)
     - lpar - expression for matching left-parentheses
       (default= ``Suppress('(')``)
     - rpar - expression for matching right-parentheses
       (default= ``Suppress(')')``)

    Example::

        # simple example of four-function arithmetic with ints and
        # variable names
        integer = pyparsing_common.signed_integer
        varname = pyparsing_common.identifier

        arith_expr = infixNotation(integer | varname,
            [
            ('-', 1, opAssoc.RIGHT),
            (oneOf('* /'), 2, opAssoc.LEFT),
            (oneOf('+ -'), 2, opAssoc.LEFT),
            ])

        arith_expr.runTests('''
            5+3*6
            (5+3)*6
            -2--11
            ''', fullDump=False)

    prints::

        5+3*6
        [[5, '+', [3, '*', 6]]]

        (5+3)*6
        [[[5, '+', 3], '*', 6]]

        -2--11
        [[['-', 2], '-', ['-', 11]]]
    """
operatorPrecedence = infixNotation
dblQuotedString: Incomplete
sglQuotedString: Incomplete
quotedString: Incomplete
unicodeString: Incomplete

def nestedExpr(opener: str = '(', closer: str = ')', content=None, ignoreExpr=...):
    '''Helper method for defining nested lists enclosed in opening and
    closing delimiters ("(" and ")" are the default).

    Parameters:
     - opener - opening character for a nested list
       (default= ``"("``); can also be a pyparsing expression
     - closer - closing character for a nested list
       (default= ``")"``); can also be a pyparsing expression
     - content - expression for items within the nested lists
       (default= ``None``)
     - ignoreExpr - expression for ignoring opening and closing
       delimiters (default= :class:`quotedString`)

    If an expression is not provided for the content argument, the
    nested expression will capture all whitespace-delimited content
    between delimiters as a list of separate values.

    Use the ``ignoreExpr`` argument to define expressions that may
    contain opening or closing characters that should not be treated as
    opening or closing characters for nesting, such as quotedString or
    a comment expression.  Specify multiple expressions using an
    :class:`Or` or :class:`MatchFirst`. The default is
    :class:`quotedString`, but if no expressions are to be ignored, then
    pass ``None`` for this argument.

    Example::

        data_type = oneOf("void int short long char float double")
        decl_data_type = Combine(data_type + Optional(Word(\'*\')))
        ident = Word(alphas+\'_\', alphanums+\'_\')
        number = pyparsing_common.number
        arg = Group(decl_data_type + ident)
        LPAR, RPAR = map(Suppress, "()")

        code_body = nestedExpr(\'{\', \'}\', ignoreExpr=(quotedString | cStyleComment))

        c_function = (decl_data_type("type")
                      + ident("name")
                      + LPAR + Optional(delimitedList(arg), [])("args") + RPAR
                      + code_body("body"))
        c_function.ignore(cStyleComment)

        source_code = \'\'\'
            int is_odd(int x) {
                return (x%2);
            }

            int dec_to_hex(char hchar) {
                if (hchar >= \'0\' && hchar <= \'9\') {
                    return (ord(hchar)-ord(\'0\'));
                } else {
                    return (10+ord(hchar)-ord(\'A\'));
                }
            }
        \'\'\'
        for func in c_function.searchString(source_code):
            print("%(name)s (%(type)s) args: %(args)s" % func)


    prints::

        is_odd (int) args: [[\'int\', \'x\']]
        dec_to_hex (int) args: [[\'char\', \'hchar\']]
    '''
def indentedBlock(blockStatementExpr, indentStack, indent: bool = True):
    '''Helper method for defining space-delimited indentation blocks,
    such as those used to define block statements in Python source code.

    Parameters:

     - blockStatementExpr - expression defining syntax of statement that
       is repeated within the indented block
     - indentStack - list created by caller to manage indentation stack
       (multiple statementWithIndentedBlock expressions within a single
       grammar should share a common indentStack)
     - indent - boolean indicating whether block must be indented beyond
       the current level; set to False for block of left-most
       statements (default= ``True``)

    A valid block must contain at least one ``blockStatement``.

    Example::

        data = \'\'\'
        def A(z):
          A1
          B = 100
          G = A2
          A2
          A3
        B
        def BB(a,b,c):
          BB1
          def BBA():
            bba1
            bba2
            bba3
        C
        D
        def spam(x,y):
             def eggs(z):
                 pass
        \'\'\'


        indentStack = [1]
        stmt = Forward()

        identifier = Word(alphas, alphanums)
        funcDecl = ("def" + identifier + Group("(" + Optional(delimitedList(identifier)) + ")") + ":")
        func_body = indentedBlock(stmt, indentStack)
        funcDef = Group(funcDecl + func_body)

        rvalue = Forward()
        funcCall = Group(identifier + "(" + Optional(delimitedList(rvalue)) + ")")
        rvalue << (funcCall | identifier | Word(nums))
        assignment = Group(identifier + "=" + rvalue)
        stmt << (funcDef | assignment | identifier)

        module_body = OneOrMore(stmt)

        parseTree = module_body.parseString(data)
        parseTree.pprint()

    prints::

        [[\'def\',
          \'A\',
          [\'(\', \'z\', \')\'],
          \':\',
          [[\'A1\'], [[\'B\', \'=\', \'100\']], [[\'G\', \'=\', \'A2\']], [\'A2\'], [\'A3\']]],
         \'B\',
         [\'def\',
          \'BB\',
          [\'(\', \'a\', \'b\', \'c\', \')\'],
          \':\',
          [[\'BB1\'], [[\'def\', \'BBA\', [\'(\', \')\'], \':\', [[\'bba1\'], [\'bba2\'], [\'bba3\']]]]]],
         \'C\',
         \'D\',
         [\'def\',
          \'spam\',
          [\'(\', \'x\', \'y\', \')\'],
          \':\',
          [[[\'def\', \'eggs\', [\'(\', \'z\', \')\'], \':\', [[\'pass\']]]]]]]
    '''

alphas8bit: Incomplete
punc8bit: Incomplete
anyOpenTag: Incomplete
anyCloseTag: Incomplete
commonHTMLEntity: Incomplete

def replaceHTMLEntity(t):
    """Helper parser action to replace common HTML entities with their special characters"""

cStyleComment: Incomplete
htmlComment: Incomplete
restOfLine: Incomplete
dblSlashComment: Incomplete
cppStyleComment: Incomplete
javaStyleComment = cppStyleComment
pythonStyleComment: Incomplete
commaSeparatedList: Incomplete

class pyparsing_common:
    """Here are some common low-level expressions that may be useful in
    jump-starting parser development:

     - numeric forms (:class:`integers<integer>`, :class:`reals<real>`,
       :class:`scientific notation<sci_real>`)
     - common :class:`programming identifiers<identifier>`
     - network addresses (:class:`MAC<mac_address>`,
       :class:`IPv4<ipv4_address>`, :class:`IPv6<ipv6_address>`)
     - ISO8601 :class:`dates<iso8601_date>` and
       :class:`datetime<iso8601_datetime>`
     - :class:`UUID<uuid>`
     - :class:`comma-separated list<comma_separated_list>`

    Parse actions:

     - :class:`convertToInteger`
     - :class:`convertToFloat`
     - :class:`convertToDate`
     - :class:`convertToDatetime`
     - :class:`stripHTMLTags`
     - :class:`upcaseTokens`
     - :class:`downcaseTokens`

    Example::

        pyparsing_common.number.runTests('''
            # any int or real number, returned as the appropriate type
            100
            -100
            +100
            3.14159
            6.02e23
            1e-12
            ''')

        pyparsing_common.fnumber.runTests('''
            # any int or real number, returned as float
            100
            -100
            +100
            3.14159
            6.02e23
            1e-12
            ''')

        pyparsing_common.hex_integer.runTests('''
            # hex numbers
            100
            FF
            ''')

        pyparsing_common.fraction.runTests('''
            # fractions
            1/2
            -3/4
            ''')

        pyparsing_common.mixed_integer.runTests('''
            # mixed fractions
            1
            1/2
            -3/4
            1-3/4
            ''')

        import uuid
        pyparsing_common.uuid.setParseAction(tokenMap(uuid.UUID))
        pyparsing_common.uuid.runTests('''
            # uuid
            12345678-1234-5678-1234-567812345678
            ''')

    prints::

        # any int or real number, returned as the appropriate type
        100
        [100]

        -100
        [-100]

        +100
        [100]

        3.14159
        [3.14159]

        6.02e23
        [6.02e+23]

        1e-12
        [1e-12]

        # any int or real number, returned as float
        100
        [100.0]

        -100
        [-100.0]

        +100
        [100.0]

        3.14159
        [3.14159]

        6.02e23
        [6.02e+23]

        1e-12
        [1e-12]

        # hex numbers
        100
        [256]

        FF
        [255]

        # fractions
        1/2
        [0.5]

        -3/4
        [-0.75]

        # mixed fractions
        1
        [1]

        1/2
        [0.5]

        -3/4
        [-0.75]

        1-3/4
        [1.75]

        # uuid
        12345678-1234-5678-1234-567812345678
        [UUID('12345678-1234-5678-1234-567812345678')]
    """
    convertToInteger: Incomplete
    convertToFloat: Incomplete
    integer: Incomplete
    hex_integer: Incomplete
    signed_integer: Incomplete
    fraction: Incomplete
    mixed_integer: Incomplete
    real: Incomplete
    sci_real: Incomplete
    number: Incomplete
    fnumber: Incomplete
    identifier: Incomplete
    ipv4_address: Incomplete
    _ipv6_part: Incomplete
    _full_ipv6_address: Incomplete
    _short_ipv6_address: Incomplete
    _mixed_ipv6_address: Incomplete
    ipv6_address: Incomplete
    mac_address: Incomplete
    @staticmethod
    def convertToDate(fmt: str = '%Y-%m-%d'):
        '''
        Helper to create a parse action for converting parsed date string to Python datetime.date

        Params -
         - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%d"``)

        Example::

            date_expr = pyparsing_common.iso8601_date.copy()
            date_expr.setParseAction(pyparsing_common.convertToDate())
            print(date_expr.parseString("1999-12-31"))

        prints::

            [datetime.date(1999, 12, 31)]
        '''
    @staticmethod
    def convertToDatetime(fmt: str = '%Y-%m-%dT%H:%M:%S.%f'):
        '''Helper to create a parse action for converting parsed
        datetime string to Python datetime.datetime

        Params -
         - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%dT%H:%M:%S.%f"``)

        Example::

            dt_expr = pyparsing_common.iso8601_datetime.copy()
            dt_expr.setParseAction(pyparsing_common.convertToDatetime())
            print(dt_expr.parseString("1999-12-31T23:59:59.999"))

        prints::

            [datetime.datetime(1999, 12, 31, 23, 59, 59, 999000)]
        '''
    iso8601_date: Incomplete
    iso8601_datetime: Incomplete
    uuid: Incomplete
    _html_stripper: Incomplete
    @staticmethod
    def stripHTMLTags(s, l, tokens):
        '''Parse action to remove HTML tags from web page HTML source

        Example::

            # strip HTML links from normal text
            text = \'<td>More info at the <a href="https://github.com/pyparsing/pyparsing/wiki">pyparsing</a> wiki page</td>\'
            td, td_end = makeHTMLTags("TD")
            table_text = td + SkipTo(td_end).setParseAction(pyparsing_common.stripHTMLTags)("body") + td_end
            print(table_text.parseString(text).body)

        Prints::

            More info at the pyparsing wiki page
        '''
    _commasepitem: Incomplete
    comma_separated_list: Incomplete
    upcaseTokens: Incomplete
    downcaseTokens: Incomplete

class _lazyclassproperty:
    fn: Incomplete
    __doc__: Incomplete
    __name__: Incomplete
    def __init__(self, fn) -> None: ...
    def __get__(self, obj, cls): ...

class unicode_set:
    """
    A set of Unicode characters, for language-specific strings for
    ``alphas``, ``nums``, ``alphanums``, and ``printables``.
    A unicode_set is defined by a list of ranges in the Unicode character
    set, in a class attribute ``_ranges``, such as::

        _ranges = [(0x0020, 0x007e), (0x00a0, 0x00ff),]

    A unicode set can also be defined using multiple inheritance of other unicode sets::

        class CJK(Chinese, Japanese, Korean):
            pass
    """
    _ranges: Incomplete
    @classmethod
    def _get_chars_for_ranges(cls): ...
    @_lazyclassproperty
    def printables(cls):
        """all non-whitespace characters in this range"""
    @_lazyclassproperty
    def alphas(cls):
        """all alphabetic characters in this range"""
    @_lazyclassproperty
    def nums(cls):
        """all numeric digit characters in this range"""
    @_lazyclassproperty
    def alphanums(cls):
        """all alphanumeric characters in this range"""

class pyparsing_unicode(unicode_set):
    """
    A namespace class for defining common language unicode_sets.
    """
    _ranges: Incomplete
    class Latin1(unicode_set):
        """Unicode set for Latin-1 Unicode Character Range"""
        _ranges: Incomplete
    class LatinA(unicode_set):
        """Unicode set for Latin-A Unicode Character Range"""
        _ranges: Incomplete
    class LatinB(unicode_set):
        """Unicode set for Latin-B Unicode Character Range"""
        _ranges: Incomplete
    class Greek(unicode_set):
        """Unicode set for Greek Unicode Character Ranges"""
        _ranges: Incomplete
    class Cyrillic(unicode_set):
        """Unicode set for Cyrillic Unicode Character Range"""
        _ranges: Incomplete
    class Chinese(unicode_set):
        """Unicode set for Chinese Unicode Character Range"""
        _ranges: Incomplete
    class Japanese(unicode_set):
        """Unicode set for Japanese Unicode Character Range, combining Kanji, Hiragana, and Katakana ranges"""
        _ranges: Incomplete
        class Kanji(unicode_set):
            """Unicode set for Kanji Unicode Character Range"""
            _ranges: Incomplete
        class Hiragana(unicode_set):
            """Unicode set for Hiragana Unicode Character Range"""
            _ranges: Incomplete
        class Katakana(unicode_set):
            """Unicode set for Katakana  Unicode Character Range"""
            _ranges: Incomplete
    class Korean(unicode_set):
        """Unicode set for Korean Unicode Character Range"""
        _ranges: Incomplete
    class CJK(Chinese, Japanese, Korean):
        """Unicode set for combined Chinese, Japanese, and Korean (CJK) Unicode Character Range"""
    class Thai(unicode_set):
        """Unicode set for Thai Unicode Character Range"""
        _ranges: Incomplete
    class Arabic(unicode_set):
        """Unicode set for Arabic Unicode Character Range"""
        _ranges: Incomplete
    class Hebrew(unicode_set):
        """Unicode set for Hebrew Unicode Character Range"""
        _ranges: Incomplete
    class Devanagari(unicode_set):
        """Unicode set for Devanagari Unicode Character Range"""
        _ranges: Incomplete

class pyparsing_test:
    """
    namespace class for classes useful in writing unit tests
    """
    class reset_pyparsing_context:
        '''
        Context manager to be used when writing unit tests that modify pyparsing config values:
         - packrat parsing
         - default whitespace characters.
         - default keyword characters
         - literal string auto-conversion class
         - __diag__ settings

        Example:
            with reset_pyparsing_context():
                # test that literals used to construct a grammar are automatically suppressed
                ParserElement.inlineLiteralsUsing(Suppress)

                term = Word(alphas) | Word(nums)
                group = Group(\'(\' + term[...] + \')\')

                # assert that the \'()\' characters are not included in the parsed tokens
                self.assertParseAndCheckLisst(group, "(abc 123 def)", [\'abc\', \'123\', \'def\'])

            # after exiting context manager, literals are converted to Literal expressions again
        '''
        _save_context: Incomplete
        def __init__(self) -> None: ...
        def save(self): ...
        def restore(self) -> None: ...
        def __enter__(self): ...
        def __exit__(self, *args): ...
    class TestParseResultsAsserts:
        """
        A mixin class to add parse results assertion methods to normal unittest.TestCase classes.
        """
        def assertParseResultsEquals(self, result, expected_list=None, expected_dict=None, msg=None) -> None:
            """
            Unit test assertion to compare a ParseResults object with an optional expected_list,
            and compare any defined results names with an optional expected_dict.
            """
        def assertParseAndCheckList(self, expr, test_string, expected_list, msg=None, verbose: bool = True) -> None:
            """
            Convenience wrapper assert to test a parser element and input string, and assert that
            the resulting ParseResults.asList() is equal to the expected_list.
            """
        def assertParseAndCheckDict(self, expr, test_string, expected_dict, msg=None, verbose: bool = True) -> None:
            """
            Convenience wrapper assert to test a parser element and input string, and assert that
            the resulting ParseResults.asDict() is equal to the expected_dict.
            """
        def assertRunTestResults(self, run_tests_report, expected_parse_results=None, msg=None) -> None:
            """
            Unit test assertion to evaluate output of ParserElement.runTests(). If a list of
            list-dict tuples is given as the expected_parse_results argument, then these are zipped
            with the report tuples returned by runTests and evaluated using assertParseResultsEquals.
            Finally, asserts that the overall runTests() success value is True.

            :param run_tests_report: tuple(bool, [tuple(str, ParseResults or Exception)]) returned from runTests
            :param expected_parse_results (optional): [tuple(str, list, dict, Exception)]
            """
        @contextmanager
        def assertRaisesParseException(self, exc_type=..., msg=None) -> Generator[None]: ...

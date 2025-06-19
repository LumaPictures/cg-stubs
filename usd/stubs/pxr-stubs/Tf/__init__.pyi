# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import types
import typing
from typing import Any, Callable, ClassVar, overload

T = typing.TypeVar('T')
NoticeT = typing.TypeVar('NoticeT', bound='Notice')
Fatal: Callable
GetCodeLocation: Callable
PrepareModule: Callable
PreparePythonModule: Callable
RaiseCodingError: Callable
RaiseRuntimeError: Callable
Status: Callable
TF_APPLICATION_EXIT_TYPE: DiagnosticType
TF_DIAGNOSTIC_CODING_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_FATAL_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_STATUS_TYPE: DiagnosticType
TF_DIAGNOSTIC_WARNING_TYPE: DiagnosticType
Warn: Callable
_Alpha: _TestEnum
_Bravo: _TestEnum
_Charlie: _TestEnum
_Delta: _TestEnum
__MFB_FULL_PACKAGE_NAME: str

class CallContext(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def file(self) -> str: ...
    @property
    def function(self) -> str: ...
    @property
    def line(self) -> int: ...
    @property
    def prettyFunction(self) -> str: ...

class CppException(Exception): ...

class Debug(Boost.Python.instance):
    '''
    Enum-based debugging messages.


    The C{TfDebug} class encapsulates a simple enum-based conditional
    debugging message system. It is meant as a tool for developers, and
    *NOT* as a means of issuing diagnostic messages to end-users. (This is
    not strictly true. The TfDebug class is extremely useful and has many
    properties that make its use attractive for issuing messages to end-
    users. However, for this purpose, please use the C{TF_INFO} macro
    which more clearly indicates its intent.)

    The features of C{TfDebug} are:
       - Debugging messages/calls for an entire enum group can be compiled
         out-of-existence.

       - The cost of checking if a specific message should be printed at
         runtime (assuming the enum group of the message has not been compile-
         time disabled) is a single inline array lookup, with a compile-time
         index into a global array.
         The use of the facility is simple: ::

      // header file
      #include "pxr/base/tf/debug.h"
      TF_DEBUG_CODES(MY_E1, MY_E2, MY_E3);
  
      // source file
      TF_DEBUG(MY_E2).Msg("something about e2\\n");
  
      TF_DEBUG(MY_E3).Msg("val = %d\\n", value);

    The code in the header file declares the debug symbols to use. Under
    the hood, this creates an enum with the values given in the argument
    to TF_DEBUG_CODES, along with a first and last sentinel values and
    passes that to TF_DEBUG_RANGE.

    If you need to obtain the enum type name, use
    decltype(SOME_ENUM_VALUE).

    In the source file, the indicated debugging messages are printed only
    if the debugging symbols are enabled. Effectively, the construct ::

      TF_DEBUG(MY_E1).Msg(msgExpr)

     is translated to ::

      if (symbol-MY_E1-is-enabled)
          output(msgExpr)

    The implications are that C{msgExpr} is only evaluated if symbol
    C{MY_E1} symbol is enabled.

    To totally disable TF_DEBUG output for a set of codes at compile time,
    declare the codes using
    TF_CONDITIONALLY_COMPILE_TIME_ENABLED_DEBUG_CODES(condition, ...)
    where... is all the debug codes. If\'condition\'is false at compile time
    then all TF_DEBUG() .Msg()s for these codes are elminated at compile
    time, so they have zero cost.

    Most commonly debug symbols are inactive by default, but can be turned
    on either by an environment variable C{TF_DEBUG}, or interactively
    once a program has started. ::

      TfDebug::DisableAll<MyDebugCodes>();     // disable everything
  
      TfDebug::Enable(MY_E1);                  // enable just MY_E1

    Description strings may be associated with debug codes as follows: ::

      // source file xyz/debugCodes.cpp
  
      #include "proj/my/debugCodes.h"
      #include "pxr/base/tf/debug.h"
      #include "pxr/base/tf/registryManager.h"
  
      TF_REGISTRY_FUNCTION(TfDebug) {
          TF_DEBUG_ENVIRONMENT_SYMBOL(MY_E1, "loading of blah-blah files");
          TF_DEBUG_ENVIRONMENT_SYMBOL(MY_E2, "parsing of mdl code");
          // etc.
      }

    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetDebugSymbolDescription(_name: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Get a description for the specified debug symbol.


        A short description of the debug symbol is returned. This is the same
        description string that is embedded in the return value of
        GetDebugSymbolDescriptions.
        """
    @staticmethod
    def GetDebugSymbolDescriptions() -> str:
        """
        Get a description of all debug symbols and their purpose.


        A single string describing all registered debug symbols along with
        short descriptions is returned.
        """
    @staticmethod
    def GetDebugSymbolNames() -> list[str]:
        """
        Get a listing of all debug symbols.
        """
    @staticmethod
    def IsDebugSymbolNameEnabled(_name: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        True if the specified debug symbol is set.
        """
    @staticmethod
    def SetDebugSymbolsByName(pattern: str | pxr.Ar.ResolvedPath, value: bool) -> list[str]:
        """
        Set registered debug symbols matching C{pattern} to C{value}.


        All registered debug symbols matching C{pattern} are set to C{value}.
        The only matching is an exact match with C{pattern}, or if C{pattern}
        ends with an'*'as is otherwise a prefix of a debug symbols. The names
        of all debug symbols set by this call are returned as a vector.
        """
    @staticmethod
    def SetOutputFile(_file: FILE, /) -> None:
        """
        Direct debug output to *either* stdout or stderr.


        Note that *file* MUST be either stdout or stderr. If not, issue an
        error and do nothing. Debug output is issued to stdout by default. If
        the environment variable TF_DEBUG_OUTPUT_FILE is set to'stderr', then
        output is issued to stderr by default.
        """

class DiagnosticType(Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...

class Enum(Boost.Python.instance):
    """
    An enum class that records both enum type and enum value.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromFullName(_fullname: str | pxr.Ar.ResolvedPath, /) -> tuple[Enum, bool]:
        '''
        Returns the enumerated value for a fully-qualified name.


        This takes a fully-qualified enumerated value name (e.g.,
        C{"Season::WINTER"} ) and returns the associated value. If there is no
        such name, this returns -1. Since -1 can sometimes be a valid value,
        the C{foundIt} flag pointer, if not C{None}, is set to C{true} if the
        name was found and C{false} otherwise. Also, since this is not a
        templated function, it has to return a generic value type, so we use
        C{TfEnum}.
        '''

class Error(_DiagnosticBase):
    """
    Represents an object that contains error information.


    See Guide To Diagnostic Facilities in the C++ API reference for a
    detailed description of the error issuing API. For a example of how to
    post an error, see C{TF_ERROR()} , also in the C++ API reference.

    In the Python API, you can raise several different types of errors,
    including coding errors (Tf.RaiseCodingError), run time errors
    (Tf.RaiseRuntimeError), fatal errors (Tf.Fatal).
    """

    class Mark(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None: ...
        def Clear(self) -> bool: ...
        def GetErrors(self) -> list:
            """A list of the errors held by this mark."""
        def IsClean(self) -> bool: ...
        def SetMark(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def errorCode(self) -> Enum:
        """
        Return the error code posted.
        """
    @property
    def errorCodeString(self): ...

class ErrorException(RuntimeError):
    __init__: ClassVar[Callable] = ...

class MallocTag(Boost.Python.instance):
    """
    Top-down memory tagging system.


    See The TfMallocTag Memory Tagging System for a detailed description.
    """

    class CallTree(Boost.Python.instance):
        """
        Summary data structure for C{malloc} statistics.


        The C{CallTree} structure is used to deliver a snapshot of the current
        malloc usage. It is accessible as publicly modifiable data because it
        is simply a returned snapshot of the current memory state.
        """

        class CallSite(Boost.Python.instance):
            """
            Record of the bytes allocated under each different tag.


            Each construction of a C{TfAutoMallocTag} object with a different
            argument produces a distinct C{CallSite} record. The total bytes
            outstanding for all memory allocations made under a given call-site
            are recorded in C{nBytes}, while the name of the call site is
            available as C{name}.
            """
            def __init__(self, *args, **kwargs) -> None:
                """Raises an exception
                This class cannot be instantiated from Python
                """
            @property
            def nBytes(self): ...
            @property
            def name(self): ...

        class PathNode(Boost.Python.instance):
            '''
            Node in the call tree structure.


            A C{PathNode} captures the hierarchy of active C{TfAutoMallocTag}
            objects that are pushed and popped during program execution. Each
            C{PathNode} thus describes a sequence of call-sites (i.e. a path down
            the call tree). Repeated call sites (in the case of co-recursive
            function calls) can be skipped, e.g. pushing
            tags"A","B","C","B","C"leads to only three path-nodes, representing
            the paths"A","AB", and"ABC". Allocations done at the bottom (i.e. when
            tags"A","B","C","B","C"are all active) are billed to the longest path
            node in the sequence, which corresponds to the path"ABC").

            Path nodes track both the memory they incur directly (
            C{nBytesDirect}) but more importantly, the total memory allocated by
            themselves and any of their children ( C{nBytes}). The name of a node
            ( C{siteName}) corresponds to the tag name of the final tag in the
            path.
            '''
            def __init__(self, *args, **kwargs) -> None:
                """Raises an exception
                This class cannot be instantiated from Python
                """
            def GetChildren(self) -> list: ...
            @property
            def nAllocations(self): ...
            @property
            def nBytes(self): ...
            @property
            def nBytesDirect(self): ...
            @property
            def siteName(self): ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def GetCallSites(self) -> list: ...
        def GetPrettyPrintString(self) -> str:
            """
            Return the malloc report string.


            Get a malloc report of the tree and/or callsites.

            The columns in the report are abbreviated. Here are the definitions.

            B{TAGNAME} : The name of the tag being tracked. This matches the
            string argument to TfAutoMallocTag constructor.

            B{BytesIncl} : Bytes Inclusive. This includes all bytes allocated by
            this tag and any bytes of its children.

            B{BytesExcl} : Bytes Exclusive. Only bytes allocated exclusively by
            this tag, not including any bytes of its children.

            B{%Prnt} : (%% Parent). me.BytesIncl / parent.BytesIncl * 100

            B{%Exc} : BytesExcl / BytesIncl * 100

            B{%Totl} : (%% Total). BytesExcl / TotalBytes * 100
            """
        def GetRoot(self) -> MallocTag.CallTree.PathNode: ...
        def LogReport(self, rootName: str | pxr.Ar.ResolvedPath = ...) -> str: ...
        @overload
        def Report(self, fileName: str | pxr.Ar.ResolvedPath, rootName: str | pxr.Ar.ResolvedPath = ...) -> None:
            """
            Generates a report to the ostream C{out}.


            This report is printed in a way that is intended to be used by
            xxtracediff. If C{rootName} is non-empty it will replace the name of
            the tree root in the report.
            """
        @overload
        def Report(self, rootName: str | pxr.Ar.ResolvedPath = ...) -> None:
            """
            This is an overloaded member function, provided for convenience. It
            differs from the above function only in what argument(s) it accepts.
            """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetCallStacks() -> list: ...
    @staticmethod
    def GetCallTree() -> MallocTag.CallTree:
        """
        Return a snapshot of memory usage.


        Returns a snapshot by writing into C{*tree}. See the C{C} *tree
        structure for documentation. If C{Initialize()} has not been called, \\\n        *tree is set to a rather blank structure (empty vectors, empty
        strings, zero in all integral fields) and C{false} is returned;
        otherwise, C{*tree} is set with the contents of the current memory
        snapshot and C{true} is returned. It is fine to call this function on
        the same C{*tree} instance; each call simply overwrites the data from
        the last call. If /p skipRepeated is C{true}, then any repeated
        callsite is skipped. See the C{CallTree} documentation for more
        details.
        """
    @staticmethod
    def GetMaxTotalBytes() -> int:
        """
        Return the maximum total number of bytes that have ever been allocated
        at one time.


        This is simply the maximum value of GetTotalBytes() since Initialize()
        was called.
        """
    @staticmethod
    def GetTotalBytes() -> int:
        """
        Return total number of allocated bytes.


        The current total memory that has been allocated and not freed is
        returned. Memory allocated before calling C{Initialize()} is not
        accounted for.
        """
    @staticmethod
    def Initialize(_errMsg: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Initialize the memory tagging system.


        This function returns C{true} if the memory tagging system can be
        successfully initialized or it has already been initialized.
        Otherwise, C{*errMsg} is set with an explanation for the failure.

        Until the system is initialized, the various memory reporting calls
        will indicate that no memory has been allocated. Note also that memory
        allocated prior to calling C{Initialize()} is not tracked i.e. all
        data refers to allocations that happen subsequent to calling
        C{Initialize()} .
        """
    @staticmethod
    def IsInitialized() -> bool:
        """
        Return true if the tagging system is active.


        If C{Initialize()} has been successfully called, this function returns
        C{true}.
        """
    @staticmethod
    def SetCapturedMallocStacksMatchList(_matchList: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Sets the tags to trace.


        When memory is allocated for any tag that matches C{matchList} a stack
        trace is recorded. When that memory is released the stack trace is
        discarded. Clients can call C{GetCapturedMallocStacks()} to get a list
        of all recorded stack traces. This is useful for finding leaks.

        Traces recorded for any tag that will no longer be matched are
        discarded by this call. Traces recorded for tags that continue to be
        matched are retained.

        C{matchList} is a comma, tab or newline separated list of malloc tag
        names. The names can have internal spaces but leading and trailing
        spaces are stripped. If a name ends in'*'then the suffix is
        wildcarded. A name can have a leading'-'or'+'to prevent or allow a
        match. Each name is considered in order and later matches override
        earlier matches. For example,'Csd*, -CsdScene::_Populate*,
        +CsdScene::_PopulatePrimCacheLocal'matches any malloc tag starting
        with'Csd'but nothing starting
        with'CsdScene::_Populate'except'CsdScene::_PopulatePrimCacheLocal'.
        Use the empty string to disable stack capturing.
        """
    @staticmethod
    def SetDebugMatchList(_matchList: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Sets the tags to trap in the debugger.


        When memory is allocated or freed for any tag that matches
        C{matchList} the debugger trap is invoked. If a debugger is attached
        the program will stop in the debugger, otherwise the program will
        continue to run. See C{ArchDebuggerTrap()} and C{ArchDebuggerWait()} .

        C{matchList} is a comma, tab or newline separated list of malloc tag
        names. The names can have internal spaces but leading and trailing
        spaces are stripped. If a name ends in'*'then the suffix is
        wildcarded. A name can have a leading'-'or'+'to prevent or allow a
        match. Each name is considered in order and later matches override
        earlier matches. For example,'Csd*, -CsdScene::_Populate*,
        +CsdScene::_PopulatePrimCacheLocal'matches any malloc tag starting
        with'Csd'but nothing starting
        with'CsdScene::_Populate'except'CsdScene::_PopulatePrimCacheLocal'.
        Use the empty string to disable debugging traps.
        """

class NamedTemporaryFile:
    """A named temporary file which keeps the internal file handle closed. 
       A class which constructs a temporary file(that isn't open) on __enter__,
       provides its name as an attribute, and deletes it on __exit__. 
       
       Note: The constructor args for this object match those of 
       python's tempfile.mkstemp() function, and will have the same effect on
       the underlying file created."""
    __init__: ClassVar[Callable] = ...
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...
    @property
    def name(self): ...

class Notice(Boost.Python.instance):
    """
    The base class for objects used to notify interested parties
    (listeners) when events have occurred.


    The TfNotice class also serves as a container for various dispatching
    routines such as Register() and Send() .

    See The TfNotice Notification System in the C++ API reference for a
    detailed description of the notification system.

    Python Example: Registering For and Sending
    ===========================================

    Notices The following code provides examples of how to set up a Notice
    listener connection (represented in Python by the Listener class),
    including creating and sending notices, registering to receive
    notices, and breaking a listener connection. ::

      # To create a new notice type:
      class APythonClass(Tf.Notice):
          '''TfNotice sent when APythonClass does something of interest.'''
          pass
      Tf.Type.Define(APythonClass)
  
      # An interested listener can register to receive notices from all
      # senders, or from a particular type of sender.
  
      # To send a notice to all registered listeners:;
      APythonClass().SendGlobally()
  
      # To send a notice to listeners who register with a specific sender:
      APythonClass().Send(self)
  
      # To register for the notice from any sender:
      my_listener = Tf.Notice.RegisterGlobally(APythonClass, self._HandleNotice)
  
      # To register for the notice from a specific sender
      my_listener = Tf.Notice.Register(APythonClass, self._HandleNotice, sender)
  
      def _HandleNotice(self, notice, sender):
         '''callback function for handling a notice'''
         # do something when the notice arrives
  
      # To revoke interest in a notice
      my_listener.Revoke()

    For more on using notices in Python, see the Editor With Notices
    tutorial.
    """

    class Listener(Boost.Python.instance):
        """Represents the Notice connection between senders and receivers of notices.  When a Listener object expires the connection is broken. You can also use the Revoke() function to break the connection. A Listener object is returned from the Register() and  RegisterGlobally() functions. """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def Revoke(self) -> None:
            """Revoke() 

            Revoke interest by a notice listener.  This function revokes interest in the particular notice type and call-back method that its Listener object was registered for."""
    def __init__(self) -> None: ...
    @staticmethod
    def Register(_listener: type[NoticeT], _method: Callable[[NoticeT, T], typing.Any], _sender: T) -> Listener:
        """    Register( noticeType, callback, sender ) -> Listener 

            noticeType : Tf.Notice
            callback : function
            sender : object

            Register a listener as being interested in a TfNotice  type from a specific sender.  Notice listener will get sender  as an argument.     Registration of interest in a notice class N automatically  registers interest in all classes derived from N.  When a  notice of appropriate type is received, the listening object's  member-function method is called with the notice.     To reverse the registration, call Revoke() on the Listener object returned by this call. 

        Register( (Type)arg1, (object)arg2, (object)arg3) -> Listener"""
    @staticmethod
    def RegisterGlobally(_listener: type[NoticeT], _method: Callable[[NoticeT, typing.Any], typing.Any]) -> Listener:
        """RegisterGlobally( noticeType, callback ) -> Listener 

        noticeType : Tf.Notice
        callback : function

        Register a listener as being interested in a TfNotice type from any sender.  The notice listener does not get sender as an argument."""
    @overload
    def Send(self, _s: Sender, /) -> int:
        """
        Deliver the notice to interested listeners, returning the number of
        interested listeners.


        This is the recommended form of Send. It takes the sender as an
        argument.

        Listeners that registered for the given sender AND listeners that
        registered globally will get the notice.

        Listeners are invoked synchronously and in arbitrary order. The value
        returned is the total number of times the notice was sent to
        listeners. Note that a listener is called in the thread in which
        C{Send()} is called and *not* necessarily in the thread that
        C{Register()} was called in.
        """
    @overload
    def Send(self, arg2: object, /) -> int:
        """    Send(sender) 

            sender : object 

            Deliver the notice to interested listeners, returning the number of interested listeners. This is the recommended form of Send.  It takes the sender as an argument. Listeners that registered for the given sender AND listeners that registered globally will get the notice. 

        Send( (Notice)arg1, (object)arg2) -> int"""
    def SendGlobally(self) -> int:
        """SendGlobally() 

        Deliver the notice to interested listeners.   For most clients it is recommended to use the Send(sender) version of Send() rather than this one.  Clients that use this form of Send will prevent listeners from being able to register to receive notices based on the sender of the notice. ONLY listeners that registered globally will get the notice."""

class PyModuleWasLoaded(Notice):
    """
    A *TfNotice* that is sent when a script module is loaded.


    Since many modules may be loaded at once, listeners are encouraged to
    defer work triggered by this notice to the end of an application
    iteration. This, of course, is good practice in general.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def name(self) -> str:
        """
        Return the name of the module that was loaded.
        """

class RefPtrTracker(Boost.Python.instance):
    '''
    Provides tracking of C{TfRefPtr} objects to particular objects.


    Clients can enable, at compile time, tracking of C{TfRefPtr} objects
    that point to particular instances of classes derived from
    C{TfRefBase}. This is useful if you have a ref counted object with a
    ref count that should\'ve gone to zero but didn\'t. This tracker can
    tell you every C{TfRefPtr} that\'s holding the C{TfRefBase} and a stack
    trace where it was created or last assigned to.

    Clients can get a report of all watched instances and how many
    C{TfRefPtr} objects are holding them using C{ReportAllWatchedCounts()}
    (in python use C{Tf.RefPtrTracker()} .GetAllWatchedCountsReport()).
    You can see all of the stack traces using C{ReportAllTraces()} (in
    python use C{Tf.RefPtrTracker()} .GetAllTracesReport()).

    Clients will typically enable tracking using code like this: ::

      #include "pxr/base/tf/refPtrTracker.h"
  
      class MyRefBaseType;
      typedef TfRefPtr<MyRefBaseType> MyRefBaseTypeRefPtr;
  
      TF_DECLARE_REFPTR_TRACK(MyRefBaseType);
  
      class MyRefBaseType {
      ...
      public:
          static bool _ShouldWatch(const MyRefBaseType*);
      ...
      };
  
      TF_DEFINE_REFPTR_TRACK(MyRefBaseType, MyRefBaseType::_ShouldWatch);

    Note that the C{TF_DECLARE_REFPTR_TRACK()} macro must be invoked
    before any use of the C{MyRefBaseTypeRefPtr} type.

    The C{MyRefBaseType::_ShouldWatch()} function returns C{true} if the
    given instance of C{MyRefBaseType} should be tracked. You can also use
    C{TfRefPtrTracker::WatchAll()} to watch every instance (but that might
    use a lot of memory and time).

    If you have a base type, C{B}, and a derived type, C{D}, and you hold
    instances of C{D} in a C{TfRefPtr < C{B>}} (i.e. a pointer to the
    base) then you must track both type C{B} and type C{D}. But you can
    use C{TfRefPtrTracker::WatchNone()} when tracking C{B} if you\'re not
    interested in instances of C{B}.
    '''
    def __init__(self) -> None: ...
    def GetAllTracesReport(self) -> str: ...
    def GetAllWatchedCountsReport(self) -> str: ...
    def GetTracesReportForWatched(self, arg2: int, /) -> str: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class ScopeDescription(Boost.Python.instance):
    """
    This class is used to provide high-level descriptions about scopes of
    execution that could possibly block, or to provide relevant
    information about high-level action that would be useful in a crash
    report.


    This class is reasonably fast to use, especially if the message
    strings are not dynamically created, however it should not be used in
    very highly performance sensitive contexts. The cost to push & pop is
    essentially a TLS lookup plus a couple of atomic operations.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self, _unknownArg1: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def SetDescription(self, _description: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Replace the description stack entry for this scope description.


        Caller guarantees that the string C{description} lives at least as
        long as this TfScopeDescription object.
        """
    def __enter__(self) -> ScopeDescription: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class ScriptModuleLoader(Boost.Python.instance):
    """
    Provides low-level facilities for shared modules with script
    bindings to register themselves with their dependences, and provides a
    mechanism whereby those script modules will be loaded when necessary.


    Currently, this is when one of our script modules is loaded, when
    TfPyInitialize is called, and when Plug opens shared modules.

    Generally, user code will not make use of this.
    """
    def __init__(self) -> None: ...
    def GetModuleNames(self) -> list[str]:
        """
        Return a list of all currently known modules in a valid dependency
        order.
        """
    def GetModulesDict(self) -> dict:
        """
        Return a python dict containing all currently known modules under
        their canonical names.
        """
    def WriteDotFile(self, _file: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Write a graphviz dot-file for the dependency graph of all.


        currently known modules/modules to *file*.
        """
    def _LoadModulesForLibrary(self, arg2: object, /) -> None: ...
    def _RegisterLibrary(self, arg2: object, arg3: object, arg4: object, /) -> None: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class Singleton(Boost.Python.instance):
    """
    Manage a single instance of an object (see.


    Typical Use for a canonical example).
    """
    def __init__(self) -> None: ...

class StatusObject(_DiagnosticBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Stopwatch(Boost.Python.instance):
    '''
    Low-cost, high-resolution timer datatype.


    A C{TfStopwatch} can be used to perform very precise timings at
    runtime, even in very tight loops. The cost of"starting"or"stopping"a
    C{TfStopwatch} is very small: approximately 40 nanoseconds on a 900
    Mhz Pentium III Linux box, 300 nanoseconds on a 400 Mhz Sun, and 200
    nanoseconds on a 250 Mhz SGI.

    Note that this class is not thread-safe: if you need to take timings
    in a multi-threaded region of a process, let each thread have its own
    C{TfStopwatch} and then combine results using the C{AddFrom()} member
    function.
    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def AddFrom(self, _t: Stopwatch, /) -> None:
        """
        Adds the accumulated time and sample count from C{t} into the
        C{TfStopwatch}.


        If you have several timers taking measurements, and you wish to
        combine them together, you can add one timer's results into another;
        for example, C{t2.AddFrom(t1)} will add C{t1} 's time and sample count
        into C{t2}.
        """
    def Reset(self) -> None:
        """
        Resets the accumulated time and the sample count to zero.
        """
    def Start(self) -> None:
        """
        Record the current time for use by the next C{Stop()} call.


        The C{Start()} function records the current time. A subsequent call to
        C{Start()} before a call to C{Stop()} simply records a later current
        time, but does not change the accumulated time of the C{TfStopwatch}.
        """
    def Stop(self) -> None:
        '''
        Increases the accumulated time stored in the C{TfStopwatch}.


        The C{Stop()} function increases the accumulated time by the duration
        between the current time and the last time recorded by a C{Start()}
        call. A subsequent call to C{Stop()} before another call to C{Start()}
        will therefore double-count time and throw off the results.

        A C{TfStopwatch} also counts the number of samples it has taken.
        The"sample count"is simply the number of times that C{Stop()} has been
        called.
        '''
    @property
    def microseconds(self) -> int:
        """
        Return the accumulated time in microseconds.


        Note that 45 minutes will overflow a 32-bit counter, so take care to
        save the result in an C{int64_t}, and not a regular C{int} or C{long}.
        """
    @property
    def milliseconds(self) -> int:
        """
        Return the accumulated time in milliseconds.
        """
    @property
    def nanoseconds(self) -> int:
        """
        Return the accumulated time in nanoseconds.


        Note that this number can easily overflow a 32-bit counter, so take
        care to save the result in an C{int64_t}, and not a regular C{int} or
        C{long}.
        """
    @property
    def sampleCount(self) -> int:
        """
        Return the current sample count.


        The sample count, which is simply the number of calls to C{Stop()}
        since creation or a call to C{Reset()} , is useful for computing
        average running times of a repeated task.
        """
    @property
    def seconds(self) -> float:
        """
        Return the accumulated time in seconds as a C{double}.
        """

class TemplateString(Boost.Python.instance):
    '''
    TfTemplateString provides simple string substitutions based on named
    placeholders.


    Instead of the\'\'-based substitutions used by printf, template strings
    use\'$\'-based substitutions, using the following rules:

       - "$$"is replaced with a single"$"

       - "$identifier"names a substitution placeholder matching a mapping
         key of"identifier". The first non-identifier character after
         the"$"character terminates the placeholder specification.

       - "${identifier}"is equivalent to"$identifier". It is required when
         valid identifier characters follow the placeholder but are not part of
         the placeholder, such as"${noun}ification".

       - An identifier is a sequence of characters"[A-Z][a-z][0-9]_".
         *TfTemplateString* is immutable: once one is created it may not be
         modified. *TfTemplateString* is fast to copy, since it shares state
         internally between copies. *TfTemplateString* is thread-safe. It may
         be read freely by multiple threads concurrently.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Constructs a new template string.
        """
    @overload
    def __init__(self, _template_: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Constructs a new template string.
        """
    def GetEmptyMapping(self) -> dict:
        """
        Returns an empty mapping for the current template.


        This method first calls IsValid to ensure that the template is valid.
        """
    def GetParseErrors(self) -> list[str]:
        """
        Returns any error messages generated during template parsing.
        """
    def SafeSubstitute(self, _unknownArg1: dict, /) -> str:
        """
        Like Substitute() , except that if placeholders are missing from the
        mapping, instead of raising a coding error, the original placeholder
        will appear in the resulting string intact.
        """
    def Substitute(self, _unknownArg1: dict, /) -> str:
        """
        Performs the template substitution, returning a new string.


        The mapping contains keys which match the placeholders in the
        template. If a placeholder is found for which no mapping is present, a
        coding error is raised.
        """
    @property
    def template(self) -> str:
        """
        Returns the template source string supplied to the constructor.
        """
    @property
    def valid(self): ...

class Tf_PyEnumWrapper(Enum):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @overload
    def __and__(self, arg2: int, /) -> Any: ...
    @overload
    def __and__(self, arg2: Tf_PyEnumWrapper, /) -> Any: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    @overload
    def __or__(self, arg2: int, /) -> Any: ...
    @overload
    def __or__(self, arg2: Tf_PyEnumWrapper, /) -> Any: ...
    def __rand__(self, arg2: int, /) -> Any: ...
    def __ror__(self, arg2: int, /) -> Any: ...
    def __rxor__(self, arg2: int, /) -> Any: ...
    @overload
    def __xor__(self, arg2: int, /) -> Any: ...
    @overload
    def __xor__(self, arg2: Tf_PyEnumWrapper, /) -> Any: ...
    @property
    def displayName(self): ...
    @property
    def fullName(self): ...
    @property
    def name(self): ...
    @property
    def value(self): ...

class Tf_TestAnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def annotation(self): ...

class Tf_TestPyContainerConversions(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def GetPairTimesTwo() -> Any: ...
    @staticmethod
    def GetTokens() -> Any: ...
    @staticmethod
    def GetVectorTimesTwo() -> Any: ...

class Tf_TestPyOptionalBoost(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def TakesOptional(optString: object = ..., optStrvec: object = ...) -> tuple: ...
    @staticmethod
    def TestOptionalChar() -> Any: ...
    @staticmethod
    def TestOptionalDouble() -> Any: ...
    @staticmethod
    def TestOptionalFloat() -> Any: ...
    @staticmethod
    def TestOptionalInt() -> Any: ...
    @staticmethod
    def TestOptionalLong() -> Any: ...
    @staticmethod
    def TestOptionalShort() -> Any: ...
    @staticmethod
    def TestOptionalString() -> Any: ...
    @staticmethod
    def TestOptionalStringVector() -> Any: ...
    @staticmethod
    def TestOptionalUChar() -> Any: ...
    @staticmethod
    def TestOptionalUInt() -> Any: ...
    @staticmethod
    def TestOptionalULong() -> Any: ...
    @staticmethod
    def TestOptionalUShort() -> Any: ...

class Tf_TestPyOptionalStd(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def TakesOptional(optString: object = ..., optStrvec: object = ...) -> tuple: ...
    @staticmethod
    def TestOptionalChar() -> Any: ...
    @staticmethod
    def TestOptionalDouble() -> Any: ...
    @staticmethod
    def TestOptionalFloat() -> Any: ...
    @staticmethod
    def TestOptionalInt() -> Any: ...
    @staticmethod
    def TestOptionalLong() -> Any: ...
    @staticmethod
    def TestOptionalShort() -> Any: ...
    @staticmethod
    def TestOptionalString() -> Any: ...
    @staticmethod
    def TestOptionalStringVector() -> Any: ...
    @staticmethod
    def TestOptionalUChar() -> Any: ...
    @staticmethod
    def TestOptionalUInt() -> Any: ...
    @staticmethod
    def TestOptionalULong() -> Any: ...
    @staticmethod
    def TestOptionalUShort() -> Any: ...

class Type(Boost.Python.instance):
    """
    TfType represents a dynamic runtime type.


    TfTypes are created and discovered at runtime, rather than compile
    time.

    Features:

       - unique typename

       - safe across DSO boundaries

       - can represent C++ types, pure Python types, or Python subclasses
         of wrapped C++ types

       - lightweight value semantics  you can copy and default construct
         TfType, unlike C{std::type_info}.

       - totally ordered  can use as a C{std::map} key

    """
    Unknown: ClassVar[Type] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct an TfType representing an unknown type.


        To actually register a new type with the TfType system, see
        TfType::Declare() .

        Note that this always holds true: ::

          TfType().IsUnknown() == true

        """
    @overload
    def __init__(self, _info: Type, /) -> None: ...
    def AddAlias(self, _base: Type, _name: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Add an alias name for this type under the given base type.


        Aliases are similar to typedefs in C++: they provide an alternate name
        for a type. The alias is defined with respect to the given C{base}
        type. Aliases must be unique with respect to both other aliases
        beneath that base type and names of derived types of that base.
        """
    @staticmethod
    def Define(arg1: object, /) -> Type: ...
    @staticmethod
    def Find(arg1: object, /) -> Type: ...
    @staticmethod
    def FindByName(_name: str | pxr.Ar.ResolvedPath, /) -> Type:
        """
        Retrieve the C{TfType} corresponding to the given C{name}.


        Every type defined in the TfType system has a unique, implementation
        independent name. In addition, aliases can be added to identify a type
        underneath a specific base type; see TfType::AddAlias() . The given
        name will first be tried as an alias under the root type, and
        subsequently as a typename.

        This method is equivalent to: ::

          TfType::GetRoot().FindDerivedByName(name)

        For any object C{obj}, ::

          Find(obj) == FindByName( Find(obj).GetTypeName() )

        """
    def FindDerivedByName(self, _name: str | pxr.Ar.ResolvedPath, /) -> Type:
        """
        Retrieve the C{TfType} that derives from this type and has the given
        alias or typename.



        AddAlias
        """
    def GetAliases(self, _derivedType: Type, /) -> tuple:
        """
        Returns a vector of the aliases registered for the derivedType under
        this, the base type.



        AddAlias()
        """
    def GetAllAncestorTypes(self) -> tuple:
        '''
        Build a vector of all ancestor types inherited by this type.


        The starting type is itself included, as the first element of the
        results vector.

        Types are given in"C3"resolution order, as used for new-style classes
        starting in Python 2.3. This algorithm is more complicated than a
        simple depth-first traversal of base classes, in order to prevent some
        subtle errors with multiple-inheritance. See the references below for
        more background.

        This can be expensive; consider caching the results. TfType does not
        cache this itself since it is not needed internally.

        Guido van Rossum."Unifying types and classes in Python 2.2: Method
        resolution order."
        http://www.python.org/download/releases/2.2.2/descrintro/#mro

        Barrett, Cassels, Haahr, Moon, Playford, Withington."A Monotonic
        Superclass Linearization for Dylan."OOPSLA 96.
        http://www.webcom.com/haahr/dylan/linearization-oopsla96.html
        '''
    def GetAllDerivedTypes(self) -> tuple:
        """
        Return the set of all types derived (directly or indirectly) from this
        type.
        """
    @staticmethod
    def GetRoot() -> Type:
        """
        Return the root type of the type hierarchy.


        All known types derive (directly or indirectly) from the root. If a
        type is specified with no bases, it is implicitly considered to derive
        from the root type.
        """
    def IsA(self, _queryType: Type, /) -> bool:
        """
        Return true if this type is the same as or derived from C{queryType}.


        If C{queryType} is unknown, this always returns C{false}.
        """
    @staticmethod
    def _DumpTypeHierarchy() -> None:
        """_DumpTypeHierarchy(TfType): Diagnostic method to print the type hierarchy beneath a given TfType."""
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality operator.



        All unknown types (see IsUnknown() ) are considered equal. This is so
        all unknown types will only occupy one key when used in an associative
        map.
        """
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool:
        """
        Comparison operator.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def baseTypes(self) -> list[Type]:
        """
        Return a vector of types from which this type was derived.
        """
    @property
    def derivedTypes(self): ...
    @property
    def isEnumType(self) -> bool:
        """
        Return true if this is an enum type.
        """
    @property
    def isPlainOldDataType(self) -> bool:
        """
        Return true if this is a plain old data type, as defined by C++.
        """
    @property
    def isUnknown(self) -> bool:
        """
        Return true if this is the unknown type, representing a type unknown
        to the TfType system.


        The unknown type does not derive from the root type, or any other
        type.
        """
    @property
    def pythonClass(self) -> PyObjWrapper:
        """
        Return the Python class object for this type.


        If this type is unknown or has not yet had a Python class defined,
        this will return C{None}, as an empty C{TfPyObjWrapper}

        DefinePythonClass()
        """
    @property
    def sizeof(self) -> int:
        """
        Return the size required to hold an instance of this type on the stack
        (does not include any heap allocated memory the instance uses).


        This is what the C++ sizeof operator returns for the type, so this
        value is not very useful for Python types (it will always be
        sizeof(boost::python::object)).
        """
    @property
    def typeName(self) -> str:
        """
        Return the machine-independent name for this type.


        This name is specified when the TfType is declared.

        Declare()
        """

class Warning(_DiagnosticBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class WindowsImportWrapper:
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...

class _ClassWithClassMethod(Boost.Python.instance):
    Test: ClassVar[method] = ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...

class _ClassWithVarArgInit(Boost.Python.instance):
    def __init__(self) -> None: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def allowExtraArgs(self): ...
    @property
    def args(self): ...
    @property
    def expired(self): ...
    @property
    def kwargs(self): ...

class _DiagnosticBase(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def commentary(self): ...
    @property
    def diagnosticCode(self): ...
    @property
    def diagnosticCodeString(self): ...
    @property
    def sourceFileName(self): ...
    @property
    def sourceFunction(self): ...
    @property
    def sourceLineNumber(self): ...

class _Enum(Boost.Python.instance):
    class TestEnum2(Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...

    class TestKeywords(Tf_PyEnumWrapper):
        False_: ClassVar[TestKeywords] = ...
        None_: ClassVar[TestKeywords] = ...
        True_: ClassVar[TestKeywords] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        global_: ClassVar[TestKeywords] = ...
        import_: ClassVar[TestKeywords] = ...
        print_: ClassVar[TestKeywords] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...

    class TestScopedEnum(Tf_PyEnumWrapper):
        Alef: ClassVar[TestScopedEnum] = ...
        Bet: ClassVar[TestScopedEnum] = ...
        Gimel: ClassVar[TestScopedEnum] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...
    One: ClassVar[TestEnum2] = ...
    Three: ClassVar[TestEnum2] = ...
    Two: ClassVar[TestEnum2] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class _TestBase(Boost.Python.instance):
    def __init__(self) -> None: ...
    def TestCallVirtual(self) -> str: ...
    @overload
    def Virtual(self) -> str: ...
    @overload
    def Virtual(self) -> None: ...
    def Virtual2(self) -> None: ...
    def Virtual3(self, arg2: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def Virtual4(self) -> str: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class _TestDerived(_TestBase):
    def __init__(self) -> None: ...
    def Virtual(self) -> str: ...
    def Virtual2(self) -> None: ...
    def Virtual3(self, arg2: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class _TestEnum(Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...

class _TestScopedEnum(Tf_PyEnumWrapper):
    Beryllium: ClassVar[_TestScopedEnum] = ...
    Boron: ClassVar[_TestScopedEnum] = ...
    Hydrogen: ClassVar[_TestScopedEnum] = ...
    Lithium: ClassVar[_TestScopedEnum] = ...
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...

class _TestStaticMethodError(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def Error() -> None: ...

class _TestStaticTokens(Boost.Python.instance):
    orange: ClassVar[str] = ...
    pear: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class _testStaticTokens(Boost.Python.instance):
    orange: ClassVar[str] = ...  # read-only
    pear: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

def DictionaryStrcmp(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, /) -> int: ...
def DumpTokenStats() -> None: ...
def FindLongestAccessiblePrefix(_path: str | pxr.Ar.ResolvedPath, /) -> int:
    """
    Return the index delimiting the longest accessible prefix of *path*.


    The returned value is safe to use to split the string via it's
    generalized copy constructor. If the entire path is accessible, return
    the length of the input string. If none of the path is accessible,
    return 0. Otherwise the index points to the path separator that
    delimits the existing prefix from the non-existing suffix.

    Examples: suppose the paths /, /usr, and /usr/anim exist, but no other
    paths exist.

    TfFindLongestAccessiblePrefix('/usr/anim') ->9
    TfFindLongestAccessiblePrefix('/usr/anim/foo') ->9
    TfFindLongestAccessiblePrefix('/foo/bar') ->0

    If an error occurs, and the *error* string is not null, it is set to
    the reason for the error. If the error string is set, the returned
    index is the path separator before the element at which the error
    occurred.
    """
def GetAppLaunchTime() -> int:
    """
    Returns the application's launch time.
    """
def GetCurrentScopeDescriptionStack() -> list[str]:
    '''
    Return a copy of the current description stack for the"main"thread as
    identified by ArchGetMainThreadId() as a vector of strings.


    The most recently pushed description is at back(), and the least
    recently pushed description is at front().
    '''
def GetEnvSetting(_setting: str | pxr.Ar.ResolvedPath, /) -> Any:
    """
    Returns the value of the specified env setting, registered using
    C{TF_DEFINE_ENV_SETTING}.
    """
def GetStackTrace() -> str:
    """
    Gets both the C++ and the python stack and returns it as a string.
    """
def InstallTerminateAndCrashHandlers() -> None:
    """
    (Re)install Tf's crash handler.


    This should not generally need to be called since Tf does this itself
    when loaded. However, when run in 3rd party environments that install
    their own signal handlers, possibly overriding Tf's, this provides a
    way to reinstall them, in hopes that they'll stick.

    This calls std::set_terminate() and installs signal handlers for
    SIGSEGV, SIGBUS, SIGFPE, and SIGABRT.
    """
def InvokeWithErrorHandling(tupleargs, dictkwds) -> typing.Any: ...
def IsValidIdentifier(_identifier: str | pxr.Ar.ResolvedPath, /) -> bool:
    """
    Test whether *identifier* is valid.


    An identifier is valid if it follows the C/Python identifier
    convention; that is, it must be at least one character long, must
    start with a letter or underscore, and must contain only letters,
    underscores, and numerals.
    """
def LogStackTrace(reason: str | pxr.Ar.ResolvedPath, logToDb: bool = ...) -> None:
    """
    Logs both the C++ and the python stack to a file in /var/tmp A message
    is printed to stderr reporting that a stack trace has been taken and
    what file it has been written to.


    If C{logtodb} is true, then the stack trace will be added to the
    stack_trace database table.
    """
def MakeValidIdentifier(_in: str | pxr.Ar.ResolvedPath, /) -> str:
    '''
    Produce a valid identifier (see TfIsValidIdentifier) from C{in} by
    replacing invalid characters with\'_\'.


    If C{in} is empty, return"_".
    '''
def PrintStackTrace(_out: typing.TextIO, _reason: str | pxr.Ar.ResolvedPath, /) -> None:
    """
    Prints both the C++ and the python stack to the *stream* provided.
    """
def RealPath(path: str | pxr.Ar.ResolvedPath, allowInaccessibleSuffix: bool = ..., raiseOnError: bool = ...) -> str:
    """
    Returns the canonical path of the specified filename, eliminating any
    symbolic links encountered in the path.


    This is a wrapper to realpath(3), which caters for situations where
    the real realpath() would return a None string, such as the case where
    the path is really just a program name. The memory allocated by
    realpath is managed internally.

    If *allowInaccessibleSuffix* is true, then this function will only
    invoke realpath on the longest accessible prefix of *path*, and then
    append the inaccessible suffix.

    If *error* is provided, it is set to the error reason should an error
    occur while computing the real path. If no error occurs, the string is
    cleared.
    """
def ReportActiveErrorMarks() -> None:
    """
    Report current TfErrorMark instances and the stack traces that created
    them to stdout for debugging purposes.


    To call this function, set _enableTfErrorMarkStackTraces in
    errorMark.cpp and enable the TF_ERROR_MARK_TRACKING TfDebug code.
    """
def RepostErrors(exception: object) -> bool: ...
def SetPythonExceptionDebugTracingEnabled(enabled: bool) -> None: ...
def StringSplit(_src: str | pxr.Ar.ResolvedPath, _separator: str | pxr.Ar.ResolvedPath, /) -> list[str]:
    """
    Breaks the given string apart, returning a vector of strings.


    The string C{source} is broken apart into individual words, where a
    word is delimited by the string C{separator}. This function behaves
    like pythons string split method.
    """
def StringToDouble(_txt: str | pxr.Ar.ResolvedPath, /) -> float:
    '''
    Converts text string to double.


    This method converts strings to floating point numbers. It is similar
    to libc\'s atof(), but performs the conversion much more quickly.

    It expects somewhat valid input: it will continue parsing the input
    until it hits an unrecognized character, as described by the regexp
    below, and at that point will return the results up to that point.

    (-?[0-9]+(.[0-9]*)?|-?.[0-9]+)([eE][-+]?[0-9]+)?

    It will not check to see if there is any input at all, or whitespace
    after the digits. Ie: TfStringToDouble("") == 0.0
    TfStringToDouble("blah") == 0.0 TfStringToDouble("-") == -0.0
    TfStringToDouble("1.2foo") == 1.2

    C{TfStringToDouble} is a wrapper around the extern-c TfStringToDouble
    '''
def StringToLong(_txt: str | pxr.Ar.ResolvedPath, /) -> int:
    """
    Convert a sequence of digits in C{txt} to a long int value.


    Caller is responsible for ensuring that C{txt} has content matching:
    ::

      -?[0-9]+

    If the digit sequence's value is out of range, set C{*outOfRange} to
    true (if C{outOfRange} is not None) and return either
    std::numeric_limits<long>::min() or max(), whichever is closest to the
    true value.
    """
def StringToULong(_txt: str | pxr.Ar.ResolvedPath, /) -> int:
    """
    Convert a sequence of digits in C{txt} to an unsigned long value.


    Caller is responsible for ensuring that C{txt} has content matching:
    ::

      [0-9]+

    If the digit sequence's value is out of range, set C{*outOfRange} to
    true (if C{outOfRange} is not None) and return
    std::numeric_limits<unsignedlong>::max().
    """
def TouchFile(fileName: str | pxr.Ar.ResolvedPath, create: bool = ...) -> bool:
    """
    Touch C{fileName}, updating access and modification time to'now'.


    A simple touch-like functionality. Simple in a sense that it does not
    offer as many options as the same-name unix touch command, but
    otherwise is identical to the default touch behavior. If C{create} is
    true and the file does not already exist, an empty file gets created,
    otherwise the touch call fails if the file does not already exist.
    """
def _CallThrowTest(arg1: object, /) -> None: ...
def _ConvertByteListToByteArray(arg1: list, /) -> Any: ...
def _DerivedFactory() -> _TestDerived: ...
def _DerivedNullFactory() -> _TestDerived: ...
def _Fatal(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int, /) -> None: ...
def _GetLongMax() -> int: ...
def _GetLongMin() -> int: ...
def _GetULongMax() -> int: ...
def _RaiseCodingError(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int, /) -> None: ...
def _RaiseRuntimeError(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int, /) -> None: ...
def _ReturnsBase(arg1: object, /) -> Any: ...
def _ReturnsBaseRefPtr(arg1: object, /) -> Any: ...
def _ReturnsConstBase(arg1: object, /) -> Any: ...
def _RoundTripWrapperCallTest(arg1: object, /) -> Any: ...
def _RoundTripWrapperIndexTest(arg1: object, arg2: int, /) -> Any: ...
def _RoundTripWrapperTest(arg1: object, /) -> Any: ...
def _Status(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int, /) -> None: ...
def _TakesBase(arg1: object, /) -> tuple: ...
def _TakesConstBase(arg1: object, /) -> str: ...
def _TakesDerived(arg1: object, /) -> str: ...
def _TakesReference(arg1: object, /) -> None: ...
def _TakesVecVecString(arg1: object, /) -> int: ...
def _TestAnnotatedBoolResult(arg1: bool, arg2: str | pxr.Ar.ResolvedPath, /) -> Tf_TestAnnotatedBoolResult: ...
def _ThrowCppException() -> str: ...
def _ThrowTest(arg1: str | pxr.Ar.ResolvedPath, /) -> None: ...
def _Warn(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int, /) -> None: ...
def __SetErrorExceptionClass(arg1: object, /) -> None: ...
def _callUnboundInstance(arg1: object, arg2: str | pxr.Ar.ResolvedPath, /) -> str: ...
def _callback(arg1: object, /) -> None: ...
def _doErrors() -> None: ...
def _invokeTestCallback() -> str: ...
def _mightRaise(arg1: bool, /) -> None: ...
def _registerInvalidEnum(arg1: object, /) -> None: ...
def _returnsTfEnum(arg1: object, /) -> Any: ...
def _sendTfNoticeWithSender(arg1: object, /) -> None: ...
def _setTestCallback(arg1: object, /) -> None: ...
def _stringCallback(arg1: object, /) -> str: ...
def _stringStringCallback(arg1: object, /) -> str: ...
def _takesTestEnum(arg1: object, /) -> None: ...
def _takesTestEnum2(arg1: object, /) -> None: ...
def _takesTfEnum(arg1: object, /) -> None: ...

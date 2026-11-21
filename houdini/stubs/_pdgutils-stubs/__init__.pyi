from collections.abc import Sequence
from typing import ClassVar, Never
import types
from typing import Any, ClassVar, overload

class FileReader:
    def __init__(self, path: str, binary: bool = ...) -> None:
        """__init__(self: _pdgutils.FileReader, path: str, binary: bool = True) -> None"""
    def close(self) -> None:
        """close(self: _pdgutils.FileReader) -> None

        Closes the stream
        """
    def fileno(self) -> int:
        """fileno(self: _pdgutils.FileReader) -> object

        Returns the file descriptor if it has one
        """
    def flush(self) -> None:
        """flush(self: _pdgutils.FileReader) -> object

        Flushes underlying buffers
        """
    def isatty(self) -> bool:
        """isatty(self: _pdgutils.FileReader) -> bool

        Returns true if the stream is interactive
        """
    def read(self, size: int = ...) -> bytes | str:
        """read(self: _pdgutils.FileReader, size: int = 0) -> object

        Reads at most size bytes, returned as bytes.

        If the size is negative or ommited, return until EOF is reached.
        """
    def readable(self) -> bool:
        """readable(self: _pdgutils.FileReader) -> bool

        Returns True if the stream can be read from.
        """
    def readline(self) -> bytes | str | None:
        """readline(self: _pdgutils.FileReader) -> object

        next line from the file as bytes
        """
    def seek(self, offset: int, whence: int = ...) -> None:
        """seek(self: _pdgutils.FileReader, offset: int, whence: int = 0) -> object

        Move to new file position.
        Argument offset is a byte count.  Optional argument whence defaults to  0 (offset from start of file, offset should be >= 0); other values are 1 (move relative to current position, positive or negative), and 2 (move relative to end of file, usually negative
        """
    @overload
    def seekable(self) -> bool:
        """seekable(self: _pdgutils.FileReader) -> bool

        Returns True if the stream is seekable (random access).
        """
    @overload
    def seekable(self, randomaccess: Never) -> bool:
        """seekable(self: _pdgutils.FileReader) -> bool

        Returns True if the stream is seekable (random access).
        """
    def tell(self) -> int:
        """tell(self: _pdgutils.FileReader) -> object

        Returns current file position
        """
    def writable(self) -> bool:
        """writable(self: _pdgutils.FileReader) -> bool

        Returns True if the stream is writeable.
        """
    def __enter__(self) -> FileReader:
        """__enter__(self: _pdgutils.FileReader) -> _pdgutils.FileReader"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdgutils.FileReader, arg0: object, arg1: object, arg2: object) -> bool"""
    def __iter__(self) -> FileReader:
        """__iter__(self: _pdgutils.FileReader) -> object"""
    def __next__(self) -> bytes | str:
        """__next__(self: _pdgutils.FileReader) -> object"""
    @property
    def closed(self) -> bool: ...

class PDGNMQRelay:
    def __init__(self) -> None:
        """__init__(self: _pdgutils.PDGNMQRelay) -> None"""
    def connectToMQ(self, arg0: str, arg1: int, arg2: str, arg3: int, arg4: int, arg5: int, arg6: PDGNetTLSConfig) -> int:
        """connectToMQ(self: _pdgutils.PDGNMQRelay, arg0: str, arg1: int, arg2: str, arg3: int, arg4: int, arg5: int, arg6: _pdgutils.PDGNetTLSConfig) -> int

        Connects to existing MQ server

        """
    def disconnectFromMQ(self) -> None:
        """disconnectFromMQ(self: _pdgutils.PDGNMQRelay) -> None

        Disconnect from MQ server

        """
    def getHTTPPort(self) -> int:
        """getHTTPPort(self: _pdgutils.PDGNMQRelay) -> int

        Returns HTTP listening port of the MQ server.

        """
    def getMQPort(self) -> int:
        """getMQPort(self: _pdgutils.PDGNMQRelay) -> int

        Returns listening port of the MQ server.

        """
    def getNextReceivedMessage(self) -> PDGNMessage | None:
        """getNextReceivedMessage(self: _pdgutils.PDGNMQRelay) -> _pdgutils.PDGNMessageBase

        Returns the next received message

        """
    def getNumReceivedMessages(self) -> int:
        """getNumReceivedMessages(self: _pdgutils.PDGNMQRelay) -> int

        Returns number of received messages

        """
    def isConnectedToMQ(self) -> bool:
        """isConnectedToMQ(self: _pdgutils.PDGNMQRelay) -> bool

        Returns True if this has connected to MQ server

        """
    def isHTTPListenerRunning(self) -> bool:
        """isHTTPListenerRunning(self: _pdgutils.PDGNMQRelay) -> bool

        Returns True if the MQ server supports HTTP requests

        """
    def isMQStarted(self) -> bool:
        """isMQStarted(self: _pdgutils.PDGNMQRelay) -> bool

        Returns True if the MQ server started

        """
    def startMQ(self, url: str, port: int, num_connections: int, persistent: bool, tls_cfg: PDGNetTLSConfig = ...) -> int:
        """startMQ(self: _pdgutils.PDGNMQRelay, url: str, port: int, num_connections: int, persistent: bool, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> int

        Starts the MQ server

        """
    def startMQHTTP(self, arg0: str, arg1: int, arg2: int) -> int:
        """startMQHTTP(self: _pdgutils.PDGNMQRelay, arg0: str, arg1: int, arg2: int) -> int

        Starts the HTTP listener on the MQ server

        """
    def stopAll(self) -> None:
        """stopAll(self: _pdgutils.PDGNMQRelay) -> None

        Stops server and connection to server.

        """
    def stopMQ(self) -> None:
        """stopMQ(self: _pdgutils.PDGNMQRelay) -> None

        Stops the MQ server

        """
    def waitUntilConnectedToMQ(self, arg0: float) -> bool:
        """waitUntilConnectedToMQ(self: _pdgutils.PDGNMQRelay, arg0: float) -> bool

        Wait until connected to MQ server with optional time out

        """

class PDGNMQServer:
    def __init__(self) -> None:
        """__init__(self: _pdgutils.PDGNMQServer) -> None"""
    def getHTTPPort(self) -> int:
        """getHTTPPort(self: _pdgutils.PDGNMQServer) -> int

        Returns HTTP port of the MQ server.

        """
    def getIdleKillTime(self) -> float:
        """getIdleKillTime(self: _pdgutils.PDGNMQServer) -> float

        Get the time before automatically shutting down due to lack of network activity

        """
    def getLastError(self) -> int:
        """getLastError(self: _pdgutils.PDGNMQServer) -> int

        Returns the last error

        """
    def getListenPort(self) -> int:
        """getListenPort(self: _pdgutils.PDGNMQServer) -> int

        Returns listening port of the MQ server.

        """
    def getURL(self) -> str:
        """getURL(self: _pdgutils.PDGNMQServer) -> str

        Returns the server address

        """
    def isHTTPListenerRunning(self) -> bool:
        """isHTTPListenerRunning(self: _pdgutils.PDGNMQServer) -> bool

        Returns True if the MQ server supports HTTP requests

        """
    def isServerRunning(self) -> bool:
        """isServerRunning(self: _pdgutils.PDGNMQServer) -> bool

        Returns True if the MQ server is running

        """
    def isServerStopped(self) -> bool:
        """isServerStopped(self: _pdgutils.PDGNMQServer) -> bool

        Returns True if the MQ server is stopped

        """
    def setIdleKillTime(self, arg0: float) -> None:
        """setIdleKillTime(self: _pdgutils.PDGNMQServer, arg0: float) -> None

        Set the time before automatically shutting down due to lack of network activity

        """
    def start(self, ip: str, port: int, num_connections: int, persistent: bool, tls_cfg: PDGNetTLSConfig = ...) -> int:
        """start(self: _pdgutils.PDGNMQServer, ip: str, port: int, num_connections: int, persistent: bool, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> int

        Starts the MQ server

        """
    def startHTTP(self, arg0: str, arg1: int, arg2: int) -> int:
        """startHTTP(self: _pdgutils.PDGNMQServer, arg0: str, arg1: int, arg2: int) -> int

        Start the MQ HTTP listener

        """
    def stop(self) -> None:
        """stop(self: _pdgutils.PDGNMQServer) -> None

        Stops the MQ server

        """
    def writeConnectionFile(self, arg0: str) -> None:
        """writeConnectionFile(self: _pdgutils.PDGNMQServer, arg0: str) -> None

        Writes out the server's connection file at given file path.

        """

class PDGNMessage(PDGNMessageBase):
    def __init__(self) -> None:
        """__init__(self: _pdgutils.PDGNMessage) -> None"""
    def cancelReplyAsync(self) -> None:
        """cancelReplyAsync(self: _pdgutils.PDGNMessage) -> None

        For message waiting on reply asynchronously, this cancels the waiting operation and resets message state.

        """
    def clear(self) -> int:
        """clear(self: _pdgutils.PDGNMessage) -> int

        Clear out the currently written data and reset to start of stream.

        """
    def completeReplyAsync(self) -> int:
        """completeReplyAsync(self: _pdgutils.PDGNMessage) -> int

        For message waiting on reply asynchronously, once hasReplyAsyncReceived() is \t\tTrue, this can be called to read the received message and complete the \t\tasynchronous operation.

        """
    def getClientName(self) -> str:
        """getClientName(self: _pdgutils.PDGNMessage) -> str

        Returns name of client who sent message.

        """
    def getError(self) -> int:
        """getError(self: _pdgutils.PDGNMessage) -> int

        Returns error code of message.

        """
    def getErrorMessage(self, arg0: int) -> str:
        """getErrorMessage(self: _pdgutils.PDGNMessage, arg0: int) -> str

        Returns error text of given error code.

        """
    def getLength(self) -> int:
        """getLength(self: _pdgutils.PDGNMessage) -> int

        Get total length of current message

        """
    def getLengthLeft(self) -> int:
        """getLengthLeft(self: _pdgutils.PDGNMessage) -> int

        Get length left of current message

        """
    def getMessageType(self) -> PDGNetMessageType:
        """getMessageType(self: _pdgutils.PDGNMessage) -> _pdgutils.PDGNetMessageType

        Returns message type.

        """
    def getReplyID(self) -> int:
        """getReplyID(self: _pdgutils.PDGNMessage) -> int

        Returns reply ID of message.

        """
    def hasReplyAsyncReceived(self) -> bool:
        """hasReplyAsyncReceived(self: _pdgutils.PDGNMessage) -> bool

        For message waiting on reply asynchronously, this returns True if reply has been received.

        """
    def isValid(self) -> bool:
        """isValid(self: _pdgutils.PDGNMessage) -> bool

        Returns true if message has no error.

        """
    def readBytes(self) -> bytes:
        """readBytes(self: _pdgutils.PDGNMessageBase) -> bytes

        Read size of bytes, then the bytes from message

        """
    def readInt16(self, arg0: int) -> int:
        """readInt16(self: _pdgutils.PDGNMessageBase, arg0: int) -> int

        Read int16 from message

        """
    def readInt32(self, arg0: int) -> int:
        """readInt32(self: _pdgutils.PDGNMessageBase, arg0: int) -> int

        Read int32 from message

        """
    def readString(self) -> str:
        """readString(self: _pdgutils.PDGNMessageBase) -> str

        Read string from message

        """
    def readUInt16(self, arg0: int) -> int:
        """readUInt16(self: _pdgutils.PDGNMessageBase, arg0: int) -> int

        Read uint16 from message

        """
    def readUInt32(self, arg0: int) -> int:
        """readUInt32(self: _pdgutils.PDGNMessageBase, arg0: int) -> int

        Read uint32 from message

        """
    def seek(self, arg0: int) -> int:
        """seek(self: _pdgutils.PDGNMessage, arg0: int) -> int

        Seek to a position in buffer

        """
    def sendTo(self, url: str, timeout: int, allow_resend: bool = ..., tls_cfg: PDGNetTLSConfig = ...) -> int:
        """sendTo(self: _pdgutils.PDGNMessage, url: str, timeout: int, allow_resend: bool = True, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> int

        Send this message.

        """
    def sendToGetReply(self, url: str, timeout: int, allow_resend: bool = ..., tls_cfg: PDGNetTLSConfig = ...) -> int:
        """sendToGetReply(self: _pdgutils.PDGNMessage, url: str, timeout: int, allow_resend: bool = True, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> int

        Send this message and load reply into it.

        """
    def sendToGetReplyAsync(self, url: str, timeout: int = ..., allow_resend: bool = ..., tls_cfg: PDGNetTLSConfig = ...) -> int:
        """sendToGetReplyAsync(self: _pdgutils.PDGNMessage, url: str, timeout: int = -1, allow_resend: bool = True, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> int

        Send this message asynchronously and load reply into it.

        """
    def tell(self) -> int:
        """tell(self: _pdgutils.PDGNMessage) -> int

        Tell current position in buffer

        """
    def writeBytes(self, arg0: bytes, arg1: int) -> int:
        """writeBytes(self: _pdgutils.PDGNMessageBase, arg0: bytes, arg1: int) -> int

        Write size of given bytes, and then the bytes into message

        """
    def writeInt16(self, arg0: int) -> int:
        """writeInt16(self: _pdgutils.PDGNMessage, arg0: int) -> int

        Write int16 into message

        """
    def writeInt32(self, arg0: int) -> int:
        """writeInt32(self: _pdgutils.PDGNMessage, arg0: int) -> int

        Write int32 into message

        """
    def writeString(self, arg0: str) -> int:
        """writeString(self: _pdgutils.PDGNMessage, arg0: str) -> int

        Write string into message

        """
    def writeUInt16(self, arg0: int) -> int:
        """writeUInt16(self: _pdgutils.PDGNMessage, arg0: int) -> int

        Write uint16 into message

        """
    def writeUInt32(self, arg0: int) -> int:
        """writeUInt32(self: _pdgutils.PDGNMessage, arg0: int) -> int

        Write uint32 into message

        """

class PDGNMessageBase:
    def __init__(self, *, no_constructor: Never) -> None: ...

class PDGNPollingClient(PDGNPollingClientBase):
    def __init__(self, name: str, polling_time: int = ..., net_timeout: int = ..., max_recv_msgs: int = ..., tls_cfg: PDGNetTLSConfig = ...) -> None:
        """__init__(self: _pdgutils.PDGNPollingClient, name: str, polling_time: int = 10, net_timeout: int = 5000, max_recv_msgs: int = 1000, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> None"""
    def areClientsAuthenticated(self) -> bool:
        """areClientsAuthenticated(self: _pdgutils.PDGNPollingClient) -> bool

        Returns whether all clients are authenticated.

        """
    def clientName(self) -> str:
        """clientName(self: _pdgutils.PDGNPollingClient) -> str

        Returns name of client.

        """
    def getLastError(self) -> int:
        """getLastError(self: _pdgutils.PDGNPollingClient) -> int

        Get the last error.

        """
    def getNextReceivedMessage(self) -> PDGNMessage | None:
        """getNextReceivedMessage(self: _pdgutils.PDGNPollingClient) -> _pdgutils.PDGNMessageBase

        Returns the next message received from server.

        """
    def getNumReceivedMessages(self) -> int:
        """getNumReceivedMessages(self: _pdgutils.PDGNPollingClient) -> int

        Returns the number of messages received from server.

        """
    def isConnected(self) -> bool:
        """isConnected(self: _pdgutils.PDGNPollingClient) -> bool

        Returns True if connected.

        """
    def isDisconnected(self) -> bool:
        """isDisconnected(self: _pdgutils.PDGNPollingClient) -> bool

        Returns True if disconnected.

        """
    def isErrored(self) -> bool:
        """isErrored(self: _pdgutils.PDGNPollingClient) -> bool

        Returns True if errored.

        """
    def isServerAuthenticated(self) -> bool:
        """isServerAuthenticated(self: _pdgutils.PDGNPollingClient) -> bool

        Returns whether the server is authenticated.

        """
    def isServerDisconnected(self) -> bool:
        """isServerDisconnected(self: _pdgutils.PDGNPollingClient) -> bool

        Returns True if server has disconnected.

        """
    def netTimeout(self) -> int:
        """netTimeout(self: _pdgutils.PDGNPollingClient) -> int

        Returns the net time out in milliseconds.

        """
    def pollingTime(self) -> int:
        """pollingTime(self: _pdgutils.PDGNPollingClient) -> int

        Returns the polling rate in milliseconds.

        """
    def receiveMessage(self, arg0: PDGNMessageBase) -> int:
        """receiveMessage(self: _pdgutils.PDGNPollingClient, arg0: _pdgutils.PDGNMessageBase) -> int

        Receive message from server (blocking).

        """
    def sendMessage(self, arg0: PDGNMessageBase) -> int:
        """sendMessage(self: _pdgutils.PDGNPollingClient, arg0: _pdgutils.PDGNMessageBase) -> int

        Sends specified message to server (blocking).

        """
    def setLastError(self, arg0: int) -> None:
        """setLastError(self: _pdgutils.PDGNPollingClient, arg0: int) -> None

        Set the last error.

        """
    def setPollingTime(self, arg0: int) -> None:
        """setPollingTime(self: _pdgutils.PDGNPollingClient, arg0: int) -> None

        Set the polling rate in milliseconds.

        """
    def start(self, arg0: str, arg1: int) -> int:
        """start(self: _pdgutils.PDGNPollingClient, arg0: str, arg1: int) -> int

        Starts the client by connecting to server.

        """
    def stop(self) -> None:
        """stop(self: _pdgutils.PDGNPollingClient) -> None

        Stops the client and disconnects from server.

        """
    def waitUntilConnected(self, arg0: float) -> bool:
        """waitUntilConnected(self: _pdgutils.PDGNPollingClient, arg0: float) -> bool

        Blocks until connected to server or times/errors out.

        """

class PDGNPollingClientBase:
    def __init__(self, *, no_constructor: Never) -> None: ...

class PDGNetError:
    __members__: ClassVar[dict[str, PDGNetError]] = ...  # read-only
    PDGN_ERROR_CLIENT_INVALID_STATE: ClassVar[PDGNetError] = ...
    PDGN_ERROR_CLIENT_MAX_RECV_MESSAGES: ClassVar[PDGNetError] = ...
    PDGN_ERROR_CLIENT_NOT_CONNECTED: ClassVar[PDGNetError] = ...
    PDGN_ERROR_CLIENT_NOT_REGISTERED: ClassVar[PDGNetError] = ...
    PDGN_ERROR_CLIENT_REGISTER_FAIL: ClassVar[PDGNetError] = ...
    PDGN_ERROR_CLIENT_START: ClassVar[PDGNetError] = ...
    PDGN_ERROR_HTTP_BAD_HEADER: ClassVar[PDGNetError] = ...
    PDGN_ERROR_HTTP_RESPONSE_FAIL: ClassVar[PDGNetError] = ...
    PDGN_ERROR_IPRESOLVE_CONNECT: ClassVar[PDGNetError] = ...
    PDGN_ERROR_IPRESOLVE_CONV: ClassVar[PDGNetError] = ...
    PDGN_ERROR_IPRESOLVE_EAFNOSUPPORT: ClassVar[PDGNetError] = ...
    PDGN_ERROR_IPRESOLVE_ENOSPC: ClassVar[PDGNetError] = ...
    PDGN_ERROR_IPRESOLVE_SOCKET: ClassVar[PDGNetError] = ...
    PDGN_ERROR_IPRESOLVE_SOCKETNAME: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_CLIENT_NAME: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_DATA: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_EMPTY: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_INVALID: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_OVERFLOW: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_STRING_SIZE: ClassVar[PDGNetError] = ...
    PDGN_ERROR_MSG_UNSUPPORTED: ClassVar[PDGNetError] = ...
    PDGN_ERROR_PYTHON_STATE: ClassVar[PDGNetError] = ...
    PDGN_ERROR_REPLY_FAIL: ClassVar[PDGNetError] = ...
    PDGN_ERROR_REPLY_UNEXPECTED: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SEND_FAIL: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_BAD_SETTINGS: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_INVALID_STATE: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_NOT_RUNNING: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_START: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_WORKER_DISABLED: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_WORKER_INIT: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SERVER_WORKER_INVALID_STATE: ClassVar[PDGNetError] = ...
    PDGN_ERROR_SOCKET_FAIL: ClassVar[PDGNetError] = ...
    PDGN_ERROR_START: ClassVar[PDGNetError] = ...
    __entries: ClassVar[dict[str, tuple[PDGNetError, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdgutils.PDGNetError, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdgutils.PDGNetError) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdgutils.PDGNetError) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PDGNetLogLevel:
    __members__: ClassVar[dict[str, PDGNetLogLevel]] = ...  # read-only
    PDGN_LOG_ALL: ClassVar[PDGNetLogLevel] = ...
    PDGN_LOG_ERROR: ClassVar[PDGNetLogLevel] = ...
    PDGN_LOG_NONE: ClassVar[PDGNetLogLevel] = ...
    PDGN_LOG_WARNING: ClassVar[PDGNetLogLevel] = ...
    __entries: ClassVar[dict[str, tuple[PDGNetLogLevel, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdgutils.PDGNetLogLevel, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdgutils.PDGNetLogLevel) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdgutils.PDGNetLogLevel) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PDGNetMessageType:
    __members__: ClassVar[dict[str, PDGNetMessageType]] = ...  # read-only
    PDGN_MSG_CLIENT_DISCONNECTED: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_CLIENT_NOT_FOUND: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_CLIENT_REGISTER: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_CLIENT_REGISTER_OK: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_CLIENT_UNREGISTER: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_HEARTBEAT: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_HEARTBEAT_OK: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_KILL_SERVER: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_KILL_SERVER_IGNORED: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_KILL_SERVER_OK: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_NONE: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_PULL: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_PULL_OK: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_PUSH: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_PUSH_OK: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_REPLY: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_REPLY_FAILED: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_REPLY_OK: ClassVar[PDGNetMessageType] = ...
    PDGN_MSG_TYPE_NOT_SUPPORTED: ClassVar[PDGNetMessageType] = ...
    __entries: ClassVar[dict[str, tuple[PDGNetMessageType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdgutils.PDGNetMessageType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdgutils.PDGNetMessageType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdgutils.PDGNetMessageType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PDGNetTLSConfig:
    def __init__(self) -> None:
        """__init__(self: _pdgutils.PDGNetTLSConfig) -> None"""
    @staticmethod
    def clientFromFiles(cert_key_file: str, server_name: str, ca_chain_files: str = ...) -> PDGNetTLSConfig | None:
        """clientFromFiles(cert_key_file: str, server_name: str, ca_chain_files: str = []) -> object"""
    @staticmethod
    def clientFromStrings(cert: str, key: str, server_name: str, ca_chains: str = ...) -> PDGNetTLSConfig | None:
        """clientFromStrings(cert: str, key: str, server_name: str, ca_chains: str = []) -> object"""
    def makeURL(self, arg0: str, arg1: int) -> str:
        """makeURL(self: _pdgutils.PDGNetTLSConfig, arg0: str, arg1: int) -> str"""
    @staticmethod
    def serverFromFiles(cert_key_file: str, ca_chain_files: Sequence[str] = ...) -> PDGNetTLSConfig | None:
        """serverFromFiles(cert_key_file: str, ca_chain_files: UT_Array[str] = []) -> object"""
    @staticmethod
    def serverFromStrings(cert: str, key: str, ca_chains: Sequence[str] = ...) -> PDGNetTLSConfig | None:
        """serverFromStrings(cert: str, key: str, ca_chains: UT_Array[str] = []) -> object"""

def mqCreateMessage(arg0: PDGNetMessageType, arg1: bool, arg2: int, arg3: str) -> PDGNMessage:
    """mqCreateMessage(arg0: _pdgutils.PDGNetMessageType, arg1: bool, arg2: int, arg3: str) -> PDGN::PDGN_Message

    Creates and returns a general message.

    """
def mqCreateReplyMessage(arg0: str, arg1: int, arg2: str) -> PDGNMessage:
    """mqCreateReplyMessage(arg0: str, arg1: int, arg2: str) -> PDGN::PDGN_Message

    Creates and returns a reply message.

    """
def mqGetError(arg0: int) -> str:
    """mqGetError(arg0: int) -> str

    Get error description for error code.

    """
def mqLog(arg0: str) -> None:
    """mqLog(arg0: str) -> None

    General log.

    """
def mqLogError(arg0: str) -> None:
    """mqLogError(arg0: str) -> None

    Error log.

    """
def mqLogWarning(arg0: str) -> None:
    """mqLogWarning(arg0: str) -> None

    Warning log.

    """
def mqSendMessage(url: str, port: int, client_name: str, data: str, timeout: int, allow_resend: bool = ..., tls_cfg: PDGNetTLSConfig = ...) -> int:
    """mqSendMessage(url: str, port: int, client_name: str, data: str, timeout: int, allow_resend: bool = True, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> int

    Send a network message synchronously.

    """
def mqSendMessageGetReply(url: str, port: int, client_name: str, data: str, timeout: int, allow_resend: bool = ..., tls_cfg: PDGNetTLSConfig = ...) -> PDGNMessage:
    """mqSendMessageGetReply(url: str, port: int, client_name: str, data: str, timeout: int, allow_resend: bool = True, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> PDGN::PDGN_Message

    Send a network message synchronously and wait for reply.

    """
def mqSendMessageGetReplyAsync(url: str, port: int, client_name: str, data: str, timeout: int, allow_resend: bool = ..., tls_cfg: PDGNetTLSConfig = ...) -> PDGNMessage:
    """mqSendMessageGetReplyAsync(url: str, port: int, client_name: str, data: str, timeout: int, allow_resend: bool = True, tls_cfg: _pdgutils.PDGNetTLSConfig = <_pdgutils.PDGNetTLSConfig object>) -> PDGN::PDGN_Message

    Send a network message synchronously and receive reply asynchronously.

    """
def mqSetLogLevel(arg0: PDGNetLogLevel) -> None:
    """mqSetLogLevel(arg0: _pdgutils.PDGNetLogLevel) -> None

    Set the log level for MQ.

    """

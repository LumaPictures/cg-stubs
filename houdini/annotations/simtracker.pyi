import queue
import socket
import socketserver
import threading
from _typeshed import SupportsWrite
from collections.abc import Callable, Iterable, Sequence
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import NotRequired, TypedDict

class _PeerAddress(TypedDict):
    address: str
    port: int

class _JobPeer(TypedDict):
    proc: int
    port: int
    address: str
    acquiretime: float
    donetime: float

class _BarrierPeer(TypedDict):
    jobname: str
    address: str
    port: int
    acquiretime: float
    waitval: int
    donetime: float

class _Job(TypedDict):
    nproc: int
    done: int
    error: bool
    starttime: float
    synctime: float
    donetime: float
    proclist: list[_JobPeer]
    jobname: NotRequired[str]

class _Barrier(TypedDict):
    val: int
    settime: float
    proclist: list[_BarrierPeer]

glb_readqueue: queue.Queue[tuple[socket.socket, tuple[str, int]]]
glb_writequeue: queue.Queue[tuple[_PeerAddress, str]]
glb_msgqueue: queue.Queue[tuple[tuple[str, int], str]]
joblist: dict[str, _Job]
glb_donelist: list[_Job]
glb_doneEvent: threading.Event
glb_joblock: threading.RLock
glb_barrierlist: dict[str, _Barrier]
glb_barrierdone: list[_BarrierPeer]
glb_listenReadyEvent: threading.Event
glb_webReadyEvent: threading.Event
default_timer: Callable[[], float]
glb_port: int
glb_webPort: int
glb_verbose: bool

def getListenPort() -> int: ...
def getWebPort() -> int: ...
def printMsg(msg: str) -> None: ...
def setVerbosity(verbose: bool) -> None: ...
def waitForCompletion(timeout: float | None = ...) -> bool: ...
def waitForListener() -> None: ...
def writeBarrierInfo(wfile: SupportsWrite[str], job: _Barrier, jobname: str) -> None: ...
def writeBarrierPeerInfo(wfile: SupportsWrite[str], peerlist: Sequence[_BarrierPeer]) -> None: ...
def writeJobInfo(wfile: SupportsWrite[str], job: _Job, jobname: str) -> None: ...
def writeHtml(wfile: SupportsWrite[str]) -> None: ...

class TrackerHttpServer(HTTPServer):
    def __init__(self, address: tuple[str, int]) -> None: ...

class WFileAdaptor:
    wfile: SupportsWrite[bytes]
    def __init__(self, wfile: SupportsWrite[bytes]) -> None: ...
    def write(self, s: str) -> None: ...

class TrackerHttpHandler(BaseHTTPRequestHandler):
    def __init__(self, request: socket.socket, client_address: tuple[str, int], server: socketserver.BaseServer) -> None: ...
    def do_GET(self) -> None: ...
    def log_message(self, format: str, *args: object) -> None: ...

class HttpServerThread(threading.Thread):
    port: int
    def __init__(self, port: int) -> None: ...
    def run(self) -> None: ...

class ListenThread(threading.Thread):
    port: int
    def __init__(self, port: int) -> None: ...
    def run(self) -> None: ...

class ReadThread(threading.Thread):
    def run(self) -> None: ...

class WriteThread(threading.Thread):
    def run(self) -> None: ...

def readmessage(s: socket.socket) -> str: ...
def writemessage(s: socket.socket, data: str) -> None: ...
def postmessage(peer: _PeerAddress, data: str) -> None: ...
def sendmessage(peer: _PeerAddress, data: str) -> None: ...
def sendclientlist(client: _PeerAddress, list: Iterable[_JobPeer]) -> None: ...
def serve(port: int, webport: int) -> None: ...

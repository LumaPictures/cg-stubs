import socket
from _typeshed import Incomplete

PROXY_TYPE_SOCKS4: int
PROXY_TYPE_SOCKS5: int
PROXY_TYPE_HTTP: int
PROXY_TYPE_HTTP_NO_TUNNEL: int
_defaultproxy: Incomplete
_orgsocket = socket.socket

class ProxyError(Exception): ...
class GeneralProxyError(ProxyError): ...
class Socks5AuthError(ProxyError): ...
class Socks5Error(ProxyError): ...
class Socks4Error(ProxyError): ...
class HTTPError(ProxyError): ...

_generalerrors: Incomplete
_socks5errors: Incomplete
_socks5autherrors: Incomplete
_socks4errors: Incomplete

def setdefaultproxy(proxytype=None, addr=None, port=None, rdns: bool = True, username=None, password=None) -> None:
    """setdefaultproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
    Sets a default proxy which all further socksocket objects will use,
    unless explicitly changed.
    """
def wrapmodule(module) -> None:
    """wrapmodule(module)

    Attempts to replace a module's socket library with a SOCKS socket. Must set
    a default proxy using setdefaultproxy(...) first.
    This will only work on modules that import socket directly into the
    namespace;
    most of the Python Standard Library falls into this category.
    """

class socksocket(socket.socket):
    """socksocket([family[, type[, proto]]]) -> socket object
    Open a SOCKS enabled socket. The parameters are the same as
    those of the standard socket init. In order for SOCKS to work,
    you must specify family=AF_INET, type=SOCK_STREAM and proto=0.
    """
    __proxy: Incomplete
    __proxysockname: Incomplete
    __proxypeername: Incomplete
    __httptunnel: bool
    def __init__(self, family=..., type=..., proto: int = 0, _sock=None) -> None: ...
    def __recvall(self, count):
        """__recvall(count) -> data
        Receive EXACTLY the number of bytes requested from the socket.
        Blocks until the required number of bytes have been received.
        """
    def sendall(self, content, *args):
        """ override socket.socket.sendall method to rewrite the header
        for non-tunneling proxies if needed
        """
    def __rewriteproxy(self, header):
        """ rewrite HTTP request headers to support non-tunneling proxies
        (i.e. those which do not support the CONNECT method).
        This only works for HTTP (not HTTPS) since HTTPS requires tunneling.
        """
    def __getauthheader(self): ...
    def setproxy(self, proxytype=None, addr=None, port=None, rdns: bool = True, username=None, password=None, headers=None) -> None:
        """setproxy(proxytype, addr[, port[, rdns[, username[, password]]]])

        Sets the proxy to be used.
        proxytype -    The type of the proxy to be used. Three types
                are supported: PROXY_TYPE_SOCKS4 (including socks4a),
                PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP
        addr -        The address of the server (IP or DNS).
        port -        The port of the server. Defaults to 1080 for SOCKS
                servers and 8080 for HTTP proxy servers.
        rdns -        Should DNS queries be preformed on the remote side
                (rather than the local side). The default is True.
                Note: This has no effect with SOCKS4 servers.
        username -    Username to authenticate with to the server.
                The default is no authentication.
        password -    Password to authenticate with to the server.
                Only relevant when username is also provided.
        headers -     Additional or modified headers for the proxy connect
        request.
        """
    def __negotiatesocks5(self, destaddr, destport) -> None:
        """__negotiatesocks5(self,destaddr,destport)
        Negotiates a connection through a SOCKS5 server.
        """
    def getproxysockname(self):
        """getsockname() -> address info
        Returns the bound IP address and port number at the proxy.
        """
    def getproxypeername(self):
        """getproxypeername() -> address info
        Returns the IP and port number of the proxy.
        """
    def getpeername(self):
        """getpeername() -> address info
        Returns the IP address and port number of the destination
        machine (note: getproxypeername returns the proxy)
        """
    def __negotiatesocks4(self, destaddr, destport) -> None:
        """__negotiatesocks4(self,destaddr,destport)
        Negotiates a connection through a SOCKS4 server.
        """
    def __negotiatehttp(self, destaddr, destport) -> None:
        """__negotiatehttp(self,destaddr,destport)
        Negotiates a connection through an HTTP server.
        """
    def connect(self, destpair) -> None:
        """connect(self, despair)
        Connects to the specified destination through a proxy.
        destpar - A tuple of the IP/DNS address and the port number.
        (identical to socket's connect).
        To select the proxy server use setproxy().
        """

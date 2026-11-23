import http.client
import json
import base64



class PainterError(Exception):
    def __init__(self, message):
        super(PainterError, self).__init__(message)


class ExecuteScriptError(PainterError):
    def __init__(self, data):
        super(PainterError, self).__init__('An error occurred when executing script: {0}'.format(data))


class RemotePainter() :
    def __init__(self, port=60041, host='localhost'):
        self._host = host
        self._port = port

        # Json server connection
        self._PAINTER_ROUTE = '/run.json'
        self._HEADERS = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

    # Execute a HTTP POST request to the Substance Painter server and send/receive JSON data
    def _jsonPostRequest( self, route, body, type ) :
        connection = http.client.HTTPConnection(self._host, self._port, timeout=3600)
        connection.request('POST', route, body, self._HEADERS)
        response = connection.getresponse()

        data = response.read()
        connection.close()

        if type == "js" :
            data = json.loads( data.decode('utf-8') or "" ).strip()

        j_data = json.loads(data)
        if j_data and isinstance(j_data, dict) and 'error' in j_data:
            raise ExecuteScriptError(j_data['error']["description"])

        return data

    def checkConnection(self):
        connection = http.client.HTTPConnection(self._host, self._port)
        connection.connect()

    # Execute a command
    def execScript( self, script, type ) :
        Command = base64.b64encode( script.encode('utf-8') )

        if type == "js" :
            Command = '{{"js":"{0}"}}'.format( Command.decode('utf-8') )
        else :
            Command = '{{"python":"{0}"}}'.format( Command.decode('utf-8') )

        Command = Command.encode( "utf-8" )

        return self._jsonPostRequest( self._PAINTER_ROUTE, Command, type )


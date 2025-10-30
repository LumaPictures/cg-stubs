from types import ModuleType

__all__ = ['QtCore', 'QtGui', 'QtWidgets', 'QtPrintSupport', 'QtSql', 'QtNetwork', 'QtTest', 'QtConcurrent', 'QtDBus', 'QtDesigner', 'QtXml', 'QtHelp', 'QtMultimedia', 'QtMultimediaWidgets', 'QtOpenGL', 'QtOpenGLWidgets', 'QtPdf', 'QtPdfWidgets', 'QtPositioning', 'QtLocation', 'QtNetworkAuth', 'QtNfc', 'QtQml', 'QtQuick', 'QtQuick3D', 'QtQuickControls2', 'QtQuickTest', 'QtQuickWidgets', 'QtRemoteObjects', 'QtScxml', 'QtSensors', 'QtSerialPort', 'QtSerialBus', 'QtStateMachine', 'QtTextToSpeech', 'QtCharts', 'QtSpatialAudio', 'QtSvg', 'QtSvgWidgets', 'QtDataVisualization', 'QtGraphs', 'QtGraphsWidgets', 'QtBluetooth', 'QtUiTools', 'QtWebChannel', 'QtWebEngineCore', 'QtWebEngineWidgets', 'QtWebEngineQuick', 'QtWebSockets', 'QtHttpServer', 'QtWebView', 'Qt3DCore', 'Qt3DRender', 'Qt3DInput', 'Qt3DLogic', 'Qt3DAnimation', 'Qt3DExtras']

class ModuleDict(dict):
    def __missing__(self, key): ...

class SubModule(ModuleType): ...

# Names in __all__ with no definition:
#   Qt3DAnimation
#   Qt3DCore
#   Qt3DExtras
#   Qt3DInput
#   Qt3DLogic
#   Qt3DRender
#   QtBluetooth
#   QtCharts
#   QtConcurrent
#   QtCore
#   QtDBus
#   QtDataVisualization
#   QtDesigner
#   QtGraphs
#   QtGraphsWidgets
#   QtGui
#   QtHelp
#   QtHttpServer
#   QtLocation
#   QtMultimedia
#   QtMultimediaWidgets
#   QtNetwork
#   QtNetworkAuth
#   QtNfc
#   QtOpenGL
#   QtOpenGLWidgets
#   QtPdf
#   QtPdfWidgets
#   QtPositioning
#   QtPrintSupport
#   QtQml
#   QtQuick
#   QtQuick3D
#   QtQuickControls2
#   QtQuickTest
#   QtQuickWidgets
#   QtRemoteObjects
#   QtScxml
#   QtSensors
#   QtSerialBus
#   QtSerialPort
#   QtSpatialAudio
#   QtSql
#   QtStateMachine
#   QtSvg
#   QtSvgWidgets
#   QtTest
#   QtTextToSpeech
#   QtUiTools
#   QtWebChannel
#   QtWebEngineCore
#   QtWebEngineQuick
#   QtWebEngineWidgets
#   QtWebSockets
#   QtWebView
#   QtWidgets
#   QtXml
__version__: str
__version_info__: tuple[int, int, float, str, str]

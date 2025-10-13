from __future__ import absolute_import, print_function

import datetime
import sys
from typing import Any, ClassVar, List, TYPE_CHECKING

import PySide2
import pytest
from PySide2 import QtCore, QtGui, QtQuick, QtWidgets

from stubgenlib.test_helpers import assert_type

pyside_version = PySide2.__version_info__


def test_qmenu1() -> None:
    # FIXME: these tests are very slow, but I can't figure out how to make them faster
    self = QtWidgets.QWidget()
    pos = QtCore.QPoint(0, 0)

    # Add actions to the menu
    action1 = QtWidgets.QAction("Action 1")
    menu1 = QtWidgets.QMenu(self)
    menu1.addAction(action1)
    menu1.exec_(pos, at=action1)


def test_qmenu() -> None:
    self = QtWidgets.QWidget()
    pos = QtCore.QPoint(0, 0)
    action = QtWidgets.QAction("Action 1")
    QtWidgets.QMenu.exec_([action], pos, action, self)


def test_qmenu2() -> None:
    self = QtWidgets.QWidget()
    pos = QtCore.QPoint(0, 0)
    action2 = QtWidgets.QAction("Action 1")
    menu2 = QtWidgets.QMenu(self)
    menu2.exec_([action2], pos, action2, self)


def test_qmenu3() -> None:
    self = QtWidgets.QWidget()
    action3 = QtWidgets.QAction("Action 1")
    menu3 = QtWidgets.QMenu(self)
    # Add actions to the menu
    menu3.addAction(action3)
    menu3.exec_()


def test_qmenu_failures() -> None:
    with pytest.raises(Exception):
        QtWidgets.QMenu.exec_(actions)  # type: ignore

    if TYPE_CHECKING:
        # these cause python to crash
        with pytest.raises(Exception):
            QtWidgets.QMenu.exec_(pos)  # type: ignore

        with pytest.raises(Exception):
            QtWidgets.QMenu.exec_()  # type: ignore

        with pytest.raises(Exception):
            QtWidgets.QMenu(self).exec_(None)  # type: ignore


def test_qapplication() -> None:
    def slotAppStateChanged(*args: Any) -> None:
        pass

    app = QtWidgets.QApplication.instance()
    assert_type(app.instance(), QtWidgets.QApplication)
    assert_type(app, QtWidgets.QApplication)

    app.applicationStateChanged.connect(slotAppStateChanged)
    QtWidgets.QApplication.processEvents()


def test_qaction() -> None:
    a = QtWidgets.QAction()
    a.setShortcut("Ctrl+F")


@pytest.mark.skipif(
    pyside_version <= (5, 14), reason="causes crash in PySide2 < 5.14.2.3"
)
def test_qbytearray() -> None:
    byte_array = QtCore.QByteArray(b"foo")
    b: bytes
    b = byte_array[0]
    assert isinstance(b, bytes)
    b = bytes(byte_array)

    x: bytes
    for x in byte_array:
        assert isinstance(x, bytes)


def test_qcoreapplication() -> None:
    assert_type(
        QtCore.QCoreApplication.translate("GitFlowAdvanceIntBranch", "hidden", None),
        str,
    )
    assert_type(
        QtCore.QCoreApplication.translate(
            "GitFlowAdvanceIntBranch", "hidden", "some help"
        ),
        str,
    )


def test_qdate() -> None:
    d = QtCore.QDate(datetime.date(1980, 3, 31))
    assert d.daysTo(datetime.date(1981, 3, 31)) == 365

    assert QtCore.QDate.isValid(2025, 1, 1) is True
    assert QtCore.QDate(2025, 1, 1).isValid() is True

    with pytest.raises(Exception):
        # it is not acceptable to call the instance method with an argument
        QtCore.QDate(2025, 1, 1).isValid("BAD")  # type: ignore[call-overload]

    with pytest.raises(Exception):
        # confirm that the static method fails with the wrong arguments
        QtCore.QDate.isValid("BAD")  # type: ignore[call-arg, arg-type]


def test_qdatetime() -> None:
    d = QtCore.QDateTime(datetime.datetime(1980, 3, 31))
    assert d.daysTo(datetime.datetime(1981, 3, 31)) == 365


def test_qdialog() -> None:
    d = QtWidgets.QDialog()
    f = d.exec_
    f = d.exec


def test_qdialogbuttonbox() -> None:
    a: QtWidgets.QDialogButtonBox.StandardButtons
    a = (
        QtWidgets.QDialogButtonBox.StandardButton.Ok
        | QtWidgets.QDialogButtonBox.StandardButton.Ok
    )
    assert isinstance(a, QtWidgets.QDialogButtonBox.StandardButtons)
    d = a | QtWidgets.QDialogButtonBox.StandardButton.Ok
    assert isinstance(d, QtWidgets.QDialogButtonBox.StandardButtons)
    e = a | a


def test_qguiapplication() -> None:
    app: QtGui.QGuiApplication
    app = QtGui.QGuiApplication.instance()
    app.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)


def test_qicon() -> None:
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(":/img/multigit-logo-256.png"),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off,
    )


def test_qlabel() -> None:
    l = QtWidgets.QLabel()
    l.setAlignment(QtCore.Qt.AlignCenter)


def test_qmessagebox() -> None:
    multiple_buttons = QtWidgets.QMessageBox.StandardButtons()
    multiple_buttons = (
        QtWidgets.QMessageBox.StandardButton.Ok
        | QtWidgets.QMessageBox.StandardButton.Ok
    )
    multiple_buttons = QtWidgets.QMessageBox.StandardButton.Ok | 0
    multiple_buttons = multiple_buttons | 0
    multiple_buttons = multiple_buttons | QtWidgets.QMessageBox.StandardButton.Ok
    multiple_buttons = multiple_buttons | multiple_buttons
    multiple_buttons = QtWidgets.QMessageBox.StandardButtons(44)
    multiple_buttons = QtWidgets.QMessageBox.StandardButtons(
        QtWidgets.QMessageBox.StandardButton.Ok
    )
    multiple_buttons = QtWidgets.QMessageBox.StandardButtons(
        QtWidgets.QMessageBox.StandardButton.Ok
        | QtWidgets.QMessageBox.StandardButton.Ok
    )

    one_button = QtWidgets.QMessageBox.StandardButton.Ok
    one_button = QtWidgets.QMessageBox.StandardButton(44)
    one_button = QtWidgets.QMessageBox.StandardButton(
        QtWidgets.QMessageBox.StandardButton.Ok
    )
    one_button = QtWidgets.QMessageBox.Ok


def test_qobject() -> None:
    o1 = QtWidgets.QWidget()
    o2 = QtWidgets.QWidget(o1)
    o3 = QtCore.QObject(o1)

    a: List[QtCore.QObject]
    a = o1.findChildren(QtCore.QObject)
    assert type(a) == list
    assert isinstance(a[0], QtCore.QObject)

    b: List[QtWidgets.QWidget]
    b = o1.findChildren(QtWidgets.QWidget)
    assert type(b) == list
    assert isinstance(b[0], QtWidgets.QWidget)

    # incorrect here, correctly detected by mypy
    c: List[QtWidgets.QWidget]
    c = o1.findChildren(QtCore.QObject, "")  # type: ignore[arg-type]

    # cast works, List[QWidget] is a List[QObject]
    d: List[QtCore.QObject]
    d = o1.findChildren(QtWidgets.QWidget, "")


def test_qpainter() -> None:
    painter = QtGui.QPainter()

    painter.beginNativePainting()
    painter.drawConvexPolygon(
        [QtCore.QPoint(0, 0), QtCore.QPoint(1, 1), QtCore.QPoint(2, 2)]
    )
    painter.drawConvexPolygon(
        [QtCore.QPointF(0.0, 0.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(2.0, 2.0)]
    )

    painter.drawPolygon([QtCore.QPoint(0, 0), QtCore.QPoint(1, 1), QtCore.QPoint(2, 2)])
    painter.drawPolygon(
        [QtCore.QPointF(0.0, 0.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(2.0, 2.0)]
    )
    painter.drawPolygon(
        [QtCore.QPoint(0, 0), QtCore.QPoint(1, 1), QtCore.QPoint(2, 2)],
        QtCore.Qt.FillRule.OddEvenFill,
    )
    # painter.drawPolygon([QtCore.QPoint(0, 0), QtCore.QPoint(1, 1), QtCore.QPoint(2, 2)],
    #                     None)
    painter.drawPolyline(
        [QtCore.QPoint(0, 0), QtCore.QPoint(1, 1), QtCore.QPoint(2, 2)]
    )
    painter.drawPolyline(
        [QtCore.QPointF(0.0, 0.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(2.0, 2.0)]
    )
    painter.drawRects(
        [
            QtCore.QRectF(0.0, 1.0, 2.0, 3.0),
            QtCore.QRectF(1.0, 2.0, 3.0, 4.0),
            QtCore.QRectF(2.0, 3.0, 4.0, 5.0),
        ]
    )
    painter.drawRects(
        [QtCore.QRect(0, 1, 2, 3), QtCore.QRect(1, 2, 3, 4), QtCore.QRect(2, 3, 4, 5)]
    )
    painter.drawLines(
        [
            QtCore.QLineF(0.0, 1.0, 2.0, 3.0),
            QtCore.QLineF(1.0, 2.0, 3.0, 4.0),
            QtCore.QLineF(2.0, 3.0, 4.0, 5.0),
        ]
    )
    painter.drawLines(
        [QtCore.QLine(0, 1, 2, 3), QtCore.QLine(1, 2, 3, 4), QtCore.QLine(2, 3, 4, 5)]
    )
    painter.drawPoints([QtCore.QPoint(0, 0), QtCore.QPoint(1, 1), QtCore.QPoint(2, 2)])
    painter.drawPoints(
        [QtCore.QPointF(0.0, 0.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(2.0, 2.0)]
    )

    painter.drawText(QtCore.QRectF(0.0, 1.0, 2.0, 3.0), QtCore.Qt.AlignLeft, "text")
    painter.drawText(QtCore.QRect(0, 1, 2, 3), QtCore.Qt.AlignLeft, "text")
    painter.end()


def test_qpixmap() -> None:
    emptyPixmap = QtGui.QPixmap(16, 16)
    emptyPixmap.fill(QtCore.Qt.transparent)
    # we currenly choose not to allow str literals because it is too ambiguous.
    # use constants to enforce proper types
    # emptyPixmap.fill("white")
    emptyPixmap.fill(QtCore.Qt.GlobalColor.white)
    emptyPixmap.fill(0xFFFFFF)


def test_qpolygon() -> None:
    point: QtCore.QPoint
    point_list: List[QtCore.QPoint]

    point = QtCore.QPoint()
    point_list = [point]

    polygon = QtGui.QPolygon()
    polygon << point << point
    polygon << [point, point]
    polygon << [point, point] << [point, point]

    assert type(polygon << point) == QtGui.QPolygon
    poly: QtGui.QPolygon
    poly = polygon << point

    assert type(polygon << [point]) == QtGui.QPolygon
    poly = polygon << [point]

    point_list = polygon + [point]
    assert type(point_list) == list
    assert type(point_list[0]) == QtCore.QPoint
    point_list = polygon + [point]

    polygon += point
    assert type(polygon) == QtGui.QPolygon


def test_qprocess() -> None:
    v = int(QtCore.QProcess.ExitStatus.NormalExit)


def test_qprogressdialog() -> None:
    qp = QtWidgets.QProgressDialog()
    qp.setCancelButton(None)


def test_qpropertyanimation() -> None:
    dialog = QtWidgets.QDialog()
    anim = QtCore.QPropertyAnimation(dialog)
    anim.setPropertyName("geometry".encode("ascii"))
    assert isinstance(anim.propertyName(), QtCore.QByteArray)


def test_qquickitem() -> None:
    qi = QtQuick.QQuickItem()
    qi.setCursor(QtCore.Qt.WaitCursor)


def test_qsize() -> None:
    qs1 = QtCore.QSize(1, 2)
    qs2 = QtCore.QSize(3, 4)
    qs3 = QtCore.QSize(5, 6)

    qs3 = qs1 + qs2
    assert type(qs3) == QtCore.QSize
    qs3 = qs1 - qs2
    assert type(qs3) == QtCore.QSize
    qs3 += qs1
    assert type(qs3) == QtCore.QSize
    qs3 -= qs2
    assert type(qs3) == QtCore.QSize

    qs3 = qs1 * 3
    assert type(qs3) == QtCore.QSize
    qs3 = qs1 * 3.0
    assert type(qs3) == QtCore.QSize

    qs3 = 3 * qs1
    assert type(qs3) == QtCore.QSize
    qs3 = 3.0 * qs1
    assert type(qs3) == QtCore.QSize

    qs3 = qs1 / 2.0
    assert type(qs3) == QtCore.QSize

    qs3 *= 3
    assert type(qs3) == QtCore.QSize
    qs3 *= 3.0
    assert type(qs3) == QtCore.QSize

    qs3 /= 3.0
    assert type(qs3) == QtCore.QSize

    # QSizeF tests
    qsf1 = QtCore.QSizeF(1.0, 2.0)
    qsf2 = QtCore.QSizeF(3.0, 4.0)
    qsf3 = QtCore.QSizeF(5.0, 6.0)

    qsf3 = qsf1 + qsf2
    assert type(qsf3) == QtCore.QSizeF
    qsf3 = qsf1 - qsf2
    assert type(qsf3) == QtCore.QSizeF
    qsf3 += qsf1
    assert type(qsf3) == QtCore.QSizeF
    qsf3 -= qsf2
    assert type(qsf3) == QtCore.QSizeF

    qsf3 = qsf1 * 3
    assert type(qsf3) == QtCore.QSizeF
    qsf3 = qsf1 * 3.0
    assert type(qsf3) == QtCore.QSizeF

    qsf3 = 3 * qsf1
    assert type(qsf3) == QtCore.QSizeF
    qsf3 = 3.0 * qsf1
    assert type(qsf3) == QtCore.QSizeF

    qsf3 = qsf1 / 2.0
    assert type(qsf3) == QtCore.QSizeF

    qsf3 *= 3
    assert type(qsf3) == QtCore.QSizeF
    qsf3 *= 3.0
    assert type(qsf3) == QtCore.QSizeF

    qsf3 /= 3.0
    assert type(qsf3) == QtCore.QSizeF


def test_qspaceritem() -> None:
    # in C++ the size args are named hPolicy and vPolicy, but in PySide they
    # renamed to hData and vData, but both are valid.
    s = QtWidgets.QSpacerItem(
        10,
        20,
        hPolicy=QtWidgets.QSizePolicy.Expanding,
        vPolicy=QtWidgets.QSizePolicy.Expanding,
    )
    s = QtWidgets.QSpacerItem(
        10,
        20,
        hData=QtWidgets.QSizePolicy.Expanding,
        vData=QtWidgets.QSizePolicy.Expanding,
    )


def test_qsplitter() -> None:
    s = QtWidgets.QSplitter()
    b: QtCore.QByteArray
    b = s.saveState()
    assert isinstance(b, QtCore.QByteArray)


def test_qtimer() -> None:
    timout_sig_unbound: QtCore.Signal = QtCore.QTimer.timeout
    assert isinstance(timout_sig_unbound, QtCore.Signal)

    timer = QtCore.QTimer()
    timeout_sig_bount: QtCore.SignalInstance = timer.timeout
    assert isinstance(timeout_sig_bount, QtCore.SignalInstance)

    timer.timeout.connect(lambda: None)


def test_qtreewidget() -> None:
    t = QtWidgets.QTreeWidget()
    item = t.topLevelItem(400)
    assert item is None
    # default type returned by topLevelItem() should allow None value
    item = None


def test_qtreewidgetitem() -> None:
    t = QtWidgets.QTreeWidgetItem()

    b = True  # type: bool
    b = t < t
    if pyside_version >= (5, 15, 0):
        b = t == t
        b = t != t

    t.setForeground(3, QtGui.QColor(QtCore.Qt.red))
    t.setBackground(3, QtGui.QColor(QtCore.Qt.red))

    t.setData(0, QtCore.Qt.ItemDataRole(33), "bla")
    t.setData(0, QtCore.Qt.ToolTipRole, "bla")

    t.data(0, QtCore.Qt.ItemDataRole(33))
    t.data(0, QtCore.Qt.ToolTipRole)


def test_qversion() -> None:
    s = ""  # type: str
    s = QtCore.qVersion()
    assert isinstance(s, str)


def test_qwidget() -> None:
    w = QtWidgets.QWidget()
    w.setCursor(QtCore.Qt.WaitCursor)


def test_qwindow() -> None:
    w = QtGui.QWindow()
    w.setCursor(QtCore.Qt.WaitCursor)


def test_signal_slot() -> None:
    class SomeClassWithSignal(QtCore.QObject):
        signal_no_arg: ClassVar[QtCore.Signal] = QtCore.Signal()
        signal_str: ClassVar[QtCore.Signal] = QtCore.Signal(str)

        def __init__(self) -> None:
            super().__init__()  # note: this is mandatory for mypy to pickup the class attribute access

        def my_slot_no_arg(self) -> None:
            pass

        def my_slot_str(self, msg: str) -> None:
            pass

    instance = SomeClassWithSignal()

    connection = True
    connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
    instance.signal_no_arg.emit()
    assert isinstance(connection, bool)

    connection = instance.signal_str.connect(instance.my_slot_str)
    instance.signal_str.emit("toto")
    assert isinstance(connection, bool)

    instance.signal_str.disconnect()

    connection = instance.signal_str[str].connect(instance.my_slot_str)
    instance.signal_str[str].emit("toto")
    assert isinstance(connection, bool)


def test_qbrush_implicit_args() -> None:
    painter = QtGui.QPainter()
    grad = QtGui.QLinearGradient(0, 0, 0, 100)
    grad.setColorAt(0.0, QtGui.QColor(0, 0, 0, 0))
    grad.setColorAt(0.4, QtGui.QColor(0, 0, 0, 0))
    grad.setColorAt(0.9, QtGui.QColor(0, 0, 0, 180))

    painter.setBrush(grad)
    painter.setBrush(QtGui.QColor(0, 0, 0, 0))
    painter.setBrush(QtCore.Qt.GlobalColor.black)


@pytest.mark.skipif(pyside_version < (5, 14), reason="fails in PySide2 < 5.14.2.3")
def test_iterability() -> None:
    # works with list or iterator
    option1 = QtCore.QCommandLineOption(["one", "won"])
    option2 = QtCore.QCommandLineOption(iter(["two", "too"]))
    option3 = QtCore.QCommandLineOption("three")

    parser = QtCore.QCommandLineParser()
    # This fails even with a list:
    # parser.addOptions(iter([option1, option2]))
    # parser.addOptions([option1, option2])
    parser.addOption(option1)
    parser.addOption(option2)
    parser.addOption(option3)

    # No errors, but these don't work as expected, even with a list:
    # assert QDir.match('*.txt', '/path/to/foo.txt') is True
    # assert QDir.match(['*.txt'], '/path/to/foo.txt') is True
    # assert QDir.match(iter(['*.txt']), '/path/to/foo.txt') is True

    array = QtCore.QJsonArray.fromStringList(iter(["foo", "bar"]))
    assert array.at(0).isString()

    combo = QtWidgets.QComboBox()
    combo.addItems(iter(["one", "two", "three"]))
    assert combo.count() == 3

    model = QtCore.QStringListModel()
    model.setStringList(iter(["one", "two", "three"]))
    assert model.stringList() == ["one", "two", "three"]

    group = QtWidgets.QListWidget()
    group.addItems(iter(["one", "two", "three"]))
    assert combo.count() == 3


def test_fonts() -> None:
    w = QtWidgets.QTextEdit()
    w.setFontWeight(QtGui.QFont.DemiBold)


def test_qfile() -> None:
    current_file: str | None = sys.modules[__name__].__file__
    assert current_file is not None
    qfile = QtCore.QFile(current_file)
    assert qfile.exists() is True
    assert QtCore.QFile.exists(current_file) is True


def test_qline() -> None:
    line = QtCore.QLineF(1, 2, 3, 4)

    # Get line as tuple: (x1, y1, x2, y2)
    coords = line.toTuple()
    assert_type(coords, tuple[Any, ...])

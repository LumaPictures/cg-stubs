from .common import FixableDoubleValidator as FixableDoubleValidator
from .preferencesUI import Ui_Preferences as Ui_Preferences
from .qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

class Preferences(QtWidgets.QDialog):
    """The dataModel provided to this VC must conform to the following
    interface:

    Editable properties:
       fontSize, int

    Readable properties:

    Signals:
       viewSettings.signalSettingChanged() - whenever any view setting 
                                             may have changed.
    """
    _ui: Incomplete
    _dataModel: Incomplete
    _muteUpdates: bool
    def __init__(self, parent, dataModel) -> None: ...
    def _updateEditorsFromDataModel(self) -> None: ...
    def _apply(self) -> None: ...
    def _buttonBoxButtonClicked(self, button) -> None: ...

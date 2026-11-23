import PySide6.QtGui  # type: ignore[import-not-found]
import PySide6.QtWidgets  # type: ignore[import-not-found]
from _typeshed import Incomplete

from _substance_painter.ui import UIMode as UIMode
from _substance_painter.ui import ApplicationMenu as ApplicationMenu

def show_main_window() -> None:
    """Show Substance 3D Painter main window in the windowing system and give it the focus.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def get_main_window() -> PySide6.QtWidgets.QMainWindow:
    """Get access to Substance 3D Painter main window.

    Returns:
        PySide6.QtWidgets.QMainWindow: The application main window.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def get_layout(mode: UIMode) -> bytes:
    """Get Substance 3D Painter layout state for the given UI mode.

    Args:
        mode (UIMode): Selected UI mode.

    Returns:
        bytes: The layout state.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def get_layout_mode(layout: bytes) -> UIMode:
    """Get the Substance 3D Painter UI layout mode of a given state.

    Args:
        layout (bytes): The layout state, obtained with :func:`get_layout`.

    Returns:
        UIMode: The state associated UI mode.

    Raises:
        RuntimeError: In case of incorrect layout data.
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def set_layout(layout: bytes) -> UIMode:
    """Restore a Substance 3D Painter layout state optained with :func:`get_layout`.

    Args:
        layout (bytes): The layout state to be restored.

    Returns:
        UIMode: The restored UI mode.

    Raises:
        RuntimeError: In case of incorrect layout data.
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def reset_layout(mode: UIMode):
    """Reset Substance 3D Painter layout to default for a selected UI mode.

    Args:
        mode (UIMode): Selected UI mode.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def add_dock_widget(widget: PySide6.QtWidgets.QWidget, ui_modes: int = ...) -> PySide6.QtWidgets.QDockWidget:
    """Add a widget as a QDockWidget to the main window.

    If the widget has a ``windowIcon``, it will be used as a quick button to easily
    reopen the QDockWidget when closed. If the widget has a unique ``objectName`` it
    will be used to properly save and restore the dock widget location and geometry.

    Args:
        widget (PySide6.QtWidgets.QWidget): The widget to be added as a dock widget.
        ui_modes (int, optional): A combination of `UIMode` flags.

    Returns:
        PySide6.QtWidgets.QDockWidget: The corresponding dock widget.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def add_plugins_toolbar_widget(widget: PySide6.QtWidgets.QWidget):
    """Add a widget to the plugins toolbar.

    Args:
        widget (PySide6.QtWidgets.QWidget): The widget to be added.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def add_menu(menu: PySide6.QtWidgets.QMenu):
    """Add the given menu to the application main window.

    Args:
        menu (PySide6.QtWidgets.QMenu): The menu to be added.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def add_toolbar(title: str, object_name: str, ui_modes: int = ...) -> PySide6.QtWidgets.QToolBar:
    """Create and add a toolbar to the application main window.

    Args:
        title (str): The title of the toolbar.
        object_name (str): The toolbar object name. A unique object name is mandatory for proper
            save and restore of the UI layout.
        ui_modes (int): A combination of `UIMode` flags.

    Returns:
        PySide6.QtWidgets.QToolBar: The newly created toolbar.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def add_action(menu: ApplicationMenu, action: PySide6.QtGui.QAction):
    """Add the given action to the given application menu.

    This will clear the action tooltip.

    Args:
        menu (ApplicationMenu): One of the predefined `ApplicationMenu`.
        action (PySide6.QtGui.QAction): The action to be added.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def delete_ui_element(element: PySide6.QtWidgets.QWidget):
    """Delete a UI element.

    The element passed as parameter is deleted. After that, any attempt to call a
    method on ``element`` will throw an exception.

    Args:
        element: The UI element to delete.
    """
def get_current_mode() -> UIMode:
    """
    Get the current UI mode.

    Returns:
        UIMode: The current UI mode.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """
def switch_to_mode(mode: UIMode) -> None:
    """
    Switch to some UI mode.

    Args:
        mode (UIMode): UI mode to switch to.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started its UI service.
    """

# mypy: disable-error-code="misc, override, no-redef"

import pxr.Plug as Plug
import pxr.Tf as Tf
from _typeshed import Incomplete
from pxr.Tf import PluginContainerTfType as PluginContainerTfType

class CommandPlugin:
    """A Usdview command plugin object. The plugin's `callback` parameter must
    be a callable object which takes a UsdviewApi object as its only parameter.
    """
    def __init__(self, name, displayName, callback, description, usdviewApi) -> None: ...
    def run(self):
        """Run the command's callback function."""
    @property
    def description(self): ...
    @property
    def displayName(self): ...
    @property
    def name(self): ...

class DeferredImport:
    '''Defers importing a module until one of the target callable objects is
    called for the first time. Note that there is no way to know if a callable
    object exists in the target module or even if the target module exists until
    import time. All objects that are referenced are assumed to exist until
    proven otherwise when they are called (at which point an ImportError is
    raised).

    Example:

    math = DeferredImport("math")

    # You can pull as many callable objects from `math` as desired, even if they
    # don\'t actually exist in `math`.
    sqrt = math.sqrt
    cos = math.cos
    foo = math.foo # does not exist in the real `math` module

    # The `math` module will only be imported when this next line runs because
    # this is the first invocation of a callable object from `math`.
    cos(0)

    # This will raise an ImportError because `math.foo` doesn\'t really exist.
    foo(0)
    '''
    def __init__(self, moduleName, packageName: Incomplete | None = ...) -> None: ...
    def __getattr__(self, attr):
        """Returns a function which calls the target function of the module and
                passes along any parameters. The module is lazy-imported when a function
                returned by this method is called for the first time.
        """

class DuplicateCommandPlugin(Exception):
    """Exception raised when two command plugins are registered with the same
    name.
    """
    def __init__(self, name) -> None: ...

class PluginContainer:
    """A base class for a container which holds some Usdview plugins. Specific
    containers should inherit from this class and define the 'registerPlugins'
    and 'configureView' methods.
    """
    def configureView(self, plugRegistry, plugUIBuilder):
        """This method is called directly after 'registerPlugins' and can be
                used to add menus which invoke a plugin command using the plugUIBuilder.
        """
    def deferredImport(self, moduleName):
        """Return a DeferredImport object which can be used to lazy load
                functions when they are invoked for the first time.
        """
    def registerPlugins(self, plugRegistry, plugCtx):
        """This method is called after the container is discovered by Usdview,
                and should call 'registerCommandPlugin' one or more times on the
                plugRegistry to add commands to Usdview.
        """

class PluginMenu:
    """Object which adds Usdview command plugins to a QMenu."""
    def __init__(self, qMenu) -> None: ...
    def addItem(self, commandPlugin, shortcut: Incomplete | None = ...):
        """Add a new command plugin to the menu. Optionally, provide a hotkey/
                shortcut.
        """
    def addSeparator(self):
        """Add a separator to the menu."""
    def findOrCreateSubmenu(self, menuName):
        """Get a PluginMenu object for the submenu with the given name. If no
                submenu with the given name exists, it is created.
        """

class PluginRegistry:
    """Manages all plugins loaded by Usdview."""
    def __init__(self, usdviewApi) -> None: ...
    def getCommandPlugin(self, name):
        """Finds and returns a registered command plugin. If no plugin with the
                given name is registered, return None instead.
        """
    def registerCommandPlugin(self, name, displayName, callback, description: str = ...):
        '''Creates, registers, and returns a new command plugin.

                The plugin\'s `name` parameter is used to find the plugin from the
                registry later. It is good practice to prepend the plugin container\'s
                name to the plugin\'s `name` parameter to avoid duplicate names
                (i.e. "MyPluginContainer.myPluginName"). If a duplicate name is found, a
                DuplicateCommandPlugin exception will be raised.

                The `displayName` parameter is the name displayed to users.

                The plugin\'s `callback` parameter must be a callable object which takes
                a UsdviewApi object as its only parameter.

                The optional `description` parameter is a short description of what the
                command does which can be displayed to users.
        '''

class PluginUIBuilder:
    """Used by plugins to construct UI elements in Usdview."""
    def __init__(self, mainWindow) -> None: ...
    def findOrCreateMenu(self, menuName):
        """Get a PluginMenu object for the menu with the given name. If no menu
                with the given name exists, it is created.
        """

def loadPlugins(usdviewApi, mainWindow):
    """Find and load all Usdview plugins."""

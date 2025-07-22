from . import core as core, plugins as plugins

__doc__: str  # type: ignore[no-redef]

class HookScript(plugins.PythonPlugin):  # type: ignore[name-defined]
    _serializable_label: str
    def __init__(self, name=None, filepath=None) -> None:
        """HookScript plugin constructor."""
    def run(self, in_timeline, argument_map={}):
        """Run the hook_function associated with this plugin."""
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

def names():
    """Return a list of all the registered hooks."""
def available_hookscript_names():
    """Return the names of HookScripts that have been registered."""
def available_hookscripts():
    """Return the HookScripts objects that have been registered."""
def scripts_attached_to(hook):
    """Return an editable list of all the hook scripts that are attached to
    the specified hook, in execution order.  Changing this list will change the
    order that scripts run in, and deleting a script will remove it from
    executing
    """
def run(hook, tl, extra_args=None):
    """Run all the scripts associated with hook, passing in tl and extra_args.

    Will return the return value of the last hook script.

    If no hookscripts are defined, returns tl.
    """

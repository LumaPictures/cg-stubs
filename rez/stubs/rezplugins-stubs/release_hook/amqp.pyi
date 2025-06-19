from _typeshed import Incomplete
from rez.release_hook import ReleaseHook

class AmqpReleaseHook(ReleaseHook):
    """
    Publishes a message to the broker.

    The message is a json encoded dictionary of the form -
        {
            package : {
                handle : {},
                name : ...
                version : ...
                user: ... (who released the package)
                qualified_name : ...
                uri : ...
            },
            variants : [
                { handle : {} },
                { handle : {} }
            ]
        }
    """
    schema_dict: Incomplete
    @classmethod
    def name(cls) -> str: ...  # type: ignore[override]
    def __init__(self, source_path) -> None: ...
    def post_release(self, user, install_path, variants, **kwargs) -> None: ...  # type: ignore[override]
    def publish_message(self, data) -> None: ...

def register_plugin(): ...

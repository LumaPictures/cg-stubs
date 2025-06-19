import atexit
from _typeshed import Incomplete
from rez.config import config as config
from rez.utils.logging_ import print_error as print_error
from rez.vendor.pika.adapters.blocking_connection import BlockingConnection as BlockingConnection  # type: ignore[import-not-found]
from rez.vendor.pika.connection import ConnectionParameters as ConnectionParameters  # type: ignore[import-not-found]
from rez.vendor.pika.credentials import PlainCredentials as PlainCredentials  # type: ignore[import-not-found]
from rez.vendor.pika.spec import BasicProperties as BasicProperties  # type: ignore[import-not-found]

_lock: Incomplete
_queue: Incomplete
_thread: Incomplete
_num_pending: int

def publish_message(host, amqp_settings, routing_key, data, block: bool = True):
    """Publish an AMQP message.

    Returns:
        bool: True if message was sent successfully.
    """
def _publish_message(host, amqp_settings, routing_key, data) -> bool:
    """Publish an AMQP message.

    Returns:
        bool: True if message was sent successfully.
    """
def _publish_messages_async() -> None: ...
@atexit.register
def on_exit() -> None: ...
def parse_host_and_port(url): ...
def set_pika_log_level() -> None: ...

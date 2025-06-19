from _typeshed import Incomplete

variant_key_conversions: Incomplete

def convert_old_variant_handle(handle_dict):
    """Convert a variant handle from serialize_version < 4.0."""
def convert_old_command_expansions(command):
    """Convert expansions from !OLD! style to {new}."""

within_unescaped_quotes_regex: Incomplete

def convert_old_commands(commands: list[str], annotate: bool = True) -> str:
    """Converts old-style package commands into equivalent Rex code."""

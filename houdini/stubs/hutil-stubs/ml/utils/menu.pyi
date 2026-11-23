import enum
from collections.abc import Iterable, Sequence

from typing import TypeVar
from typing import TypeVar
_E = TypeVar('_E', bound=enum.Enum)
def named_menu(enum_names: Iterable[enum.Enum]) -> list[str]:
    """
    Given a list of names of an Enum (or a sub-list)
    return menu entries that can be used in a Menu Script of a digital asset
    
    Each token will be lowercase, with the underscored stripped
    Each label will have all underscores replaced by spaces
    """
def enum_name_from_token(enum_names: Iterable[_E], query_token: str) -> _E | None:
    """
    Given a token from a menu formed using the named_menu function,
    find the corresponding enum name
    
    This assumes that no two elements of enum_names map to the same token;
    no two entries of enum_names should be the same after stripping underscores
    and converting to lower case
    """
def indexed_menu(enum_names: Iterable[enum.Enum], override_labels: Sequence[str] = ...) -> list[str]:
    """
    Given a list of names of an Enum (or a sub-list)
    return menu entries that can be used in a Menu Script of a digital asset
    
    Each token will be the index in the 'enum_names' list, as a string
    Each label will have all underscores replaced by spaces

    If override_labels is specified, then the correpsonding entry in the
    override list will be used as the menu label for each entry
    """

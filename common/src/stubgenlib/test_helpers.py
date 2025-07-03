from __future__ import absolute_import, print_function

from typing import TYPE_CHECKING
import typeguard

if TYPE_CHECKING:
    from typing_extensions import assert_type
else:
    def assert_type(val, typ, /):
        return typeguard.check_type(val, typ)

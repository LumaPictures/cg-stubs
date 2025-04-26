from _typeshed import Incomplete
from rez.package_resources import help_schema as help_schema, late_bound as late_bound
from rez.serialise import FileFormat as FileFormat
from rez.utils.formatting import PackageRequest as PackageRequest, as_block_string as as_block_string, dict_to_attributes_code as dict_to_attributes_code, indent as indent
from rez.utils.schema import Required as Required, extensible_schema_dict as extensible_schema_dict
from rez.utils.sourcecode import SourceCode as SourceCode
from rez.utils.yaml import dump_yaml as dump_yaml
from rez.vendor.schema.schema import And as And, Optional as Optional, Or as Or, Schema as Schema, Use as Use  # type: ignore[import-not-found]
from rez.version import Version as Version

package_key_order: Incomplete
version_schema: Incomplete
package_request_schema: Incomplete
source_code_schema: Incomplete
tests_schema: Incomplete
package_serialise_schema: Incomplete

def dump_package_data(data, buf, format_=..., skip_attributes: Incomplete | None = None) -> None:
    """Write package data to `buf`.

    Args:
        data (dict): Data source - must conform to `package_serialise_schema`.
        buf (typing.IO): Destination stream.
        format_ (`FileFormat`): Format to dump data in.
        skip_attributes (list of str): List of attributes to not print.
    """
def _commented_old_command_annotations(sourcecode): ...
def _dump_package_data_yaml(items, buf) -> None: ...
def _dump_package_data_py(items, buf) -> None: ...

dump_functions: Incomplete

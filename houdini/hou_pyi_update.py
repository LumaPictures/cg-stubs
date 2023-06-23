#! /usr/bin/env python
"""
Fill out hou.pyi typing stub based on hou.py docstrings and _hou.so symbol table
"""
from __future__ import absolute_import, division, print_function

import bootstrap_luma

import json
import os
import re
import subprocess
import textwrap
from builtins import filter, next, range
from collections import OrderedDict
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    TypeVar,
)

import attr

import pylib.strings
import setpkglib
from pylib.compat import str

if TYPE_CHECKING:
    from typing import *

T = TypeVar('T')

# FIXME: Update this to use lib2to3/doc484:
#  https://github.com/chadrik/doc484/blob/master/doc484/fixes/fix_type_comments.py

PY2 = False
if PY2:
    HFS = '/luma/soft/applications/SideFx/Linux-x86_64/houdini-19.0.657/'
    HOUPY = HFS + 'houdini/python2.7libs/hou.py'
    HOUSO = HFS + 'houdini/python2.7libs/_hou.so'
else:
    HFS = '/luma/soft/applications/SideFx/Linux-x86_64/houdini-19.5.569/'
    HOUPY = HFS + 'houdini/python3.7libs/hou.py'
    HOUSO = HFS + 'houdini/python3.7libs/_hou.so'
HOUPYI = '/tmp/hou.pyi'
HOUPYI_OUT = os.path.expandvars('$REPO_PATH/houdini/python/hou.pyi')

PYI_RECORD_FMT = (
    "## Created stubs from HFS: %s\n"
    "# standard mypy stub can be created by running:\n"
    "# setpkg houdini\n"
    "# $(dirname $(which mypy))/../bin/stubgen "
    "--no-import $HH/python3.7libs/hou.py -o $REPO_PATH/houdini/python/"
)
PYI_RECORD_ADDED_COMMENT = "  ## Added by typing stub update"
PYI_RECORD_UPDATED_COMMENT = "  ## Updated by typing stub update"
MODULE_LEVEL_IMPORTS = (
    "import datetime",
    "import Qt.QtGui as QtGui",
    "import Qt.QtWidgets as QtWidgets",
    "import pxr.Sdf",
    "import pxr.Usd",
    "from pxr import Usd",
    "from pxr import Sdf",
    "from typing import *",
    # "from typing_extensions import Literal"
)

CLASS_GENERICS = {
    'Error': 'BaseException',
    # 'ParmTuple': 'Tuple[Parm, ...]',
}
CLASS_REDEF_SUPERCLASS_FMT = "%(indent)sclass %(name)s(%(superclass)s):"
CLASS_REDEF_NOSUPERCLASS_FMT = "%(indent)sclass %(name)s:"

ARG_TYPES_FROM_NAME = {
    'name': 'str',
    'file_path': 'str',
    'label': 'str',
    'path': 'str',
    'node': 'Node',
    'parm': 'Parm',
    'parm_tuple': 'ParmTuple',
    'parm_template': 'ParmTemplate',
    'label_or_labels': 'Union[str, Sequence[str]]',
    'name_or_parm_template': 'Union[str, ParmTemplate]',
    'name_or_parm_template_or_indices': 'Union[str, ParmTemplate, Sequence[int]]',
    'label_or_labels_or_parm_template_or_indices': 'Union[str, Sequence[str], ParmTemplate, Sequence[int]]',
    'name_or_attrib': 'Union[str, Attrib]',
    'attrib_or_name': 'Union[str, Attrib]',
    'attrib_value': 'Any',
    'vector2': 'Union[Sequence[float], Vector2]',
    'vector3': 'Union[Sequence[float], Vector3]',
    'vector4': 'Union[Sequence[float], Vector4, Quaternion]',
    'matrix3': 'Matrix3',
    'matrix4': 'Matrix4',
    'quaternion_or_scalar': 'Union[float, Quaternion]',
    'scalar_or quaternion': 'Union[float, Quaternion]',
    'matrix2_or_scalar': 'Union[float, Matrix2]',
    'matrix3_or_scalar': 'Union[float, Matrix3]',
    'matrix4_or_scalar': 'Union[float, Matrix4]',
    'scalar_or_matrix2': 'Union[float, Matrix2]',
    'scalar_or_matrix3': 'Union[float, Matrix3]',
    'scalar_or_matrix4': 'Union[float, Matrix4]',
    'matrix3_or_matrix4': 'Union[Matrix3, Matrix4]',
    'scalar_or_matrix3_or_matrix4': 'Union[float, Matrix3, Matrix4]',
    'output_name_or_index': 'Union[str, int]',
    'point_or_bbox': 'Union[Sequence[float], Vector3, BoundingBox]',
    'point_or_rect': 'Union[Sequence[float], Vector2, BoundingRect]',
    'type_or_name': 'Union[EnumValue, str]',
    'point_or_none': 'Optional[Point]',
    'prim_or_none': 'Optional[Prim]',
    'vertex_or_none': 'Optional[Vertex]',
    'pattern_or_none': 'Optional[str]',
    'point_or_list_or_point_group': 'Union[Vector3, Point, Sequence[Point], PointGroup]',
    'vertex_or_list_or_vertex_group': 'Union[Vertex, Sequence[Vertex], VertexGroup]',
    'edge_or_list_or_edge_group': 'Union[Edge, Sequence[Edge], EdgeGroup]',
    'prim_or_list_or_prim_group': 'Union[Prim, Sequence[Prim], PrimGroup]',
    'position': 'Union[Sequence[float], Vector3]',
    'tuple_of_default_expression_languages': 'Sequence[EnumValue]',
    'tuple_of_default_expressions': 'Sequence[str]',
    'node_or_node_type': 'Union[Node, NodeType]',
    'geometry_types': 'Sequence[EnumValue]',
    'primitive_types': 'Sequence[EnumValue]',
    'PtrOrNull[LopLockedStage]': 'Optional[LopLockedStage]',
    'PtrOrNull': 'Optional',
}

ARG_TYPE_PATCHES = {
    # Omitted namespaces typos in Houdini types
    'RopByRop': 'hou.renderMethod.RopByRop',
    'positionType.WorldSpace': 'hou.positionType.WorldSpace',
    'promptMessageType.Prompt': 'hou.promptMessageType.Prompt',
    'BoundingBox()': 'hou.BoundingBox()',
    # Nested Houdini types which are difficult to parse.
    'ik_Skeleton': '_ik_Skeleton',
    'ik_Target': '_ik_Target',
    'ik_Joint': '_ik_Joint',
    'ik.targetType.Position': 'EnumValue',
    'logging_LogEntry': '_logging_LogEntry',
    # English language conversions
    'true': 'True',
    'false': 'False',
    'integer': 'int',
    'string': 'str',
    'callback': 'Callable',
    'callbacks': 'Callable',
    # Simple C types
    'void': 'None',
    'int64': 'int',
    'double': 'float',
    'byte': 'str',
    'char': 'str',
    'std::map': 'Dict',
    'std::vector': 'Sequence',
    'std::string': 'str',
    'std::pair': 'Tuple',
    'BinaryString': 'str',
    'PyObject': 'Any',
    'obj': 'Any',
    # More complicated C types
    'hboost::any': 'Any',
    'AdvancedDrawable::DrawH': 'Any',
    'AdvancedDrawable::Params': 'Any',
    'ViewerStateTemplate::MenuItemParms': 'Any',
    'Qt.QtWidgets.QWidget subclass': 'QtWidgets.QWidget',
    'swig::SwigPyIterator': 'SwigPyIterator',
    'ptrdiff_t': 'int',
    # Random typos in types
    'bool`': 'bool',
    'dictionary': 'dict',
    'dictionarie': 'dict',
    'hou.NodeBundle': 'Bundle',
    'NodeBundle': 'Bundle',
    'FlipbookSetting': 'FlipbookSettings',
    'HDAOption': 'HDAOptions',
    'LopViewportLoadMask': 'LopViewportLoadMasks',
    'LopViewportOverride': 'LopViewportOverrides',
    'GeometryViewportBGImage': 'GeometryViewportBackground',
    '`hou.Matrix4': 'Matrix4',
    '`Matrix4`': 'Matrix4',
    'Color`': 'Color',
    # Explicit conversions for complex descriptions (possibly including typos).
    'dictionary of (, tuple of hou.BaseKeyframe) pairs': 'Dict[Parm, Tuple[BaseKeyFrame, ...]]',
    'dict of (str, int) to str': 'Dict[Tuple[str, int], str]',
    'dict of str to bool, int, float, str': 'Dict[str, Union[bool, int, float, str]]',
    'dict od str to str': 'Dict[str, str]',
    'dict of str to any python object': 'Dict[str, Any]',
    'dict of str to any python object`': 'Dict[str, Any]',
    'dict mapping names to path': 'Dict[str, str]',
    'any python obect or None': 'Optional[Any]',
    'any python object or None': 'Optional[Any]',
    '(int, tuple of str)': 'Tuple[int, Tuple[str, ...]]',
    '(origin_point, direction)': 'Tuple[Vector3, Vector3]',
    '(tuple of hou.RopNode, tuple of tuples of float)': 'Tuple[Tuple[RopNode, Tuple[float, ...]], ...]',
    'tuple of houNode and str': 'Tuple[Node, str]',
    'tuple of double': 'Tuple[float, ...]',
    'tuple of dict of str to str': 'Tuple[Dict[str, str], ...]',
    '(bool, tuple of Parm and string tuples)': 'Tuple[bool, Tuple[Tuple[Parm, str], ...]',
    'hou.ObjNode, hou.SopNode, or None': 'Optional[Union[ObjNode, SopNode]]',
    'tuple of int, float, or str, or hou.Ramp': 'Union[Tuple[int, ...], Tuple[float, ...], Tuple[str, ...], Ramp]',
    'tuple of int, float, str, or hou.Ramp': 'Union[Tuple[int, ...], Tuple[float, ...], Tuple[str, ...], Ramp]',
    'tuple of int, float, or str': 'Union[Tuple[int, ...], Tuple[float, ...], Tuple[str, ...]]',
    'bool, int, float, str, hou.Vector2, hou.Vector3, hou.Vector4, hou.Quaternion, hou.Matrix3, hou.Matrix4, tuple of int, or tuple of float': 'Union[bool, int, float, str, Vector2, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]',
    'int, float, str or tuple': 'Union[int, float, str, Tuple[int, ...], Tuple[float, ...], Tuple[str, ...]]',
    'str for Python 2, bytes for Python 3': 'str',
}


DEFAULT_VALUE_PATCHES = {
    # Nested Houdini types which are difficult to parse.
    'ik.targetType.Position': '_ik_targetType.Position',
}

# Some docstrings don't report their return types accurately.
# If all we need to change is the return type, and not specify
# new arguments, we can set those here.
RETURN_TYPE_PATCHES = {
    'Node.creator': 'Node',
    'Node.inputIndex': 'int',
    'Node.outputIndex': 'int',
    'Node.isHidden': 'bool',
    'ChopNode.sampleRange': 'Tuple[float, float]',
    'Clip.sampleRange': 'Tuple[float, float]',
    'crowds.computeRotationLimits': 'Dict[str, Union[int, EnumValue, List[AgentClip], Vector2, Vector3]]',
    'SopVerb.parms': 'Dict[str, Any]',
    'Geometry.countPrimType': 'int',
    'Geometry.modificationCounter': 'int',
    'GeometryViewport.resolutionInPixels': 'Tuple[int, int]',
    'GeometryViewportCamera.translation': 'Tuple[float, float, float]',
    'Parm.evalAsJSONMapAtFrame': 'Dict[str, str]',
    'hscriptExpression': 'Union[float, str, Tuple[float, ...], Tuple[str, ...]]',
    'Ramp.basis': 'Tuple[EnumValue, ...]',
    'Ramp.colorType': 'EnumValue',
    'WebServer.files': 'Dict[str, Any]',
    'WebServerRequest.files': 'Dict[str, Any]',
    'ViewerDragger.drag': 'Dict[str, Union[Vector3, Matrix3]]',
    'DataParmTemplate.defaultExpressionLanguage': 'Tuple[EnumValue, ...]',
    'FloatParmTemplate.defaultExpressionLanguage': 'Tuple[EnumValue, ...]',
    'IntParmTemplate.defaultExpressionLanguage': 'Tuple[EnumValue, ...]',
    'MenuParmTemplate.defaultExpressionLanguage': 'EnumValue',
    'RampParmTemplate.defaultExpressionLanguage': 'Tuple[EnumValue, ...]',
    'StringParmTemplate.defaultExpressionLanguage': 'Tuple[EnumValue, ...]',
    'ToggleParmTemplate.defaultExpressionLanguage': 'Tuple[EnumValue, ...]',
    'ui.displayFileDependencyDialog': 'Tuple[bool, Tuple[Tuple[Parm, str], ...]]',
    'qt._floatingPanelWindow': 'QtWidgets.QWidget',
}

ADDITIONAL_ENUM_VALUES = {
    'fbxMaterialMode': [
        'FBXShaderNodes',
        'PrincipledShaders',
        'VopNetworks',
    ],
    'fbxCompatibilityMode': [
        'FBXStandard',
        'Maya',
    ],
    '_ik_targetType': [
        'All',
        'Orientation',
        'Position',
    ],
    'parmTemplateType': [
        'Folder',
        'Data',
    ],
    'optionalBool': [
        'Yes',
        'No',
        'NoOpinion',
    ],
}

ITERABLE_TYPES_BY_CHAR = {
    '(': 'Tuple',
    '[': 'List',
}

ILLEGAL_ARG_NAMES = [
    'global',
]

# Some functions should not be written to the stub at all, and simply inherit from object.
SKIP_FUNCS = (
    '*.__ne__',
    '*.__eq__',
)

# Some docstrings are wildly incorrect and aligning the type hints to named
# docstring arguments is impossible to rectify automatically and too much
# work to patch manually.
FUNCTIONS_SKIP_TYPE_HINTS = (
    'ButtonParmTemplate.__init__',
    'DataParmTemplate.__init__',
    'FloatParmTemplate.__init__',
    'FolderParmTemplate.__init__',
    'FolderSetParmTemplate.__init__',
    'IntParmTemplate.__init__',
    'LabelParmTemplate.__init__',
    'MenuParmTemplate.__init__',
    'RampParmTemplate.__init__',
    'SeparatorParmTemplate.__init__',
    'StringParmTemplate.__init__',
    'ToggleParmTemplate.__init__',
    # 'Geometry.addAttrib',
    'Prim.setAttribValue',
)

NO_DEFAULT = "NO_DEFAULT"
SKIP_LINE_WRITE = "SKIP_LINE_WRITE"

reClass = re.compile(
    r'(?P<indentsize>[ \t]*)class (?P<name>[_\w]+)(?::|\((?P<superclass>[_\w\[\], ]+)\))?'
)
reClassNoSuperClass = re.compile(r'(?P<indentsize>[ \t]*)class (?P<name>[_\w]+):')
reFakeNamespaceClassName = re.compile(r'(?P<name>[a-z]\w+)')
reTopLevelFunc = re.compile(r'(?P<name>[a-z][a-zA-Z]+): Any$')
reFunction = re.compile(
    r'(?P<indentsize>[ \t]*)def (?P<name>[_a-zA-Z]\w*)\((?P<args>.*)\):\W*$'
)
reFunctionReturn = re.compile(
    r'(?P<indentsize>[ \t]*)def (?P<name>[_a-zA-Z]\w*)\((?P<args>.*)\)( -> (?P<returnType>.+)):'
)
reFunctionArgs = re.compile(
    r'(?:USAGE)?(?P<indentsize>[ \t]*)(?P<name>[_a-zA-Z]\w*)\((?P<args>.*)\)'
)
reFunctionReturnArgs = re.compile(
    r'(?:USAGE)?(?P<indentsize>[ \t]*)(?P<name>[_a-zA-Z]\w*)\((?P<args>.*)\)( -> (?P<returnType>.+))'
)
reClassMember = re.compile(r'(?P<indentsize>[ \t]*)(?P<name>[a-z_][a-zA-Z0-9_]+):.*')
reIndents = re.compile(r'(?P<indentsize>[ \t]*)[\w_]')
reEmptyLine = re.compile(r'(?P<indentsize>[ \t]*)$')
reBlockComment = re.compile(r'(?P<indentsize>[ \t]+)r?"""')
reCommentBlockSections = re.compile(r'\n\n+')
reClassCall = re.compile(r'(?P<name>[A-Z]\w*)\((?P<args>.*)\)')
reFuncCall = re.compile(r'(?P<name>[a-z]\w*)\((?P<args>.*)\)')

reOrSplit = re.compile(r'(?<!,) or ')
reCommaSeparatedList = re.compile(r',(?: or)?')
reTupleOrListArg = re.compile(
    r'(?P<char>[(\[])(?P<arg>[[$.\w*"' + r"'" + r']+)[,;]?.*[)\]]'
)
reTupleSimple = re.compile(r'\(.*?\)')
reTupleWithWordSimplePrefix = re.compile(r'tuple +of +')
reTupleWithNumber = re.compile(r'tuple +of +(?P<count>[\d+]) +(?P<type>.*)')
reTupleWithNumberPrefix = re.compile(r'(?P<count>[\d+])-tuple +of +(?P<type>.*)')
reTupleWithTwoTypes = re.compile(
    r'tuple +of +(?P<type1>.*) +and +(?P<type2>.*) +tuples'
)
reTupleTypeExtraction = re.compile(r'(?P<prefix>.*\[)(?P<type>.*)')
reListSimple = re.compile(r'\[.*?\]')
reListType = re.compile(r'list +of +(?P<type>.+)')
reSingleQuoted = re.compile(r"'.*?'")
reDoubleQuoted = re.compile(r'".*?"')
reGeneratorType = re.compile(r'generator +of +(?P<type>.+)')
reDictType = re.compile(r'dict +of +(?P<fromtype>.+) +to +(?P<totype>.+)')
reOrNone = re.compile(r'(?P<type>[\w.]+) [oO]r [nN]one')
rePxrType = re.compile(r'(?P<enumname>pxr\.\w+(?:.\w+)?)')
reEnumValueType = re.compile(r'(?P<enumname>[a-z]\w*\.[a-z]\w*(?:.[A-Z]\w*)?)')
reEnumValues = re.compile(r'enum values?')
reEndsWithTuples = re.compile(r'(?P<prefix>.*) tuples?$')
reStartsWithTupleOfAndParenthesis = re.compile(r'^tuple of \(')
reHOMArgumentFormat = re.compile(r'\[Hom:(?:hou\.)?(?P<type>.*?)\]')
reHOUArgumentFormat = re.compile(r'hou\.(?P<type>.*?)')
reExtraSpaces = re.compile(r' +')
reLowercasePluralWord = re.compile(r'^[a-z]\w*s$')

reHouSOArgument = re.compile(
    r"in method '(?P<name>.*?)', argument (?P<num>\d+) of type '(?P<type>.*?)'"
)
reHouSOHOM = re.compile(r"HOM_")
reHouSOConst = re.compile(r" const")
reHouSOTail = re.compile(r" [*&]")
reHouSOType = re.compile(r'::[a-z]+_type')
reHouSOToken = re.compile(r"(?P<token>[\w:_]+)")
reHouSOSpaces = re.compile(' +')
reHouSOColonTail = re.compile(': *(?P<char>[,}])')
reHouSOQuoteTail = re.compile('" *(?P<char>[,}])')
reHouSOEndChar = re.compile(r', (?P<char>[\]$])')


@attr.s
class Arg(object):
    name = attr.ib(type=str, converter=str)
    type = attr.ib(type=str, converter=str)
    default = attr.ib(type=str, converter=str)


@attr.s
class HouFunc(object):
    name = attr.ib(type=str)
    comment = attr.ib(type=str, repr=False)
    args = attr.ib(type=List[Arg])
    returnType = attr.ib(type=str)
    className = attr.ib(type=Optional[str], default=None)

    argsByName = attr.ib(type=Dict[str, Arg], repr=False)
    argsByIndex = attr.ib(type=Dict[int, Arg], repr=False)
    written = attr.ib(type=bool, default=False)
    namespacedName = attr.ib(type=str)

    @argsByName.default
    def getArgsByName(self):
        # type: () -> Dict[str, Arg]
        return {arg.name: arg for arg in self.args}

    @argsByIndex.default
    def getArgsByIndex(self):
        # type: () -> Dict[int, Arg]
        # Note that these indices start at 1 to match the strings output.
        return {index: arg for index, arg in enumerate(self.args, start=1)}

    @namespacedName.default
    def getNamespacedName(self):
        # type: () -> str
        if self.className:
            return "%s.%s" % (self.className, self.name)
        return self.name

    def formatArguments(self):
        # type: () -> str
        """
        Format the arguments for a function definition.

        Returns
        -------
        str
        """
        if self.name == '__init__':
            if not self.args:
                self.args.append(Arg('self', self.className, NO_DEFAULT))
                self.argsByIndex = self.getArgsByIndex()
            self.returnType = 'None'

        args = []
        for i, arg in self.argsByIndex.items():
            # In case we have some lame trailing typing from the previous
            # argument, throw it away and just keep the name.
            name = arg.name.split(" ")[-1]
            if i == 1 and self.className is not None:
                if reFakeNamespaceClassName.match(self.className):
                    # Do not add the class argument for fake namespace classes.
                    continue
                elif not name:
                    name = 'self'
            elif not name:
                name = 'arg%d' % i

            data = {"name": name, "type": arg.type, "default": arg.default}
            if arg.type and arg.type != 'Any':
                if arg.default != NO_DEFAULT:
                    args.append('%(name)s: %(type)s=%(default)s' % data)
                else:
                    args.append('%(name)s: %(type)s' % data)
            else:
                # No typing information.
                if arg.default != NO_DEFAULT:
                    args.append('%(name)s=%(default)s' % data)
                else:
                    args.append('%(name)s' % data)
        return ', '.join(args)

    def formatLine(self, indent, addReceipt=False, overloaded=False):
        # type: (int, bool, bool) -> str
        """
        Format the line as it will appear in the typing stub.

        Parameters
        ----------
        indent : int
        addReceipt : bool
        overloaded : bool

        Returns
        -------
        str
        """
        if self.returnType:
            fmt = "%(indent)sdef %(name)s(%(args)s) -> %(type)s: ...%(receipt)s\n"
        else:
            fmt = "%(indent)sdef %(name)s(%(args)s): ...%(receipt)s\n"
        data = {
            "indent": ' ' * indent,
            "name": self.name,
            "args": self.formatArguments(),
            "type": self.returnType,
            "receipt": PYI_RECORD_ADDED_COMMENT if addReceipt else '',
        }
        self.written = True
        line = fmt % data

        if overloaded:
            line = ' ' * indent + '@overload\n' + line

        if self.className and reFakeNamespaceClassName.match(self.className):
            line = ' ' * indent + '@staticmethod\n' + line

        return line


# A dictionary of {className : {funcName: docstring}}
# We use this to patch in docstrings for functions which do not
# appear in hou.py, but should and are in wide use.
MISSING_FUNCTION_DEFINITIONS = {
    None: {
        'applicationVersion': HouFunc(
            name='applicationVersion',
            comment='Redefining the function to take no arguments.',
            args=[],
            returnType='Tuple[int, int, int]',
            className=None,
        ),
        'expandString': HouFunc(
            name='expandString',
            comment='Backwards compatibility.',
            args=[
                Arg(name='text', type='str', default='NO_DEFAULT'),
            ],
            returnType='str',
            className=None,
        ),
        'expandStringAtFrame': HouFunc(
            name='expandStringAtFrame',
            comment='Backwards compatibility.',
            args=[
                Arg(name='text', type='str', default='NO_DEFAULT'),
                Arg(name='frame_number', type='float', default='NO_DEFAULT'),
            ],
            returnType='str',
            className=None,
        ),
        'runVex': HouFunc(
            name='runVex',
            comment='Redefine.',
            args=[
                Arg(name='vex_file', type='str', default='NO_DEFAULT'),
                Arg(name='inputs', type='Dict[str, Any]', default='NO_DEFAULT'),
                Arg(name='precision', type='Literal["32", "64"]', default='"32"'),
            ],
            returnType='Dict[str, Any]',
            className=None,
        ),
        'startHoudiniEngineDebugger': HouFunc(
            name='startHoudiniEngineDebugger',
            comment='Redefine.',
            args=[
                Arg(
                    name='portOrPipeName', type='Union[int, str]', default='NO_DEFAULT'
                ),
            ],
            returnType='None',
            className=None,
        ),
    },
    'NetworkItem': {
        '__lt__': HouFunc(
            name='__lt__',
            comment='Missing',
            args=[
                Arg(name='self', type='NetworkItem', default='NO_DEFAULT'),
                Arg(name='other', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='NetworkItem',
        ),
        '__le__': HouFunc(
            name='__le__',
            comment='Missing',
            args=[
                Arg(name='self', type='NetworkItem', default='NO_DEFAULT'),
                Arg(name='other', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='NetworkItem',
        ),
        '__gt__': HouFunc(
            name='__gt__',
            comment='Missing',
            args=[
                Arg(name='self', type='NetworkItem', default='NO_DEFAULT'),
                Arg(name='other', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='NetworkItem',
        ),
        '__ge__': HouFunc(
            name='__ge__',
            comment='Missing',
            args=[
                Arg(name='self', type='NetworkItem', default='NO_DEFAULT'),
                Arg(name='other', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='NetworkItem',
        ),
        '__eq__': HouFunc(
            name='__eq__',
            comment='Missing',
            args=[
                Arg(name='self', type='NetworkItem', default='NO_DEFAULT'),
                Arg(name='other', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='NetworkItem',
        ),
        '__ne__': HouFunc(
            name='__ne__',
            comment='Missing',
            args=[
                Arg(name='self', type='NetworkItem', default='NO_DEFAULT'),
                Arg(name='other', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='NetworkItem',
        ),
    },
    'NetworkMovableItem': {
        'shiftPosition': HouFunc(
            name='shiftPosition',
            comment='Redefine',
            args=[
                Arg(name='self', type='NetworkMovableItem', default='NO_DEFAULT'),
                Arg(
                    name='vector2',
                    type='Union[Sequence[float], Vector2]',
                    default='NO_DEFAULT',
                ),
            ],
            returnType='None',
            className='NetworkMovableItem',
        ),
    },
    'Node': {
        'simulation': HouFunc(
            name='simulation',
            comment='Elevating the DopNode.simulation() definition, '
            'since Node.simulation() exists, but has no '
            'information, which causes typing errors.',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
            ],
            returnType='DopSimulation',
            className='Node',
        ),
        'setInput': HouFunc(
            name='setInput',
            comment='Redefine',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
                Arg(name='input_index', type='int', default='NO_DEFAULT'),
                Arg(
                    name='item_to_become_input',
                    type='Optional[NetworkMovableItem]',
                    default='NO_DEFAULT',
                ),
                Arg(name='output_index', type='int', default='0'),
            ],
            returnType='None',
            className='Node',
        ),
        'setFirstInput': HouFunc(
            name='setFirstInput',
            comment='Redefine',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
                Arg(
                    name='item_to_become_input',
                    type='Optional[NetworkMovableItem]',
                    default='NO_DEFAULT',
                ),
                Arg(name='output_index', type='int', default='0'),
            ],
            returnType='None',
            className='Node',
        ),
        'setParms': HouFunc(
            name='setParms',
            comment='Missing',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
                Arg(name='parm_dict', type='Dict[str, Any]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='Node',
        ),
        'setParmExpressions': HouFunc(
            name='setParmExpressions',
            comment='Missing',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
                Arg(name='parm_dict', type='Dict[str, Any]', default='NO_DEFAULT'),
                Arg(name='language', type='Optional[EnumValue]', default='None'),
                Arg(name='replace_expressions', type='bool', default='True'),
            ],
            returnType='None',
            className='Node',
        ),
        'parmTemplateGroup': HouFunc(
            name='parmTemplateGroup',
            comment='Missing',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
            ],
            returnType='ParmTemplateGroup',
            className='Node',
        ),
        'addSpareParmTuple': HouFunc(
            name='addSpareParmTuple',
            comment='Missing',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
                Arg(name='parm_template', type='ParmTemplate', default='NO_DEFAULT'),
                Arg(name='in_folder', type='Tuple[str, ...]', default='()'),
                Arg(name='create_missing_folders', type='bool', default='False'),
            ],
            returnType='ParmTuple',
            className='Node',
        ),
        'layoutChildren': HouFunc(
            name='layoutChildren',
            comment='Redefine',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
                Arg(name='items', type='Sequence[NetworkMovableItem]', default='()'),
                Arg(name='horizontal_spacing', type='float', default='1.0'),
                Arg(name='vertical_spacing', type='float', default='1.0'),
            ],
            returnType='None',
            className='Node',
        ),
        'createOutputNode': HouFunc(
            name='createOutputNode',
            comment='Missing',
            args=[
                Arg(name='self', type='T', default='NO_DEFAULT'),
                Arg(name='node_type_name', type='str', default='NO_DEFAULT'),
                Arg(name='node_name', type='Optional[str]', default='None'),
                Arg(name='run_init_scripts', type='bool', default='True'),
                Arg(name='load_contents', type='bool', default='True'),
                Arg(name='exact_type_name', type='bool', default='False'),
            ],
            returnType='T',
            className='Node',
        ),
        'createInputNode': HouFunc(
            name='createInputNode',
            comment='Missing',
            args=[
                Arg(name='self', type='T', default='NO_DEFAULT'),
                Arg(name='input_index', type='int', default='NO_DEFAULT'),
                Arg(name='node_type_name', type='str', default='NO_DEFAULT'),
                Arg(name='node_name', type='Optional[str]', default='None'),
                Arg(name='run_init_scripts', type='bool', default='True'),
                Arg(name='load_contents', type='bool', default='True'),
                Arg(name='exact_type_name', type='bool', default='False'),
            ],
            returnType='T',
            className='Node',
        ),
        'creationTime': HouFunc(
            name='creationTime',
            comment='Missing',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
            ],
            returnType='datetime.datetime',
            className='Node',
        ),
        'modificationTime': HouFunc(
            name='modificationTime',
            comment='Missing',
            args=[
                Arg(name='self', type='Node', default='NO_DEFAULT'),
            ],
            returnType='datetime.datetime',
            className='Node',
        ),
        'inputs': HouFunc(
            name='inputs',
            comment='Redefine for type var',
            args=[
                Arg(name='self', type='T', default='NO_DEFAULT'),
            ],
            returnType='Tuple[T, ...]',
            className='Node',
        ),
        'input': HouFunc(
            name='input',
            comment='Redefine for type var',
            args=[
                Arg(name='self', type='T', default='NO_DEFAULT'),
                Arg(name='inputidx', type='int', default='NO_DEFAULT'),
            ],
            returnType='T',
            className='Node',
        ),
        'outputs': HouFunc(
            name='outputs',
            comment='Redefine for type var',
            args=[
                Arg(name='self', type='T', default='NO_DEFAULT'),
            ],
            returnType='Tuple[T, ...]',
            className='Node',
        ),
    },
    'LopNode': {
        'displayNode': HouFunc(
            name='displayNode',
            comment='LopNode display nodes are LOPs.',
            args=[
                Arg(name='self', type='LopNode', default='NO_DEFAULT'),
            ],
            returnType='LopNode',
            className='LopNode',
        ),
        'setLastModifiedPrims': HouFunc(
            name='setLastModifiedPrims',
            comment='Redefine',
            args=[
                Arg(name='self', type='LopNode', default='NO_DEFAULT'),
                Arg(name='primPaths', type='Sequence[str]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='LopNode',
        ),
    },
    'Geometry': {
        'addAttrib': HouFunc(
            name='addAttrib',
            comment='Redefine',
            args=[
                Arg(name='self', type='Geometry', default='NO_DEFAULT'),
                Arg(name='type', type='EnumValue', default='NO_DEFAULT'),
                Arg(name='name', type='str', default='NO_DEFAULT'),
                Arg(name='default_value', type='Any', default='NO_DEFAULT'),
                Arg(name='transform_as_normal', type='bool', default='True'),
                Arg(name='create_local_variable', type='bool', default='True'),
            ],
            returnType='Attrib',
            className='Geometry',
        ),
        'setGlobalAttribValue': HouFunc(
            name='setGlobalAttribValue',
            comment='Redefine',
            args=[
                Arg(name='self', type='Geometry', default='NO_DEFAULT'),
                Arg(
                    name='name_or_attrib',
                    type='Union[str, Attrib]',
                    default='NO_DEFAULT',
                ),
                Arg(name='attrib_value', type='Any', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='Geometry',
        ),
    },
    'StickyNote': {
        'setSize': HouFunc(
            name='setSize',
            comment='Redefine',
            args=[
                Arg(name='self', type='StickyNote', default='NO_DEFAULT'),
                Arg(
                    name='size',
                    type='Union[Sequence[float], Vector2]',
                    default='NO_DEFAULT',
                ),
            ],
            returnType='None',
            className='StickyNote',
        ),
    },
    'Parm': {
        'set': HouFunc(
            name='set',
            comment='Missing!',
            args=[
                Arg(name='self', type='Parm', default='NO_DEFAULT'),
                Arg(
                    name='value',
                    type='Union[int, float, str, Parm, Ramp]',
                    default='NO_DEFAULT',
                ),
                Arg(name='language', type='Optional[EnumValue]', default='None'),
                Arg(name='follow_parm_reference', type='bool', default='True'),
            ],
            returnType='None',
            className='Parm',
        ),
    },
    'ParmTuple': {
        '__iter__': HouFunc(
            name='__iter__',
            comment='Missing!',
            args=[
                Arg(name='self', type='ParmTuple', default='NO_DEFAULT'),
            ],
            returnType='Iterator[Parm]',
            className='ParmTuple',
        ),
        'set': HouFunc(
            name='set',
            comment='Missing!',
            args=[
                Arg(name='self', type='ParmTuple', default='NO_DEFAULT'),
                Arg(
                    name='value',
                    type='Union[Iterable[int], Iterable[float], Iterable[str], Iterable[Parm], ParmTuple]',
                    default='NO_DEFAULT',
                ),
                Arg(name='language', type='Optional[EnumValue]', default='None'),
                Arg(name='follow_parm_reference', type='bool', default='True'),
            ],
            returnType='None',
            className='ParmTuple',
        ),
    },
    'ParmTemplate': {
        'conditionals': HouFunc(
            name='conditionals',
            comment='Redefine',
            args=[
                Arg(name='self', type='ParmTemplate', default='NO_DEFAULT'),
            ],
            returnType='Dict[EnumValue, str]',
            className='ParmTemplate',
        ),
        'setTags': HouFunc(
            name='setTags',
            comment='Redefine',
            args=[
                Arg(name='self', type='ParmTemplate', default='NO_DEFAULT'),
                Arg(name='tags', type='Dict[str, str]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='ParmTemplate',
        ),
    },
    'DataParmTemplate': {
        '__init__': HouFunc(
            name='__init__',
            comment='Init takes more arguments than is described in the '
            'docstring and is difficult to divine.  We redefine here to '
            'forcibly add them in the location we believe them to exist.',
            args=[
                Arg(name='self', type='DataParmTemplate', default='NO_DEFAULT'),
                Arg(name='name', type='', default='NO_DEFAULT'),
                Arg(name='label', type='', default='NO_DEFAULT'),
                Arg(name='num_components', type='int', default='NO_DEFAULT'),
                Arg(name='look', type='EnumValue', default='parmLook.Regular'),
                Arg(
                    name='naming_scheme',
                    type='EnumValue',
                    default='parmNamingScheme.XYZW',
                ),
                Arg(name='unknown_str', type='Optional[str]', default='None'),
                Arg(name='disable_when', type='Optional[str]', default='None'),
                Arg(name='is_hidden', type='bool', default='False'),
                Arg(name='is_label_hidden', type='bool', default='False'),
                Arg(name='join_with_next', type='bool', default='False'),
                Arg(name='help', type='Optional[str]', default='None'),
                Arg(name='script_callback', type='Optional[str]', default='None'),
                Arg(
                    name='script_callback_language',
                    type='EnumValue',
                    default='scriptLanguage.Hscript',
                ),
                Arg(name='tags', type='Dict[str, str]', default='{}'),
                Arg(name='unknown_dict', type='Dict[EnumValue, str]', default='{}'),
                Arg(name='default_expression', type='Sequence[str]', default='()'),
                Arg(
                    name='default_expression_language',
                    type='Sequence[EnumValue]',
                    default='()',
                ),
            ],
            returnType='DataParmTemplate',
            className='DataParmTemplate',
        ),
    },
    'FolderSetParmTemplate': {
        'folderNames': HouFunc(
            name='folderNames',
            comment='Redefine',
            args=[
                Arg(name='self', type='FolderSetParmTemplate', default='NO_DEFAULT'),
            ],
            returnType='List[str]',
            className='FolderSetParmTemplate',
        ),
        'setFolderNames': HouFunc(
            name='setFolderNames',
            comment='Redefine',
            args=[
                Arg(name='self', type='FolderSetParmTemplate', default='NO_DEFAULT'),
                Arg(name='folder_names', type='Sequence[str]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='FolderSetParmTemplate',
        ),
    },
    'MenuParmTemplate': {
        'setDefaultExpressionLanguage': HouFunc(
            name='setDefaultExpressionLanguage',
            comment='Redefine',
            args=[
                Arg(name='self', type='MenuParmTemplate', default='NO_DEFAULT'),
                Arg(
                    name='default_expression_language',
                    type='EnumValue',
                    default='NO_DEFAULT',
                ),
            ],
            returnType='None',
            className='MenuParmTemplate',
        ),
    },
    'Vector2': {
        '__iter__': HouFunc(
            name='__iter__',
            comment='Missing!',
            args=[
                Arg(name='self', type='Vector2', default='NO_DEFAULT'),
            ],
            returnType='Iterator[float]',
            className='Vector2',
        ),
    },
    'Vector3': {
        '__iter__': HouFunc(
            name='__iter__',
            comment='Missing!',
            args=[
                Arg(name='self', type='Vector3', default='NO_DEFAULT'),
            ],
            returnType='Iterator[float]',
            className='Vector3',
        ),
    },
    'Vector4': {
        '__iter__': HouFunc(
            name='__iter__',
            comment='Missing!',
            args=[
                Arg(name='self', type='Vector4', default='NO_DEFAULT'),
            ],
            returnType='Iterator[float]',
            className='Vector4',
        ),
    },
    'Matrix2': {
        '__init__': HouFunc(
            name='__init__',
            comment='Init takes more types than we can derive automatically',
            args=[
                Arg(name='self', type='Matrix2', default='NO_DEFAULT'),
                Arg(
                    name='values',
                    type='Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]]',
                    default='0',
                ),
            ],
            returnType='Matrix2',
            className='Matrix2',
        ),
    },
    'Matrix3': {
        '__init__': HouFunc(
            name='__init__',
            comment='Init takes more types than we can derive automatically',
            args=[
                Arg(name='self', type='Matrix3', default='NO_DEFAULT'),
                Arg(
                    name='values',
                    type='Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]]',
                    default='0',
                ),
            ],
            returnType='Matrix3',
            className='Matrix3',
        ),
    },
    'Matrix4': {
        '__init__': HouFunc(
            name='__init__',
            comment='Init takes more types than we can derive automatically',
            args=[
                Arg(name='self', type='Matrix4', default='NO_DEFAULT'),
                Arg(
                    name='values',
                    type='Union[int, float, Sequence[Union[int, float]], Sequence[Sequence[Union[int, float]]]]',
                    default='0',
                ),
            ],
            returnType='Matrix4',
            className='Matrix4',
        ),
    },
    'Take': {
        'name': HouFunc(
            name='name',
            comment='Missing!',
            args=[
                Arg(name='self', type='Take', default='NO_DEFAULT'),
            ],
            returnType='str',
            className='Take',
        ),
    },
    'Prim': {
        'setIntrinsicValue': HouFunc(
            name='setIntrinsicValue',
            comment='Redefining the last argument to take additional types.',
            args=[
                Arg(name='self', type='Prim', default='NO_DEFAULT'),
                Arg(name='intrinsic_name', type='str', default='NO_DEFAULT'),
                Arg(
                    name='value',
                    type='Union[int, float, str, Iterable[int], Iterable[float], Iterable[str]]',
                    default='NO_DEFAULT',
                ),
            ],
            returnType='None',
            className='Prim',
        ),
    },
    'VDB': {
        'voxelRange': HouFunc(
            name='voxelRange',
            comment='Redefining to return additional types.',
            args=[
                Arg(name='self', type='Prim', default='NO_DEFAULT'),
                Arg(name='range', type='BoundingBox', default='NO_DEFAULT'),
            ],
            returnType='Union[Tuple[bool, ...], Tuple[int, ...], Tuple[float, ...], Tuple[Vector3, ...]]',
            className='Prim',
        ),
        'voxelRangeAsBool': HouFunc(
            name='voxelRangeAsBool',
            comment='Missing.',
            args=[
                Arg(name='self', type='Prim', default='NO_DEFAULT'),
                Arg(name='range', type='BoundingBox', default='NO_DEFAULT'),
            ],
            returnType='Tuple[bool, ...]',
            className='Prim',
        ),
        'voxelRangeAsInt': HouFunc(
            name='voxelRangeAsInt',
            comment='Missing.',
            args=[
                Arg(name='self', type='Prim', default='NO_DEFAULT'),
                Arg(name='range', type='BoundingBox', default='NO_DEFAULT'),
            ],
            returnType='Tuple[int, ...]',
            className='Prim',
        ),
        'voxelRangeAsFloat': HouFunc(
            name='voxelRangeAsFloat',
            comment='Missing.',
            args=[
                Arg(name='self', type='Prim', default='NO_DEFAULT'),
                Arg(name='range', type='BoundingBox', default='NO_DEFAULT'),
            ],
            returnType='Tuple[float, ...]',
            className='Prim',
        ),
        'voxelRangeAsVector3': HouFunc(
            name='voxelRangeAsVector3',
            comment='Missing.',
            args=[
                Arg(name='self', type='Prim', default='NO_DEFAULT'),
                Arg(name='range', type='BoundingBox', default='NO_DEFAULT'),
            ],
            returnType='Tuple[Vector3, ...]',
            className='Prim',
        ),
    },
    'Keyframe': {
        '__init__': HouFunc(
            name='__init__',
            comment='Redefine',
            args=[
                Arg(name='self', type='Keyframe', default='NO_DEFAULT'),
                Arg(name='value', type='Optional[float]', default='None'),
                Arg(name='time', type='Optional[float]', default='None'),
            ],
            returnType='None',
            className='Keyframe',
        ),
    },
    'StringKeyframe': {
        '__init__': HouFunc(
            name='__init__',
            comment='Redefine',
            args=[
                Arg(name='self', type='StringKeyframe', default='NO_DEFAULT'),
                Arg(name='expression', type='Optional[str]', default='None'),
                Arg(name='time', type='Optional[float]', default='None'),
                Arg(
                    name='language',
                    type='Optional[EnumValue]',
                    default='exprLanguage.Python',
                ),
            ],
            returnType='None',
            className='Keyframe',
        ),
    },
    'SceneViewer': {
        'groupListMask': HouFunc(
            name='groupListMask',
            comment='Redefine',
            args=[
                Arg(name='self', type='SceneViewer', default='NO_DEFAULT'),
            ],
            returnType='str',
            className='SceneViewer',
        ),
        'isGroupPicking': HouFunc(
            name='isGroupPicking',
            comment='Redefine',
            args=[
                Arg(name='self', type='SceneViewer', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='SceneViewer',
        ),
        'selectGeometry': HouFunc(
            name='selectGeometry',
            comment='Redefine for more permissive typing on *_types arguments',
            args=[
                Arg(name='self', type='SceneViewer', default='NO_DEFAULT'),
                Arg(name='prompt', type='str', default='"Select geometry"'),
                Arg(name='sel_index', type='int', default='0'),
                Arg(name='allow_drag', type='bool', default='False'),
                Arg(name='quick_select', type='bool', default='False'),
                Arg(name='use_existing_selection', type='bool', default='True'),
                Arg(name='initial_selection', type='Optional[str]', default='None'),
                Arg(
                    name='initial_selection_type',
                    type='Optional[EnumValue]',
                    default='None',
                ),
                Arg(name='ordered', type='bool', default='False'),
                Arg(name='geometry_types', type='Sequence[EnumValue]', default='()'),
                Arg(name='primitive_types', type='Sequence[EnumValue]', default='()'),
                Arg(name='allow_obj_sel', type='bool', default='True'),
                Arg(name='icon', type='Optional[str]', default='None'),
                Arg(name='label', type='Optional[str]', default='None'),
                Arg(name='prior_selection_paths', type='list', default='[]'),
                Arg(name='prior_selection_ids', type='list', default='[]'),
                Arg(name='prior_selections', type='list', default='[]'),
                Arg(name='allow_other_sops', type='bool', default='True'),
                Arg(name='consume_selections', type='bool', default='True'),
            ],
            returnType='GeometrySelection',
            className='SceneViewer',
        ),
    },
    'ViewportVisualizer': {
        'setParm': HouFunc(
            name='setParm',
            comment='Redefine',
            args=[
                Arg(name='self', type='ViewportVisualizer', default='NO_DEFAULT'),
                Arg(name='parm_name', type='str', default='NO_DEFAULT'),
                Arg(name='value', type='Union[int, float, str]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='ViewportVizualizer',
        ),
    },
    'NetworkEditor': {
        'flashMessage': HouFunc(
            name='flashMessage',
            comment='Redefine',
            args=[
                Arg(name='self', type='NetworkEditor', default='NO_DEFAULT'),
                Arg(name='image', type='Optional[str]', default='NO_DEFAULT'),
                Arg(name='message', type='Optional[str]', default='NO_DEFAULT'),
                Arg(name='duration', type='float', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='NetworkEditor',
        ),
        'registerPref': HouFunc(
            name='registerPref',
            comment='Redefine for illegal argument',
            args=[
                Arg(name='self', type='NetworkEditor', default='NO_DEFAULT'),
                Arg(name='pref', type='str', default='NO_DEFAULT'),
                Arg(name='value', type='str', default='NO_DEFAULT'),
                Arg(name='_global', type='bool', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='NetworkEditor',
        ),
    },
    'Selection': {
        'numSelected': HouFunc(
            name='numSelected',
            comment='Redefine',
            args=[
                Arg(name='self', type='Selection', default='NO_DEFAULT'),
            ],
            returnType='int',
            className='Selection',
        ),
    },
    'NodeInfoTree': {
        '__init__': HouFunc(
            name='__init__',
            comment='Redefine',
            args=[
                Arg(name='self', type='NodeInfoTree', default='NO_DEFAULT'),
                Arg(name='tree_root', type='Any', default='NO_DEFAULT'),
                Arg(name='tree', type='Any', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='NodeInfoTree',
        ),
    },
    'PerfMonProfile': {
        'stats': HouFunc(
            name='stats',
            comment='Redefine',
            args=[
                Arg(name='self', type='PerfMonProfile', default='NO_DEFAULT'),
            ],
            returnType='Dict[str, Any]',
            className='PerfMonProfile',
        ),
    },
    'SwigPyIterator': {
        '__eq__': HouFunc(
            name='__eq__',
            comment='Redefine',
            args=[
                Arg(name='self', type='SwigPyIterator', default='NO_DEFAULT'),
                Arg(name='x', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='SwigPyIterator',
        ),
        '__ne__': HouFunc(
            name='__ne__',
            comment='Redefine',
            args=[
                Arg(name='self', type='SwigPyIterator', default='NO_DEFAULT'),
                Arg(name='x', type='object', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='SwigPyIterator',
        ),
        '__sub__': HouFunc(
            name='__sub__',
            comment='Redefine',
            args=[
                Arg(name='self', type='SwigPyIterator', default='NO_DEFAULT'),
                Arg(name='n', type='int', default='NO_DEFAULT'),
            ],
            returnType='Any',
            className='SwigPyIterator',
        ),
    },
    'OperationFailed': {
        '__init__': HouFunc(
            name='__init__',
            comment='Redefine',
            args=[
                Arg(name='self', type='OperationFailed', default='NO_DEFAULT'),
                Arg(name='message', type='Optional[str]', default='""'),
            ],
            returnType='None',
            className='OperationFailed',
        ),
    },
    'AgentMetadata': {
        'data': HouFunc(
            name='data',
            comment='Redefine to fix return type',
            args=[
                Arg(name='self', type='AgentMetadata', default='NO_DEFAULT'),
            ],
            returnType='Dict[str, Any]',
            className='AgentMetadata',
        ),
        'setData': HouFunc(
            name='setData',
            comment='Redefine',
            args=[
                Arg(name='self', type='AgentMetadata', default='NO_DEFAULT'),
                Arg(name='data', type='Dict[str, Any]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='AgentMetadata',
        ),
    },
    'AssetGalleryDataSource': {
        'setMetadata': HouFunc(
            name='setMetadata',
            comment='Redefine',
            args=[
                Arg(name='self', type='AssetGalleryDataSource', default='NO_DEFAULT'),
                Arg(name='item_id', type='str', default='NO_DEFAULT'),
                Arg(name='metadata', type='Dict[str, Any]', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='AgentMetadata',
        ),
    },
    'ChannelGraph': {
        'selectedKeyframes': HouFunc(
            name='selectedKeyframes',
            comment='Redefine',
            args=[
                Arg(name='self', type='ChannelGraph', default='NO_DEFAULT'),
            ],
            returnType='Dict[Parm, Tuple[BaseKeyframe, ...]]',
            className='ChannelGraph',
        ),
    },
    'GeometryViewport': {
        'changeType': HouFunc(
            name='changeType',
            comment='Redefine',
            args=[
                Arg(name='self', type='GeometryViewport', default='NO_DEFAULT'),
                Arg(name='type', type='EnumValue', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='GeometryViewport',
        ),
    },
    '_StringMapDoubleTuple': {
        '__iter__': HouFunc(
            name='__iter__',
            comment='Redefine',
            args=[
                Arg(name='self', type='_StringMapDoubleTuple', default='NO_DEFAULT'),
            ],
            returnType='Iterator[str]',
            className='_StringMapDoubleTuple',
        ),
    },
    'VopNode': {
        'deleteIndependentInputNodes': HouFunc(
            name='deleteIndependentInputNodes',
            comment='Redefine',
            args=[
                Arg(name='self', type='VopNode', default='NO_DEFAULT'),
                Arg(name='input_index', type='int', default='NO_DEFAULT'),
                Arg(name='make_parm_node', type='bool', default='NO_DEFAULT'),
                Arg(name='reference_input_defaults', type='Any', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='VopNode',
        ),
    },
    'hda': {
        'reloadHDAModule': HouFunc(
            name='reloadHDAModule',
            comment='Missing.',
            args=[
                Arg(name='self', type='hda', default='NO_DEFAULT'),
                Arg(name='hda_module', type='HDAModule', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='hda',
        ),
    },
    'hmath': {
        'buildTransform': HouFunc(
            name='buildTransform',
            comment='Redefine',
            args=[
                Arg(name='self', type='hmath', default='NO_DEFAULT'),
                Arg(
                    name='values_dict',
                    type='Dict[str, Union[Vector3, Sequence[float]]]',
                    default='NO_DEFAULT',
                ),
                Arg(name='transform_order', type='str', default='"srt"'),
                Arg(name='rotate_order', type='str', default='"xyz"'),
            ],
            returnType='Matrix4',
            className='hmath',
        ),
    },
    'playbar': {
        'setChannelList': HouFunc(
            name='setChannelList',
            comment='Redefine',
            args=[
                Arg(name='arg', type='ChannelList', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='playbar',
        ),
    },
    'hotkeys': {
        'assignments': HouFunc(
            name='assignments',
            comment='Redefine',
            args=[
                Arg(name='self', type='hotkeys', default='NO_DEFAULT'),
                Arg(name='hotkey_symbol', type='str', default='NO_DEFAULT'),
            ],
            returnType='List[str]',
            className='hotkeys',
        ),
    },
    'qt': {
        'mainWindow': HouFunc(
            name='mainWindow',
            comment='Missing',
            args=[
                Arg(name='self', type='qt', default='NO_DEFAULT'),
            ],
            returnType='QtWidgets.QMainWindow',
            className='qt',
        ),
        'Icon': HouFunc(
            name='Icon',
            comment='Missing.  This is actually a class, but a simple enough '
            'one that we can pretend it is a function to avoid the '
            'complication of defining a wholly missing class from hou.py',
            args=[
                Arg(name='self', type='qt', default='NO_DEFAULT'),
                Arg(name='icon_name', type='str', default='NO_DEFAULT'),
                Arg(name='width', type='Optional[int]', default='None'),
                Arg(name='height', type='Optional[int]', default='None'),
            ],
            returnType='QtGui.QIcon',
            className='qt',
        ),
    },
    'ui': {
        'displayConfirmation': HouFunc(
            name='displayConfirmation',
            comment='Missing',
            args=[
                Arg(name='self', type='ui', default='NO_DEFAULT'),
                Arg(name='text', type='str', default='NO_DEFAULT'),
                Arg(name='severity', type='EnumValue', default='severityType.Message'),
                Arg(name='help', type='Optional[str]', default='None'),
                Arg(name='title', type='Optional[str]', default='None'),
                Arg(name='details', type='Optional[str]', default='None'),
                Arg(name='destails_label', type='Optional[str]', default='None'),
                Arg(name='destails_expanded', type='bool', default='False'),
            ],
            returnType='bool',
            className='ui',
        ),
        'hasDragSourceData': HouFunc(
            name='hasDragSourceData',
            comment='Redefine',
            args=[
                Arg(name='label', type='str', default='NO_DEFAULT'),
                Arg(name='index', type='int', default='NO_DEFAULT'),
            ],
            returnType='bool',
            className='ui',
        ),
        'selectFile': HouFunc(
            name='selectFile',
            comment='Missing',
            args=[
                Arg(name='self', type='ui', default='NO_DEFAULT'),
                Arg(name='start_directory', type='Optional[str]', default='None'),
                Arg(name='title', type='Optional[str]', default='None'),
                Arg(name='collapse_sequences', type='bool', default='False'),
                Arg(name='file_type', type='EnumValue', default='fileType.Any'),
                Arg(name='pattern', type='Optional[str]', default='None'),
                Arg(name='default_value', type='Optional[str]', default='None'),
                Arg(name='multiple_select', type='bool', default='False'),
                Arg(name='image_chooser', type='bool', default='False'),
                Arg(
                    name='chooser_mode',
                    type='EnumValue',
                    default='fileChooserMode.ReadAndWrite',
                ),
                Arg(name='width', type='int', default='0'),
                Arg(name='height', type='int', default='0'),
            ],
            returnType='str',
            className='ui',
        ),
    },
    'webServer': {
        'registerOpdefPath': HouFunc(
            name='registerOpdefPath',
            comment='Redefine',
            args=[
                Arg(name='self', type='webServer', default='NO_DEFAULT'),
                Arg(name='prefix', type='str', default='NO_DEFAULT'),
            ],
            returnType='None',
            className='webServer',
        ),
    },
}  # type: Dict[Optional[str], Dict[str, HouFunc]]


OVERLOAD_FUNCTION_DEFINITIONS = {
    None: {
        'nodeType': [
            HouFunc(
                name='nodeType',
                comment='Overloaded!',
                args=[
                    Arg(name='category', type='NodeTypeCategory', default='NO_DEFAULT'),
                    Arg(name='internal_name', type='str', default='NO_DEFAULT'),
                ],
                returnType='Optional[NodeType]',
            ),
            HouFunc(
                name='nodeType',
                comment='Overloaded!',
                args=[
                    Arg(
                        name='internal_name_with_category',
                        type='str',
                        default='NO_DEFAULT',
                    ),
                ],
                returnType='Optional[NodeType]',
            ),
        ],
    },
    'hmath': {
        'buildTranslate': [
            HouFunc(
                name='buildTranslate',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(name='x', type='float', default='NO_DEFAULT'),
                    Arg(name='y', type='float', default='NO_DEFAULT'),
                    Arg(name='z', type='float', default='NO_DEFAULT'),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
            HouFunc(
                name='buildTranslate',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(
                        name='components',
                        type='Union[Sequence[float], Vector3]',
                        default='NO_DEFAULT',
                    ),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
        ],
        'buildScale': [
            HouFunc(
                name='buildScale',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(name='sx', type='float', default='NO_DEFAULT'),
                    Arg(name='sy', type='float', default='NO_DEFAULT'),
                    Arg(name='sz', type='float', default='NO_DEFAULT'),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
            HouFunc(
                name='buildScale',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(
                        name='components',
                        type='Union[Sequence[float], Vector3]',
                        default='NO_DEFAULT',
                    ),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
        ],
        'buildShear': [
            HouFunc(
                name='buildShear',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(name='shearx', type='float', default='NO_DEFAULT'),
                    Arg(name='sheary', type='float', default='NO_DEFAULT'),
                    Arg(name='shearz', type='float', default='NO_DEFAULT'),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
            HouFunc(
                name='buildShear',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(
                        name='components',
                        type='Union[Sequence[float], Vector3]',
                        default='NO_DEFAULT',
                    ),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
        ],
        'buildRotate': [
            HouFunc(
                name='buildRotate',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(name='rx', type='float', default='NO_DEFAULT'),
                    Arg(name='ry', type='float', default='NO_DEFAULT'),
                    Arg(name='rz', type='float', default='NO_DEFAULT'),
                    Arg(name='order', type='str', default='"xyz"'),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
            HouFunc(
                name='buildRotate',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='hmath', default='NO_DEFAULT'),
                    Arg(
                        name='components',
                        type='Union[Sequence[float], Vector3]',
                        default='NO_DEFAULT',
                    ),
                    Arg(name='order', type='str', default='"xyz"'),
                ],
                returnType='Matrix4',
                className='hmath',
            ),
        ],
    },
    'Color': {
        '__init__': [
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Color', default='NO_DEFAULT'),
                    Arg(
                        name='rgb_tuple',
                        type='Sequence[float]',
                        default='(0.0, 0.0, 0.0)',
                    ),
                ],
                returnType='None',
                className='Color',
            ),
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Color', default='NO_DEFAULT'),
                    Arg(name='r', type='float', default='0.0'),
                    Arg(name='g', type='float', default='0.0'),
                    Arg(name='b', type='float', default='0.0'),
                ],
                returnType='None',
                className='Color',
            ),
        ],
    },
    'Vector2': {
        '__init__': [
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Vector2', default='NO_DEFAULT'),
                    Arg(name='values', type='Sequence[float]', default='(0.0, 0.0)'),
                ],
                returnType='None',
                className='Vector2',
            ),
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Vector2', default='NO_DEFAULT'),
                    Arg(name='x', type='float', default='0.0'),
                    Arg(name='y', type='float', default='0.0'),
                ],
                returnType='None',
                className='Vector2',
            ),
        ],
    },
    'Vector3': {
        '__init__': [
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Vector3', default='NO_DEFAULT'),
                    Arg(
                        name='values', type='Sequence[float]', default='(0.0, 0.0, 0.0)'
                    ),
                ],
                returnType='None',
                className='Vector3',
            ),
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Vector3', default='NO_DEFAULT'),
                    Arg(name='x', type='float', default='0.0'),
                    Arg(name='y', type='float', default='0.0'),
                    Arg(name='z', type='float', default='0.0'),
                ],
                returnType='None',
                className='Vector3',
            ),
        ],
    },
    'Vector4': {
        '__init__': [
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Vector4', default='NO_DEFAULT'),
                    Arg(
                        name='values',
                        type='Sequence[float]',
                        default='(0.0, 0.0, 0.0, 0.0)',
                    ),
                ],
                returnType='None',
                className='Vector4',
            ),
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Vector4', default='NO_DEFAULT'),
                    Arg(name='x', type='float', default='0.0'),
                    Arg(name='y', type='float', default='0.0'),
                    Arg(name='z', type='float', default='0.0'),
                    Arg(name='w', type='float', default='0.0'),
                ],
                returnType='None',
                className='Vector4',
            ),
        ],
    },
    'BoundingRect': {
        '__init__': [
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='BoundingRect', default='NO_DEFAULT'),
                    Arg(name='p1', type='Iterable[float]', default='(0.0, 0.0)'),
                    Arg(name='p2', type='Iterable[float]', default='(0.0, 0.0)'),
                ],
                returnType='None',
                className='BoundingRect',
            ),
            HouFunc(
                name='__init__',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='BoundingRect', default='NO_DEFAULT'),
                    Arg(name='xmin', type='float', default='0.0'),
                    Arg(name='ymin', type='float', default='0.0'),
                    Arg(name='xmax', type='float', default='0.0'),
                    Arg(name='ymax', type='float', default='0.0'),
                ],
                returnType='None',
                className='BoundingRect',
            ),
        ],
    },
    'Prim': {
        'intrinsicValue': [
            HouFunc(
                name='intrinsicValue',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Prim', default='NO_DEFAULT'),
                    Arg(
                        name='intrinsic_name',
                        type='Literal["transform"]',
                        default='NO_DEFAULT',
                    ),
                ],
                returnType='Tuple[float, ...]',
                className='Prim',
            ),
            HouFunc(
                name='intrinsicValue',
                comment='Overloaded!',
                args=[
                    Arg(name='self', type='Prim', default='NO_DEFAULT'),
                    Arg(name='intrinsic_name', type='str', default='NO_DEFAULT'),
                ],
                returnType='Union[int, float, str, Tuple[int, ...], Tuple[float, ...], Tuple[str, ...]]',
                className='Prim',
            ),
        ],
    },
}  # type: Dict[Optional[str], Dict[str, List[HouFunc]]]

# Flipbook settings use the same method for getting and setting, based on
# whether arguments are provided.  All of these methods take exactly the same
# argument type as their return type.  For instance, resolution takes a
# Tuple[float, float], not two float arguments.
for method, argType in [
    ('outputToMPlay', 'bool'),
    ('cropOutMaskOverlay', 'bool'),
    ('overrideGamma', 'bool'),
    ('useResolution', 'bool'),
    ('leaveFrameAtEnd', 'bool'),
    ('beautyPassOnly', 'bool'),
    ('renderAllViewports', 'bool'),
    ('appendFramesToCurrent', 'bool'),
    ('scopeChannelKeyframesOnly', 'bool'),
    ('blockEditing', 'bool'),
    ('initializeSimulations', 'bool'),
    ('overrideLUT', 'bool'),
    ('useMotionBlur', 'bool'),
    ('shutterFromCamera', 'bool'),
    ('useDepthOfField', 'bool'),
    ('depthOfFieldFromCamera', 'bool'),
    ('useSheetSize', 'bool'),
    ('fromAudioPanel', 'bool'),
    ('output', 'str'),
    ('LUT', 'str'),
    ('sessionLabel', 'str'),
    ('audioFilename', 'str'),
    ('backgroundImage', 'str'),
    ('gamma', 'float'),
    ('audioFrameStart', 'float'),
    ('audioTimeOffset', 'float'),
    ('shutter', 'float'),
    ('depthOfFieldQuality', 'float'),
    ('focusDistance', 'float'),
    ('aperture', 'float'),
    ('fStop', 'float'),
    ('outputZoom', 'int'),
    ('motionBlurSegments', 'int'),
    ('visibleTypes', 'EnumValue'),
    ('antialias', 'EnumValue'),
    ('motionBlurFrameRange', 'EnumValue'),
    ('visibleObjects', 'str'),
    ('frameRange', 'Tuple[float, float]'),
    ('frameIncrement', 'int'),
    ('resolution', 'Tuple[int, int]'),
    ('sheetSize', 'Tuple[int, int]'),
]:
    OVERLOAD_FUNCTION_DEFINITIONS.setdefault('FlipbookSettings', {})[method] = [
        HouFunc(
            name=method,
            comment='Overloaded!',
            args=[
                Arg(name='self', type='FlipbookSettings', default='NO_DEFAULT'),
            ],
            returnType=argType,
            className='FlipbookSettings',
        ),
        HouFunc(
            name=method,
            comment='Overloaded!',
            args=[
                Arg(name='self', type='FlipbookSettings', default='NO_DEFAULT'),
                Arg(name='value', type=argType, default='NO_DEFAULT'),
            ],
            returnType='None',
            className='FlipbookSettings',
        ),
    ]


OVERLOADED_FUNCTIONS = set()  # type: Set[str]
for _clsName in OVERLOAD_FUNCTION_DEFINITIONS:
    for _fnName in OVERLOAD_FUNCTION_DEFINITIONS[_clsName]:
        for _fn in OVERLOAD_FUNCTION_DEFINITIONS[_clsName][_fnName]:
            OVERLOADED_FUNCTIONS.add(_fn.namespacedName)


@attr.s
class HouClass(object):
    name = attr.ib(type=str)
    comment = attr.ib(type=str)
    functions = attr.ib(type=Dict[str, HouFunc], factory=dict, repr=False)
    enumValues = attr.ib(type=List[str], repr=False)

    @enumValues.default
    def getEnumValuesFromComment(self):
        """
        Determine the enumeration values from the docstring
        """
        enumValues = []
        if 'VALUES' in self.comment:
            # If 'VALUES' is in the docstring, we will parse it for
            # enumeration values names.
            headerIndent = -1
            valuesIndent = -1
            readingValues = False
            for line in self.comment.split('\n'):
                indentMatch = reIndents.match(line)
                if indentMatch:
                    indent = len(indentMatch.group('indentsize'))
                    if indent == headerIndent:
                        # We have unindented after reading the VALUES block.
                        readingValues = False
                        break
                    if line == 'VALUES':
                        # Once we encounter VALUES, record the indentation of
                        # where we see it, so we know when we have exited.
                        headerIndent = indent
                        readingValues = True
                        continue

                    if readingValues and valuesIndent == -1:
                        # We have entered into the VALUES block.
                        valuesIndent = indent

                    if indent == valuesIndent:
                        # We check that the indent matches where we expect to
                        # find enum values to avoid reading in the description
                        # of an enum value, which will be further indented.

                        # Since some enum values will be the fully qualified
                        # name and others will just be the end, and we only
                        # want the member name, we only take the last part.
                        enumValue = line.split('.')[-1].strip()
                        if enumValue in enumValues:
                            continue
                        enumValues.append(enumValue)

        return sorted(enumValues)

    def unwrittenFunctions(self):
        # type: () -> Iterator[HouFunc]
        """
        Get a list of the functions which have not been written to the PYI file.

        Yields
        -------
        HouFunc
        """
        for name, func in self.functions.items():  # type: str, HouFunc
            if (
                func.namespacedName in SKIP_FUNCS
                or func.namespacedName in OVERLOADED_FUNCTIONS
                or '*.%s' % name in SKIP_FUNCS
            ):
                continue

            if not func.written:
                yield func


class LineIterator(Generic[T]):
    """
    Iterate over a generator, keeping track of the current index.

    We use this to help us debug wonky formatting in the original file.
    """

    def __init__(self, generator):
        # type: (Iterable[T]) -> None
        """
        Parameters
        ----------
        generator : Iterable[T]
        """
        if not hasattr(generator, 'next'):
            generator = iter(generator)
        self.generator = generator
        self.lineno = 0
        self.current = ""

    def __iter__(self):
        # type: () -> Iterator[T]
        """
        Yields
        ------
        T
        """
        while True:
            try:
                yield next(self)
            except StopIteration:
                break

    def __next__(self):
        # type: () -> T
        """
        Advance the iterator and return the next line

        Returns
        -------
        T
        """
        self.current = next(self.generator)
        self.lineno += 1
        return self.current


class Tree(OrderedDict):
    """
    An ordered dictionary that allows for duplicate keys.

    Not advisable to access items by key, since the dictionary might
    have duplicate keys.
    """

    rePrefix = re.compile(r'^%[0-9]+%')

    def __setitem__(self, key, value):
        if key in self:
            key = "%%%d%%%s" % (len(self), key)
        return super(Tree, self).__setitem__(key, value)

    def __iter__(self):
        for item in super(Tree, self).__iter__():
            yield self.rePrefix.sub('', item)


def getHouStructs(typeHints):
    # type: (Dict[str, Dict[int, str]]) -> Tuple[Dict[str, HouClass], Dict[str, HouFunc]]
    """
    Determine the types of hou.py arguments and return values.

    Parameters
    ----------
    typeHints : Dict[str, Dict[int, str]]

    Returns
    -------
    Dict[str, HouClass]
    Dict[str, HouFunc]
    """
    funcsByNamespace = {}  # type: Dict[str, HouFunc]
    with open(HOUPY, 'r') as houFile:
        lines = houFile.readlines()
        houClasses, houFuncs = parsePyFile(LineIterator(lines), typeHints)

    for className, houClass in houClasses.items():
        for funcName, houFunc in houClass.functions.items():
            funcsByNamespace['%s.%s' % (className, funcName)] = houFunc
    funcsByNamespace.update(houFuncs)

    # Some of the docstrings are just wrong, so we provide a last
    # minute spot to update them with patches.
    for namespacedName, returnType in RETURN_TYPE_PATCHES.items():
        if namespacedName not in funcsByNamespace:
            # print("WARNING: Return type patch %s not used." % namespacedName)
            continue
        funcsByNamespace[namespacedName].returnType = returnType

    return houClasses, funcsByNamespace


def parsePyFile(lines, typeHints):
    # type: (LineIterator[str], Dict[str, Dict[int, str]]) -> Tuple[Dict[str, HouClass], Dict[str, HouFunc]]
    """
    Parse classes and functions from the lines of hou.py

    Parameters
    ----------
    lines : LineIterator[str]
    typeHints : Dict[str, Dict[int, str]]

    Returns
    -------
    Dict[str, HouClass]
    Dict[str, HouFunc]
    """
    classes = {}  # type: Dict[str, HouClass]
    functions = {}  # type: Dict[str, HouFunc]
    line = next(lines)

    while True:
        classMatch = reClass.match(line)
        if classMatch:
            houClass = parseClass(classMatch, lines, typeHints)
            if houClass:
                classes[str(classMatch.group('name'))] = houClass
                line = lines.current

                # Immediately continue the loop here to avoid advancing the
                # iterator, since the end of parseClass needs to advance the loop
                # in order to detect that the class definition has finished.
                continue

        funcMatch = reFunctionReturn.match(line)
        if not funcMatch:
            funcMatch = reFunction.match(line)
        if funcMatch:
            houFunc = parseFunction(funcMatch, lines, typeHints)
            if houFunc:
                functions[str(funcMatch.group('name'))] = houFunc
                line = lines.current

                # Immediately continue the loop here to avoid advancing the
                # iterator, since we do not want to skip any lines.
                continue
        try:
            line = next(lines)
        except StopIteration:
            break

    for funcName in MISSING_FUNCTION_DEFINITIONS[None]:
        # Note that we are overriding definitions found in the original
        #  file with anything that exists in the constant dictionary.
        #  This is because we use this constant as a patch for docstrings
        #  which indicate incorrect results.
        func = MISSING_FUNCTION_DEFINITIONS[None][funcName]
        if funcName in functions:
            # If we have a real comment from the original hou.py, keep it.
            func.comment = functions[funcName].comment
        functions[funcName] = func

    return classes, functions


def extractBlockComment(lines):
    # type: (Iterator[str]) -> str
    """
    Extract a block comment

    Parameters
    ----------
    lines : Iterator[str]

    Returns
    -------
    str
    """
    blockComment = []

    # Current line will be """, so we want to look ahead to start.
    try:
        line = next(lines)
        while not reBlockComment.match(line):
            blockComment.append(line)
            line = next(lines)
    except StopIteration:
        pass

    return textwrap.dedent(''.join(blockComment)).strip()


def parseClass(classMatch, lines, typeHints):
    # type: (Match, LineIterator[str], Dict[str, Dict[int, str]]) -> Optional[HouClass]
    """
    Parse a houdini class from lines of hou.py

    Parameters
    ----------
    classMatch : Match
    lines : LineIterator[str]
    typeHints : Dict[str, Dict[int, str]]

    Returns
    -------
    Optional[HouClass]
    """
    name = str(classMatch.group('name'))
    classIndents = len(classMatch.group('indentsize'))

    comment = ''
    functions = {}  # type: Dict[str, HouFunc]
    for line in lines:
        if reBlockComment.match(line):
            comment = extractBlockComment(lines)

        funcMatch = reFunctionReturn.match(line)
        if not funcMatch:
            funcMatch = reFunction.match(line)

        if funcMatch:
            houFunc = parseFunction(funcMatch, lines, typeHints, name)
            if houFunc:
                functions[houFunc.name] = houFunc

        currentIndents = reIndents.match(line)
        if currentIndents:
            # NOTE: In order to know when the class definition has been
            #  unindented to the point of completion, we need to look at the
            #  next line (which might be the next class definition.  We need to
            #  be careful that the outer loop (in parseFile) is allowed to
            #  inspect this line again if we are breaking out.
            if classIndents >= len(currentIndents.group('indentsize')):
                # If we have unindented to the point of our class definition,
                # for further back, then we have finished processing the class
                # and we can move on.
                break

    # Now add in any special cased missing functions
    if name in MISSING_FUNCTION_DEFINITIONS:
        for fname in MISSING_FUNCTION_DEFINITIONS[name]:
            # Note that we are overriding definitions found in the original
            #  file with anything that exists in the constant dictionary.
            #  This is because we use this constant as a patch for docstrings
            #  which indicate incorrect results.
            houfunc = MISSING_FUNCTION_DEFINITIONS[name][fname]
            if fname in functions:
                # If we have a real comment from the original hou.py, keep it.
                houfunc.comment = functions[fname].comment
            functions[fname] = houfunc

    houClass = HouClass(name, comment, functions)

    if name in ADDITIONAL_ENUM_VALUES:
        for enumValueName in ADDITIONAL_ENUM_VALUES[name]:
            if enumValueName not in houClass.enumValues:
                houClass.enumValues.append(enumValueName)

    return houClass


def buildCleanFunction(namespacedName, funcMatch, typeHints, className=None):
    # type: (str, Match, Dict[str, Dict[int, str]], Optional[str]) -> HouFunc
    """
    Build a clean function for one that has no comment block in hou.py

    Starting with Houdini 19.5, the hou.py lines have C++ typing, which makes
    the default stubs have all kinds of terrible typing that we need to reset
    back what we had with Houdini 19.0, which typed every argument as 'Any'

    Parameters
    ----------
    namespacedName : str
    funcMatch : Match
    typeHints : Dict[str, Dict[int, str]]
    className : Optional[str]

    Returns
    -------
    HouFunc
    """
    argstr = str(funcMatch.group('args'))
    args = parseArgs(namespacedName, argstr, typeHints, className)
    try:
        rawReturn = funcMatch.group('returnType').strip('"\'')
        returnType = rawReturn
        returnType = 'Any'
    except IndexError:
        # no return
        returnType = 'None'

    return HouFunc(
        str(funcMatch.group('name')),
        'No comment',
        args,
        returnType,
        className,
    )


def parseArgs(namespacedName, argstr, typeHints, className=None):
    # type: (str, str, Dict[str, Dict[int, str]], Optional[str]) -> List[Arg]
    """
    Parse arguments for a function.

    Parameters
    ----------
    argstr : str
    typeHints : Dict[str, Dict[int, str]]
    namespacedName : str
    className : Optional[str]

    Returns
    -------
    List[Arg]
    """
    args = []  # type: List[Arg]

    # The quoted
    argstr = reSingleQuoted.sub('"Any"', argstr)
    argstr = reDoubleQuoted.sub('"Any"', argstr)

    # Replace the commas in tuples default arguments with a
    # semicolon so we don't split with that.  We don't use
    # it, so it doesn't matter.
    # This will not handle nested default tuples,
    # but AFAIK, there are none in hou.
    for tupleDefault in reTupleSimple.findall(argstr):
        argstr = argstr.replace(tupleDefault, tupleDefault.replace(',', ';'))
    for listDefault in reListSimple.findall(argstr):
        argstr = argstr.replace(listDefault, listDefault.replace(',', ';'))

    rawArgsSplit = argstr.split(",")
    if className is not None and not (rawArgsSplit and rawArgsSplit[0] == 'self'):
        # Ensure the first argument is self for class methods, since
        # the docstrings are inconsistent with whether or not they
        # provide the class argument.
        rawArgsSplit.insert(0, 'self')

    for i, rawArg in enumerate(rawArgsSplit):
        typeHint = typeHints.get(namespacedName, {}).get(i + 1)
        if '=' in rawArg:
            argName, argValue = rawArg.split('=', 1)
            # We strip after the split so we remove any bad
            # whitespace around the operator.
            argName = argName.strip().split(':')[0]
            argValue = argValue.strip().replace('\\"', '"').replace("\\'", "'")
            argType, argValue = determineArgType(
                argName, argValue, typeHint, namespacedName
            )
        else:
            argName = rawArg.strip()
            argType = ''
            # Some of the docstrings supply an argument type instead
            # of an argument name.  This looks to only happen if it's
            # an EnumValue though.
            if reHOMArgumentFormat.match(argName):
                argName = pylib.strings.toSnakeCase(
                    reHOMArgumentFormat.sub(r'\g<type>', argName)
                )
                argType = 'EnumValue'
            elif reHOUArgumentFormat.match(argName):
                argName = pylib.strings.toSnakeCase(
                    reHOUArgumentFormat.sub(r'\g<type>', argName)
                )
                argType = 'EnumValue'

            argName = argName.split(':')[0]

            argValue = NO_DEFAULT
            if not argType:
                argType = ARG_TYPES_FROM_NAME.get(argName, 'Any')

        argValue = argValue.replace(";", ",")
        if (
            typeHint
            and typeHint not in ('None', argType)
            and argType in ('Any', 'tuple')
            and namespacedName not in FUNCTIONS_SKIP_TYPE_HINTS
        ):
            # See if we have a better option.
            # Note that we do not use this for the primary method of
            #  obtaining typing information since the docstrings aren't
            #  reliable compared to the C symbol table.  Specifically
            #  the other of arguments in the symbol table is sometimes
            #  different than how they are described in the docstring
            #  (see ViewerStateTemplate.bindDynamicsSelector for an
            #  example). Since, for typing, we need to make the
            #  association of the argument name to a type, we are going
            #  to prefer the incorrect docstring information.
            argType = typeHint

        if argType == 'tuple':
            # If we are left with just Tuple[Any] as a type, we should
            # generalize it to take an iterable.
            argType = 'Iterable[Any]'

        if not argName and argType == 'Any':
            # Do not append unnamed arguments with no type. This will
            # normally happen due to a mismatch between how python and
            # C handle the first argument of fake namespace functions,
            # ex. hou.undos.redoLabels() is not a method on some `undos`
            # object.  Rather it is a function in the hou.undos
            # namespace, implemented in a wacky way.  We will complete
            # this thought with decorating each of these functions with
            # @staticmethod in the typing stub.
            continue

        # if keyword.iskeyword(argName) or argName in __builtin__.__dict__:
        if argName == ILLEGAL_ARG_NAMES:
            # Do not allow argument names to be stuff like "global"
            argName = 'arg%d' % i

        args.append(Arg(argName, argType, argValue))

    return args


def parseFunction(funcMatch, lines, typeHints, className=None):
    # type: (Match, LineIterator[str], Dict[str, Dict[int, str]], Optional[str]) -> HouFunc
    """
    Parse a houdini class from lines of hou.py

    Parameters
    ----------
    funcMatch : Match
    lines : LineIterator[str]
    typeHints : Dict[str, Dict[int, str]]
    className : Optional[str]

    Returns
    -------
    HouFunc
    """
    name = str(funcMatch.group('name'))

    args = []  # type: List[Arg]
    returnType = 'None'
    namespacedName = '%s.%s' % (className, name) if className else name

    if reBlockComment.match(next(lines)):
        comment = extractBlockComment(lines)
    else:
        # If we could not read a comment, then do not try to
        # determine typing information.
        return buildCleanFunction(namespacedName, funcMatch, typeHints, className)

    hasFunctionDefInComment = False
    for commentChunk in reCommentBlockSections.split(comment):
        if not commentChunk.strip():
            continue

        commentLine = textwrap.dedent(''.join(commentChunk)).replace('\n', ' ')
        funcArgsMatch = reFunctionReturnArgs.match(commentLine.strip())
        if funcArgsMatch:
            # First see if we can match with the return type
            returnType = determineReturnType(
                funcArgsMatch.group('returnType'), namespacedName
            )
        else:
            # We could not match with the return type, so see if it's a
            # function without a return.
            funcArgsMatch = reFunctionArgs.match(commentLine.strip())

        if funcArgsMatch:
            hasFunctionDefInComment = True
            argstr = str(funcArgsMatch.group('args'))
            args.extend(parseArgs(namespacedName, argstr, typeHints, className))

    if not hasFunctionDefInComment:
        # We need to make sure that we don't forward along any BS typing
        # from the hou.py if the function has a comment, but no reliable
        # typing to provide.
        return buildCleanFunction(namespacedName, funcMatch, typeHints, className)

    return HouFunc(name, comment, args, returnType, className)


def determineArgType(name, value, typeHint, funcName):
    # type: (str, str, Optional[str], str) -> Tuple[str, str]
    """
    Determine a type from a given string representation.

    Parameters
    ----------
    name : str
    value : str
    typeHint : Optional[str]
    funcName : str

    Returns
    -------
    str
        The argument type
    str
        The default value
    """
    value = ARG_TYPE_PATCHES.get(value, value).replace('`', '')

    # Some of the values still refer to the C++ namespaces
    value = reHOMArgumentFormat.sub(r'\g<type>', value)
    value = value.replace('::', '.')

    if value.startswith("hou."):
        value = value[4:]

        # Check if the default argument is a call to a class, like `BoundingBox()`
        classCallMatch = reClassCall.match(value)
        if classCallMatch:
            # This is some call to a class or function, and we want to
            argType = str(classCallMatch.group('name'))
        else:
            # Now check if the default is a function call.
            funcCallMatch = reFuncCall.match(value)
            if funcCallMatch:
                # If the default value is a function call, we would need to see
                # what the return value of that function is.  Since we aren't
                # currently making two passes at this, we don't know for sure
                # that the function has already been identified, so we will
                # just need to type this as `Any`.
                # TODO: Maybe mark this with some token to indicate that we
                #  should update this later, once we have function return values.
                argType = 'Any'
            else:
                # This is going to be an enum value, such as
                # hou.scriptLanguage.Python, and we want 'scriptLanguage' from it.
                # If there was such a thing as hou.Enum, we would want:
                #   argType = value.split(".", 1)[0]
                # But since the enums are just objects that contain EnumValue,
                # we need to just use EnumValue as the type.
                argType = "EnumValue"
    else:
        tupleOrListMatch = reTupleOrListArg.match(value)
        if tupleOrListMatch:
            iterableType = ITERABLE_TYPES_BY_CHAR[tupleOrListMatch.group('char')]
            nestedArgType, _ = determineArgType(
                name, tupleOrListMatch.group('arg'), typeHint, funcName
            )
            # NOTE: argument types are generally more permissive for what they
            #  take, so here we generalize the tuple or list arg to Sequence.
            argType = 'Sequence[%s]' % nestedArgType
        else:
            argType = eval(value).__class__.__name__
            if argType == 'NoneType':
                # This is some optional argument that we won't be able to
                # figure out easily.
                if typeHint and typeHint != 'None':
                    argType = typeHint
                else:
                    argType = ARG_TYPES_FROM_NAME.get(name, 'Any')
                argType = 'Optional[%s]' % ARG_TYPE_PATCHES.get(argType, argType)
            elif argType == 'type':
                # Could not determine a type for this arg
                argType = 'Any'

    return argType, DEFAULT_VALUE_PATCHES.get(value, value)


def determineReturnType(arg, funcName):
    # type: (str, str) -> str
    """
    Determine a type from a given string representation.

    Parameters
    ----------
    arg : str
    funcName : str

    Returns
    -------
    str
    """
    possibleTypes = []
    if arg in ARG_TYPE_PATCHES:
        # If we have special cased some nutty return type
        return ARG_TYPE_PATCHES[arg]

    # First convert any arguments that are 'or None' to Optional,
    # to allow us to split nicely.
    arg = reEnumValues.sub("", arg)
    arg = reOrNone.sub(
        lambda x: 'Optional['
        + ARG_TYPE_PATCHES.get(x.group('type'), x.group('type'))
        + ']',
        arg,
    )
    for typeString in reOrSplit.split(arg):
        # Clear off any typing or namespace cruft.
        typeString = ARG_TYPE_PATCHES.get(typeString, typeString)
        typeString = reStartsWithTupleOfAndParenthesis.sub("(", typeString)
        typeString = reHOMArgumentFormat.sub(r'\g<type>', typeString)
        if rePxrType.match(typeString):
            # Leave pxr types alone.  Currently includes:
            # * pxr.Sdf.Layer
            # * pxr.Usd.Stage
            pass
        elif reEnumValueType.search(typeString):
            # Since hou.Enum does not exist, we cannot validate to the
            # particular parent type of EnumValue, so we just need to say that
            # each one EnumValue, unfortunately.
            typeString = 'EnumValue'
        # By this point, any references to hou should be class names,
        # such as hou.Vector3
        typeString = typeString.replace("hou.", "").strip()

        if typeString == "tuple":
            # If it's literally just "tuple", we need to get a little creative.
            if possibleTypes:
                # If the comment is badly formed, such as "float or tuple",
                # then we make an assumption that we are building a
                # tuple of floats.  This is confirmed by anedotal reading of
                # the docstrings for some of these badly described functions.
                typed = "Tuple[%s, ...]" % possibleTypes[0]
            else:
                typed = "Tuple[Any, ...]"
        elif 'list of' in typeString:
            typed = reListType.sub(r'List[\g<type>]', typeString)
        elif 'generator of' in typeString:
            typed = reGeneratorType.sub(r'Iterator[\g<type>]', typeString)
        elif 'dict of' in typeString:
            typed = reDictType.sub(r'Dict[\g<fromtype>, \g<totype>]', typeString)
        else:
            # Formats for tuples in hou.py include:
            # * tuple of type
            # * tuple of types  //pluralized type
            # * tuple of (type, type, type)
            # * tuple of (type, type, type) tuples
            # * (type, type, type)
            # * tuple of 3 ints
            # The following cases are handled in ARG_TYPE_PATCHES for the moment.
            # * (tuple of typeA, tuple of tuples of typeB)
            # * (NotATypeA, NotATypeB)
            # * dict of (str, int) to str

            tupleWithNumberPrefixMatch = reTupleWithNumberPrefix.match(typeString)
            tupleWithNumberMatch = reTupleWithNumber.match(typeString)
            tupleWithTwoTypesMatch = reTupleWithTwoTypes.match(typeString)
            if tupleWithNumberPrefixMatch:
                # Something like "2-tuple of floats"
                count = int(tupleWithNumberPrefixMatch.group('count'))
                typeMatch = tupleWithNumberPrefixMatch.group('type').rstrip('s')
                typed = 'Tuple[%s]' % ', '.join([typeMatch] * count)

            elif tupleWithNumberMatch:
                # Something like "tuple of 2 floats"
                count = int(tupleWithNumberMatch.group('count'))
                typeMatch = tupleWithNumberMatch.group('type').rstrip('s')
                typed = 'Tuple[%s]' % ', '.join([typeMatch] * count)

            elif tupleWithTwoTypesMatch:
                type1 = str(tupleWithTwoTypesMatch.group('type1'))
                type2 = str(tupleWithTwoTypesMatch.group('type2'))
                typed = 'Tuple[Tuple[%s, %s], ...]' % (type1, type2)

            elif '(' in typeString:
                # If the docs already report this as a tuple, we will wrap it
                # in the correct formatting.  Note that the more complicated
                # examples of nested tuples of different types are special
                # cased in ARG_TYPE_PATCHES for the time being.

                # Check if the docstring ends with 'tuples', then remove it.
                endsWithTuplesMatch = reEndsWithTuples.match(typeString)
                if endsWithTuplesMatch:
                    typeString = reEndsWithTuples.sub(r'\g<prefix>', typeString)
                    # Each type needs to be a tuple of its defined type
                    types = ', '.join(
                        [
                            t.rstrip('s').strip()
                            for t in typeString.strip('()').split(',')
                        ]
                    )
                    typed = 'Tuple[Tuple[' + types + '], ...]'
                else:
                    types = ', '.join(
                        [
                            t.rstrip('s').strip()
                            for t in typeString.strip('()').split(',')
                        ]
                    )
                    typed = 'Tuple[' + types + ']'
            else:
                # This will be a simpler tuple string like
                #    tuple of tuple of floats
                typed = reTupleWithWordSimplePrefix.sub('Tuple[', typeString)
                if typed.endswith('s') and not typed.endswith('Settings'):
                    # Note that it is hard to distinguish between
                    #  'Nodes' and 'FlipbookSettings' for what we should strip
                    #  the suffix off, so we fix the errors we introduce by
                    #  remapping through our ARG_TYPE_PATCH dictionary at the end.
                    typed = typed.rstrip('s')
                typed = reTupleTypeExtraction.sub(
                    lambda x: x.group('prefix')
                    + ARG_TYPE_PATCHES.get(x.group('type'), x.group('type')),
                    typed,
                )
                for i in range(typed.count("Tuple[")):
                    typed += ", ...]"
                typed = ARG_TYPE_PATCHES.get(typed, typed)
        possibleTypes.append(typed)

    # Massage any values that have been left as comma separated lists.
    pts = []  # type: List[str]
    for possibleType in possibleTypes:
        if ',' in possibleType and '[' not in possibleType:
            # FIXME: This is really bad.  Essentially, we're making an
            #  assumption that the only things that are left as comma
            #  separated values are things that we haven't previously
            #  been able to parse.  ex. "int, float, or str"
            #  However, since the formatting of these strings is so
            #  inconsistent, we're going to do our best here and
            #  special case the rest.
            pt = reCommaSeparatedList.split(possibleType)
            possibleType = 'Union[%s]' % ', '.join(pt)
        possibleType = possibleType.replace("string", "str")
        possibleType = reExtraSpaces.sub(' ', possibleType)
        pts.append(possibleType)
    possibleTypes = pts

    if len(possibleTypes) == 0:
        return 'None'
    elif len(possibleTypes) == 1:
        return possibleTypes[0]
    else:
        return 'Union[%s]' % ','.join(possibleTypes)


def extractCTypes():
    # type: () -> Dict[str, Dict[int, str]]
    """
    Extract the types from the hou symbol table

    Returns
    -------
    Dict[str, Dict[int, str]]
    """
    proc = subprocess.Popen(
        ('strings %s | c++filt' % HOUSO), stdout=subprocess.PIPE, shell=True
    )
    stdout, stderr = proc.communicate()

    filteredData = filter(
        lambda x: x.startswith("in method '"), stdout.decode('utf-8').split('\n')
    )
    lines = LineIterator(filteredData)
    argTypes = {}  # Dict[str, Dict[int, str]]
    for line in lines:
        soArgMatch = reHouSOArgument.match(line)
        if soArgMatch:
            namespacedName = str(soArgMatch.group('name').replace('_', '.', 1))
            argOffset = 0
            if namespacedName.startswith('new.'):
                # Constructors look like new_class instead of class___init__
                # These instances also don't specify themselves the way other
                # methods do, but since python wants them, we will include it
                # ourselves here as well.
                className = namespacedName[4:]
                namespacedName = className + '.__init__'
                argTypes.setdefault(namespacedName, {})[1] = className

                # Additional arguments will need to be offset to make room.
                argOffset = 1
            argNum = int(soArgMatch.group('num')) + argOffset
            try:
                argType = parseCType(str(soArgMatch.group('type')))
            except ValueError:
                # Some types are extra wacky, but they are all defined by
                # protected classes that we don't care about.  So we're just
                # going to say they're Any and forget about it.
                argType = 'Any'
            argTypes.setdefault(namespacedName, {})[argNum] = argType

    return argTypes


def parseCArgDict(argDict, parent=''):
    # type: (Dict[str, Any], str) -> str
    """
    Walk an argument dictionary, constructing a type string.

    Parameters
    ----------
    argDict : Dict[str, Any]
    parent : str

    Returns
    -------
    str
    """
    result = ''
    for i, key in enumerate(argDict):
        value = argDict[key]

        if key == 'std::allocator':
            continue

        if parent == 'std::map' and i > 1:
            # Python dictionaries only take two arguments.
            continue

        result += ARG_TYPE_PATCHES.get(key, key)
        if value is not True:
            # If value is True, it means that it shouldn't actually be a
            # dictionary in the first place, so use the key as the value.
            result += '[' + parseCArgDict(value, key) + ']'

        if i < len(argDict) - 1:
            result += ', '

    return reHouSOEndChar.sub(r'\g<char>', result)


def parseCType(argType):
    # type: (str) -> str
    """
    Parse out a type from a given std C++ type

    Parameters
    ----------
    argType : str
    root = Optional[Dict[str, Any]]

    Returns
    -------
    str
    """
    argType = reHouSOHOM.sub('', argType)
    argType = reHouSOConst.sub('', argType)
    argType = reHouSOTail.sub('', argType)
    argType = argType.replace("<", "{")
    argType = argType.replace(">", "}")
    argType = '{%s}' % argType
    argType = reHouSOToken.sub(r'"\g<token>":', argType)
    argType = reHouSOSpaces.sub('', argType)
    argType = reHouSOColonTail.sub(r'\g<char>', argType)
    argType = reHouSOQuoteTail.sub(r'":true\g<char>', argType)

    argTypeDict = json.loads(argType, object_pairs_hook=Tree)  # type: Tree[str, Any]

    return parseCArgDict(argTypeDict)


def createPYIFile():
    # type: () -> None
    """
    Create a starting PYI file.

    This will copy the hou.py to a temp folder to avoid the relative
    import error when generating the stub.
    """
    tmp = '/tmp/hou.py'
    with open(HOUPY) as infp:
        with open(tmp, 'w') as outfp:
            contents = infp.read().replace(
                'if __package__ or "." in __name__:\n'
                '    from . import _hou\n'
                'else:\n'
                '    import _hou\n',
                'import _hou\n',
            )
            outfp.write(contents)

    # Find the location of the mypy stubgen
    mypyRaw = setpkglib.check_output(['which', 'mypy'], packages=['mypy']).strip()
    mypy = re.match(r".*?(/[^']+)", str(mypyRaw)).group(1)
    stubgen = os.path.join(os.path.normpath(mypy + '/../..'), 'bin/stubgen')

    # Generate the stubs
    if PY2:
        setpkglib.check_call(
            [stubgen, '--py2', '--no-import', tmp, '-o', '/tmp/'], packages=['mypy']
        )
    else:
        setpkglib.check_call(
            [stubgen, '--no-import', tmp, '-o', '/tmp/'], packages=['mypy']
        )


def updatePYIFile(classes, funcs):
    # type: (Dict[str, HouClass], Dict[Optional[str], HouFunc]) -> None
    """
    Read the PYI file, updating the definitions as we come to them.

    Parameters
    ----------
    classes: Dict[str, HouClass]
    funcs: Dict[Optional[str], HouFunc]
    """
    encounteredFunctionNames = set()  # type: Set[str]
    pyiOutput = []
    with open(HOUPYI, 'r') as pyiFile:
        allPYILines = pyiFile.readlines()

        currentClass = None  # type: Optional[str]
        classIndentSize = 0
        lines = LineIterator(allPYILines)

        for line in lines:
            lineOriginal = line
            prependLines = []  # type: List[str]
            if line.startswith('from typing import'):
                # We will take care of this ourselves.
                continue
            if reTopLevelFunc.match(line):
                # We don't need typing for these weirdos.
                # These are function definitions that are created at the top
                # level, but are otherwise already defined.
                # For example, hou.expandStringAtFrame
                continue

            try:
                if currentClass:
                    indentMatch = reIndents.match(line)
                    if indentMatch:
                        currentIndent = indentMatch.group('indentsize')
                        currentIndentSize = len(currentIndent)
                        if classIndentSize == currentIndentSize:
                            # We have just finished our class definition.

                            # Add any enum values that we found from the
                            # docstring.  We do this at the end of the
                            # definition in case we have an enum for 'Any'
                            # which will cause conflicts with anything else
                            # in the class that is typed as Any
                            for enumName in classInfo.enumValues:
                                prependLines.append(
                                    (
                                        classIndent
                                        + "    %s: EnumValue = ..."
                                        + PYI_RECORD_ADDED_COMMENT
                                        + "\n"
                                    )
                                    % enumName
                                )

                            # Now write any functions that we found for this
                            # class which weren't already defined.  This
                            # includes functions we've special-case added.
                            for unwritten in classes[currentClass].unwrittenFunctions():
                                prependLines.append(
                                    unwritten.formatLine(
                                        currentIndentSize + 4, addReceipt=True
                                    )
                                )

                            currentClass = None

                classMatch = reClass.match(line)
                if classMatch:
                    name = str(classMatch.group('name'))
                    if name not in classes:
                        currentClass = None
                        continue

                    classInfo = classes[name]
                    currentClass = name
                    classIndent = classMatch.group('indentsize')
                    classIndentSize = len(classIndent)

                    if name in CLASS_GENERICS:
                        classData = {
                            "name": name,
                            "indent": classIndent,
                            "superclass": CLASS_GENERICS[name],
                        }
                        if (
                            not classData["superclass"]
                            or classData["superclass"] == "object"
                        ):
                            fmt = CLASS_REDEF_NOSUPERCLASS_FMT
                        else:
                            fmt = CLASS_REDEF_SUPERCLASS_FMT
                        line = (fmt + PYI_RECORD_UPDATED_COMMENT) % classData + '\n'
                    continue

                funcMatch = reFunctionReturn.match(line)
                if not funcMatch:
                    funcMatch = reFunction.match(line)

                if funcMatch:
                    funcIndent = funcMatch.group('indentsize')
                    funcIndentLength = len(funcIndent)
                    if funcIndentLength <= classIndentSize:
                        currentClass = None

                    funcName = funcMatch.group('name')
                    if currentClass:
                        namespacedName = '%s.%s' % (currentClass, funcName)
                    else:
                        namespacedName = funcName

                    # if namespacedName in SKIP_FUNCS or '*.%s' % funcName in SKIP_FUNCS:
                    #     continue

                    if (
                        namespacedName in encounteredFunctionNames
                        or namespacedName in SKIP_FUNCS
                        or '*.%s' % funcName in SKIP_FUNCS
                    ):
                        line = SKIP_LINE_WRITE
                    else:
                        encounteredFunctionNames.add(namespacedName)

                    houFunc = funcs.get(namespacedName)
                    if not houFunc:
                        # Function is not documented, so we won't be able to
                        # determine proper argument names.
                        continue

                    if namespacedName in OVERLOADED_FUNCTIONS:
                        # This function should write down a bunch of overloaded
                        # function defs instead of the one we derived from the
                        # docstring or symbol table.
                        overloadedFuncs = OVERLOAD_FUNCTION_DEFINITIONS[
                            houFunc.className
                        ][houFunc.name]
                        line = ''
                        for overloadedFunc in overloadedFuncs:
                            line += overloadedFunc.formatLine(
                                funcIndentLength, overloaded=True
                            )
                    elif line != SKIP_LINE_WRITE:
                        line = houFunc.formatLine(funcIndentLength)

                classMemberMatch = reClassMember.match(line)
                if classMemberMatch:
                    memberName = classMemberMatch.group('name')
                    if currentClass:
                        namespacedName = '%s.%s' % (currentClass, memberName)
                    else:
                        namespacedName = memberName

                    if namespacedName in encounteredFunctionNames:
                        line = SKIP_LINE_WRITE
                    else:
                        encounteredFunctionNames.add(namespacedName)

            finally:
                # Keep adding to our PYI typing stub after we've processed each line.
                pyiOutput.extend(prependLines)
                if line != SKIP_LINE_WRITE:
                    pyiOutput.append(line)

        # Now write any functions that we found for this
        # class which weren't already defined.  This
        # includes functions we've special-case added.
        for n, func in funcs.items():  # type: HouFunc
            if (
                func.namespacedName in SKIP_FUNCS
                or func.namespacedName in OVERLOADED_FUNCTIONS
                or '*.%s' % func.name in SKIP_FUNCS
            ):
                continue
            if not (func.written or func.className or func.name.startswith('_')):
                pyiOutput.append(func.formatLine(currentIndentSize, addReceipt=True))

    with open(HOUPYI_OUT, 'w') as pyiOutputFile:
        print("Writing %s" % HOUPYI_OUT)
        pyiOutputFile.write(PYI_RECORD_FMT % HFS + "\n")
        for importLine in MODULE_LEVEL_IMPORTS:
            pyiOutputFile.write(importLine + PYI_RECORD_ADDED_COMMENT + "\n")
        pyiOutputFile.write("\nT = TypeVar('T')\n\n")

        pyiOutputFile.writelines(pyiOutput)


if __name__ == "__main__":
    createPYIFile()
    cTypes = extractCTypes()
    hClasses, hFuncs = getHouStructs(cTypes)
    updatePYIFile(hClasses, hFuncs)
    # import pprint
    # pprint.pprint (sorted(hClasses.keys()))
    # print(hFuncs['Vector2.__iter__'].written)
    # print(hClasses['Node'].functions['needsToCook'])

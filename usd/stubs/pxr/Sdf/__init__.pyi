# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Tf
import pxr.Vt
import types
import typing
import typing_extensions
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, overload

AngularUnitDegrees: AngularUnit
AngularUnitRadians: AngularUnit
AuthoringErrorUnrecognizedFields: AuthoringError
AuthoringErrorUnrecognizedSpecType: AuthoringError
DimensionlessUnitDefault: DimensionlessUnit
DimensionlessUnitPercent: DimensionlessUnit
Find: Callable
LengthUnitCentimeter: LengthUnit
LengthUnitDecimeter: LengthUnit
LengthUnitFoot: LengthUnit
LengthUnitInch: LengthUnit
LengthUnitKilometer: LengthUnit
LengthUnitMeter: LengthUnit
LengthUnitMile: LengthUnit
LengthUnitMillimeter: LengthUnit
LengthUnitYard: LengthUnit
ListOpTypeAdded: ListOpType
ListOpTypeAppended: ListOpType
ListOpTypeDeleted: ListOpType
ListOpTypeExplicit: ListOpType
ListOpTypeOrdered: ListOpType
ListOpTypePrepended: ListOpType
PermissionPrivate: Permission
PermissionPublic: Permission
SpecTypeAttribute: SpecType
SpecTypeConnection: SpecType
SpecTypeExpression: SpecType
SpecTypeMapper: SpecType
SpecTypeMapperArg: SpecType
SpecTypePrim: SpecType
SpecTypePseudoRoot: SpecType
SpecTypeRelationship: SpecType
SpecTypeRelationshipTarget: SpecType
SpecTypeUnknown: SpecType
SpecTypeVariant: SpecType
SpecTypeVariantSet: SpecType
SpecifierClass: Specifier
SpecifierDef: Specifier
SpecifierOver: Specifier
VariabilityUniform: Variability
VariabilityVarying: Variability
_PathElemsToPrefixes: Callable
__MFB_FULL_PACKAGE_NAME: str

class AngularUnit(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class AssetPath(Boost.Python.instance):
    """
    Contains an asset path and an optional resolved path.


    Asset paths may contain non-control UTF-8 encoded characters.
    Specifically, U+0000..U+001F (C0 controls), U+007F (delete), and
    U+0080..U+009F (C1 controls) are disallowed. Attempts to construct
    asset paths with such characters will issue a TfError and produce the
    default-constructed empty asset path.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct an empty asset path.
        """
    @overload
    def __init__(self, _path: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Construct an asset path with C{path} and no associated resolved path.


        If the passed C{path} is not valid UTF-8 or contains C0 or C1 control
        characters, raise a TfError and return the default-constructed empty
        asset path.
        """
    @overload
    def __init__(self, _path: str | pxr.Ar.ResolvedPath, _resolvedPath: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Construct an asset path with C{path} and an associated
        C{resolvedPath}.


        If either the passed \\path or C{resolvedPath} are not valid UTF-8 or
        either contain C0 or C1 control characters, raise a TfError and return
        the default-constructed empty asset path.
        """
    @overload
    def __init__(self, arg2: AssetPath | str, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality, including the resolved path.
        """
    def __ge__(self, other: object) -> bool:
        """
        Greater than or equal operator.



        SdfAssetPath::operator<(const SdfAssetPath&)
        """
    def __gt__(self, other: object) -> bool:
        """
        Greater than operator.



        SdfAssetPath::operator<(const SdfAssetPath&)
        """
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool:
        """
        Less than or equal operator.



        SdfAssetPath::operator<(const SdfAssetPath&)
        """
    def __lt__(self, other: object) -> bool:
        """
        Ordering first by asset path, then by resolved path.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def path(self): ...
    @property
    def resolvedPath(self) -> str:
        """
        Return the resolved asset path, if any.


        Note that SdfAssetPath carries a resolved path only if its creator
        passed one to the constructor. SdfAssetPath never performs resolution
        itself.
        """

class AssetPathArray(Boost.Python.instance):
    """An array of type SdfAssetPath."""
    _isVtArray: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, array: typing.Iterable) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, size: int, array: typing.Iterable) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, size: int) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> Any: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...

class AttributeSpec(PropertySpec):
    """
    A subclass of SdfPropertySpec that holds typed data.


    Attributes are typed data containers that can optionally hold any and
    all of the following:
       - A single default value.

       - An array of knot values describing how the value varies over
         time.

       - A dictionary of posed values, indexed by name.
         The values contained in an attribute must all be of the same type. In
         the Python API the C{typeName} property holds the attribute type. In
         the C++ API, you can get the attribute type using the GetTypeName()
         method. In addition, all values, including all knot values, must be
         the same shape. For information on shapes, see the VtShape class
         reference in the C++ documentation.
    """
    ConnectionPathsKey: ClassVar[str] = ...
    DefaultValueKey: ClassVar[str] = ...
    DisplayUnitKey: ClassVar[str] = ...
    allowedTokens: pxr.Vt.TokenArray
    colorSpace: str
    displayUnit: pxr.Tf.Enum
    def __init__(self, owner: PrimSpec, name: str, typeName: ValueTypeName, variability: Variability = ..., custom: bool = ...) -> None:
        """
        Constructs a new prim attribute instance.


        Creates and returns a new attribute for the given prim. The C{owner}
        will own the newly created attribute.
        """
    def ClearColorSpace(self) -> None:
        """
        Clears the colorSpace metadata value set on this attribute.
        """
    def HasColorSpace(self) -> bool:
        """
        Returns true if this attribute has a colorSpace value authored.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def connectionPathList(self) -> ListEditorProxy_SdfPathKeyPolicy:
        """
        Returns a proxy for editing the attribute's connection paths.


        The returned proxy, which is an SdfListEditorProxy, modifies the
        SdfListOp that represents this attribute's connections.
        """
    @property
    def expired(self): ...
    @property
    def roleName(self) -> str:
        """
        Returns the roleName for this attribute's typeName.


        If the typeName has no roleName, return empty token.
        """
    @property
    def typeName(self): ...
    @property
    def valueType(self): ...

class AuthoringError(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class BatchNamespaceEdit(Boost.Python.instance):
    """
    A description of an arbitrarily complex namespace edit.


    A C{SdfBatchNamespaceEdit} object describes zero or more namespace
    edits. Various types providing a namespace will allow the edits to be
    applied in a single operation and also allow testing if this will
    work.

    Clients are encouraged to group several edits into one object because
    that may allow more efficient processing of the edits. If, for
    example, you need to reparent several prims it may be faster to add
    all of the reparents to a single C{SdfBatchNamespaceEdit} and apply
    them at once than to apply each separately.

    Objects that allow applying edits are free to apply the edits in any
    way and any order they see fit but they should guarantee that the
    resulting namespace will be as if each edit was applied one at a time
    in the order they were added.

    Note that the above rule permits skipping edits that have no effect or
    generate a non-final state. For example, if renaming A to B then to C
    we could just rename A to C. This means notices may be elided.
    However, implementations must not elide notices that contain
    information about any edit that clients must be able to know but
    otherwise cannot determine.
    """
    @overload
    def __init__(self) -> None:
        """
        Create an empty sequence of edits.
        """
    @overload
    def __init__(self, arg2: BatchNamespaceEdit, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def Add(self, _edit: NamespaceEdit, /) -> None:
        """
        Add a namespace edit.
        """
    @overload
    def Add(self, _currentPath: Path | str, _newPath: Path | str, _index: int, /) -> None:
        """
        Add a namespace edit.
        """
    @overload
    def Add(self, arg2: Path | str, arg3: Path | str, /) -> None: ...
    def Process(self, hasObjectAtPath: HasObjectAtPath, canEdit: CanEdit, fixBackpointers: bool = ...) -> tuple:
        """
        Validate the edits and generate a possibly more efficient edit
        sequence.


        Edits are treated as if they were performed one at time in sequence,
        therefore each edit occurs in the namespace resulting from all
        previous edits.

        Editing the descendants of the object in each edit is implied. If an
        object is removed then the new path will be empty. If an object is
        removed after being otherwise edited, the other edits will be
        processed and included in C{processedEdits} followed by the removal.
        This allows clients to fixup references to point to the object's final
        location prior to removal.

        This function needs help to determine if edits are allowed. The
        callbacks provide that help. C{hasObjectAtPath} returns C{true} iff
        there's an object at the given path. This path will be in the original
        namespace not any intermediate or final namespace. C{canEdit} returns
        C{true} iff the object at the current path can be namespace edited to
        the new path, ignoring whether an object already exists at the new
        path. Both paths are in the original namespace. If it returns C{false}
        it should set the string to the reason why the edit isn't allowed. It
        should not write either path to the string.

        If C{hasObjectAtPath} is invalid then this assumes objects exist where
        they should and don't exist where they shouldn't. Use this with care.
        If C{canEdit} in invalid then it's assumed all edits are valid.

        If C{fixBackpointers} is C{true} then target/connection paths are
        expected to be in the intermediate namespace resulting from all
        previous edits. If C{false} and any current or new path contains a
        target or connection path that has been edited then this will generate
        an error.

        This method returns C{true} if the edits are allowed and sets
        C{processedEdits} to a new edit sequence at least as efficient as the
        input sequence. If not allowed it returns C{false} and appends reasons
        why not to C{details}.
        """
    @property
    def edits(self) -> list[NamespaceEdit]:
        """
        Returns the edits.
        """

class ChangeBlock(Boost.Python.instance):
    """
    B{DANGER DANGER DANGER}


    Please make sure you have read and fully understand the issues below
    before using a changeblock! They are very easy to use in an unsafe way
    that could make the system crash or corrupt data. If you have any
    questions, please contact the USD team, who would be happy to help!

    SdfChangeBlock provides a way to group a round of related changes to
    scene description in order to process them more efficiently.

    Normally, Sdf sends notification immediately as changes are made so
    that downstream representations like UsdStage can update accordingly.

    However, sometimes it can be advantageous to group a series of Sdf
    changes into a batch so that they can be processed more efficiently,
    with a single round of change processing. An example might be when
    setting many avar values on a model at the same time.

    Opening a changeblock tells Sdf to delay sending notification about
    changes until the outermost changeblock is exited. Until then, Sdf
    internally queues up the notification it needs to send.

    It is *not* safe to use Usd or other downstream API while a
    changeblock is open!! This is because those derived representations
    will not have had a chance to update while the changeblock is open.
    Not only will their view of the world be stale, it could be unsafe to
    even make queries from, since they may be holding onto expired handles
    to Sdf objects that no longer exist. If you need to make a bunch of
    changes to scene description, the best approach is to build a list of
    necessary changes that can be performed directly via the Sdf API, then
    submit those all inside a changeblock without talking to any
    downstream modules. For example, this is how many mutators in Usd
    that operate on more than one field or Spec work.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self, enabled: bool = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate(Boost.Python.instance):
    class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: AttributeSpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_Iterator: ...
    def keys(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: AttributeSpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> AttributeSpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> AttributeSpec: ...
    def __iter__(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec__(Boost.Python.instance):
    class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: AttributeSpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___Iterator: ...
    def keys(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: AttributeSpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> AttributeSpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> AttributeSpec: ...
    def __iter__(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec__(Boost.Python.instance):
    class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: PrimSpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___Iterator: ...
    def keys(self) -> ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: PrimSpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> PrimSpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> PrimSpec: ...
    def __iter__(self) -> ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec__(Boost.Python.instance):
    class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: PropertySpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___Iterator: ...
    def keys(self) -> ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: PropertySpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> PropertySpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> PropertySpec: ...
    def __iter__(self) -> ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate(Boost.Python.instance):
    class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: RelationshipSpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_Iterator: ...
    def keys(self) -> ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: RelationshipSpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> RelationshipSpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> RelationshipSpec: ...
    def __iter__(self) -> ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec__(Boost.Python.instance):
    class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: VariantSpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___Iterator: ...
    def keys(self) -> ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: VariantSpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> VariantSpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> VariantSpec: ...
    def __iter__(self) -> ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec__(Boost.Python.instance):
    class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def index(self, arg2: object, /) -> int: ...
    @overload
    def index(self, arg2: VariantSetSpec, /) -> int: ...
    def items(self) -> ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___Iterator: ...
    def keys(self) -> ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___KeyIterator: ...
    def values(self) -> ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___ValueIterator: ...
    @overload
    def __contains__(self, arg2: object, /) -> bool: ...
    @overload
    def __contains__(self, arg2: VariantSetSpec, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> VariantSetSpec: ...
    @overload
    def __getitem__(self, arg2: int, /) -> VariantSetSpec: ...
    def __iter__(self) -> ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___ValueIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class CleanupEnabler(Boost.Python.instance):
    """
    An RAII class which, when an instance is alive, enables scheduling of
    automatic cleanup of SdfLayers.


    Any affected specs which no longer contribute to the scene will be
    removed when the last SdfCleanupEnabler instance goes out of scope.
    Note that for this purpose, SdfPropertySpecs are removed if they have
    only required fields (see SdfPropertySpecs::HasOnlyRequiredFields),
    but only if the property spec itself was affected by an edit that left
    it with only required fields. This will have the effect of
    uninstantiating on-demand attributes. For example, if its parent prim
    was affected by an edit that left it otherwise inert, it will not be
    removed if it contains an SdfPropertySpec with only required fields,
    but if the property spec itself is edited leaving it with only
    required fields, it will be removed, potentially uninstantiating it if
    it's an on-demand property.

    SdfCleanupEnablers are accessible in both C++ and Python.

    /// SdfCleanupEnabler can be used in the following manner: ::

      {
          SdfCleanupEnabler enabler;
      
          // Perform any action that might otherwise leave inert specs around, 
          // such as removing info from properties or prims, or removing name 
          // children. i.e:
          primSpec->ClearInfo(SdfFieldKeys->Default);
  
          // When enabler goes out of scope on the next line, primSpec will 
          // be removed if it has been left as an empty over.
      }

    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class DimensionlessUnit(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class FileFormat(Boost.Python.instance):
    """
    Base class for file format implementations.
    """

    class Tokens(Boost.Python.instance):
        TargetArg: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def CanRead(self, _file: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{file} can be read by this format.
        """
    @staticmethod
    def FindAllDerivedFileFormatExtensions(_baseType: pxr.Tf.Type, /) -> list[str]:
        """
        Returns a set containing the extension(s) corresponding to all
        registered file formats that derive from C{baseType}.


        C{baseType} must derive from SdfFileFormat.
        """
    @staticmethod
    def FindAllFileFormatExtensions() -> list[str]:
        """
        Returns a set containing the extension(s) corresponding to all
        registered file formats.
        """
    @overload
    @staticmethod
    def FindByExtension(extension: str | pxr.Ar.ResolvedPath, target: str | pxr.Ar.ResolvedPath = ...) -> FileFormat:
        """
        Returns the file format instance that supports the extension for
        C{path}.


        If a format with a matching extension is not found, this returns a
        null file format pointer.

        An extension may be handled by multiple file formats, but each with a
        different target. In such cases, if no C{target} is specified, the
        file format that is registered as the primary plugin will be returned.
        Otherwise, the file format whose target matches C{target} will be
        returned.
        """
    @overload
    @staticmethod
    def FindByExtension(extension: str | pxr.Ar.ResolvedPath, args: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> FileFormat:
        """
        Returns a file format instance that supports the extension for C{path}
        and whose target matches one of those specified by the given C{args}.


        If the C{args} specify no target, then the file format that is
        registered as the primary plugin will be returned. If a format with a
        matching extension is not found, this returns a null file format
        pointer.
        """
    @staticmethod
    def FindById(_formatId: str | pxr.Ar.ResolvedPath, /) -> FileFormat:
        """
        Returns the file format instance with the specified C{formatId}
        identifier.


        If a format with a matching identifier is not found, this returns a
        null file format pointer.
        """
    @staticmethod
    def FormatSupportsEditing(extension: str | pxr.Ar.ResolvedPath, target: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Returns true if the file format for the supplied C{extension} and
        C{target} pair supports editing.


        This method will not load the plugin that provides the specified file
        format. If the extension and target pair is invalid, this method will
        return false.

        FormatSupportsReading

        FormatSupportsWriting
        """
    @staticmethod
    def FormatSupportsReading(extension: str | pxr.Ar.ResolvedPath, target: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Returns true if the file format for the supplied C{extension} and
        C{target} pair supports reading.


        This method will not load the plugin that provides the specified file
        format. If the extension and target pair is invalid, this method will
        return false.

        FormatSupportsWriting

        FormatSupportsEditing
        """
    @staticmethod
    def FormatSupportsWriting(extension: str | pxr.Ar.ResolvedPath, target: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Returns true if the file format for the supplied C{extension} and
        C{target} pair supports writing.


        This method will not load the plugin that provides the specified file
        format. If the extension and target pair is invalid, this method will
        return false.

        FormatSupportsReading

        FormatSupportsEditing
        """
    @staticmethod
    def GetFileExtension(_s: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Returns the file extension for path or file name C{s}, without the
        leading dot character.
        """
    def GetFileExtensions(self) -> list[str]:
        """
        Returns a list of extensions that this format supports.
        """
    def IsPackage(self) -> bool:
        """
        Returns true if this file format is a package containing other assets.
        """
    def IsSupportedExtension(self, _extension: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{extension} matches one of the extensions returned by
        GetFileExtensions.
        """
    def SupportsEditing(self) -> bool:
        """
        This is a convenience method for invoking FormatSupportsEditing with
        this format's extension and target.
        """
    def SupportsReading(self) -> bool:
        """
        Returns true if this file format supports reading.


        This is a convenience method for invoking FormatSupportsReading with
        this format's extension and target
        """
    def SupportsWriting(self) -> bool:
        """
        This is a convenience method for invoking FormatSupportsWriting with
        this format's extension and target.
        """
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...
    @property
    def fileCookie(self) -> str:
        """
        Returns the cookie to be used when writing files with this format.
        """
    @property
    def formatId(self) -> str:
        """
        Returns the format identifier.
        """
    @property
    def primaryFileExtension(self) -> str:
        """
        Returns the primary file extension for this format.


        This is the extension that is reported for layers using this file
        format.
        """
    @property
    def target(self) -> str:
        """
        Returns the target for this file format.
        """

class Int64ListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: Int64ListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> Int64ListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> Int64ListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class IntListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: IntListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> IntListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> IntListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class Layer(Boost.Python.instance):
    '''
    A scene description container that can combine with other such
    containers to form simple component assets, and successively larger
    aggregates.


    The contents of an SdfLayer adhere to the SdfData data model. A layer
    can be ephemeral, or be an asset accessed and serialized through the
    ArAsset and ArResolver interfaces.

    The SdfLayer class provides a consistent API for accesing and
    serializing scene description, using any data store provided by Ar
    plugins. Sdf itself provides a UTF-8 text format for layers identified
    by the".sdf"identifier extension, but via the SdfFileFormat
    abstraction, allows downstream modules and plugins to adapt arbitrary
    data formats to the SdfData/SdfLayer model.

    The FindOrOpen() method returns a new SdfLayer object with scene
    description from any supported asset format. Once read, a layer
    remembers which asset it was read from. The Save() method saves the
    layer back out to the original asset. You can use the Export() method
    to write the layer to a different location. You can use the
    GetIdentifier() method to get the layer\'s Id or GetRealPath() to get
    the resolved, full URI.

    Layer identifiers are UTF-8 encoded strings. A layer\'s file format is
    determined via the identifier\'s extension (as resolved by Ar) with
    [A-Z] (and no other characters) explicitly case folded.

    Layers can have a timeCode range (startTimeCode and endTimeCode). This
    range represents the suggested playback range, but has no impact on
    the extent of the animation data that may be stored in the layer. The
    metadatum"timeCodesPerSecond"is used to annotate how the time ordinate
    for samples contained in the file scales to seconds. For example, if
    timeCodesPerSecond is 24, then a sample at time ordinate 24 should be
    viewed exactly one second after the sample at time ordinate 0.
    '''

    class DetachedLayerRules(Boost.Python.instance):
        '''
        Object used to specify detached layers.


        Layers may be included or excluded from the detached layer set by
        specifying simple substring patterns for layer identifiers. For
        example, the following will include all layers in the detached layer
        set, except for those whose identifiers contain the
        substring"sim"or"geom": ::

          SdfLayer::SetDetachedLayerRules(
              SdfLayer::DetachedLayerRules()
                  .IncludeAll();
                  .Exclude({"sim", "geom"})
          );

        '''
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None:
            """
            A default constructed rules object Excludes all layers from the
            detached layer set.
            """
        def Exclude(self, _patterns: typing.Iterable[str | pxr.Ar.ResolvedPath], /) -> Layer.DetachedLayerRules:
            """
            Exclude layers whose identifiers contain any of the strings in
            C{patterns} from the detached layer set.
            """
        def GetExcluded(self) -> list[str]: ...
        def GetIncluded(self) -> list[str]: ...
        def Include(self, _patterns: typing.Iterable[str | pxr.Ar.ResolvedPath], /) -> Layer.DetachedLayerRules:
            """
            Include layers whose identifiers contain any of the strings in
            C{patterns} in the detached layer set.
            """
        def IncludeAll(self) -> Layer.DetachedLayerRules:
            """
            Include all layers in the detached layer set.
            """
        def IncludedAll(self) -> bool: ...
        def IsIncluded(self, _identifier: str | pxr.Ar.ResolvedPath, /) -> bool:
            """
            Returns true if C{identifier} is included in the detached layer set,
            false otherwise.


            C{identifier} is included if it matches an include pattern (or the
            mask includes all identifiers) and it does not match any of the
            exclude patterns. Anonymous layer identifiers are always excluded from
            the mask.
            """
    ColorConfigurationKey: ClassVar[str] = ...
    ColorManagementSystemKey: ClassVar[str] = ...
    CommentKey: ClassVar[str] = ...
    DocumentationKey: ClassVar[str] = ...
    EndFrameKey: ClassVar[str] = ...
    EndTimeCodeKey: ClassVar[str] = ...
    FramePrecisionKey: ClassVar[str] = ...
    FramesPerSecondKey: ClassVar[str] = ...
    HasOwnedSubLayers: ClassVar[str] = ...
    LayerRelocatesKey: ClassVar[str] = ...
    OwnerKey: ClassVar[str] = ...
    SessionOwnerKey: ClassVar[str] = ...
    StartFrameKey: ClassVar[str] = ...
    StartTimeCodeKey: ClassVar[str] = ...
    TimeCodesPerSecondKey: ClassVar[str] = ...
    colorConfiguration: AssetPath
    colorManagementSystem: str
    comment: str
    customLayerData: dict
    defaultPrim: str
    documentation: str
    endTimeCode: float
    expressionVariables: dict
    framePrecision: int
    framesPerSecond: float
    hasOwnedSubLayers: bool
    identifier: str
    owner: str
    relocates: list[tuple[Path, Path]]
    rootPrimOrder: ListProxy_SdfNameTokenKeyPolicy
    sessionOwner: str
    startTimeCode: float
    subLayerPaths: ListProxy_SdfSubLayerTypePolicy
    timeCodesPerSecond: float
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def AddToMutedLayers(_mutedPath: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Add the specified path to the muted layers set.
        """
    def Apply(self, _unknownArg1: BatchNamespaceEdit, /) -> bool:
        """
        Performs a batch of namespace edits.


        Returns C{true} on success and C{false} on failure. On failure, no
        namespace edits will have occurred.
        """
    def ApplyRootPrimOrder(self, _vec: list[str] | list[pxr.Ar.ResolvedPath], /) -> list:
        """
        Reorders the given list of prim names according to the reorder
        rootPrims statement for this layer.


        This routine employs the standard list editing operations for ordered
        items in a ListEditor.
        """
    def CanApply(self, _unknownArg1: BatchNamespaceEdit, /) -> tuple[NamespaceEditDetail.Result, list[NamespaceEditDetail]]:
        """
        Check if a batch of namespace edits will succeed.


        This returns C{SdfNamespaceEditDetail::Okay} if they will succeed as a
        batch, C{SdfNamespaceEditDetail::Unbatched} if the edits will succeed
        but will be applied unbatched, and C{SdfNamespaceEditDetail::Error} if
        they will not succeed. No edits will be performed in any case.

        If C{details} is not C{None} and the method does not return C{Okay}
        then details about the problems will be appended to C{details}. A
        problem may cause the method to return early, so C{details} may not
        list every problem.

        Note that Sdf does not track backpointers so it's unable to fix up
        targets/connections to namespace edited objects. Clients must fix
        those to prevent them from falling off. In addition, this method will
        report failure if any relational attribute with a target to a
        namespace edited object is subsequently edited (in the same batch).
        Clients should perform edits on relational attributes first.

        Clients may wish to report unbatch details to the user to confirm that
        the edits should be applied unbatched. This will give the user a
        chance to correct any problems that cause batching to fail and try
        again.
        """
    def Clear(self) -> None:
        """
        Clears the layer of all content.


        This restores the layer to a state as if it had just been created with
        CreateNew() . This operation is Undo-able.

        The fileName and whether journaling is enabled are not affected by
        this method.
        """
    def ClearColorConfiguration(self) -> None:
        """
        Clears the color configuration metadata authored in this layer.



        HasColorConfiguration() , SetColorConfiguration()
        """
    def ClearColorManagementSystem(self) -> None:
        """
        Clears the'colorManagementSystem'metadata authored in this layer.



        HascolorManagementSystem(), SetColorManagementSystem()
        """
    def ClearCustomLayerData(self) -> None:
        """
        Clears out the CustomLayerData dictionary associated with this layer.
        """
    def ClearDefaultPrim(self) -> None:
        """
        Clear the default prim metadata for this layer.


        See GetDefaultPrim() and SetDefaultPrim() .
        """
    def ClearEndTimeCode(self) -> None:
        """
        Clear the endTimeCode opinion.
        """
    def ClearExpressionVariables(self) -> None:
        """
        Clears the expression variables dictionary authored on this layer.
        """
    def ClearFramePrecision(self) -> None:
        """
        Clear the framePrecision opinion.
        """
    def ClearFramesPerSecond(self) -> None:
        """
        Clear the framesPerSecond opinion.
        """
    def ClearOwner(self) -> None:
        """
        Clear the owner opinion.
        """
    def ClearRelocates(self) -> None:
        """
        Clears the layer relocates opinion in the layer's metadata.
        """
    def ClearSessionOwner(self) -> None: ...
    def ClearStartTimeCode(self) -> None:
        """
        Clear the startTimeCode opinion.
        """
    def ClearTimeCodesPerSecond(self) -> None:
        """
        Clear the timeCodesPerSecond opinion.
        """
    def ComputeAbsolutePath(self, _assetPath: str | pxr.Ar.ResolvedPath, /) -> str:
        '''
        Returns the path to the asset specified by C{assetPath} using this
        layer to anchor the path if necessary.


        Returns C{assetPath} if it\'s empty or an anonymous layer identifier.

        This method can be used on asset paths that are authored in this layer
        to create new asset paths that can be copied to other layers. These
        new asset paths should refer to the same assets as the original asset
        paths. For example, if the underlying ArResolver is filesystem-based
        and C{assetPath} is a relative filesystem path, this method might
        return the absolute filesystem path using this layer\'s location as the
        anchor.

        The returned path should in general not be assumed to be an absolute
        filesystem path or any other specific form. It is"absolute"in that it
        should resolve to the same asset regardless of what layer it\'s
        authored in.
        '''
    @overload
    @staticmethod
    def CreateAnonymous(tag: str | pxr.Ar.ResolvedPath = ..., args: dict = ...) -> Layer:
        """
        Creates a new *anonymous* layer with an optional C{tag}.


        An anonymous layer is a layer with a system assigned identifier, that
        cannot be saved to disk via Save() . Anonymous layers have an
        identifier, but no real path or other asset information fields.

        Anonymous layers may be tagged, which can be done to aid debugging
        subsystems that make use of anonymous layers. The tag becomes the
        display name of an anonymous layer, and is also included in the
        generated identifier. Untagged anonymous layers have an empty display
        name.

        Additional arguments may be supplied via the C{args} parameter. These
        arguments may control behavior specific to the layer's file format.
        """
    @overload
    @staticmethod
    def CreateAnonymous(tag: str | pxr.Ar.ResolvedPath, format: FileFormat, args: dict = ...) -> Layer:
        """
        Create an anonymous layer with a specific C{format}.
        """
    @staticmethod
    def CreateIdentifier(_layerPath: str | pxr.Ar.ResolvedPath, _arguments: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath], /) -> str:
        """
        Joins the given layer path and arguments into an identifier.
        """
    @staticmethod
    def CreateNew(identifier: str | pxr.Ar.ResolvedPath, args: dict = ...) -> Layer:
        """
        Creates a new empty layer with the given identifier.


        Additional arguments may be supplied via the C{args} parameter. These
        arguments may control behavior specific to the layer's file format.
        """
    @staticmethod
    def DumpLayerInfo() -> None:
        """Debug helper to examine content of the current layer registry and
        the asset/real path of all layers in the registry."""
    def EraseTimeSample(self, _path: Path | str, _time: float, /) -> None: ...
    def Export(self, filename: str | pxr.Ar.ResolvedPath, comment: str | pxr.Ar.ResolvedPath = ..., args: dict = ...) -> bool:
        """
        Exports this layer to a file.


        Returns C{true} if successful, C{false} if an error occurred.

        If C{comment} is not empty, the layer gets exported with the given
        comment. Additional arguments may be supplied via the C{args}
        parameter. These arguments may control behavior specific to the
        exported layer's file format.

        Note that the file name or comment of the original layer is not
        updated. This only saves a copy of the layer to the given filename.
        Subsequent calls to Save() will still save the layer to it's
        previously remembered file name.
        """
    def ExportToString(self) -> str:
        """
        Writes this layer to the given string.


        Returns C{true} if successful and sets C{result}, otherwise returns
        C{false}.
        """
    @staticmethod
    def Find(identifier: str | pxr.Ar.ResolvedPath, args: dict = ...) -> Layer:
        """
        Return an existing layer with the given C{identifier} and C{args}.


        If the layer can't be found, an error is posted and a null layer is
        returned.

        Arguments in C{args} will override any arguments specified in
        C{identifier}.
        """
    @staticmethod
    def FindOrOpen(identifier: str | pxr.Ar.ResolvedPath, args: dict = ...) -> Layer:
        """
        Return an existing layer with the given C{identifier} and C{args}, or
        else load it.


        If the layer can't be found or loaded, an error is posted and a null
        layer is returned.

        Arguments in C{args} will override any arguments specified in
        C{identifier}.
        """
    @staticmethod
    def FindOrOpenRelativeToLayer(anchor: Layer, identifier: str | pxr.Ar.ResolvedPath, args: dict = ...) -> Layer:
        """
        Return an existing layer with the given C{identifier} and C{args}, or
        else load it.


        The given C{identifier} will be resolved relative to the C{anchor}
        layer. If the layer can't be found or loaded, an error is posted and a
        null layer is returned.

        If the C{anchor} layer is invalid, issues a coding error and returns a
        null handle.

        Arguments in C{args} will override any arguments specified in
        C{identifier}.
        """
    @staticmethod
    def FindRelativeToLayer(anchor: Layer, assetPath: str | pxr.Ar.ResolvedPath, args: dict = ...) -> Layer:
        """
        Return an existing layer with the given C{identifier} and C{args}.


        The given C{identifier} will be resolved relative to the C{anchor}
        layer. If the layer can't be found, an error is posted and a null
        layer is returned.

        If the C{anchor} layer is invalid, a coding error is raised, and a
        null handle is returned.

        Arguments in C{args} will override any arguments specified in
        C{identifier}.
        """
    def GetAssetInfo(self) -> Any:
        """
        Returns resolve information from the last time the layer identifier
        was resolved.
        """
    def GetAssetName(self) -> str:
        """
        Returns the asset name associated with this layer.
        """
    def GetAttributeAtPath(self, _path: Path | str, /) -> AttributeSpec:
        """
        Returns an attribute at the given C{path}.


        Returns C{None} if there is no attribute at C{path}. This is simply a
        more specifically typed version of C{GetObjectAtPath()} .
        """
    def GetBracketingTimeSamples(self, _time: float, /) -> tuple: ...
    def GetBracketingTimeSamplesForPath(self, _path: Path | str, _time: float, /) -> tuple: ...
    def GetCompositionAssetDependencies(self) -> list[str]:
        """
        Return paths of all assets this layer depends on due to composition
        fields.


        This includes the paths of all layers referred to by reference,
        payload, and sublayer fields in this layer. This function only returns
        direct composition dependencies of this layer, i.e. it does not
        recurse to find composition dependencies from its dependent layer
        assets.
        """
    @staticmethod
    def GetDetachedLayerRules() -> Layer.DetachedLayerRules:
        """
        Returns the current rules for the detached layer set.
        """
    def GetDisplayName(self) -> str:
        """
        Returns the layer's display name.


        The display name is the base filename of the identifier.
        """
    @staticmethod
    def GetDisplayNameFromIdentifier(_identifier: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Returns the display name for the given C{identifier}, using the same
        rules as GetDisplayName.
        """
    def GetExternalAssetDependencies(self) -> list[str]:
        """
        Returns a set of resolved paths to all external asset dependencies the
        layer needs to generate its contents.


        These are additional asset dependencies that are determined by the
        layer's file format and will be consulted during Reload() when
        determining if the layer needs to be reloaded. This specifically does
        not include dependencies related to composition, i.e. this will not
        include assets from references, payloads, and sublayers.
        """
    def GetExternalReferences(self) -> tuple:
        """
        Deprecated

        Use GetCompositionAssetDependencies instead.
        """
    def GetFileFormat(self) -> FileFormat:
        """
        Returns the file format used by this layer.
        """
    def GetFileFormatArguments(self) -> dict[str, str]:
        """
        Returns the file format-specific arguments used during the
        construction of this layer.
        """
    @staticmethod
    def GetLoadedLayers() -> list[Layer]:
        """
        Returns handles for all layers currently held by the layer registry.
        """
    @staticmethod
    def GetMutedLayers() -> list[str]:
        """
        Returns the set of muted layer paths.
        """
    def GetNumTimeSamplesForPath(self, _path: Path | str, /) -> int: ...
    def GetObjectAtPath(self, _path: Path | str, /) -> Spec:
        """
        Returns the object at the given C{path}.


        There is no distinction between an absolute and relative path at the
        SdLayer level.

        Returns C{None} if there is no object at C{path}.
        """
    def GetPrimAtPath(self, _path: Path | str, /) -> PrimSpec:
        """
        Returns the prim at the given C{path}.


        Returns C{None} if there is no prim at C{path}. This is simply a more
        specifically typed version of C{GetObjectAtPath()} .
        """
    def GetPropertyAtPath(self, _path: Path | str, /) -> PropertySpec:
        """
        Returns a property at the given C{path}.


        Returns C{None} if there is no property at C{path}. This is simply a
        more specifically typed version of C{GetObjectAtPath()} .
        """
    def GetRelationshipAtPath(self, _path: Path | str, /) -> RelationshipSpec:
        """
        Returns a relationship at the given C{path}.


        Returns C{None} if there is no relationship at C{path}. This is simply
        a more specifically typed version of C{GetObjectAtPath()} .
        """
    def HasColorConfiguration(self) -> bool:
        """
        Returns true if color configuration metadata is set in this layer.



        GetColorConfiguration() , SetColorConfiguration()
        """
    def HasColorManagementSystem(self) -> bool:
        """
        Returns true if colorManagementSystem metadata is set in this layer.



        GetColorManagementSystem() , SetColorManagementSystem()
        """
    def HasCustomLayerData(self) -> bool:
        """
        Returns true if CustomLayerData is authored on the layer.
        """
    def HasDefaultPrim(self) -> bool:
        """
        Return true if the default prim metadata is set in this layer.


        See GetDefaultPrim() and SetDefaultPrim() .
        """
    def HasEndTimeCode(self) -> bool:
        """
        Returns true if the layer has an endTimeCode opinion.
        """
    def HasExpressionVariables(self) -> bool:
        """
        Returns true if expression variables are authored on this layer.
        """
    def HasFramePrecision(self) -> bool:
        """
        Returns true if the layer has a frames precision opinion.
        """
    def HasFramesPerSecond(self) -> bool:
        """
        Returns true if the layer has a frames per second opinion.
        """
    def HasOwner(self) -> bool:
        """
        Returns true if the layer has an owner opinion.
        """
    def HasRelocates(self) -> bool:
        """
        Returns true if this layer's metadata has any relocates opinion,
        including that there should be no relocates (i.e.


        an empty list). An empty list (no relocates) does not mean the same
        thing as a missing list (no opinion).
        """
    def HasSessionOwner(self) -> bool:
        """
        Returns true if the layer has a session owner opinion.
        """
    def HasStartTimeCode(self) -> bool:
        """
        Returns true if the layer has a startTimeCode opinion.
        """
    def HasTimeCodesPerSecond(self) -> bool:
        """
        Returns true if the layer has a timeCodesPerSecond opinion.
        """
    def Import(self, _layerPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Imports the content of the given layer path, replacing the content of
        the current layer.


        Note: If the layer path is the same as the current layer's real path,
        no action is taken (and a warning occurs). For this case use Reload()
        .
        """
    def ImportFromString(self, _string: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Reads this layer from the given string.


        Returns C{true} if successful, otherwise returns C{false}.
        """
    @staticmethod
    def IsAnonymousLayerIdentifier(_identifier: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if the C{identifier} is an anonymous layer unique
        identifier.
        """
    def IsDetached(self) -> bool:
        """
        Returns true if this layer is detached from its serialized data store,
        false otherwise.


        Detached layers are isolated from external changes to their serialized
        data.
        """
    @staticmethod
    def IsIncludedByDetachedLayerRules(_identifier: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns whether the given layer identifier is included in the current
        rules for the detached layer set.


        This is equivalent to GetDetachedLayerRules() .IsIncluded(identifier).
        """
    def IsMuted(self) -> bool:
        """
        Returns C{true} if the current layer is muted.
        """
    def ListAllTimeSamples(self) -> list[float]: ...
    def ListTimeSamplesForPath(self, _path: Path | str, /) -> list[float]: ...
    @staticmethod
    def New(fileFormat: FileFormat, identifier: str | pxr.Ar.ResolvedPath, args: dict = ...) -> Layer:
        """
        Creates a new empty layer with the given identifier for a given file
        format class.


        The new layer will not be dirty and will not be saved.

        Additional arguments may be supplied via the C{args} parameter. These
        arguments may control behavior specific to the layer's file format.
        """
    @staticmethod
    def OpenAsAnonymous(filePath: str | pxr.Ar.ResolvedPath = ..., metadataOnly: bool = ..., tag: str | pxr.Ar.ResolvedPath = ...) -> Layer:
        """
        Load the given layer from disk as a new anonymous layer.


        If the layer can't be found or loaded, an error is posted and a null
        layer is returned.

        The anonymous layer does not retain any knowledge of the backing file
        on the filesystem.

        C{metadataOnly} is a flag that asks for only the layer metadata to be
        read in, which can be much faster if that is all that is required.
        Note that this is just a hint: some FileFormat readers may disregard
        this flag and still fully populate the layer contents.

        An optional C{tag} may be specified. See CreateAnonymous for details.
        """
    def QueryTimeSample(self, arg2: Path | str, arg3: float, /) -> Any: ...
    def Reload(self, force: bool = ...) -> bool:
        """
        Reloads the layer from its persistent representation.


        This restores the layer to a state as if it had just been created with
        FindOrOpen() . This operation is Undo-able.

        The fileName and whether journaling is enabled are not affected by
        this method.

        When called with force = false (the default), Reload attempts to avoid
        reloading layers that have not changed on disk. It does so by
        comparing the file's modification time (mtime) to when the file was
        loaded. If the layer has unsaved modifications, this mechanism is not
        used, and the layer is reloaded from disk. If the layer has any
        external asset dependencies their modification state will also be
        consulted when determining if the layer needs to be reloaded.

        Passing true to the C{force} parameter overrides this behavior,
        forcing the layer to be reloaded from disk regardless of whether it
        has changed.
        """
    @staticmethod
    def ReloadLayers(_layers: typing.Iterable[Layer], /, force: bool = ...) -> bool:
        """
        Reloads the specified layers.


        Returns C{false} if one or more layers failed to reload.

        See C{Reload()} for a description of the C{force} flag.
        """
    @staticmethod
    def RemoveFromMutedLayers(_mutedPath: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Remove the specified path from the muted layers set.
        """
    def RemoveInertSceneDescription(self) -> None:
        """
        Removes all scene description in this layer that does not affect the
        scene.


        This method walks the layer namespace hierarchy and removes any prims
        and that are not contributing any opinions.
        """
    def Save(self, force: bool = ...) -> bool:
        """
        Returns C{true} if successful, C{false} if an error occurred.


        Returns C{false} if the layer has no remembered file name or the layer
        type cannot be saved. The layer will not be overwritten if the file
        exists and the layer is not dirty unless C{force} is true.
        """
    def ScheduleRemoveIfInert(self, _spec: Spec, /) -> None:
        """
        Cause C{spec} to be removed if it no longer affects the scene when the
        last change block is closed, or now if there are no change blocks.
        """
    @staticmethod
    def SetDetachedLayerRules(_mask: Layer.DetachedLayerRules, /) -> None:
        '''
        Sets the rules specifying detached layers.


        Newly-created or opened layers whose identifiers are included in
        C{rules} will be opened as detached layers. Existing layers that are
        now included or no longer included will be reloaded. Any unsaved
        modifications to those layers will be lost.

        This function is not thread-safe. It may not be run concurrently with
        any other functions that open, close, or read from any layers.

        The detached layer rules are initially set to exclude all layers. This
        may be overridden by setting the environment variables
        SDF_LAYER_INCLUDE_DETACHED and SDF_LAYER_EXCLUDE_DETACHED to specify
        the initial set of include and exclude patterns in the rules. These
        variables can be set to a comma-delimited list of patterns.
        SDF_LAYER_INCLUDE_DETACHED may also be set to"*"to include all layers.
        Note that these environment variables only set the initial state of
        the detached layer rules; these values may be overwritten by
        subsequent calls to this function.

        See SdfLayer::DetachedLayerRules::IsIncluded for details on how the
        rules are applied to layer identifiers.
        '''
    def SetMuted(self, _muted: bool, /) -> None:
        """
        Mutes the current layer if C{muted} is C{true}, and unmutes it
        otherwise.
        """
    def SetPermissionToEdit(self, _allow: bool, /) -> None:
        """
        Sets permission to edit.
        """
    def SetPermissionToSave(self, _allow: bool, /) -> None:
        """
        Sets permission to save.
        """
    def SetTimeSample(self, arg2: Path | str, arg3: float, arg4: object, /) -> None: ...
    @staticmethod
    def SplitIdentifier(_identifier: str | pxr.Ar.ResolvedPath, /) -> tuple:
        """
        Splits the given layer identifier into its constituent layer path and
        arguments.
        """
    def StreamsData(self) -> bool:
        """
        Returns true if this layer streams data from its serialized data store
        on demand, false otherwise.


        Layers with streaming data are treated differently to avoid pulling in
        data unnecessarily. For example, reloading a streaming layer will not
        perform fine-grained change notification, since doing so would require
        the full contents of the layer to be loaded.
        """
    def TransferContent(self, _layer: Layer, /) -> None:
        """
        Copies the content of the given layer into this layer.


        Source layer is unmodified.
        """
    def Traverse(self, path: Path | str, func: typing.Callable[[Path | str], None]) -> None: ...
    def UpdateAssetInfo(self) -> None:
        """
        Update layer asset information.


        Calling this method re-resolves the layer identifier, which updates
        asset information such as the layer's resolved path and other asset
        info. This may be used to update the layer after external changes to
        the underlying asset system.
        """
    def UpdateCompositionAssetDependency(self, _oldAssetPath: str | pxr.Ar.ResolvedPath, _newAssetPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        '''
        Updates the asset path of a composation dependency in this layer.


        If C{newAssetPath} is supplied, the update works as"rename", updating
        any occurrence of C{oldAssetPath} to C{newAssetPath} in all reference,
        payload, and sublayer fields.

        If C{newAssetPath} is not given, this update behaves as a"delete",
        removing all occurrences of C{oldAssetPath} from all reference,
        payload, and sublayer fields.
        '''
    def UpdateExternalReference(self, _oldAssetPath: str | pxr.Ar.ResolvedPath, _newAssetPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Deprecated

        Use UpdateCompositionAssetDependency instead.
        """
    def _WriteDataFile(self, arg2: object, /) -> bool: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def anonymous(self): ...
    @property
    def dirty(self): ...
    @property
    def empty(self): ...
    @property
    def expired(self): ...
    @property
    def externalReferences(self) -> list[str]:
        """
        Deprecated

        Use GetCompositionAssetDependencies instead.
        """
    @property
    def fileExtension(self) -> str:
        """
        Returns the file extension to use for this layer.


        If this layer was loaded from disk, it should match the extension of
        the file format it was loaded as; if this is an anonymous in-memory
        layer it will be the default extension.
        """
    @property
    def permissionToEdit(self): ...
    @property
    def permissionToSave(self): ...
    @property
    def pseudoRoot(self) -> PrimSpec:
        """
        Returns the layer's pseudo-root prim.


        The layer's root prims are namespace children of the pseudo-root. The
        pseudo-root exists to make the namespace hierarchy a tree instead of a
        forest. This simplifies the implementation of some algorithms.

        A layer always has a pseudo-root prim.
        """
    @property
    def realPath(self) -> str:
        """
        Returns the resolved path for this layer.


        This is equivalent to GetResolvedPath() .GetPathString().
        """
    @property
    def repositoryPath(self) -> str:
        """
        Returns the layer identifier in asset path form.


        In the presence of a properly configured path resolver, the asset path
        is a double-slash prefixed depot path. If the path resolver is not
        configured, the asset path of a layer is empty.
        """
    @property
    def resolvedPath(self) -> pxr.Ar.ResolvedPath:
        """
        Returns the resolved path for this layer.


        This is the path where this layer exists or may exist after a call to
        Save() .
        """
    @property
    def rootPrims(self) -> ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec__:
        """
        Returns a vector of the layer's root prims.
        """
    @property
    def subLayerOffsets(self) -> list[LayerOffset]:
        """
        Returns the layer offsets for all the subLayer paths.
        """
    @property
    def version(self) -> str:
        """
        Returns the asset system version of this layer.


        If a layer is loaded from a location that is not version managed, or a
        configured asset system is not present when the layer is loaded or
        created, the version is empty. By default, asset version tracking is
        disabled; this method returns empty unless asset version tracking is
        enabled.
        """

class LayerOffset(Boost.Python.instance):
    """
    Represents a time offset and scale between layers.


    The SdfLayerOffset class is an affine transform, providing both a
    scale and a translate. It supports vector algebra semantics for
    composing SdfLayerOffsets together via multiplication. The
    SdfLayerOffset class is unitless: it does not refer to seconds or
    frames.

    For example, suppose layer A uses layer B, with an offset of X:  when
    bringing animation from B into A, you first apply the scale of X, and
    then the offset. Suppose you have a scale of 2 and an offset of 24:
    first multiply B's frame numbers by 2, and then add 24. The animation
    from B as seen in A will take twice as long and start 24 frames later.

    Offsets are typically used in either sublayers or prim references. For
    more information, see the SetSubLayerOffset() method of the SdfLayer
    class (the subLayerOffsets property in Python), as well as the
    SetReference() and GetReferenceLayerOffset() methods (the latter is
    the referenceLayerOffset property in Python) of the SdfPrimSpec class.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, offset: float = ..., scale: float = ...) -> None:
        """
        Constructs a new SdfLayerOffset instance.
        """
    @overload
    def __init__(self, arg2: LayerOffset, /) -> None: ...
    def GetInverse(self) -> LayerOffset:
        """
        Gets the inverse offset, which performs the opposite transformation.
        """
    def IsIdentity(self) -> bool:
        """
        Returns C{true} if this is an identity transformation, with an offset
        of 0.0 and a scale of 1.0.
        """
    def __eq__(self, other: object) -> bool:
        """
        Returns whether the offsets are equal.
        """
    @overload
    def __mul__(self, arg2: LayerOffset, /) -> Any: ...
    @overload
    def __mul__(self, arg2: TimeCode | float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def offset(self) -> float:
        """
        Returns the time offset.
        """
    @property
    def scale(self) -> float:
        """
        Returns the time scale factor.
        """

class LayerTree(Boost.Python.instance):
    """
    A SdfLayerTree is an immutable tree structure representing a sublayer
    stack and its recursive structure.


    Layers can have sublayers, which can in turn have sublayers of their
    own. Clients that want to represent that hierarchical structure in
    memory can build a SdfLayerTree for that purpose.

    We use TfRefPtr<SdfLayerTree> as handles to LayerTrees, as a simple
    way to pass them around as immutable trees without worrying about
    lifetime.
    """
    @overload
    def __init__(self, _layer: Layer, _childTrees: list[LayerTree], _cumulativeOffset: LayerOffset, /) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: Layer, arg3: object, /) -> None: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def childTrees(self) -> list[LayerTree]:
        """
        Returns the children of this tree node.
        """
    @property
    def expired(self): ...
    @property
    def layer(self) -> Layer:
        """
        Returns the layer handle this tree node represents.
        """
    @property
    def offset(self) -> LayerOffset:
        """
        Returns the cumulative layer offset from the root of the tree.
        """

class LengthUnit(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class ListEditorProxy_SdfNameKeyPolicy(Boost.Python.instance):
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def Add(self, arg2: object, /) -> None: ...
    def Append(self, arg2: object, /) -> None: ...
    @overload
    def ApplyEditsToList(self, arg2: object, /) -> list: ...
    @overload
    def ApplyEditsToList(self, arg2: object, arg3: object, /) -> list: ...
    def ClearEdits(self) -> bool: ...
    def ClearEditsAndMakeExplicit(self) -> bool: ...
    def ContainsItemEdit(self, item: object, onlyAddOrExplicit: bool = ...) -> bool: ...
    def CopyItems(self, arg2: ListEditorProxy_SdfNameKeyPolicy, /) -> bool: ...
    def Erase(self, arg2: object, /) -> None: ...
    def GetAddedOrExplicitItems(self) -> tuple: ...
    def GetAppliedItems(self) -> tuple: ...
    def ModifyItemEdits(self, arg2: object, /) -> None: ...
    def Prepend(self, arg2: object, /) -> None: ...
    def Remove(self, arg2: object, /) -> None: ...
    def RemoveItemEdits(self, arg2: object, /) -> None: ...
    def ReplaceItemEdits(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def isExpired(self): ...
    @property
    def isExplicit(self): ...
    @property
    def isOrderedOnly(self): ...

class ListEditorProxy_SdfPathKeyPolicy(Boost.Python.instance):
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def Add(self, arg2: Path | str, /) -> None: ...
    def Append(self, arg2: Path | str, /) -> None: ...
    @overload
    def ApplyEditsToList(self, arg2: object, /) -> list: ...
    @overload
    def ApplyEditsToList(self, arg2: object, arg3: object, /) -> list: ...
    def ClearEdits(self) -> bool: ...
    def ClearEditsAndMakeExplicit(self) -> bool: ...
    def ContainsItemEdit(self, item: Path | str, onlyAddOrExplicit: bool = ...) -> bool: ...
    def CopyItems(self, arg2: ListEditorProxy_SdfPathKeyPolicy, /) -> bool: ...
    def Erase(self, arg2: Path | str, /) -> None: ...
    def GetAddedOrExplicitItems(self) -> tuple: ...
    def GetAppliedItems(self) -> tuple: ...
    def ModifyItemEdits(self, arg2: object, /) -> None: ...
    def Prepend(self, arg2: Path | str, /) -> None: ...
    def Remove(self, arg2: Path | str, /) -> None: ...
    def RemoveItemEdits(self, arg2: Path | str, /) -> None: ...
    def ReplaceItemEdits(self, arg2: Path | str, arg3: Path | str, /) -> None: ...
    @property
    def isExpired(self): ...
    @property
    def isExplicit(self): ...
    @property
    def isOrderedOnly(self): ...

class ListEditorProxy_SdfPayloadTypePolicy(Boost.Python.instance):
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def Add(self, arg2: Payload, /) -> None: ...
    def Append(self, arg2: Payload, /) -> None: ...
    @overload
    def ApplyEditsToList(self, arg2: object, /) -> list: ...
    @overload
    def ApplyEditsToList(self, arg2: object, arg3: object, /) -> list: ...
    def ClearEdits(self) -> bool: ...
    def ClearEditsAndMakeExplicit(self) -> bool: ...
    def ContainsItemEdit(self, item: Payload, onlyAddOrExplicit: bool = ...) -> bool: ...
    def CopyItems(self, arg2: ListEditorProxy_SdfPayloadTypePolicy, /) -> bool: ...
    def Erase(self, arg2: Payload, /) -> None: ...
    def GetAddedOrExplicitItems(self) -> tuple: ...
    def GetAppliedItems(self) -> tuple: ...
    def ModifyItemEdits(self, arg2: object, /) -> None: ...
    def Prepend(self, arg2: Payload, /) -> None: ...
    def Remove(self, arg2: Payload, /) -> None: ...
    def RemoveItemEdits(self, arg2: Payload, /) -> None: ...
    def ReplaceItemEdits(self, arg2: Payload, arg3: Payload, /) -> None: ...
    @property
    def isExpired(self): ...
    @property
    def isExplicit(self): ...
    @property
    def isOrderedOnly(self): ...

class ListEditorProxy_SdfReferenceTypePolicy(Boost.Python.instance):
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def Add(self, arg2: Reference, /) -> None: ...
    def Append(self, arg2: Reference, /) -> None: ...
    @overload
    def ApplyEditsToList(self, arg2: object, /) -> list: ...
    @overload
    def ApplyEditsToList(self, arg2: object, arg3: object, /) -> list: ...
    def ClearEdits(self) -> bool: ...
    def ClearEditsAndMakeExplicit(self) -> bool: ...
    def ContainsItemEdit(self, item: Reference, onlyAddOrExplicit: bool = ...) -> bool: ...
    def CopyItems(self, arg2: ListEditorProxy_SdfReferenceTypePolicy, /) -> bool: ...
    def Erase(self, arg2: Reference, /) -> None: ...
    def GetAddedOrExplicitItems(self) -> tuple: ...
    def GetAppliedItems(self) -> tuple: ...
    def ModifyItemEdits(self, arg2: object, /) -> None: ...
    def Prepend(self, arg2: Reference, /) -> None: ...
    def Remove(self, arg2: Reference, /) -> None: ...
    def RemoveItemEdits(self, arg2: Reference, /) -> None: ...
    def ReplaceItemEdits(self, arg2: Reference, arg3: Reference, /) -> None: ...
    @property
    def isExpired(self): ...
    @property
    def isExplicit(self): ...
    @property
    def isOrderedOnly(self): ...

class ListOpType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class ListProxy_SdfNameKeyPolicy(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ApplyEditsToList(self, arg2: object, /) -> Any: ...
    def ApplyList(self, arg2: ListProxy_SdfNameKeyPolicy, /) -> None: ...
    def append(self, arg2: object, /) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> list: ...
    def count(self, arg2: object, /) -> int: ...
    def index(self, arg2: object, /) -> int: ...
    def insert(self, arg2: int, arg3: object, /) -> None: ...
    def remove(self, arg2: object, /) -> None: ...
    def replace(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __delitem__(self, arg2: int, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: int, /) -> str: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class ListProxy_SdfNameTokenKeyPolicy(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ApplyEditsToList(self, arg2: object, /) -> Any: ...
    def ApplyList(self, arg2: ListProxy_SdfNameTokenKeyPolicy, /) -> None: ...
    def append(self, arg2: object, /) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> list: ...
    def count(self, arg2: object, /) -> int: ...
    def index(self, arg2: object, /) -> int: ...
    def insert(self, arg2: int, arg3: object, /) -> None: ...
    def remove(self, arg2: object, /) -> None: ...
    def replace(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __delitem__(self, arg2: int, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class ListProxy_SdfPathKeyPolicy(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ApplyEditsToList(self, arg2: object, /) -> Any: ...
    def ApplyList(self, arg2: ListProxy_SdfPathKeyPolicy, /) -> None: ...
    def append(self, arg2: Path | str, /) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> list: ...
    def count(self, arg2: Path | str, /) -> int: ...
    def index(self, arg2: Path | str, /) -> int: ...
    def insert(self, arg2: int, arg3: Path | str, /) -> None: ...
    def remove(self, arg2: Path | str, /) -> None: ...
    def replace(self, arg2: Path | str, arg3: Path | str, /) -> None: ...
    @overload
    def __delitem__(self, arg2: int, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    @overload
    def __delitem__(self, arg2: Path | str, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Path: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Path | str, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class ListProxy_SdfPayloadTypePolicy(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ApplyEditsToList(self, arg2: object, /) -> Any: ...
    def ApplyList(self, arg2: ListProxy_SdfPayloadTypePolicy, /) -> None: ...
    def append(self, arg2: Payload, /) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> list: ...
    def count(self, arg2: Payload, /) -> int: ...
    def index(self, arg2: Payload, /) -> int: ...
    def insert(self, arg2: int, arg3: Payload, /) -> None: ...
    def remove(self, arg2: Payload, /) -> None: ...
    def replace(self, arg2: Payload, arg3: Payload, /) -> None: ...
    @overload
    def __delitem__(self, arg2: int, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    @overload
    def __delitem__(self, arg2: Payload, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Payload: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Payload, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class ListProxy_SdfReferenceTypePolicy(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ApplyEditsToList(self, arg2: object, /) -> Any: ...
    def ApplyList(self, arg2: ListProxy_SdfReferenceTypePolicy, /) -> None: ...
    def append(self, arg2: Reference, /) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> list: ...
    def count(self, arg2: Reference, /) -> int: ...
    def index(self, arg2: Reference, /) -> int: ...
    def insert(self, arg2: int, arg3: Reference, /) -> None: ...
    def remove(self, arg2: Reference, /) -> None: ...
    def replace(self, arg2: Reference, arg3: Reference, /) -> None: ...
    @overload
    def __delitem__(self, arg2: int, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    @overload
    def __delitem__(self, arg2: Reference, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Reference: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Reference, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class ListProxy_SdfSubLayerTypePolicy(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ApplyEditsToList(self, arg2: object, /) -> Any: ...
    def ApplyList(self, arg2: ListProxy_SdfSubLayerTypePolicy, /) -> None: ...
    def append(self, arg2: object, /) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> list: ...
    def count(self, arg2: object, /) -> int: ...
    def index(self, arg2: object, /) -> int: ...
    def insert(self, arg2: int, arg3: object, /) -> None: ...
    def remove(self, arg2: object, /) -> None: ...
    def replace(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __delitem__(self, arg2: int, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: int, /) -> str: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class MapEditProxy_VtDictionary(Boost.Python.instance):
    class MapEditProxy_VtDictionary_Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class MapEditProxy_VtDictionary_KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class MapEditProxy_VtDictionary_ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def copy(self, arg2: object, /) -> None: ...
    @overload
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def get(self, arg2: object, arg3: object, /) -> Any: ...
    def items(self) -> MapEditProxy_VtDictionary_Iterator: ...
    def keys(self) -> MapEditProxy_VtDictionary_KeyIterator: ...
    def pop(self, arg2: object, /) -> Any: ...
    def popitem(self) -> tuple: ...
    def setdefault(self, arg2: object, arg3: object, /) -> Any: ...
    @overload
    def update(self, arg2: dict, /) -> None: ...
    @overload
    def update(self, arg2: list, /) -> None: ...
    def values(self) -> MapEditProxy_VtDictionary_ValueIterator: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __delitem__(self, arg2: object, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: object, /) -> Any: ...
    def __iter__(self) -> MapEditProxy_VtDictionary_KeyIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath___(Boost.Python.instance):
    class MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def copy(self, arg2: object, /) -> None: ...
    @overload
    def get(self, arg2: Path | str, /) -> Any: ...
    @overload
    def get(self, arg2: Path | str, arg3: Path | str, /) -> Path: ...
    def items(self) -> MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____Iterator: ...
    def keys(self) -> MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____KeyIterator: ...
    def pop(self, arg2: Path | str, /) -> Path: ...
    def popitem(self) -> tuple: ...
    def setdefault(self, arg2: Path | str, arg3: Path | str, /) -> Path: ...
    @overload
    def update(self, arg2: dict, /) -> None: ...
    @overload
    def update(self, arg2: list, /) -> None: ...
    def values(self) -> MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____ValueIterator: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, arg2: Path | str, /) -> bool: ...
    def __delitem__(self, arg2: Path | str, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: Path | str, /) -> Path: ...
    def __iter__(self) -> MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath____KeyIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setitem__(self, arg2: Path | str, arg3: Path | str, /) -> None: ...
    @property
    def expired(self): ...

class MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string___(Boost.Python.instance):
    class MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____KeyIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...

    class MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____ValueIterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def copy(self, arg2: object, /) -> None: ...
    @overload
    def get(self, arg2: object, /) -> Any: ...
    @overload
    def get(self, arg2: object, arg3: object, /) -> str: ...
    def items(self) -> MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____Iterator: ...
    def keys(self) -> MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____KeyIterator: ...
    def pop(self, arg2: object, /) -> str: ...
    def popitem(self) -> tuple: ...
    def setdefault(self, arg2: object, arg3: object, /) -> str: ...
    @overload
    def update(self, arg2: dict, /) -> None: ...
    @overload
    def update(self, arg2: list, /) -> None: ...
    def values(self) -> MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____ValueIterator: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __delitem__(self, arg2: object, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: object, /) -> str: ...
    def __iter__(self) -> MapEditProxy___1_map_string__string____1_less_string_____1_allocator___1_pair_stringconst__string____KeyIterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @property
    def expired(self): ...

class NamespaceEdit(Boost.Python.instance):
    """
    A single namespace edit.


    It supports renaming, reparenting, reparenting with a rename,
    reordering, and removal.
    """
    atEnd: ClassVar[int] = ...  # read-only
    same: ClassVar[int] = ...  # read-only
    currentPath: Incomplete
    index: Incomplete
    newPath: Incomplete
    @overload
    def __init__(self) -> None:
        """
        The default edit maps the empty path to the empty path.
        """
    @overload
    def __init__(self, _currentPath_: Path | str, _newPath_: Path | str, _index_: int = ..., /) -> None:
        """
        The fully general edit.
        """
    @staticmethod
    def Remove(_currentPath: Path | str, /) -> NamespaceEdit:
        """
        Returns a namespace edit that removes the object at C{currentPath}.
        """
    @staticmethod
    def Rename(_currentPath: Path | str, _name: str | pxr.Ar.ResolvedPath, /) -> NamespaceEdit:
        """
        Returns a namespace edit that renames the prim or property at
        C{currentPath} to C{name}.
        """
    @staticmethod
    def Reorder(_currentPath: Path | str, _index: int, /) -> NamespaceEdit:
        """
        Returns a namespace edit to reorder the prim or property at
        C{currentPath} to index C{index}.
        """
    @staticmethod
    def Reparent(_currentPath: Path | str, _newParentPath: Path | str, _index: int, /) -> NamespaceEdit:
        """
        Returns a namespace edit to reparent the prim or property at
        C{currentPath} to be under C{newParentPath} at index C{index}.
        """
    @staticmethod
    def ReparentAndRename(_currentPath: Path | str, _newParentPath: Path | str, _name: str | pxr.Ar.ResolvedPath, _index: int, /) -> NamespaceEdit:
        """
        Returns a namespace edit to reparent the prim or property at
        C{currentPath} to be under C{newParentPath} at index C{index} with the
        name C{name}.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class NamespaceEditDetail(Boost.Python.instance):
    """
    Detailed information about a namespace edit.
    """

    class Result(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    Error: ClassVar[VariableExpression.Result] = ...
    Okay: ClassVar[VariableExpression.Result] = ...
    Unbatched: ClassVar[VariableExpression.Result] = ...
    edit: Incomplete
    reason: Incomplete
    result: Incomplete
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _unknownArg1: VariableExpression.Result, _edit: NamespaceEdit, _reason: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Notice(Boost.Python.instance):
    class Base(pxr.Tf.Notice):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class LayerDidReloadContent(Notice.LayerDidReplaceContent):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class LayerDidReplaceContent(Notice.Base):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class LayerDirtinessChanged(Notice.Base):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class LayerIdentifierDidChange(Notice.Base):
        """
        Sent when the identifier of a layer has changed.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @property
        def newIdentifier(self) -> str:
            """
            Returns the new identifier for the layer.
            """
        @property
        def oldIdentifier(self) -> str:
            """
            Returns the old identifier for the layer.
            """

    class LayerInfoDidChange(Notice.Base):
        """
        Sent when the (scene spec) info of a layer have changed.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def key(self) -> Any: ...

    class LayerMutenessChanged(Notice.Base):
        """
        Sent after a layer has been added or removed from the set of muted
        layers.


        Note this does not necessarily mean the specified layer is currently
        loaded.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @property
        def layerPath(self) -> str:
            """
            Returns the path of the layer that was muted or unmuted.
            """
        @property
        def wasMuted(self): ...

    class LayersDidChange(Notice.Base):
        """
        Global notice sent to indicate that layer contents have changed.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def GetLayers(self) -> list: ...
        def GetSerialNumber(self) -> int: ...

    class LayersDidChangeSentPerLayer(Notice.Base):
        """
        Notice sent per-layer indicating all layers whose contents have
        changed within a single round of change processing.


        If more than one layer changes in a single round of change processing,
        we send this notice once per layer with the same changeVec and
        serialNumber. This is so clients can listen to notices from only the
        set of layers they care about rather than listening to the global
        LayersDidChange notice.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def GetLayers(self) -> list: ...
        def GetSerialNumber(self) -> int: ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class OpaqueValue(Boost.Python.instance):
    """
    In-memory representation of the value of an opaque attribute.


    Opaque attributes cannot have authored values, but every typename in
    Sdf must have a corresponding constructable C++ value type;
    SdfOpaqueValue is the type associated with opaque attributes. Opaque
    values intentionally cannot hold any information, cannot be parsed,
    and cannot be serialized to a layer.

    SdfOpaqueValue is also the type associated with group attributes. A
    group attribute is an opaque attribute that represents a group of
    other properties.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class Path(Boost.Python.instance):
    '''
    A path value used to locate objects in layers or scenegraphs.


    Overview
    ========

    SdfPath is used in several ways:
       - As a storage key for addressing and accessing values held in a
         SdfLayer

       - As a namespace identity for scenegraph objects

       - As a way to refer to other scenegraph objects through relative
         paths
         The paths represented by an SdfPath class may be either relative or
         absolute. Relative paths are relative to the prim object that contains
         them (that is, if an SdfRelationshipSpec target is relative, it is
         relative to the SdfPrimSpec object that owns the SdfRelationshipSpec
         object).

    SdfPath objects can be readily created from and converted back to
    strings, but as SdfPath objects, they have behaviors that make it easy
    and efficient to work with them. The SdfPath class provides a full
    range of methods for manipulating scene paths by appending a namespace
    child, appending a relationship target, getting the parent path, and
    so on. Since the SdfPath class uses a node-based representation
    internally, you should use the editing functions rather than
    converting to and from strings if possible.

    Path Syntax
    ===========

    Like a filesystem path, an SdfPath is conceptually just a sequence of
    path components. Unlike a filesystem path, each component has a type,
    and the type is indicated by the syntax.

    Two separators are used between parts of a path. A slash ("/")
    following an identifier is used to introduce a namespace child. A
    period (".") following an identifier is used to introduce a property.
    A property may also have several non-sequential colons (\':\') in its
    name to provide a rudimentary namespace within properties but may not
    end or begin with a colon.

    A leading slash in the string representation of an SdfPath object
    indicates an absolute path. Two adjacent periods indicate the parent
    namespace.

    Brackets ("["and"]") are used to indicate relationship target paths
    for relational attributes.

    The first part in a path is assumed to be a namespace child unless it
    is preceded by a period. That means:
       - C{/Foo} is an absolute path specifying the root prim Foo.

       - C{/Foo/Bar} is an absolute path specifying namespace child Bar of
         root prim Foo.

       - C{/Foo/Bar.baz} is an absolute path specifying property C{baz} of
         namespace child Bar of root prim Foo.

       - C{Foo} is a relative path specifying namespace child Foo of the
         current prim.

       - C{Foo/Bar} is a relative path specifying namespace child Bar of
         namespace child Foo of the current prim.

       - C{Foo/Bar.baz} is a relative path specifying property C{baz} of
         namespace child Bar of namespace child Foo of the current prim.

       - C{.foo} is a relative path specifying the property C{foo} of the
         current prim.

       - C{/Foo.bar[/Foo.baz].attrib} is a relational attribute path. The
         relationship C{/Foo.bar} has a target C{/Foo.baz}. There is a
         relational attribute C{attrib} on that relationship->target pair.

    A Note on Thread-Safety
    =======================

    SdfPath is strongly thread-safe, in the sense that zero additional
    synchronization is required between threads creating or using SdfPath
    values. Just like TfToken, SdfPath values are immutable. Internally,
    SdfPath uses a global prefix tree to efficiently share representations
    of paths, and provide fast equality/hashing operations, but
    modifications to this table are internally synchronized. Consequently,
    as with TfToken, for best performance it is important to minimize the
    number of values created (since it requires synchronized access to
    this table) or copied (since it requires atomic ref-counting
    operations).
    '''

    class AncestorsRange(Boost.Python.instance):
        class _iterator(Boost.Python.instance):
            def __init__(self, *args, **kwargs) -> None:
                """Raises an exception
                This class cannot be instantiated from Python
                """
            def __next__(self) -> Path: ...
        __instance_size__: ClassVar[int] = ...
        def __init__(self, arg2: Path | str, /) -> None: ...
        def GetPath(self) -> Path: ...
        def __iter__(self) -> _iterator: ...

    class _IsValidPathStringResult(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        def __init__(self, arg2: bool, arg3: object, /) -> None: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __getitem__(self, arg2: int, /) -> Any: ...
        def __ne__(self, other: object) -> bool: ...
        @property
        def errorMessage(self): ...
    absoluteRootPath: ClassVar[Path] = ...  # read-only
    emptyPath: ClassVar[Path] = ...  # read-only
    reflexiveRelativePath: ClassVar[Path] = ...  # read-only
    absoluteIndicator: ClassVar[str] = ...
    childDelimiter: ClassVar[str] = ...
    expressionIndicator: ClassVar[str] = ...
    mapperArgDelimiter: ClassVar[str] = ...
    mapperIndicator: ClassVar[str] = ...
    namespaceDelimiter: ClassVar[str] = ...
    parentPathElement: ClassVar[str] = ...
    propertyDelimiter: ClassVar[str] = ...
    relationshipTargetEnd: ClassVar[str] = ...
    relationshipTargetStart: ClassVar[str] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def __init__(self, arg2: Path | str = ..., /) -> None: ...
    def AppendChild(self, _childName: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Creates a path by appending an element for C{childName} to this path.


        This path must be a prim path, the AbsoluteRootPath or the
        ReflexiveRelativePath.
        """
    def AppendElementString(self, _element: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Creates a path by extracting and appending an element from the given
        ascii element encoding.


        Attempting to append a root or empty path (or malformed path) or
        attempting to append *to* the EmptyPath will raise an error and return
        the EmptyPath.

        May also fail and return EmptyPath if this path's type cannot possess
        a child of the type encoded in C{element}.
        """
    def AppendExpression(self) -> Path:
        """
        Creates a path by appending an expression element.


        This path must be a prim property or relational attribute path.
        """
    def AppendMapper(self, _targetPath: Path | str, /) -> Path:
        """
        Creates a path by appending a mapper element for C{targetPath}.


        This path must be a prim property or relational attribute path.
        """
    def AppendMapperArg(self, _argName: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Creates a path by appending an element for C{argName}.


        This path must be a mapper path.
        """
    def AppendPath(self, _newSuffix: Path | str, /) -> Path:
        """
        Creates a path by appending a given relative path to this path.


        If the newSuffix is a prim path, then this path must be a prim path or
        a root path.

        If the newSuffix is a prim property path, then this path must be a
        prim path or the ReflexiveRelativePath.
        """
    def AppendProperty(self, _propName: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Creates a path by appending an element for C{propName} to this path.


        This path must be a prim path or the ReflexiveRelativePath.
        """
    def AppendRelationalAttribute(self, _attrName: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Creates a path by appending an element for C{attrName} to this path.


        This path must be a target path.
        """
    def AppendTarget(self, _targetPath: Path | str, /) -> Path:
        """
        Creates a path by appending an element for C{targetPath}.


        This path must be a prim property or relational attribute path.
        """
    def AppendVariantSelection(self, _variantSet: str | pxr.Ar.ResolvedPath, _variant: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Creates a path by appending an element for C{variantSet} and
        C{variant} to this path.


        This path must be a prim path.
        """
    def ContainsPrimVariantSelection(self) -> bool:
        """
        Returns whether the path or any of its parent paths identifies a
        variant selection for a prim.
        """
    def ContainsPropertyElements(self) -> bool:
        """
        Return true if this path contains any property elements, false
        otherwise.


        A false return indicates a prim-like path, specifically a root path, a
        prim path, or a prim variant selection path. A true return indicates a
        property-like path: a prim property path, a target path, a relational
        attribute path, etc.
        """
    def ContainsTargetPath(self) -> bool:
        """
        Return true if this path is or has a prefix that's a target path or a
        mapper path.
        """
    @staticmethod
    def FindLongestPrefix(arg2: Path | str, /) -> Any: ...
    @staticmethod
    def FindLongestStrictPrefix(arg2: Path | str, /) -> Any: ...
    @staticmethod
    def FindPrefixedRange(arg2: Path | str, /) -> Any:
        """
        Find the subrange of the sorted range [ *begin*, *end*) that includes
        all paths prefixed by *path*.


        The input range must be ordered according to SdfPath::operator< . If
        your range's iterators'value_types are not SdfPath, but you can obtain
        SdfPaths from them (e.g. map<SdfPath, X>::iterator), you can pass a
        function to extract the path from the dereferenced iterator in
        C{getPath}.
        """
    def GetAbsoluteRootOrPrimPath(self) -> Path:
        """
        Creates a path by stripping all properties and relational attributes
        from this path, leaving the path to the containing prim.


        If the path is already a prim or absolute root path, the same path is
        returned.
        """
    def GetAllTargetPathsRecursively(self) -> list:
        """
        Returns all the relationship target or connection target paths
        contained in this path, and recursively all the target paths contained
        in those target paths in reverse depth-first order.


        For example, given the
        path:'/A/B.a[/C/D.a[/E/F.a]].a[/A/B.a[/C/D.a]]'this method
        produces:'/A/B.a[/C/D.a]','/C/D.a','/C/D.a[/E/F.a]','/E/F.a'
        """
    def GetAncestorsRange(self) -> AncestorsRange:
        """
        Return a range for iterating over the ancestors of this path.


        The range provides iteration over the prefixes of a path, ordered from
        longest to shortest (the opposite of the order of the prefixes
        returned by GetPrefixes).
        """
    def GetCommonPrefix(self, _path: Path | str, /) -> Path:
        """
        Returns a path with maximal length that is a prefix path of both this
        path and C{path}.
        """
    @staticmethod
    def GetConciseRelativePaths(_paths: typing.Iterable[Path | str], /) -> list[Path]:
        """
        Given some vector of paths, get a vector of concise unambiguous
        relative paths.


        GetConciseRelativePaths requires a vector of absolute paths. It finds
        a set of relative paths such that each relative path is unique.
        """
    def GetParentPath(self) -> Path:
        """
        Return the path that identifies this path's namespace parent.


        For a prim path (like'/foo/bar'), return the prim's parent's path
        ('/foo'). For a prim property path (like'/foo/bar.property'), return
        the prim's path ('/foo/bar'). For a target path
        (like'/foo/bar.property[/target]') return the property path
        ('/foo/bar.property'). For a mapper path
        (like'/foo/bar.property.mapper[/target]') return the property path
        ('/foo/bar.property). For a relational attribute path
        (like'/foo/bar.property[/target].relAttr') return the relationship
        target's path ('/foo/bar.property[/target]'). For a prim variant
        selection path (like'/foo/bar{var=sel}') return the prim path
        ('/foo/bar'). For a root prim path (like'/rootPrim'), return
        AbsoluteRootPath() ('/'). For a single element relative prim path
        (like'relativePrim'), return ReflexiveRelativePath() ('.'). For
        ReflexiveRelativePath() , return the relative parent path ('..').

        Note that the parent path of a relative parent path ('..') is a
        relative grandparent path ('../..'). Use caution writing loops that
        walk to parent paths since relative paths have infinitely many
        ancestors. To more safely traverse ancestor paths, consider iterating
        over an SdfPathAncestorsRange instead, as returned by
        GetAncestorsRange() .
        """
    def GetPrefixes(self, numPrefixes: int = ...) -> list[Path]:
        """
        Return up to C{numPrefixes} prefix paths of this path.


        Prefixes are returned in order of shortest to longest. The path itself
        is returned as the last prefix. Note that if the prefix order does not
        need to be from shortest to longest, it is more efficient to use
        GetAncestorsRange, which produces an equivalent set of paths, ordered
        from longest to shortest. If C{numPrefixes} is 0 or greater than the
        number of this path's prefixes, fill all prefixes.
        """
    def GetPrimOrPrimVariantSelectionPath(self) -> Path:
        """
        Creates a path by stripping all relational attributes, targets, and
        properties, leaving the nearest path for which
        *IsPrimOrPrimVariantSelectionPath()* returns true.


        See *GetPrimPath* also.

        If the path is already a prim or a prim variant selection path, the
        same path is returned.
        """
    def GetPrimPath(self) -> Path:
        """
        Creates a path by stripping all relational attributes, targets,
        properties, and variant selections from the leafmost prim path,
        leaving the nearest path for which *IsPrimPath()* returns true.


        See *GetPrimOrPrimVariantSelectionPath* also.

        If the path is already a prim path, the same path is returned.
        """
    def GetVariantSelection(self) -> tuple:
        """
        Returns the variant selection for this path, if this is a variant
        selection path.


        Returns a pair of empty strings if this path is not a variant
        selection path.
        """
    def HasPrefix(self, _prefix: Path | str, /) -> bool:
        """
        Return true if both this path and *prefix* are not the empty path and
        this path has *prefix* as a prefix.


        Return false otherwise.
        """
    def IsAbsolutePath(self) -> bool:
        """
        Returns whether the path is absolute.
        """
    def IsAbsoluteRootOrPrimPath(self) -> bool:
        """
        Returns whether the path identifies a prim or the absolute root.
        """
    def IsAbsoluteRootPath(self) -> bool:
        """
        Return true if this path is the AbsoluteRootPath() .
        """
    def IsExpressionPath(self) -> bool:
        """
        Returns whether the path identifies a connection expression.
        """
    def IsMapperArgPath(self) -> bool:
        """
        Returns whether the path identifies a connection mapper arg.
        """
    def IsMapperPath(self) -> bool:
        """
        Returns whether the path identifies a connection mapper.
        """
    def IsNamespacedPropertyPath(self) -> bool:
        """
        Returns whether the path identifies a namespaced property.


        A namespaced property has colon embedded in its name.
        """
    def IsPrimPath(self) -> bool:
        """
        Returns whether the path identifies a prim.
        """
    def IsPrimPropertyPath(self) -> bool:
        """
        Returns whether the path identifies a prim's property.


        A relational attribute is not a prim property.
        """
    def IsPrimVariantSelectionPath(self) -> bool:
        """
        Returns whether the path identifies a variant selection for a prim.
        """
    def IsPropertyPath(self) -> bool:
        """
        Returns whether the path identifies a property.


        A relational attribute is considered to be a property, so this method
        will return true for relational attributes as well as properties of
        prims.
        """
    def IsRelationalAttributePath(self) -> bool:
        """
        Returns whether the path identifies a relational attribute.


        If this is true, IsPropertyPath() will also be true.
        """
    def IsRootPrimPath(self) -> bool:
        """
        Returns whether the path identifies a root prim.


        the path must be absolute and have a single element (for example
        C{/foo}).
        """
    def IsTargetPath(self) -> bool:
        """
        Returns whether the path identifies a relationship or connection
        target.
        """
    @staticmethod
    def IsValidIdentifier(_name: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns whether C{name} is a legal identifier for any path component.
        """
    @staticmethod
    def IsValidNamespacedIdentifier(_name: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns whether C{name} is a legal namespaced identifier.


        This returns C{true} if IsValidIdentifier() does.
        """
    @staticmethod
    def IsValidPathString(_pathString: str | pxr.Ar.ResolvedPath, /) -> _IsValidPathStringResult:
        """
        Return true if C{pathString} is a valid path string, meaning that
        passing the string to the *SdfPath* constructor will result in a
        valid, non-empty SdfPath.


        Otherwise, return false and if C{errMsg} is not None, set the pointed-
        to string to the parse error.
        """
    @overload
    @staticmethod
    def JoinIdentifier(_lhs: str | pxr.Ar.ResolvedPath, _rhs: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Join C{lhs} and C{rhs} into a single identifier using the namespace
        delimiter.


        Returns C{lhs} if C{rhs} is empty and vice verse. Returns an empty
        string if both C{lhs} and C{rhs} are empty.
        """
    @overload
    @staticmethod
    def JoinIdentifier(arg1: object, /) -> str: ...
    @overload
    def MakeAbsolutePath(self, _anchor: Path | str, /) -> Path:
        """
        Returns the absolute form of this path using C{anchor} as the relative
        basis.


        C{anchor} must be an absolute prim path.

        If this path is a relative path, resolve it using C{anchor} as the
        relative basis.

        If this path is already an absolute path, just return a copy.
        """
    @overload
    def MakeAbsolutePath(self, arg2: Path | str, /) -> Path: ...
    @overload
    def MakeRelativePath(self, _anchor: Path | str, /) -> Path:
        """
        Returns the relative form of this path using C{anchor} as the relative
        basis.


        C{anchor} must be an absolute prim path.

        If this path is an absolute path, return the corresponding relative
        path that is relative to the absolute path given by C{anchor}.

        If this path is a relative path, return the optimal relative path to
        the absolute path given by C{anchor}. (The optimal relative path from
        a given prim path is the relative path with the least leading dot-
        dots.
        """
    @overload
    def MakeRelativePath(self, arg2: Path | str, /) -> Path: ...
    @staticmethod
    def RemoveAncestorPaths(_paths: list[Path] | list[str], /) -> list:
        """
        Remove all elements of *paths* that prefix other elements in *paths*.


        As a side-effect, the result is left in sorted order.
        """
    def RemoveCommonSuffix(self, _otherPath: Path | str, /, stopAtRootPrim: bool = ...) -> tuple:
        """
        Find and remove the longest common suffix from two paths.


        Returns this path and C{otherPath} with the longest common suffix
        removed (first and second, respectively). If the two paths have no
        common suffix then the paths are returned as-is. If the paths are
        equal then this returns empty paths for relative paths and absolute
        roots for absolute paths. The paths need not be the same length.

        If C{stopAtRootPrim} is C{true} then neither returned path will be the
        root path. That, in turn, means that some common suffixes will not be
        removed. For example, if C{stopAtRootPrim} is C{true} then the paths
        /A/B and /B will be returned as is. Were it C{false} then the result
        would be /A and /. Similarly paths /A/B/C and /B/C would return /A/B
        and /B if C{stopAtRootPrim} is C{true} but /A and / if it's C{false}.
        """
    @staticmethod
    def RemoveDescendentPaths(_paths: list[Path] | list[str], /) -> list:
        """
        Remove all elements of *paths* that are prefixed by other elements in
        *paths*.


        As a side-effect, the result is left in sorted order.
        """
    def ReplaceName(self, _newName: str | pxr.Ar.ResolvedPath, /) -> Path:
        """
        Return a copy of this path with its final component changed to
        *newName*.


        This path must be a prim or property path.

        This method is shorthand for path.GetParentPath().AppendChild(newName)
        for prim paths, path.GetParentPath().AppendProperty(newName) for prim
        property paths, and
        path.GetParentPath().AppendRelationalAttribute(newName) for relational
        attribute paths.

        Note that only the final path component is ever changed. If the name
        of the final path component appears elsewhere in the path, it will not
        be modified.

        Some examples:

        ReplaceName('/chars/MeridaGroup','AngusGroup')
        ->'/chars/AngusGroup'ReplaceName('/Merida.tx','ty')
        ->'/Merida.ty'ReplaceName('/Merida.tx[targ].tx','ty')
        ->'/Merida.tx[targ].ty'
        """
    def ReplacePrefix(self, oldPrefix: Path | str, newPrefix: Path | str, fixTargetPaths: bool = ...) -> Path:
        """
        Returns a path with all occurrences of the prefix path C{oldPrefix}
        replaced with the prefix path C{newPrefix}.


        If fixTargetPaths is true, any embedded target paths will also have
        their paths replaced. This is the default.

        If this is not a target, relational attribute or mapper path this will
        do zero or one path prefix replacements, if not the number of
        replacements can be greater than one.
        """
    def ReplaceTargetPath(self, _newTargetPath: Path | str, /) -> Path:
        """
        Replaces the relational attribute's target path.


        The path must be a relational attribute path.
        """
    def StripAllVariantSelections(self) -> Path:
        """
        Create a path by stripping all variant selections from all components
        of this path, leaving a path with no embedded variant selections.
        """
    @staticmethod
    def StripNamespace(_name: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Returns C{name} stripped of any namespaces.


        This does not check the validity of the name; it just attempts to
        remove anything that looks like a namespace.
        """
    @staticmethod
    def StripPrefixNamespace(_name: str | pxr.Ar.ResolvedPath, _matchNamespace: str | pxr.Ar.ResolvedPath, /) -> tuple:
        """
        Returns ( C{name}, C{true}) where C{name} is stripped of the prefix
        specified by C{matchNamespace} if C{name} indeed starts with
        C{matchNamespace}.


        Returns ( C{name}, C{false}) otherwise, with C{name} unmodified.

        This function deals with both the case where C{matchNamespace}
        contains the trailing namespace delimiter':'or not.
        """
    @staticmethod
    def TokenizeIdentifier(_name: str | pxr.Ar.ResolvedPath, /) -> list[str]:
        """
        Tokenizes C{name} by the namespace delimiter.


        Returns the empty vector if C{name} is not a valid namespaced
        identifier.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality operator.
        """
    def __ge__(self, other: object) -> bool:
        """
        Greater than or equal operator.



        SdfPath::operator<(const SdfPath&)
        """
    def __gt__(self, other: object) -> bool:
        """
        Greater than operator.



        SdfPath::operator<(const SdfPath&)
        """
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool:
        """
        Less than or equal operator.



        SdfPath::operator<(const SdfPath&)
        """
    def __lt__(self, other: object) -> bool:
        """
        Comparison operator.


        This orders paths lexicographically, aka dictionary-style.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def elementString(self) -> str:
        '''
        Returns an ascii representation of the"terminal"element of this path,
        which can be used to reconstruct the path using
        C{AppendElementString()} on its parent.


        EmptyPath() , AbsoluteRootPath() , and ReflexiveRelativePath() are
        *not* considered elements (one of the defining properties of elements
        is that they have a parent), so C{GetElementString()} will return the
        empty string for these paths.

        Unlike C{GetName()} and C{GetTargetPath()} , which provide
        you"some"information about the terminal element, this provides a
        complete representation of the element, for all element types.

        Also note that whereas C{GetName()} , C{GetNameToken()} , C{GetText()}
        , C{GetString()} , and C{GetTargetPath()} return cached results,
        C{GetElementString()} always performs some amount of string
        manipulation, which you should keep in mind if performance is a
        concern.
        '''
    @property
    def isEmpty(self) -> bool:
        """
        Returns true if this is the empty path ( SdfPath::EmptyPath() ).
        """
    @property
    def name(self) -> str:
        '''
        Returns the name of the prim, property or relational attribute
        identified by the path.


        Returns EmptyPath if this path is a target or mapper path.

           - Returns""for EmptyPath.

           - Returns"."for ReflexiveRelativePath.

           - Returns".."for a path ending in ParentPathElement.

        '''
    @property
    def pathElementCount(self) -> int:
        """
        Returns the number of path elements in this path.
        """
    @property
    def pathString(self): ...
    @property
    def targetPath(self) -> Path:
        '''
        Returns the relational attribute or mapper target path for this path.


        Returns EmptyPath if this is not a target, relational attribute or
        mapper path.

        Note that it is possible for a path to have multiple"target"paths. For
        example a path that identifies a connection target for a relational
        attribute includes the target of the connection as well as the target
        of the relational attribute. In these cases, the"deepest"or right-most
        target path will be returned (the connection target in this example).
        '''

class PathArray(Boost.Python.instance):
    """An array of type SdfPath."""
    _isVtArray: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, array: typing.Iterable) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, size: int, array: typing.Iterable) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, size: int) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> Any: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...

class PathExpression(Boost.Python.instance):
    '''
    Objects of this class represent a logical expression syntax tree
    consisting of SdfPath matching patterns (with optionally embedded
    predicate expressions) joined by the set-algebraic operators C{+}
    (union), C{&} (intersection), C{-} (difference), C{~} (complement) and
    an implied-union operator represented by two subexpressions joined by
    whitespace.


    An SdfPathExpression can be constructed from a string, which will
    parse the string into an expression object. The syntax for an
    expression is as follows:

    The fundamental building blocks are path patterns and expression
    references. A path pattern is similar to an SdfPath, but it may
    contain glob-style wild-card characters, embedded brace-enclosed
    predicate expressions (see SdfPredicateExpression) and C{//} elements
    indicating arbitrary levels of prim hierarchy. For example, consider
    C{/foo//bar*  /baz{active:false}} . This pattern matches absolute
    paths whose first component is C{foo}, that also have some descendant
    prim whose name begins with C{bar}, which in turn has a child named
    C{baz} where the predicate C{active:false} evaluates to true.

    An expression reference starts with C{%} followed by a prim path, a
    C{:} , and a name. There is also one"special"expression reference,
    C{_} which means"the weaker"expression when composing expressions
    together. See ComposeOver() and ResolveReferences() for more
    information.

    These building blocks may be joined as mentioned above, with C{+} ,
    C{-} , C{&} , or whitespace, and may be complemented with C{~} , and
    grouped with C{(} and C{)} .
    '''

    class ExpressionReference(Boost.Python.instance):
        """
        Objects of this class represent references to other path expressions,
        which will be resolved later by a call to ResolveReferences() or
        ComposeOver() .
        """
        __instance_size__: ClassVar[int] = ...
        name: Incomplete
        path: Incomplete
        def __init__(self) -> None: ...
        @staticmethod
        def Weaker() -> PathExpression.ExpressionReference:
            '''
            Return the special"weaker"reference, whose syntax in an
            SdfPathExpression is"%_".


            An ExpressionReference represents this as the empty C{path}, and the
            name"_".
            '''
        def __eq__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...

    class Op(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class PathPattern(Boost.Python.instance):
        """
        Objects of this class represent SdfPath matching patterns, consisting
        of an SdfPath prefix followed by a sequence of components, which may
        contain wildcards and optional embedded predicate expressions (see
        SdfPredicateExpression).
        """
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None:
            """
            Construct the empty pattern whose bool-conversion operator returns
            false.
            """
        def AppendChild(self, text: str | pxr.Ar.ResolvedPath, predExpr: PredicateExpression = ...) -> None:
            """
            Append a prim child component to this pattern, with optional predicate
            expression C{predExpr}.


            If this pattern does not yet contain any wildcards or components with
            predicate expressions, and the input text does not contain wildcards,
            and C{predExpr} is empty, then append a child component to this
            pattern's prefix path (see GetPrefix() ). Otherwise append this
            component to the sequence of components.
            """
        def AppendProperty(self, text: str | pxr.Ar.ResolvedPath, predExpr: PredicateExpression = ...) -> None:
            """
            Append a prim property component to this pattern, with optional
            predicate expression C{predExpr}.


            If this pattern does not yet contain any wildcards or components with
            predicate expressions, and the input text does not contain wildcards,
            and C{predExpr} is empty, then append a property component to this
            pattern's prefix path (see GetPrefix() ). Otherwise append this
            component to the sequence of components.
            """
        def GetPrefix(self) -> Path:
            """
            Return this pattern's non-speculative prefix (leading path components
            with no wildcards and no predicates).
            """
        def GetText(self) -> str:
            """
            Return the string representation of this pattern.
            """
        def SetPrefix(self, prefix: Path | str) -> None:
            """
            Set this pattern's non-speculative prefix (leading path components
            with no wildcards and no predicates).
            """
        def __bool__(self) -> bool:
            """
            Return true if this pattern is not empty, false if it is.
            """
        def __eq__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
    Complement: ClassVar[PathExpression.Op] = ...
    Difference: ClassVar[PathExpression.Op] = ...
    ExpressionRef: ClassVar[PathExpression.Op] = ...
    ImpliedUnion: ClassVar[PathExpression.Op] = ...
    Intersection: ClassVar[PathExpression.Op] = ...
    Pattern: ClassVar[PathExpression.Op] = ...
    Union: ClassVar[PathExpression.Op] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        '''
        Default construction produces the"empty"expression.


        Conversion to bool returns\'false\'. The empty expression matches
        nothing.
        '''
    @overload
    def __init__(self, patternString: str | pxr.Ar.ResolvedPath, parseContext: str | pxr.Ar.ResolvedPath = ...) -> None:
        """
        Construct an expression by parsing C{expr}.


        If provided, C{parseContext} appears in a parse error, if one is
        generated. See GetParseError() . See the class documentation for
        details on expression syntax.
        """
    @overload
    def __init__(self, arg2: PathExpression, /) -> None: ...
    def ComposeOver(self, weaker: PathExpression) -> PathExpression:
        '''
        Return a new expression created by replacing references to
        the"weakerexpression"(i.e."%_") in this expression with C{weaker}.


        This is a restricted form of ResolveReferences() that only
        resolves"weaker"references, replacing them by C{weaker}, leaving other
        references unmodified. As a special case, if this expression IsEmpty()
        , return C{weaker}.
        '''
    def ContainsExpressionReferences(self) -> bool:
        """
        Return true if this expression contains any references to other
        collections.
        """
    def ContainsWeakerExpressionReference(self) -> bool:
        '''
        Return true if this expression contains one or more"weaker"expression
        references, expressed as\'_\'in the expression language.


        Return false otherwise.
        '''
    @staticmethod
    def Everything() -> PathExpression:
        '''
        Return the expression"//"which matches all paths.
        '''
    def GetText(self) -> str:
        """
        Return a text representation of this expression that parses to the
        same expression.
        """
    def IsAbsolute(self) -> bool:
        """
        Return true if all contained pattern prefixes are absolute, false
        otherwise.


        Call MakeAbsolute() to anchor any relative paths and make them
        absolute.
        """
    def IsComplete(self) -> bool:
        '''
        Return true if this expression is considered"complete".


        Here, complete means that the expression has all absolute paths, and
        contains no expression references. This is equivalent to: ::

          !expr.ContainsExpressionReferences() && expr.IsAbsolute()

        To complete an expression, call MakeAbsolute() , ResolveReferences()
        and/or ComposeOver() .
        '''
    def IsEmpty(self) -> bool:
        """
        Return true if this is the empty expression; i.e.


        default-constructed or constructed from a string with invalid syntax.
        """
    def MakeAbsolute(self, anchor: Path | str) -> PathExpression:
        """
        Return a new expression created by making any relative path prefixes
        in this expression absolute by SdfPath::MakeAbsolutePath() .
        """
    @overload
    @staticmethod
    def MakeAtom(ref: PathExpression.ExpressionReference) -> PathExpression:
        """
        Produce a new expression containing only the reference C{ref}.
        """
    @overload
    @staticmethod
    def MakeAtom(pattern: PathExpression.PathPattern) -> PathExpression:
        """
        Produce a new expression containing only the pattern C{pattern}.
        """
    @staticmethod
    def MakeComplement(right: PathExpression) -> PathExpression:
        """
        Produce a new expression representing the set-complement of C{right}.
        """
    @staticmethod
    def MakeOp(op: PathExpression.Op, left: PathExpression, right: PathExpression) -> PathExpression:
        """
        Produce a new expression representing the set-algebraic operation
        C{op} with operands C{left} and C{right}.


        The C{op} must be one of ImpliedUnion, Union, Intersection, or
        Difference.
        """
    @staticmethod
    def Nothing() -> PathExpression:
        """
        Return the empty expression which matches no paths.


        This is the same as a default-constructed SdfPathExpression.
        """
    def ReplacePrefix(self, oldPrefix: Path | str, newPrefix: Path | str) -> PathExpression:
        """
        Return a new expression created by replacing literal path prefixes
        that start with C{oldPrefix} with C{newPrefix}.
        """
    def ResolveReferences(self, resolve: typing.Callable) -> PathExpression:
        '''
        Return a new expression created by resolving collection references in
        this expression.


        This function calls C{resolve} to produce a subexpression from a"%"
        ExpressionReference. To leave an expression reference unchanged,
        return an expression containing the passed argument by calling
        MakeAtom() .
        '''
    def Walk(self, logic: typing.Callable, ref: typing.Callable, pattern: typing.Callable) -> None:
        '''
        Walk this expression\'s syntax tree in depth-first order, calling
        C{pattern} with the current PathPattern when one is encountered,
        C{ref} with the current ExpressionReference when one is encountered,
        and C{logic} multiple times for each logical operation encountered.


        When calling C{logic}, the logical operation is passed as the C{Op}
        parameter, and an integer indicating"where"we are in the set of
        operands is passed as the int parameter. For a Complement, call
        C{logic} (Op=Complement, int=0) to start, then after the subexpression
        that the Complement applies to is walked, call C{logic}
        (Op=Complement, int=1). For the other operators like Union and
        Intersection, call C{logic(Op, 0)} before the first argument, then
        C{logic(Op, 1)} after the first subexpression, then C{logic(Op, 2)}
        after the second subexpression. For a concrete example, consider the
        following expression:

        /foo/bar// /foo/baz//&~/foo/bar/qux// _

        logic(Intersection, 0) logic(ImpliedUnion, 0) pattern(/foo/bar//)
        logic(ImpliedUnion, 1) pattern(/foo/baz//) logic(ImpliedUnion, 2)
        logic(Intersection, 1) logic(ImpliedUnion, 0) logic(Complement, 0)
        pattern(/foo/bar/qux//) logic(Complement, 1) logic(ImpliedUnion, 1)
        ref(_) logic(ImpliedUnion, 2) logic(Intersection, 2)
        '''
    @staticmethod
    def WeakerRef() -> PathExpression:
        '''
        Return the expression"%_", consisting solely of a reference to
        the"weaker"path expression, to be resolved by ComposeOver() or
        ResolveReferences()
        '''
    def __bool__(self) -> bool:
        """
        Return true if this expression contains any operations, false
        otherwise.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class PathListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: PathListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> PathListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> PathListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: Path | str, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class Payload(Boost.Python.instance):
    """
    Represents a payload and all its meta data.


    A payload represents a prim reference to an external layer. A payload
    is similar to a prim reference (see SdfReference) with the major
    difference that payloads are explicitly loaded by the user.

    Unloaded payloads represent a boundary that lazy composition and
    system behaviors will not traverse across, providing a user-visible
    way to manage the working set of the scene.
    """
    __instance_size__: ClassVar[int] = ...
    assetPath: str
    layerOffset: LayerOffset
    primPath: Path
    @overload
    def __init__(self, assetPath: str | pxr.Ar.ResolvedPath = ..., primPath: Path | str = ..., layerOffset: LayerOffset = ...) -> None:
        """
        Create a payload.


        See SdfAssetPath for what characters are valid in C{assetPath}. If
        C{assetPath} contains invalid characters, issue an error and set this
        payload's asset path to the empty asset path.
        """
    @overload
    def __init__(self, arg2: Payload, /) -> None: ...
    def __eq__(self, other: object) -> bool:
        """
        Returns whether this payload equals *rhs*.
        """
    def __ge__(self, other: object) -> bool:
        """

        SdfPayload::operator<
        """
    def __gt__(self, other: object) -> bool:
        """

        SdfPayload::operator<
        """
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool:
        """

        SdfPayload::operator<
        """
    def __lt__(self, other: object) -> bool:
        """
        Returns whether this payload is less than *rhs*.


        The meaning of less than is arbitrary but stable.
        """
    def __ne__(self, other: object) -> bool: ...

class PayloadListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: PayloadListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> PayloadListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> PayloadListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: Payload, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class Permission(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class PredicateExpression(Boost.Python.instance):
    '''
    Represents a logical expression syntax tree consisting of predicate
    function calls joined by the logical operators\'and\',\'or\',\'not\', and an
    implied-and operator that represents two subexpressions joined by only
    whitespace.


    An SdfPredicateExpression can be constructed with a string, which will
    parse an expression. The syntax for an expression is as follows:

    The fundamental building blocks are calls to predicate functions.
    There are three syntaxes for function calls.

       - Bare call: just a function name: C{isDefined}

       - Colon call: name, colon, positional arguments: C{isa:mammal,bird}

       - Paren call: name and parenthesized positional and keyword args:
         C{isClose(1.23, tolerance=0.01)}
         Colon call arguments are all positional and must be separated by
         commas with no spaces between arguments. In paren calls, positional
         arguments must precede keyword arguments, and whitespace is allowed
         between arguments.

    The string parser supports argument values of the following types:
    double-quoted"strings", unquoted strings, integers, floating-point
    numbers, and boolean values\'true\'and\'false\'.

    The unary operator\'not\'may appear preceding a function call, or a
    subexpresion enclosed in parentheses. The binary
    operators\'and\'and\'or\'may appear between subexpressions. If
    subexpressions appear adjacent to each other (other than possible
    whitespace), this is considered an implied\'and\'operator.

    Operator precedence in order from highest to lowest is:\'not\',<implied-
    and>,\'and\',\'or\'.

    Here are some examples of valid predicate expression syntax:

       - C{foo} (call"foo"with no arguments)

       - C{foo bar} (implicit\'and\'of"foo"and"bar")

       - C{foo not bar} (implicit\'and\'of"foo"and"not bar")

       - C{color:red (shiny or matte)}

       - C{animal or mineral or vegetable}

       - C{(mammal or bird) and (tame or small)}

       - C{isClose(100, tolerance=3.0) or negative}

    '''

    class FnArg(Boost.Python.instance):
        """
        Represents a function argument name and value.


        Positional arguments have empty names.
        """
        __instance_size__: ClassVar[int] = ...
        argName: Incomplete
        value: Incomplete
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg2: PredicateExpression.FnArg, /) -> None: ...
        @staticmethod
        def Keyword(name: str | pxr.Ar.ResolvedPath, value: Any) -> PredicateExpression.FnArg: ...
        @staticmethod
        def Positional(value: Any) -> PredicateExpression.FnArg: ...
        def __eq__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...

    class FnCall(Boost.Python.instance):
        """
        Represents a function call in an expression with calling style,
        function name, and arguments.
        """

        class Kind(pxr.Tf.Tf_PyEnumWrapper):
            _baseName: ClassVar[str] = ...
            allValues: ClassVar[tuple] = ...
            def __init__(self, *args, **kwargs) -> None:
                """Raises an exception
                This class cannot be instantiated from Python
                """
            @staticmethod
            def GetValueFromName(name: object) -> Any: ...
        BareCall: ClassVar[PredicateExpression.FnCall.Kind] = ...
        ColonCall: ClassVar[PredicateExpression.FnCall.Kind] = ...
        ParenCall: ClassVar[PredicateExpression.FnCall.Kind] = ...
        __instance_size__: ClassVar[int] = ...
        args: Incomplete
        funcName: Incomplete
        kind: Incomplete
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg2: PredicateExpression.FnCall, /) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...

    class Op(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class _PredicateExpressionFnArgVector(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None: ...
        def append(self, arg2: object, /) -> None: ...
        def extend(self, arg2: object, /) -> None: ...
        def __contains__(self, arg2: object, /) -> bool: ...
        def __delitem__(self, arg2: object, /) -> None: ...
        def __getitem__(self, arg2: object, /) -> Any: ...
        def __iter__(self) -> Any: ...
        def __len__(self) -> int: ...
        def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    And: ClassVar[PathExpression.Op] = ...
    Call: ClassVar[PathExpression.Op] = ...
    ImpliedAnd: ClassVar[PathExpression.Op] = ...
    Not: ClassVar[PathExpression.Op] = ...
    Or: ClassVar[PathExpression.Op] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct the empty expression whose bool-operator returns false.
        """
    @overload
    def __init__(self, _unknownArg1: PredicateExpression, /) -> None:
        """
        Copy construct from another expression.
        """
    @overload
    def __init__(self, exprString: str | pxr.Ar.ResolvedPath, context: str | pxr.Ar.ResolvedPath = ...) -> None:
        """
        Construct an expression by parsing C{expr}.


        If provided, C{context} appears in a parse error, if one is generated.
        See GetParseError() . See the class documentation for details on
        expression syntax.
        """
    def GetParseError(self) -> str:
        """
        Return parsing errors as a string if this function was constructed
        from a string and parse errors were encountered.
        """
    def GetText(self) -> str:
        """
        Return a text representation of this expression that parses to the
        same expression.
        """
    def IsEmpty(self) -> bool:
        """
        Return true if this is the empty expression; i.e.


        default-constructed or constructed from a string with invalid syntax.
        """
    @staticmethod
    def MakeCall(call: PredicateExpression.FnCall) -> PredicateExpression:
        """
        Produce a new expression containing just a the function call C{call}.
        """
    @staticmethod
    def MakeNot(right: PredicateExpression) -> PredicateExpression:
        """
        Produce a new expression by prepending the'not'operator onto C{right}.
        """
    @staticmethod
    def MakeOp(op: PathExpression.Op, left: PredicateExpression, right: PredicateExpression) -> PredicateExpression:
        """
        Produce a new expression by combining C{left} and C{right} with the
        operator C{op}.


        The C{op} must be one of ImpliedAnd, And, or Or.
        """
    def Walk(self, logic: typing.Callable, call: typing.Callable) -> None:
        '''
        Walk this expression\'s syntax tree in depth-first order, calling
        C{call} with the current function call when a function call is
        encountered, and calling C{logic} multiple times for each logical
        operation encountered.


        When calling C{logic}, the logical operation is passed as the C{Op}
        parameter, and an integer indicating"where"we are in the set of
        operands is passed as the int parameter. For a\'not\', call C{logic}
        (Op=Not, int=0) to start, then after the subexpression that
        the\'not\'applies to is walked, call C{logic} (Op=Not, int=1). For the
        binary operators like\'and\'and\'or\', call C{logic(Op, 0)} before the
        first argument, then C{logic(Op, 1)} after the first subexpression,
        then C{logic(Op, 2)} after the second subexpression. For a concrete
        example, consider the following expression: (foo or bar) and not baz
        The sequence of calls from Walk() will be: logic(And, 0)logic(Or,
        0)call("foo")logic(Or, 1)call("bar")logic(Or, 2)logic(And,
        1)logic(Not, 0)call("baz")logic(Not, 1)logic(And, 2)
        '''
    def __bool__(self) -> bool:
        """
        Return true if this expression contains any operations, false
        otherwise.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class PredicateFunctionResult(Boost.Python.instance):
    '''
    Represents the result of a predicate function: a pair of the boolean
    result and a Constancy token indicating whether the function result is
    constant over"descendant"objects, or that it might vary
    over"descendant"objects.
    '''

    class Constancy(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ConstantOverDescendants: ClassVar[PredicateFunctionResult.Constancy] = ...
    MayVaryOverDescendants: ClassVar[PredicateFunctionResult.Constancy] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Default construction produces a'false'result
        that'MayVaryOverDescendants'.
        """
    @overload
    def __init__(self, _value: PredicateFunctionResult, /) -> None:
        """
        Construct with C{value} and C{MayVaryOverDescendants} constancy.
        """
    @overload
    def __init__(self, value: bool, constancy: PredicateFunctionResult.Constancy = ...) -> None:
        """
        Construct with C{value} and C{constancy}.
        """
    def GetConstancy(self) -> PredicateFunctionResult.Constancy:
        """
        Return the result constancy.
        """
    def GetValue(self) -> bool:
        """
        Return the result value.
        """
    def IsConstant(self) -> bool:
        """
        Return true if this result's constancy is ConstantOverDescendants.
        """
    @staticmethod
    def MakeConstant(value: bool) -> PredicateFunctionResult:
        """
        Create with C{value} and'ConstantOverDescendants'.
        """
    @staticmethod
    def MakeVarying(value: bool) -> PredicateFunctionResult:
        """
        Create with C{value} and'MayVaryOverDescendants'.
        """
    def SetAndPropagateConstancy(self, _other: PredicateFunctionResult, /) -> None:
        """
        Set this result's value to C{other's} value, and propagate constancy;
        if both this and C{other} are ConstantOverDescendants, this object's
        constancy remains ConstantOverDescendants.


        Otherwise set this object's constancy to MayVaryOverDescendants.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class PrimSpec(Spec):
    '''
    Represents a prim description in an SdfLayer object.


    Every SdfPrimSpec object is defined in a layer. It is identified by
    its path (SdfPath class) in the namespace hierarchy of its layer.
    SdfPrimSpecs can be created using the New() method as children of
    either the containing SdfLayer itself (for"root level"prims), or as
    children of other SdfPrimSpec objects to extend a hierarchy. The
    helper function SdfCreatePrimInLayer() can be used to quickly create a
    hierarchy of primSpecs.

    SdfPrimSpec objects have properties of two general types: attributes
    (containing values) and relationships (different types of connections
    to other prims and attributes). Attributes are represented by the
    SdfAttributeSpec class and relationships by the SdfRelationshipSpec
    class. Each prim has its own namespace of properties. Properties are
    stored and accessed by their name.

    SdfPrimSpec objects have a typeName, permission restriction, and they
    reference and inherit prim paths. Permission restrictions control
    which other layers may refer to, or express opinions about a prim. See
    the SdfPermission class for more information.

       - Insert doc about references and inherits here.

       - Should have validate... methods for name, children, properties

    '''
    ActiveKey: ClassVar[str] = ...
    AnyTypeToken: ClassVar[str] = ...
    CommentKey: ClassVar[str] = ...
    CustomDataKey: ClassVar[str] = ...
    DisplayName: ClassVar[str] = ...
    DocumentationKey: ClassVar[str] = ...
    HiddenKey: ClassVar[str] = ...
    InheritPathsKey: ClassVar[str] = ...
    KindKey: ClassVar[str] = ...
    PayloadKey: ClassVar[str] = ...
    PermissionKey: ClassVar[str] = ...
    PrefixKey: ClassVar[str] = ...
    PrefixSubstitutionsKey: ClassVar[str] = ...
    PrimOrderKey: ClassVar[str] = ...
    PropertyOrderKey: ClassVar[str] = ...
    ReferencesKey: ClassVar[str] = ...
    RelocatesKey: ClassVar[str] = ...
    SpecializesKey: ClassVar[str] = ...
    SpecifierKey: ClassVar[str] = ...
    SymmetricPeerKey: ClassVar[str] = ...
    SymmetryArgumentsKey: ClassVar[str] = ...
    SymmetryFunctionKey: ClassVar[str] = ...
    TypeNameKey: ClassVar[str] = ...
    VariantSelectionKey: ClassVar[str] = ...
    VariantSetNamesKey: ClassVar[str] = ...
    active: bool
    assetInfo: MapEditProxy_VtDictionary
    comment: str
    customData: MapEditProxy_VtDictionary
    documentation: str
    hidden: bool
    instanceable: bool
    kind: str
    name: str
    nameChildrenOrder: ListProxy_SdfNameTokenKeyPolicy
    permission: Permission
    prefix: str
    prefixSubstitutions: dict
    propertyOrder: ListProxy_SdfNameTokenKeyPolicy
    relocates: MapEditProxy_SdfRelocatesMap_SdfRelocatesMapProxyValuePolicy
    specifier: Specifier
    suffix: str
    suffixSubstitutions: dict
    symmetricPeer: str
    symmetryArguments: MapEditProxy_VtDictionary
    symmetryFunction: str
    typeName: str
    @overload
    def __init__(self, parentLayer: Layer, name: str, spec: Specifier, typeName: str = ...) -> None:
        """
        Create a root prim spec.


        Creates a prim spec with a C{name}, C{specifier} and C{typeName} as a
        root prim in the given layer.
        """
    @overload
    def __init__(self, parentPrim: PrimSpec, name: str, spec: Specifier, typeName: str = ...) -> None:
        """
        Create a prim spec.


        Creates a prim spec with a C{name}, C{specifier} and C{typeName} as a
        namespace child of the given prim.

        SdfCreatePrimInLayer() to create a PrimSpec with all required ancestor
        specs as SdfSpecifierOver.
        """
    def ApplyNameChildrenOrder(self, _vec: list[str] | list[pxr.Ar.ResolvedPath], /) -> list:
        """
        Reorders the given list of child names according to the reorder
        nameChildren statement for this prim.


        This routine employs the standard list editing operation for ordered
        items in a ListEditor.
        """
    def ApplyPropertyOrder(self, _vec: list[str] | list[pxr.Ar.ResolvedPath], /) -> list:
        """
        Reorders the given list of property names according to the reorder
        properties statement for this prim.


        This routine employs the standard list editing operation for ordered
        items in a ListEditor.
        """
    def BlockVariantSelection(self, _variantSetName: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Blocks the variant selected for the given variant set by setting the
        variant selection to empty.
        """
    def CanSetName(self, _newName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if setting the prim spec's name to C{newName} will
        succeed.


        Returns false if it won't, and sets C{whyNot} with a string describing
        why not.
        """
    def ClearActive(self) -> None:
        """
        Removes the active opinion in this prim spec if there is one.
        """
    def ClearInstanceable(self) -> None:
        """
        Clears the value for the prim's instanceable flag.
        """
    def ClearKind(self) -> None:
        """
        Remove the kind opinion from this prim spec if there is one.
        """
    def ClearPayloadList(self) -> None:
        """
        Clears the payloads for this prim.
        """
    def ClearReferenceList(self) -> None:
        """
        Clears the references for this prim.
        """
    def GetAttributeAtPath(self, _path: Path | str, /) -> AttributeSpec:
        """
        Returns an attribute given its C{path}.


        Returns invalid handle if there is no attribute at C{path}. This is
        simply a more specifically typed version of GetObjectAtPath.
        """
    def GetObjectAtPath(self, _path: Path | str, /) -> Spec:
        """
        Returns the object for the given C{path}.


        If C{path} is relative then it will be interpreted as relative to this
        prim. If it is absolute then it will be interpreted as absolute in
        this prim's layer.

        Returns invalid handle if there is no object at C{path}.
        """
    def GetPrimAtPath(self, _path: Path | str, /) -> PrimSpec:
        """
        Returns a prim given its C{path}.


        Returns invalid handle if there is no prim at C{path}. This is simply
        a more specifically typed version of GetObjectAtPath.
        """
    def GetPropertyAtPath(self, _path: Path | str, /) -> PropertySpec:
        """
        Returns a property given its C{path}.


        Returns invalid handle if there is no property at C{path}. This is
        simply a more specifically typed version of GetObjectAtPath.
        """
    def GetRelationshipAtPath(self, _path: Path | str, /) -> RelationshipSpec:
        """
        Returns a relationship given its C{path}.


        Returns invalid handle if there is no relationship at C{path}. This is
        simply a more specifically typed version of GetObjectAtPath.
        """
    def GetVariantNames(self, _name: str | pxr.Ar.ResolvedPath, /) -> list[str]:
        """
        Returns list of variant names for the given variant set.
        """
    def HasActive(self) -> bool:
        """
        Returns true if this prim spec has an opinion about active.
        """
    def HasInstanceable(self) -> bool:
        """
        Returns true if this prim spec has a value authored for its
        instanceable flag, false otherwise.
        """
    def HasKind(self) -> bool:
        """
        Returns true if this prim spec has an opinion about kind.
        """
    def RemoveProperty(self, _property: PropertySpec, /) -> None:
        """
        Removes the property.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def attributes(self) -> ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate:
        """
        Returns a view of the attributes of this prim.
        """
    @property
    def expired(self): ...
    @property
    def hasPayloads(self): ...
    @property
    def hasReferences(self): ...
    @property
    def inheritPathList(self) -> ListEditorProxy_SdfPathKeyPolicy:
        """
        Returns a proxy for the prim's inherit paths.


        Inherit paths for this prim may be modified through the proxy.
        """
    @property
    def nameChildren(self) -> ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec__:
        """
        Returns a keyed vector view of the prim's namespace children.
        """
    @property
    def nameParent(self) -> PrimSpec:
        """
        Returns the prim's namespace parent.


        This does not return the pseudo-root for root prims. Most algorithms
        that scan the namespace hierarchy upwards don't want to process the
        pseudo-root the same way as actual prims. Algorithms that do can
        always call C{GetRealNameParent()} .
        """
    @property
    def nameRoot(self) -> PrimSpec:
        """
        Returns the prim's namespace pseudo-root prim.
        """
    @property
    def payloadList(self) -> ListEditorProxy_SdfPayloadTypePolicy:
        """
        Returns a proxy for the prim's payloads.


        Payloads for this prim may be modified through the proxy.
        """
    @property
    def properties(self) -> ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec__:
        """
        Returns the prim's properties.
        """
    @property
    def realNameParent(self) -> PrimSpec:
        """
        Returns the prim's namespace parent.
        """
    @property
    def referenceList(self) -> ListEditorProxy_SdfReferenceTypePolicy:
        """
        Returns a proxy for the prim's references.


        References for this prim may be modified through the proxy.
        """
    @property
    def relationships(self) -> ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate:
        """
        Returns a view of the relationships of this prim.
        """
    @property
    def specializesList(self) -> ListEditorProxy_SdfPathKeyPolicy:
        """
        Returns a proxy for the prim's specializes paths.


        Specializes for this prim may be modified through the proxy.
        """
    @property
    def variantSelections(self) -> MapEditProxy_SdfVariantSelectionMap:
        """
        Returns an editable map whose keys are variant set names and whose
        values are the variants selected for each set.
        """
    @property
    def variantSetNameList(self) -> ListEditorProxy_SdfNameKeyPolicy:
        """
        Returns a proxy for the prim's variant sets.


        Variant sets for this prim may be modified through the proxy.
        """
    @property
    def variantSets(self) -> ChildrenProxy_SdfVariantSetView:
        """
        Returns the variant sets.


        The result maps variant set names to variant sets. Variant sets may be
        removed through the proxy.
        """

class PropertySpec(Spec):
    """
    Base class for SdfAttributeSpec and SdfRelationshipSpec.


    Scene Spec Attributes (SdfAttributeSpec) and Relationships
    (SdfRelationshipSpec) are the basic properties that make up Scene Spec
    Prims (SdfPrimSpec). They share many qualities and can sometimes be
    treated uniformly. The common qualities are provided by this base
    class.

    NOTE: Do not use Python reserved words and keywords as attribute
    names. This will cause attribute resolution to fail.
    """
    AssetInfoKey: ClassVar[str] = ...
    CommentKey: ClassVar[str] = ...
    CustomDataKey: ClassVar[str] = ...
    CustomKey: ClassVar[str] = ...
    DisplayGroupKey: ClassVar[str] = ...
    DisplayNameKey: ClassVar[str] = ...
    DocumentationKey: ClassVar[str] = ...
    HiddenKey: ClassVar[str] = ...
    PermissionKey: ClassVar[str] = ...
    PrefixKey: ClassVar[str] = ...
    SymmetricPeerKey: ClassVar[str] = ...
    SymmetryArgumentsKey: ClassVar[str] = ...
    SymmetryFunctionKey: ClassVar[str] = ...
    assetInfo: MapEditProxy_VtDictionary
    comment: str
    custom: Incomplete
    customData: MapEditProxy_VtDictionary
    default: Incomplete
    displayGroup: str
    displayName: str
    documentation: str
    hidden: bool
    name: str
    permission: Permission
    prefix: str
    symmetricPeer: str
    symmetryArguments: MapEditProxy_VtDictionary
    symmetryFunction: str
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ClearDefaultValue(self) -> None:
        """
        Clear the attribute's default value.
        """
    def HasDefaultValue(self) -> bool:
        """
        Returns true if a default value is set for this attribute.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...
    @property
    def hasOnlyRequiredFields(self): ...
    @property
    def owner(self) -> Spec:
        """
        Returns the owner prim or relationship of this property.
        """
    @property
    def variability(self) -> Variability:
        """
        Returns the variability of the property.


        An attribute's variability may be C{Varying} (the default),
        C{Uniform}, C{Config}, or C{Computed}.

        A relationship's variability may be C{Varying} or C{Uniform} (the
        default)

           - C{Varying} attributes may be directly authored, animated and
             affected by C{Actions}. They are the most flexible. Varying
             relationships can have a default and an anim spline, in addition to a
             list of targets.

           - C{Uniform} attributes may be authored only with non-animated
             values (default values). They cannot be affected by C{Actions}, but
             they can be connected to other Uniform attributes. Uniform
             relationships have a list of targets but do not have default or anim
             spline values.

           - C{Config} attributes are the same as Uniform except that a Prim
             can choose to alter its collection of built-in properties based on the
             values of its Config attributes.

           - C{Computed} attributes may not be authored in scene description.
             Prims determine the values of their Computed attributes through Prim-
             specific computation. They may not be connected.

        """

class PseudoRootSpec(PrimSpec):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class Reference(Boost.Python.instance):
    """
    Represents a reference and all its meta data.


    A reference is expressed on a prim in a given layer and it identifies
    a prim in a layer stack. All opinions in the namespace hierarchy under
    the referenced prim will be composed with the opinions in the
    namespace hierarchy under the referencing prim.

    The asset path specifies the layer stack being referenced. If this
    asset path is non-empty, this reference is considered
    an'external'reference to the layer stack rooted at the specified
    layer. If this is empty, this reference is considered
    an'internal'reference to the layer stack containing (but not
    necessarily rooted at) the layer where the reference is authored.

    The prim path specifies the prim in the referenced layer stack from
    which opinions will be composed. If this prim path is empty, it will
    be considered a reference to the default prim specified in the root
    layer of the referenced layer stack  see SdfLayer::GetDefaultPrim.

    The meta data for a reference is its layer offset and custom data. The
    layer offset is an affine transformation applied to all anim splines
    in the referenced prim's namespace hierarchy, see SdfLayerOffset for
    details. Custom data is for use by plugins or other non-tools supplied
    extensions that need to be able to store data associated with
    references.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, assetPath: str | pxr.Ar.ResolvedPath = ..., primPath: Path | str = ..., layerOffset: LayerOffset = ..., customData: dict = ...) -> None:
        """
        Creates a reference with all its meta data.


        The default reference is an internal reference to the default prim.
        See SdfAssetPath for what characters are valid in C{assetPath}. If
        C{assetPath} contains invalid characters, issue an error and set this
        reference's asset path to the empty asset path.
        """
    @overload
    def __init__(self, arg2: Reference, /) -> None: ...
    def IsInternal(self) -> bool:
        """
        Returns C{true} in the case of an internal reference.


        An internal reference is a reference with an empty asset path.
        """
    def __eq__(self, other: object) -> bool:
        """
        Returns whether this reference equals *rhs*.
        """
    def __ge__(self, other: object) -> bool:
        """

        SdfReference::operator<(const SdfReference&)
        """
    def __gt__(self, other: object) -> bool:
        """

        SdfReference::operator<(const SdfReference&)
        """
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool:
        """

        SdfReference::operator<(const SdfReference&)
        """
    def __lt__(self, other: object) -> bool:
        """
        Returns whether this reference is less than *rhs*.


        The meaning of less than is somewhat arbitrary.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def assetPath(self) -> str:
        """
        Returns the asset path to the root layer of the referenced layer
        stack.


        This will be empty in the case of an internal reference.
        """
    @property
    def customData(self) -> dict:
        """
        Returns the custom data associated with the reference.
        """
    @property
    def layerOffset(self) -> LayerOffset:
        """
        Returns the layer offset associated with the reference.
        """
    @property
    def primPath(self) -> Path:
        """
        Returns the path of the referenced prim.


        This will be empty if the referenced prim is the default prim
        specified in the referenced layer stack.
        """

class ReferenceListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: ReferenceListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> ReferenceListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> ReferenceListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: Reference, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class RelationshipSpec(PropertySpec):
    """
    A property that contains a reference to one or more SdfPrimSpec
    instances.


    A relationship may refer to one or more target prims or attributes.
    All targets of a single relationship are considered to be playing the
    same role. Note that C{role} does not imply that the target prims or
    attributes are of the same C{type}.

    Relationships may be annotated with relational attributes. Relational
    attributes are named SdfAttributeSpec objects containing values that
    describe the relationship. For example, point weights are commonly
    expressed as relational attributes.
    """
    TargetsKey: ClassVar[str] = ...
    noLoadHint: Incomplete
    def __init__(self, owner: PrimSpec, name: str, custom: bool = ..., variability: Variability = ...) -> None:
        """
        Creates a new prim relationship instance.


        Creates and returns a new relationship for the given prim. The
        C{owner} will own the newly created relationship.
        """
    def RemoveTargetPath(self, _path: Path | str, /, preserveTargetOrder: bool = ...) -> None:
        """
        Removes the specified target path.


        Removes the given target path and any relational attributes for the
        given target path. If C{preserveTargetOrder} is C{true}, Erase() is
        called on the list editor instead of RemoveItemEdits(). This preserves
        the ordered items list.
        """
    def ReplaceTargetPath(self, _oldPath: Path | str, _newPath: Path | str, /) -> None:
        """
        Updates the specified target path.


        Replaces the path given by C{oldPath} with the one specified by
        C{newPath}. Relational attributes are updated if necessary.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...
    @property
    def targetPathList(self) -> ListEditorProxy_SdfPathKeyPolicy:
        """
        Returns the relationship's target path list editor.


        The list of the target paths for this relationship may be modified
        through the proxy.
        """

class Spec(Boost.Python.instance):
    """
    Base class for all Sdf spec classes.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ClearInfo(self, key: str | pxr.Ar.ResolvedPath) -> None:
        """
        Clears the value for scene spec info with the given *key*.


        After calling this, HasInfo() will return B{false}. To make HasInfo()
        return B{true} just set a value for that scene spec info.

        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        """
    def GetAsText(self) -> str: ...
    def GetFallbackForInfo(self, _key: str | pxr.Ar.ResolvedPath, /) -> Any:
        """
        Returns the fallback for the info with the given *key*.
        """
    def GetInfo(self, _key: str | pxr.Ar.ResolvedPath, /) -> Any:
        """
        Gets the value for the given metadata key.


        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        """
    def GetMetaDataDisplayGroup(self, _key: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Returns this metadata key's displayGroup.
        """
    def GetMetaDataInfoKeys(self) -> list[str]:
        """
        Returns the list of metadata info keys for this object.


        This is not the complete list of keys, it is only those that should be
        considered to be metadata by inspectors or other presentation UI.

        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        """
    def GetTypeForInfo(self, _key: str | pxr.Ar.ResolvedPath, /) -> pxr.Tf.Type:
        """
        Returns the data type for the info with the given *key*.
        """
    def HasInfo(self, _key: str | pxr.Ar.ResolvedPath, /) -> bool:
        '''
        Returns whether there is a setting for the scene spec info with the
        given key.


        When asked for a value for one of its scene spec info, a valid value
        will always be returned. But if this API returns B{false} for a scene
        spec info, the value of that info will be the defined default value.

        When dealing with a composedLayer, it is not necessary to worry about
        whether a scene spec info"has a value"because the composed layer will
        always have a valid value, even if it is the default.

        A spec may or may not have an expressed value for some of its scene
        spec info.

        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        '''
    def IsInert(self, ignoreChildren: bool = ...) -> bool:
        '''
        Returns whether this object has no significant data.


        "Significant"here means that the object contributes opinions to a
        scene. If this spec has any child scenegraph objects (e.g., prim or
        property spec), it will be considered significant even if those child
        objects are not. However, if C{ignoreChildren} is C{true}, these child
        objects will be ignored.
        '''
    def ListInfoKeys(self) -> list[str]:
        """
        Returns the full list of info keys currently set on this object.



        This does not include fields that represent names of children.
        """
    def SetInfo(self, _key: str | pxr.Ar.ResolvedPath, _value: Any, /) -> None:
        """
        Sets the value for the given metadata key.


        It is an error to pass a value that is not the correct type for that
        given key.

        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        """
    def SetInfoDictionaryValue(self, _dictionaryKey: str | pxr.Ar.ResolvedPath, _entryKey: str | pxr.Ar.ResolvedPath, _value: Any, /) -> None:
        """
        Sets the value for C{entryKey} to C{value} within the dictionary with
        the given metadata key C{dictionaryKey}.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...
    @property
    def isInert(self):
        '''
        Returns whether this object has no significant data.


        "Significant"here means that the object contributes opinions to a
        scene. If this spec has any child scenegraph objects (e.g., prim or
        property spec), it will be considered significant even if those child
        objects are not. However, if C{ignoreChildren} is C{true}, these child
        objects will be ignored.
        '''
    @property
    def layer(self) -> Layer:
        """
        Returns the layer that this object belongs to.
        """
    @property
    def path(self) -> Path:
        """
        Returns the scene path of this object.
        """

class SpecType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class Specifier(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class StringListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: StringListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> StringListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> StringListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: object, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class TimeCode(Boost.Python.instance):
    """
    Value type that represents a time code.


    It's equivalent to a double type value but is used to indicate that
    this value should be resolved by any time based value resolution.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, _time: float, /) -> None:
        """
        Construct a time code with the given time.


        A default constructed SdfTimeCode has a time of 0.0. A double value
        can implicitly cast to SdfTimeCode.
        """
    @overload
    def __init__(self) -> None: ...
    def GetValue(self) -> float:
        """
        Return the time value.
        """
    def __add__(self, arg2: TimeCode | float, /) -> Any: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __float__(self) -> float: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __mul__(self, arg2: TimeCode | float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __radd__(self, arg2: float, /) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __rsub__(self, arg2: float, /) -> Any: ...
    def __rtruediv__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: TimeCode | float, /) -> Any: ...
    def __truediv__(self, arg2: TimeCode | float, /) -> Any: ...

class TimeCodeArray(Boost.Python.instance):
    """An array of type SdfTimeCode."""
    _isVtArray: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, array: typing.Iterable) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, size: int, array: typing.Iterable) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    @overload
    def __init__(self, size: int) -> None:
        """    __init__(values)

            values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)



        __init__( (object)arg1, (int)arg2, (object)arg3) -> object

        __init__( (object)arg1, (int)arg2) -> None"""
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, arg2: object, /) -> Any: ...
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...

class TokenListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: TokenListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> TokenListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> TokenListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: object, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class UInt64ListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: UInt64ListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> UInt64ListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> UInt64ListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class UIntListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: UIntListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> UIntListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> UIntListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class UnregisteredValue(Boost.Python.instance):
    """
    Stores a representation of the value for an unregistered metadata
    field encountered during text layer parsing.


    This provides the ability to serialize this data to a layer, as well
    as limited inspection and editing capabilities (e.g., moving this data
    to a different spec or field) even when the data type of the value
    isn't known.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Wraps an empty VtValue.
        """
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def __init__(self, arg2: UnregisteredValue, /) -> None: ...
    @overload
    def __init__(self, arg2: UnregisteredValueListOp, /) -> None: ...
    def __eq__(self, other: object) -> bool:
        """
        Returns true if the wrapped VtValues are equal.
        """
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def value(self) -> Any:
        """
        Returns the wrapped VtValue specified in the constructor.
        """

class UnregisteredValueListOp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    addedItems: Incomplete
    appendedItems: Incomplete
    deletedItems: Incomplete
    explicitItems: Incomplete
    orderedItems: Incomplete
    prependedItems: Incomplete
    def __init__(self) -> None: ...
    @overload
    def ApplyOperations(self, arg2: object, /) -> Any: ...
    @overload
    def ApplyOperations(self, arg2: UnregisteredValueListOp, /) -> Any: ...
    def Clear(self) -> None: ...
    def ClearAndMakeExplicit(self) -> None: ...
    @staticmethod
    def Create(prependedItems: object = ..., appendedItems: object = ..., deletedItems: object = ...) -> UnregisteredValueListOp: ...
    @staticmethod
    def CreateExplicit(explicitItems: object = ...) -> UnregisteredValueListOp: ...
    def GetAddedOrExplicitItems(self) -> Any: ...
    def GetAppliedItems(self) -> Any: ...
    def HasItem(self, arg2: UnregisteredValue, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def isExplicit(self): ...

class ValueBlock(Boost.Python.instance):
    """
    A special value type that can be used to explicitly author an opinion
    for an attribute's default value or time sample value that represents
    having no value.


    Note that this is different from not having a value authored.

    One could author such a value in two ways. ::

      attribute->SetDefaultValue(VtValue(SdfValueBlock());
      ...
      layer->SetTimeSample(attribute->GetPath(), 101, VtValue(SdfValueBlock()));

    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class ValueRoleNames(Boost.Python.instance):
    Color: ClassVar[str] = ...  # read-only
    EdgeIndex: ClassVar[str] = ...  # read-only
    FaceIndex: ClassVar[str] = ...  # read-only
    Frame: ClassVar[str] = ...  # read-only
    Group: ClassVar[str] = ...  # read-only
    Normal: ClassVar[str] = ...  # read-only
    Point: ClassVar[str] = ...  # read-only
    PointIndex: ClassVar[str] = ...  # read-only
    TextureCoordinate: ClassVar[str] = ...  # read-only
    Transform: ClassVar[str] = ...  # read-only
    Vector: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ValueTypeName(Boost.Python.instance):
    """
    Represents a value type name, i.e.


    an attribute's type name. Usually, a value type name associates a
    string with a C{TfType} and an optional role, along with additional
    metadata. A schema registers all known value type names and may
    register multiple names for the same TfType and role pair. All name
    strings for a given pair are collectively called its aliases.

    A value type name may also represent just a name string, without a
    C{TfType}, role or other metadata. This is currently used exclusively
    to unserialize and re-serialize an attribute's type name where that
    name is not known to the schema.

    Because value type names can have aliases and those aliases may change
    in the future, clients should avoid using the value type name's string
    representation except to report human readable messages and when
    serializing. Clients can look up a value type name by string using
    C{SdfSchemaBase::FindType()} and shouldn't otherwise need the string.
    Aliases compare equal, even if registered by different schemas.
    """
    def __init__(self) -> None:
        """
        Constructs an invalid type name.
        """
    def __bool__(self) -> bool:
        """
        Explicit bool conversion operator.


        Converts to C{true} if this is a valid, non-empty type, C{false}
        otherwise.
        """
    def __eq__(self, other: object) -> bool:
        """
        Returns C{true} if this type name is equal to C{rhs}.


        Aliases compare equal.
        """
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def aliasesAsStrings(self): ...
    @property
    def arrayType(self) -> ValueTypeName:
        """
        Returns the array version of this type name if it's an scalar type
        name, otherwise returns this type name.


        If there is no array type name then this returns the invalid type
        name.
        """
    @property
    def cppTypeName(self): ...
    @property
    def defaultUnit(self) -> pxr.Tf.Enum:
        """
        Returns the default unit enum for the type.
        """
    @property
    def defaultValue(self) -> Any:
        """
        Returns the default value for the type.
        """
    @property
    def isArray(self) -> bool:
        """
        Returns C{true} iff this type is an array.


        The invalid type is considered neither scalar nor array.
        """
    @property
    def isScalar(self) -> bool:
        """
        Returns C{true} iff this type is a scalar.


        The invalid type is considered neither scalar nor array.
        """
    @property
    def role(self) -> str:
        """
        Returns the type's role.
        """
    @property
    def scalarType(self) -> ValueTypeName:
        """
        Returns the scalar version of this type name if it's an array type
        name, otherwise returns this type name.


        If there is no scalar type name then this returns the invalid type
        name.
        """
    @property
    def type(self) -> pxr.Tf.Type:
        """
        Returns the C{TfType} of the type.
        """

class ValueTypeNames(Boost.Python.instance):
    Asset: ClassVar[ValueTypeName] = ...  # read-only
    AssetArray: ClassVar[ValueTypeName] = ...  # read-only
    Bool: ClassVar[ValueTypeName] = ...  # read-only
    BoolArray: ClassVar[ValueTypeName] = ...  # read-only
    Color3d: ClassVar[ValueTypeName] = ...  # read-only
    Color3dArray: ClassVar[ValueTypeName] = ...  # read-only
    Color3f: ClassVar[ValueTypeName] = ...  # read-only
    Color3fArray: ClassVar[ValueTypeName] = ...  # read-only
    Color3h: ClassVar[ValueTypeName] = ...  # read-only
    Color3hArray: ClassVar[ValueTypeName] = ...  # read-only
    Color4d: ClassVar[ValueTypeName] = ...  # read-only
    Color4dArray: ClassVar[ValueTypeName] = ...  # read-only
    Color4f: ClassVar[ValueTypeName] = ...  # read-only
    Color4fArray: ClassVar[ValueTypeName] = ...  # read-only
    Color4h: ClassVar[ValueTypeName] = ...  # read-only
    Color4hArray: ClassVar[ValueTypeName] = ...  # read-only
    Double: ClassVar[ValueTypeName] = ...  # read-only
    Double2: ClassVar[ValueTypeName] = ...  # read-only
    Double2Array: ClassVar[ValueTypeName] = ...  # read-only
    Double3: ClassVar[ValueTypeName] = ...  # read-only
    Double3Array: ClassVar[ValueTypeName] = ...  # read-only
    Double4: ClassVar[ValueTypeName] = ...  # read-only
    Double4Array: ClassVar[ValueTypeName] = ...  # read-only
    DoubleArray: ClassVar[ValueTypeName] = ...  # read-only
    Float: ClassVar[ValueTypeName] = ...  # read-only
    Float2: ClassVar[ValueTypeName] = ...  # read-only
    Float2Array: ClassVar[ValueTypeName] = ...  # read-only
    Float3: ClassVar[ValueTypeName] = ...  # read-only
    Float3Array: ClassVar[ValueTypeName] = ...  # read-only
    Float4: ClassVar[ValueTypeName] = ...  # read-only
    Float4Array: ClassVar[ValueTypeName] = ...  # read-only
    FloatArray: ClassVar[ValueTypeName] = ...  # read-only
    Frame4d: ClassVar[ValueTypeName] = ...  # read-only
    Frame4dArray: ClassVar[ValueTypeName] = ...  # read-only
    Group: ClassVar[ValueTypeName] = ...  # read-only
    Half: ClassVar[ValueTypeName] = ...  # read-only
    Half2: ClassVar[ValueTypeName] = ...  # read-only
    Half2Array: ClassVar[ValueTypeName] = ...  # read-only
    Half3: ClassVar[ValueTypeName] = ...  # read-only
    Half3Array: ClassVar[ValueTypeName] = ...  # read-only
    Half4: ClassVar[ValueTypeName] = ...  # read-only
    Half4Array: ClassVar[ValueTypeName] = ...  # read-only
    HalfArray: ClassVar[ValueTypeName] = ...  # read-only
    Int: ClassVar[ValueTypeName] = ...  # read-only
    Int2: ClassVar[ValueTypeName] = ...  # read-only
    Int2Array: ClassVar[ValueTypeName] = ...  # read-only
    Int3: ClassVar[ValueTypeName] = ...  # read-only
    Int3Array: ClassVar[ValueTypeName] = ...  # read-only
    Int4: ClassVar[ValueTypeName] = ...  # read-only
    Int4Array: ClassVar[ValueTypeName] = ...  # read-only
    Int64: ClassVar[ValueTypeName] = ...  # read-only
    Int64Array: ClassVar[ValueTypeName] = ...  # read-only
    IntArray: ClassVar[ValueTypeName] = ...  # read-only
    Matrix2d: ClassVar[ValueTypeName] = ...  # read-only
    Matrix2dArray: ClassVar[ValueTypeName] = ...  # read-only
    Matrix3d: ClassVar[ValueTypeName] = ...  # read-only
    Matrix3dArray: ClassVar[ValueTypeName] = ...  # read-only
    Matrix4d: ClassVar[ValueTypeName] = ...  # read-only
    Matrix4dArray: ClassVar[ValueTypeName] = ...  # read-only
    Normal3d: ClassVar[ValueTypeName] = ...  # read-only
    Normal3dArray: ClassVar[ValueTypeName] = ...  # read-only
    Normal3f: ClassVar[ValueTypeName] = ...  # read-only
    Normal3fArray: ClassVar[ValueTypeName] = ...  # read-only
    Normal3h: ClassVar[ValueTypeName] = ...  # read-only
    Normal3hArray: ClassVar[ValueTypeName] = ...  # read-only
    Opaque: ClassVar[ValueTypeName] = ...  # read-only
    PathExpression: ClassVar[ValueTypeName] = ...  # read-only
    PathExpressionArray: ClassVar[ValueTypeName] = ...  # read-only
    Point3d: ClassVar[ValueTypeName] = ...  # read-only
    Point3dArray: ClassVar[ValueTypeName] = ...  # read-only
    Point3f: ClassVar[ValueTypeName] = ...  # read-only
    Point3fArray: ClassVar[ValueTypeName] = ...  # read-only
    Point3h: ClassVar[ValueTypeName] = ...  # read-only
    Point3hArray: ClassVar[ValueTypeName] = ...  # read-only
    Quatd: ClassVar[ValueTypeName] = ...  # read-only
    QuatdArray: ClassVar[ValueTypeName] = ...  # read-only
    Quatf: ClassVar[ValueTypeName] = ...  # read-only
    QuatfArray: ClassVar[ValueTypeName] = ...  # read-only
    Quath: ClassVar[ValueTypeName] = ...  # read-only
    QuathArray: ClassVar[ValueTypeName] = ...  # read-only
    String: ClassVar[ValueTypeName] = ...  # read-only
    StringArray: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord2d: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord2dArray: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord2f: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord2fArray: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord2h: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord2hArray: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord3d: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord3dArray: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord3f: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord3fArray: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord3h: ClassVar[ValueTypeName] = ...  # read-only
    TexCoord3hArray: ClassVar[ValueTypeName] = ...  # read-only
    TimeCode: ClassVar[ValueTypeName] = ...  # read-only
    TimeCodeArray: ClassVar[ValueTypeName] = ...  # read-only
    Token: ClassVar[ValueTypeName] = ...  # read-only
    TokenArray: ClassVar[ValueTypeName] = ...  # read-only
    UChar: ClassVar[ValueTypeName] = ...  # read-only
    UCharArray: ClassVar[ValueTypeName] = ...  # read-only
    UInt: ClassVar[ValueTypeName] = ...  # read-only
    UInt64: ClassVar[ValueTypeName] = ...  # read-only
    UInt64Array: ClassVar[ValueTypeName] = ...  # read-only
    UIntArray: ClassVar[ValueTypeName] = ...  # read-only
    Vector3d: ClassVar[ValueTypeName] = ...  # read-only
    Vector3dArray: ClassVar[ValueTypeName] = ...  # read-only
    Vector3f: ClassVar[ValueTypeName] = ...  # read-only
    Vector3fArray: ClassVar[ValueTypeName] = ...  # read-only
    Vector3h: ClassVar[ValueTypeName] = ...  # read-only
    Vector3hArray: ClassVar[ValueTypeName] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def Find() -> ValueTypeName: ...

class Variability(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class VariableExpression(Boost.Python.instance):
    '''
    Class responsible for parsing and evaluating variable expressions.


    Variable expressions are written in a custom language and represented
    in scene description as a string surrounded by backticks (`). These
    expressions may refer to"expression variables", which are key-value
    pairs provided by clients. For example, when evaluating an expression
    like: ::

      `"a_${NAME}_string"`

    The"${NAME}"portion of the string with the value of expression
    variable"NAME".

    Expression variables may be any of these supported types:

       - std::string

       - int64_t (int is accepted but coerced to int64_t)

       - bool

       - VtArrays containing any of the above types.

       - None (represented by an empty VtValue)

    Expression variables are typically authored in scene description as
    layer metadata under the\'expressionVariables\'field. Higher levels of
    the system (e.g., composition) are responsible for examining fields
    that support variable expressions, evaluating them with the
    appropriate variables (via this class) and consuming the results.

    See Variable Expressions or more information on the expression
    language and areas of the system where expressions may be used.
    '''

    class Result(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @property
        def errors(self): ...
        @property
        def usedVariables(self): ...
        @property
        def value(self): ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, expression: str | pxr.Ar.ResolvedPath) -> None:
        """
        Construct using the expression C{expr}.


        If the expression cannot be parsed, this object represents an invalid
        expression. Parsing errors will be accessible via GetErrors.
        """
    @overload
    def __init__(self) -> None:
        """
        Construct an object representing an invalid expression.
        """
    def Evaluate(self, vars: dict) -> VariableExpression.Result:
        """
        Evaluates this expression using the variables in C{variables} and
        returns a Result object with the final value.


        If an error occurs during evaluation, the value field in the Result
        object will be an empty VtValue and error messages will be added to
        the errors field.

        If the expression evaluates to an empty list, the value field in the
        Result object will contain an EmptyList object instead of an empty
        VtArray<T>, as the expression language does not provide syntax for
        specifying the expected element types in an empty list.

        If this object represents an invalid expression, calling this function
        will return a Result object with an empty value and the errors from
        GetErrors() .

        If any values in C{variables} used by this expression are themselves
        expressions, they will be parsed and evaluated. If an error occurs
        while evaluating any of these subexpressions, evaluation of this
        expression fails and the encountered errors will be added in the
        Result's list of errors.
        """
    def GetErrors(self) -> list[str]:
        """
        Returns a list of errors encountered when parsing this expression.


        If the expression was parsed successfully, this list will be empty.
        However, additional errors may be encountered when evaluating the e
        expression.
        """
    @staticmethod
    def IsExpression(_s: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{s} is a variable expression, false otherwise.


        A variable expression is a string surrounded by backticks (`).

        A return value of true does not guarantee that C{s} is a valid
        expression. This function is meant to be used as an initial check to
        determine if a string should be considered as an expression.
        """
    @staticmethod
    def IsValidVariableType(_value: Any, /) -> bool:
        """
        Returns true if C{value} holds a type that is supported by variable
        expressions, false otherwise.


        If this function returns true, C{value} may be used for an expression
        variable supplied to the Evaluate function. C{value} may also be
        authored into the'expressionVariables'dictionary, unless it is an
        empty VtValue representing the None value. See class documentation for
        list of supported types.
        """
    def __bool__(self) -> bool:
        """
        Returns true if this object represents a valid expression, false if it
        represents an invalid expression.


        A return value of true does not mean that evaluation of this
        expression is guaranteed to succeed. For example, an expression may
        refer to a variable whose value is an invalid expression. Errors like
        this can only be discovered by calling Evaluate.
        """

class VariantSetSpec(Spec):
    """
    Represents a coherent set of alternate representations for part of a
    scene.


    An SdfPrimSpec object may contain one or more named SdfVariantSetSpec
    objects that define variations on the prim.

    An SdfVariantSetSpec object contains one or more named SdfVariantSpec
    objects. It may also define the name of one of its variants to be used
    by default.

    When a prim references another prim, the referencing prim may specify
    one of the variants from each of the variant sets of the target prim.
    The chosen variant from each set (or the default variant from those
    sets that the referencing prim does not explicitly specify) is
    composited over the target prim, and then the referencing prim is
    composited over the result.
    """
    @overload
    def __init__(self, prim: PrimSpec, name: str) -> None:
        """
        Constructs a new instance.
        """
    @overload
    def __init__(self, prim: VariantSpec, name: str) -> None:
        """
        Constructs a new instance.
        """
    def RemoveVariant(self, _variant: VariantSpec, /) -> None:
        """
        Removes C{variant} from the list of variants.


        If the variant set does not currently own C{variant}, no action is
        taken.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...
    @property
    def name(self) -> str:
        """
        Returns the name of this variant set.
        """
    @property
    def owner(self) -> Spec:
        """
        Returns the prim or variant that this variant set belongs to.
        """
    @property
    def variantList(self) -> list[VariantSpec]:
        """
        Returns the variants as a vector.
        """
    @property
    def variants(self) -> ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec__:
        """
        Returns the variants as a map.
        """

class VariantSpec(Spec):
    """
    Represents a single variant in a variant set.


    A variant contains a prim. This prim is the root prim of the variant.

    SdfVariantSpecs are value objects. This means they are immutable once
    created and they are passed by copy-in APIs. To change a variant spec,
    you make a new one and replace the existing one.
    """
    def __init__(self, owner: VariantSetSpec, name: str) -> None:
        """
        Constructs a new instance.
        """
    def GetVariantNames(self, _name: str | pxr.Ar.ResolvedPath, /) -> list[str]:
        """
        Returns list of variant names for the given variant set.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...
    @property
    def name(self) -> str:
        """
        Returns the name of this variant.
        """
    @property
    def owner(self) -> VariantSetSpec:
        """
        Return the SdfVariantSetSpec that owns this variant.
        """
    @property
    def primSpec(self) -> PrimSpec:
        """
        Get the prim spec owned by this variant.
        """
    @property
    def variantSets(self) -> ChildrenProxy_SdfVariantSetView:
        """
        Returns the nested variant sets.


        The result maps variant set names to variant sets. Variant sets may be
        removed through the proxy.
        """

@overload
def Cat(arg1: AssetPathArray, /) -> AssetPathArray: ...
@overload
def Cat(arg1: AssetPathArray, arg2: AssetPathArray, /) -> AssetPathArray: ...
@overload
def Cat(arg1: AssetPathArray, arg2: AssetPathArray, arg3: AssetPathArray, /) -> AssetPathArray: ...
@overload
def Cat(arg1: AssetPathArray, arg2: AssetPathArray, arg3: AssetPathArray, arg4: AssetPathArray, /) -> AssetPathArray: ...
@overload
def Cat(arg1: AssetPathArray, arg2: AssetPathArray, arg3: AssetPathArray, arg4: AssetPathArray, arg5: AssetPathArray, /) -> AssetPathArray: ...
@overload
def Cat(arg1: PathArray, /) -> PathArray: ...
@overload
def Cat(arg1: PathArray, arg2: PathArray, /) -> PathArray: ...
@overload
def Cat(arg1: PathArray, arg2: PathArray, arg3: PathArray, /) -> PathArray: ...
@overload
def Cat(arg1: PathArray, arg2: PathArray, arg3: PathArray, arg4: PathArray, /) -> PathArray: ...
@overload
def Cat(arg1: PathArray, arg2: PathArray, arg3: PathArray, arg4: PathArray, arg5: PathArray, /) -> PathArray: ...
@overload
def Cat(arg1: TimeCodeArray, /) -> TimeCodeArray: ...
@overload
def Cat(arg1: TimeCodeArray, arg2: TimeCodeArray, /) -> TimeCodeArray: ...
@overload
def Cat(arg1: TimeCodeArray, arg2: TimeCodeArray, arg3: TimeCodeArray, /) -> TimeCodeArray: ...
@overload
def Cat(arg1: TimeCodeArray, arg2: TimeCodeArray, arg3: TimeCodeArray, arg4: TimeCodeArray, /) -> TimeCodeArray: ...
@overload
def Cat(arg1: TimeCodeArray, arg2: TimeCodeArray, arg3: TimeCodeArray, arg4: TimeCodeArray, arg5: TimeCodeArray, /) -> TimeCodeArray: ...
def ComputeAssetPathRelativeToLayer(anchor: Layer, assetPath: str | pxr.Ar.ResolvedPath) -> str:
    """
    Returns the path to the asset specified by C{assetPath}, using the
    C{anchor} layer to anchor the path if it is relative.


    If the result of anchoring C{assetPath} to C{anchor's} path cannot be
    resolved and C{assetPath} is a search path, C{assetPath} will be
    returned. If C{assetPath} is not relative, C{assetPath} will be
    returned. Otherwise, the anchored path will be returned.

    Note that if C{anchor} is an anonymous layer, we will always return
    the untouched C{assetPath}.
    """
def ConvertToValidMetadataDictionary(arg1: object, /) -> tuple:
    """
    Convert C{dict} to a valid metadata dictionary for scene description.


    Valid metadata dictionaries have values that are any of
    SDF_VALUE_TYPES (or VtArrays of those), plus VtDictionary with values
    of those types (or similarly nested VtDictionaries).

    Certain conversions are performed in an attempt to produce a valid
    metadata dictionary. For example:

    Convert std::vector<VtValue>to VtArray<T>where T is the type of the
    first element in the vector. Fail conversion for empty vectors where a
    concrete type cannot be inferred.

    Convert python sequences to VtArray<T>where T is the type of the first
    element in the python sequence, when converted to VtValue, if that T
    is an SDF_VALUE_TYPE). Fail conversion for empty sequences where a
    concrete type cannot be inferred.

    If any values cannot be converted to valid SDF_VALUE_TYPES, omit those
    elements and add a message to C{errMsg} indicating which values were
    omitted.
    """
def ConvertUnit(_fromUnit: pxr.Tf.Enum, _toUnit: pxr.Tf.Enum, /) -> float:
    """
    Converts from one unit of measure to another.


    The *fromUnit* and *toUnit* units must be of the same type (for
    example, both of type SdfLengthUnit).
    """
@overload
def CopySpec(srcLayer: Layer, srcPath: Path | str, dstLayer: Layer, dstPath: Path | str, shouldCopyValueFn: ShouldCopyValueFn, shouldCopyChildrenFn: ShouldCopyChildrenFn) -> bool:
    """
    Utility function for copying spec data at C{srcPath} in C{srcLayer} to
    C{destPath} in C{destLayer}.


    Various behaviors (such as which parts of the spec to copy) are
    controlled by the supplied C{shouldCopyValueFn} and
    C{shouldCopyChildrenFn}.

    Copying is performed recursively: all child specs are copied as well,
    except where prevented by C{shouldCopyChildrenFn}.

    Parent specs of the destination are not created, and must exist before
    SdfCopySpec is called, or a coding error will result. For prim
    parents, clients may find it convenient to call SdfCreatePrimInLayer
    before SdfCopySpec.

    Variant specs may be copied to prim paths and vice versa. When copying
    a variant to a prim, the specifier and typename from the variant's
    parent prim will be used.

    As a special case, if the top-level object to be copied is a
    relationship target or a connection, the destination spec must already
    exist. That is because we don't want SdfCopySpec to impose any policy
    on how list edits are made; client code should arrange for
    relationship targets and connections to be specified as prepended,
    appended, deleted, and/or ordered, as needed.
    """
@overload
def CopySpec(srcLayer: Layer, srcPath: Path | str, dstLayer: Layer, dstPath: Path | str) -> bool:
    """
    Utility function for copying spec data at C{srcPath} in C{srcLayer} to
    C{destPath} in C{destLayer}.


    Copying is performed recursively: all child specs are copied as well.
    Any destination specs that already exist will be overwritten.

    Parent specs of the destination are not created, and must exist before
    SdfCopySpec is called, or a coding error will result. For prim
    parents, clients may find it convenient to call SdfCreatePrimInLayer
    before SdfCopySpec.

    As a special case, if the top-level object to be copied is a
    relationship target or a connection, the destination spec must already
    exist. That is because we don't want SdfCopySpec to impose any policy
    on how list edits are made; client code should arrange for
    relationship targets and connections to be specified as prepended,
    appended, deleted, and/or ordered, as needed.

    Variant specs may be copied to prim paths and vice versa. When copying
    a variant to a prim, the specifier and typename from the variant's
    parent prim will be used.

    Attribute connections, relationship targets, inherit and specializes
    paths, and internal sub-root references that target an object beneath
    C{srcPath} will be remapped to target objects beneath C{dstPath}.
    """
def CreatePrimInLayer(_layer: Layer, _primPath: Path | str, /) -> PrimSpec:
    """
    Convenience function to create a prim at the given path, and any
    necessary parent prims, in the given layer.


    If a prim already exists at the given path it will be returned
    unmodified.

    The new specs are created with SdfSpecifierOver and an empty type.
    primPath must be a valid prim path.
    """
def CreateVariantInLayer(_layer: Layer, _primPath: Path | str, _variantSetName: str | pxr.Ar.ResolvedPath, _variantName: str | pxr.Ar.ResolvedPath, /) -> VariantSpec:
    """
    Convenience function to create a variant spec for a given variant set
    and a prim at the given path with.


    The function creates the prim spec if it doesn't exist already and any
    necessary parent prims, in the given layer.

    It adds the variant set to the variant set list if it doesn't already
    exist.

    It creates a variant spec with the given name under the specified
    variant set if it doesn't already exist.
    """
@overload
def DefaultUnit(_typeName: str | pxr.Ar.ResolvedPath, /) -> pxr.Tf.Enum:
    """
    Gets the show default unit for the given /a typeName.
    """
@overload
def DefaultUnit(_unit: pxr.Tf.Enum, /) -> pxr.Tf.Enum:
    """
    Gets the show default unit for the given /a unit.
    """
@overload
def Equal(arg1: AssetPathArray, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: AssetPath | str, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: AssetPathArray, arg2: AssetPath | str, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: AssetPathArray, arg2: tuple, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: tuple, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: AssetPathArray, arg2: list, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: list, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: PathArray, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: Path | str, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: PathArray, arg2: Path | str, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: PathArray, arg2: tuple, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: tuple, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: PathArray, arg2: list, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: list, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: TimeCodeArray, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: TimeCode | float, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: TimeCodeArray, arg2: TimeCode | float, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: TimeCodeArray, arg2: tuple, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: tuple, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: TimeCodeArray, arg2: list, /) -> pxr.Vt.BoolArray: ...
@overload
def Equal(arg1: list, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
def GetNameForUnit(_unit: pxr.Tf.Enum, /) -> str:
    """
    Gets the name for a given /a unit.
    """
def GetTypeForValueTypeName(_name: str | pxr.Ar.ResolvedPath, /) -> pxr.Tf.Type:
    """
    Given an sdf valueType name, produce TfType if the type name specifies
    a valid sdf value type.
    """
def GetUnitFromName(_name: str | pxr.Ar.ResolvedPath, /) -> pxr.Tf.Enum:
    """
    Gets a unit for the given /a name.
    """
def GetValueTypeNameForValue(_value: Any, /) -> ValueTypeName:
    """
    Given a value, produce the sdf valueType name.


    If you provide a value that does not return true for
    SdfValueHasValidType, the return value is unspecified.
    """
def JustCreatePrimAttributeInLayer(layer: Layer, attrPath: Path | str, typeName: ValueTypeName, variability: Variability = ..., isCustom: bool = ...) -> bool:
    """
    Convenience function to create an attributeSpec on a primSpec at the
    given path, and any necessary parent primSpecs, in the given layer.


    If an attributeSpec already exists at the given path, just author
    typeName, variability, and custom according to passed arguments and
    return true.

    Any newly created prim specs have SdfSpecifierOver and an empty type
    (as if created by SdfJustCreatePrimInLayer() ). attrPath must be a
    valid prim property path (see SdfPath::IsPrimPropertyPath() ). Return
    false and issue an error if we fail to author the required scene
    description.
    """
def JustCreatePrimInLayer(_layer: Layer, _primPath: Path | str, /) -> bool:
    """
    Convenience function to create a prim at the given path, and any
    necessary parent prims, in the given layer.


    If a prim already exists at the given path, do nothing and return
    true.

    Any newly created specs have SdfSpecifierOver and an empty type.
    primPath must be a valid prim path. Return false and issue an error if
    we fail to author the required scene description.
    """
@overload
def NotEqual(arg1: AssetPathArray, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: AssetPath | str, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: AssetPathArray, arg2: AssetPath | str, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: AssetPathArray, arg2: tuple, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: tuple, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: AssetPathArray, arg2: list, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: list, arg2: AssetPathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: PathArray, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: Path | str, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: PathArray, arg2: Path | str, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: PathArray, arg2: tuple, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: tuple, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: PathArray, arg2: list, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: list, arg2: PathArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: TimeCodeArray, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: TimeCode | float, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: TimeCodeArray, arg2: TimeCode | float, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: TimeCodeArray, arg2: tuple, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: tuple, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: TimeCodeArray, arg2: list, /) -> pxr.Vt.BoolArray: ...
@overload
def NotEqual(arg1: list, arg2: TimeCodeArray, /) -> pxr.Vt.BoolArray: ...
def UnitCategory(_unit: pxr.Tf.Enum, /) -> str:
    """
    Gets the unit category for a given /a unit.
    """
def ValueHasValidType(_value: Any, /) -> bool:
    """
    Given a value, returns if there is a valid corresponding valueType.
    """
def _DumpPathStats() -> None: ...
def _MakeBasicMatchEval(arg1: object, /) -> Any: ...
def _PathGetDebuggerPathText(arg1: Path | str, /) -> str: ...
def _PathStress() -> None: ...
def _TestTakeOwnership(arg1: object, /) -> None: ...

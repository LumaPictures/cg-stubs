# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Tf
import pxr.Vt
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class MeshTopology(Boost.Python.instance):
    """
    Topology data for meshes.


    Once constructed, this class is immutable (except when assigned or
    moved).

    To make changing certain properties easier, several methods are
    provided. WithScheme, WithHoleIndices, and WithSubdivTags will return
    copies of the object with certain specific properites changed. ::

      PxOsdMeshTopology otherTopology =
          originalTopology.WithScheme(PxOsdOpenSubdivTokens->catmullClark);
      TF_VERIFY(otherTopology.GetScheme() ==
                PxOsdOpenSubdivTokens->catmullClark);
      TF_VERIFY(otherTopology.GetOrientation() ==
                originalTopology.GetOrientation());
      TF_VERIFY(otherTopology.GetSubdivTags() ==
                originalTopology.GetSubdivTags());
      TF_VERIFY(otherTopology.GetFaceVertexCounts() ==
                originalTopology.GetFaceVertexCounts());
      TF_VERIFY(otherTopology.GetFaceVertexIndices() ==
                originalTopology.GetFaceVertexIndices());

    The cost of copying should be mitigated by the copy semantics of
    VtArray and TfToken.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _scheme: str | pxr.Ar.ResolvedPath, _orientation: str | pxr.Ar.ResolvedPath, _faceVertexCounts: pxr.Vt.IntArray | typing.Iterable[int], _faceVertexIndices: pxr.Vt.IntArray | typing.Iterable[int], /) -> None:
        """
        Construct a topology without holes or subdiv tags.
        """
    @overload
    def __init__(self, _scheme: str | pxr.Ar.ResolvedPath, _orientation: str | pxr.Ar.ResolvedPath, _faceVertexCounts: pxr.Vt.IntArray | typing.Iterable[int], _faceVertexIndices: pxr.Vt.IntArray | typing.Iterable[int], _holeIndices: pxr.Vt.IntArray | typing.Iterable[int], _subdivTags: SubdivTags, /) -> None:
        """
        Construct a topology with holes and subdiv tags.
        """
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: pxr.Vt.IntArray | typing.Iterable[int], arg5: pxr.Vt.IntArray | typing.Iterable[int], arg6: pxr.Vt.IntArray | typing.Iterable[int], /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: pxr.Vt.IntArray | typing.Iterable[int], arg5: pxr.Vt.IntArray | typing.Iterable[int], arg6: SubdivTags, /) -> None: ...
    def ComputeHash(self) -> int:
        """
        Returns the hash value of this topology to be used for instancing.
        """
    def GetFaceVertexCounts(self) -> pxr.Vt.IntArray:
        """
        Returns face vertex counts.
        """
    def GetFaceVertexIndices(self) -> pxr.Vt.IntArray:
        """
        Returns face vertex indices.
        """
    def GetHoleIndices(self) -> pxr.Vt.IntArray: ...
    def GetOrientation(self) -> str:
        """
        Returns orientation.
        """
    def GetScheme(self) -> str:
        """
        Returns the subdivision scheme.
        """
    def GetSubdivTags(self) -> SubdivTags:
        """
        Returns subdivision tags.
        """
    def Validate(self) -> MeshTopologyValidation:
        '''
        Returns a validation object which is empty if the topology is valid.

        ::

          // Validation with minimal reporting
          if (!topology.Validate()) TF_CODING_ERROR("Invalid topology.");

         ::

          {
             PxOsdMeshTopologyValidation validation = topology.Validate();
             if (!validation){
                 for (auto const &  elem: validation){
                      TF_WARN(elem.message);
                 }
             }
          }

        Internally caches the result of the validation if the topology is
        valid
        '''
    def WithHoleIndices(self, _holeIndices: pxr.Vt.IntArray | typing.Iterable[int], /) -> MeshTopology:
        """
        Return a copy of the topology, changing only the hole indices.
        """
    def WithScheme(self, _scheme: str | pxr.Ar.ResolvedPath, /) -> MeshTopology:
        '''
        Return a copy of the topology, changing only the scheme.


        Valid values include: catmullClark, loop, bilinear.

        Note that the token"catmark"is also supported for backward
        compatibility, but has been deprecated.
        '''
    def WithSubdivTags(self, _tags: SubdivTags, /) -> MeshTopology:
        """
        Return a copy of the topology, changing only the subdiv tags.
        """
    def __eq__(self, other: object) -> bool:
        """
        Equality check between two mesh topologies.
        """
    def __ne__(self, other: object) -> bool: ...

class MeshTopologyValidation(Boost.Python.instance):
    """
    Utility to help validate an OpenSubdiv Mesh topology.


    This class is created by PxOsdMeshTopology 's Validate method.

    Internally, this will avoid dynamic allocations as long as the
    topology is valid (currently using std::unique_ptr but targeting
    std::optional for C++17).

    This class does a set of basic validation tests on the topology of a
    mesh. This set of tests isn't necessarily complete. There are other
    cases like invalid primvar size that this will not check for.

    Topology is considered valid if it passes a series of checks
    enumerated by the Code class enum.

    \\warn This doesn't currently validate that the topology of crease
    indices match valid edges.

    This class is convertable to bool and converts to true if the the
    topology is valid and false if any invalidations were found. That is
    to say, a conversion to true implies an empty invalidation vector and
    false implies a non-empty invalidation vector.
    """

    class Code(pxr.Tf.Tf_PyEnumWrapper):
        InvalidCornerIndicesElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCornerWeightsSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseIndicesElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseIndicesSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseLengthElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseMethod: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseWeightsSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVaryingInterpolationRule: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVertexCountsElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVertexIndicesElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVertexIndicesSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidOrientation: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidScheme: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidTriangleSubdivision: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidVertexInterpolationRule: ClassVar[MeshTopologyValidation.Code] = ...
        NegativeCornerWeights: ClassVar[MeshTopologyValidation.Code] = ...
        NegativeCreaseWeights: ClassVar[MeshTopologyValidation.Code] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class Invalidation(Boost.Python.instance):
        """
        A tuple containing a code describing an invalidation and a descriptive
        message.
        """
        code: Incomplete
        message: Incomplete
        def __init__(self, arg2: object, /) -> None: ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __bool__(self) -> bool:
        """
        Return true if the topology is valid.
        """
    def __iter__(self) -> Any: ...

class OpenSubdivTokens(Boost.Python.instance):
    all: ClassVar[str] = ...  # read-only
    bilinear: ClassVar[str] = ...  # read-only
    boundaries: ClassVar[str] = ...  # read-only
    catmullClark: ClassVar[str] = ...  # read-only
    chaikin: ClassVar[str] = ...  # read-only
    cornersOnly: ClassVar[str] = ...  # read-only
    cornersPlus1: ClassVar[str] = ...  # read-only
    cornersPlus2: ClassVar[str] = ...  # read-only
    edgeAndCorner: ClassVar[str] = ...  # read-only
    edgeOnly: ClassVar[str] = ...  # read-only
    leftHanded: ClassVar[str] = ...  # read-only
    loop: ClassVar[str] = ...  # read-only
    none: ClassVar[str] = ...  # read-only
    rightHanded: ClassVar[str] = ...  # read-only
    smooth: ClassVar[str] = ...  # read-only
    uniform: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class SubdivTags(Boost.Python.instance):
    """
    Tags for non-hierarchial subdiv surfaces.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _vertexInterpolationRule: str | pxr.Ar.ResolvedPath, _faceVaryingInterpolationRule: str | pxr.Ar.ResolvedPath, _creaseMethod: str | pxr.Ar.ResolvedPath, _triangleSubdivision: str | pxr.Ar.ResolvedPath, _creaseIndices: pxr.Vt.IntArray | typing.Iterable[int], _creaseLengths: pxr.Vt.IntArray | typing.Iterable[int], _creaseWeights: pxr.Vt.FloatArray | typing.Iterable[float], _cornerIndices: pxr.Vt.IntArray | typing.Iterable[int], _cornerWeights: pxr.Vt.FloatArray | typing.Iterable[float], /) -> None: ...
    def ComputeHash(self) -> int:
        """
        Returns the hash value of this topology to be used for instancing.
        """
    def GetCornerIndices(self) -> pxr.Vt.IntArray:
        """
        Returns the edge corner indices.
        """
    def GetCornerWeights(self) -> pxr.Vt.FloatArray:
        """
        Returns the edge corner weights.
        """
    def GetCreaseIndices(self) -> pxr.Vt.IntArray:
        """
        Returns the edge crease indices.
        """
    def GetCreaseLengths(self) -> pxr.Vt.IntArray:
        """
        Returns the edge crease loop lengths.
        """
    def GetCreaseMethod(self) -> str:
        """
        Returns the creasing method.
        """
    def GetCreaseWeights(self) -> pxr.Vt.FloatArray:
        """
        Returns the edge crease weights.
        """
    def GetFaceVaryingInterpolationRule(self) -> str:
        """
        Returns the face-varying boundary interpolation rule.
        """
    def GetTriangleSubdivision(self) -> str:
        """
        Returns the triangle subdivision method.
        """
    def GetVertexInterpolationRule(self) -> str:
        """
        Returns the vertex boundary interpolation rule.
        """
    def SetCornerIndices(self, _cornerIndices: pxr.Vt.IntArray | typing.Iterable[int], /) -> None:
        """
        Set the edge corner indices.
        """
    def SetCornerWeights(self, _cornerWeights: pxr.Vt.FloatArray | typing.Iterable[float], /) -> None:
        """
        Set the edge corner weights.
        """
    def SetCreaseIndices(self, _creaseIndices: pxr.Vt.IntArray | typing.Iterable[int], /) -> None:
        """
        Set the edge crease indices.
        """
    def SetCreaseLengths(self, _creaseLengths: pxr.Vt.IntArray | typing.Iterable[int], /) -> None:
        """
        Set the edge crease loop lengths.
        """
    def SetCreaseMethod(self, _creaseMethod: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Set the creasing method.
        """
    def SetCreaseWeights(self, _creaseWeights: pxr.Vt.FloatArray | typing.Iterable[float], /) -> None:
        """
        Set the edge crease weights.
        """
    def SetFaceVaryingInterpolationRule(self, _fvarInterp: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Set the face-varying boundary interpolation rule.
        """
    def SetTriangleSubdivision(self, _triangleSubdivision: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Set the triangle subdivision method.
        """
    def SetVertexInterpolationRule(self, _vtxInterp: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Set the vertex boundary interpolation rule.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

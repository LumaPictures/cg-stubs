# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import FnGeolibProducers as FnGeolibProducers
import LookFileBakeAPI.LookFileUtil as LookFileUtil
import LookFileBakeAPI.OutputFormatAPI as OutputFormatAPI
import PyFnGeolib
import typing
from LookFileBakeAPI.Exceptions import LookFileBakeException as LookFileBakeException
from LookFileBakeAPI.Utils import CheckRootLocations as CheckRootLocations, FindSharedLodGroupLocations as FindSharedLodGroupLocations, GetLookFileProducerRootId as GetLookFileProducerRootId, GetProducerFromOp as GetProducerFromOp
from _typeshed import Incomplete
from typing import Any, Set, Tuple

class BakePrePostHandlerBase:
    def notify(self, assetId: str, rootLocationProducers: dict[str, FnGeolibProducers.GeometryProducer], progressCallback: typing.Callable | None, abortCallback: typing.Callable | None): ...

class LookFileBaker:
    additionalSettings: Any
    includeGlobalAttributes: Any
    includeLodInfo: Any
    materialTreeRootLocations: Any
    outputFormatName: Any
    progressCallback: Any
    sourceAsset: Any
    sourceFile: Any
    traversalObserver: Any
    def __init__(self, outputFormatName: str): ...
    def _appendCelMatchOp(self, op, txn): ...
    def _appendLightsDefaultValuesBackupOp(self, op, txn, rootLocations): ...
    def _getModifiedPassProducer(self, op, rootLocations): ...
    def bake(self, referenceOp: PyFnGeolib.GeolibRuntime.Op, passNamesAndOps, rootLocations: typing.Iterable[str], outputPath) -> list[str]: ...
    def bakeAndPublish(self, referenceOp: PyFnGeolib.GeolibRuntime.Op, passNamesAndOps, rootLocations: typing.Iterable[str], assetId: str, assetArgs: Incomplete | None = ..., preBakeHandler: Incomplete | None = ..., postBakeHandler: Incomplete | None = ...) -> str: ...

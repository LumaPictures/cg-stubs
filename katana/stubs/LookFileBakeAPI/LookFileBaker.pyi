# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import LookFileBakeAPI.LookFileUtil as LookFileUtil
import LookFileBakeAPI.OutputFormatAPI as OutputFormatAPI
import PyFnGeolib
import PyFnGeolibProducers
import typing
from LookFileBakeAPI.Exceptions import LookFileBakeException as LookFileBakeException
from LookFileBakeAPI.Utils import CheckRootLocations as CheckRootLocations, FindSharedLodGroupLocations as FindSharedLodGroupLocations, GetLookFileProducerRootId as GetLookFileProducerRootId, GetProducerFromOp as GetProducerFromOp
from _typeshed import Incomplete
from typing import Set, Tuple

class BakePrePostHandlerBase:
    def notify(self, assetId: str, rootLocationProducers: dict[str, PyFnGeolibProducers.GeometryProducer], progressCallback: typing.Callable | None, abortCallback: typing.Callable | None): ...

class LookFileBaker:
    additionalSettings: Incomplete
    includeGlobalAttributes: Incomplete
    includeLodInfo: Incomplete
    materialTreeRootLocations: Incomplete
    outputFormatName: Incomplete
    progressCallback: Incomplete
    sourceAsset: Incomplete
    sourceFile: Incomplete
    traversalObserver: Incomplete
    def __init__(self, outputFormatName: str) -> None: ...
    @staticmethod
    def _appendCelMatchOp(op, txn): ...
    @staticmethod
    def _appendLightsDefaultValuesBackupOp(op, txn, rootLocations): ...
    @staticmethod
    def _getModifiedPassProducer(op, rootLocations): ...
    def bake(self, referenceOp: PyFnGeolib.GeolibRuntimeOp, passNamesAndOps, rootLocations: typing.Iterable[str], outputPath) -> list[str]: ...
    def bakeAndPublish(self, referenceOp: PyFnGeolib.GeolibRuntimeOp, passNamesAndOps, rootLocations: typing.Iterable[str], assetId: str, assetArgs: Incomplete | None = ..., preBakeHandler: Incomplete | None = ..., postBakeHandler: Incomplete | None = ...) -> str: ...

# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import FnGeolib as FnGeolib
import FnGeolib.GeolibRuntime
import PyFnGeolibServices as FnGeolibServices
import Nodes3DAPI as Nodes3DAPI

class ImplicitOpsManager:
    def __init__(self): ...
    def _ImplicitOpsManager__createOpChainFromOpInfo(self, txn: FnGeolib.GeolibRuntime.Transaction, opsInfo: list[str, Attribute, bool]) -> list[FnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initAfterImplicitOps(self, txn: FnGeolib.GeolibRuntime.Transaction) -> list[FnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initBeforeImplicitOps(self, txn: FnGeolib.GeolibRuntime.Transaction) -> list[FnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initImplicitOps(self, txn: FnGeolib.GeolibRuntime.Transaction) -> list[FnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initOps(self): ...
    def applyAfterImplicitOps(self, txn, op): ...
    def applyBeforeImplicitOps(self, txn, op): ...
    def applyImplicitOps(self, txn, op): ...
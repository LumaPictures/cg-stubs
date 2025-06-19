# mypy: disable-error-code="misc, override, no-redef"

class FixBrokenPixarSchemas:
    """
    A class which takes a usdLayer and clients can apply appropriate fixes
    defined as utility methods of this class, example FixupMaterialBindingAPI.

    Every Fixup method iterates on each prim in the layer and applies specific
    fixes.
    """
    def __init__(self, usdLayer) -> None: ...
    def FixupCoordSysAPI(self):
        '''
        Makes sure CoordSysAPI multiapply schema is applied and the instanced
        binding relationship is used, instead of old non-applied CoordSysAPI
        "coordSys:name" binding.
        '''
    def FixupMaterialBindingAPI(self):
        """
        Makes sure MaterialBindingAPI is applied on the prim, which defines a
        material:binding property spec. Marks the layer updated if fixes are
        applied.
        """
    def FixupSkelBindingAPI(self):
        """
        Makes sure SkelBindingAPI is applied on the prim, which defines
        appropriate UsdSkel properties which are imparted by SkelBindingAPI.
        Marks the layer as updated if fixes are applied.
        """
    def FixupUpAxis(self):
        """
        Makes sure the layer specifies a upAxis metadata, and if not upAxis
        metadata is set to the default provided by UsdGeom. Marks the layer as 
        updated if fixes are applied.
        """
    def IsLayerUpdated(self):
        """
        Returns the update status of the usdLayer, an instance of 
        FixBrokenPixarSchemas is holding. Fixer methods will set 
        self._layerUpdated to True if any of the Fixer methods applies fixes to 
        the layer.
        """
    def _ApplyAPI(self, listOp, apiSchema): ...

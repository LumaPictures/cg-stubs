# mypy: disable-error-code="misc, override, no-redef"

class UsdviewContextMenuItem:
    def isValid(self):
        """ Menu items which have an invalid internal item are considered invalid.
                    Header menus don't contain an internal _item attribute, so we
                    return true in the case of the attribute being undefined.
                    We use this function to give this state a clearer name.
        """

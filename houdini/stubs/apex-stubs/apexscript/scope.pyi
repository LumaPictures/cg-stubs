from _typeshed import Incomplete

class Scope:
    houdini_version: Incomplete
    def __init__(self, houdini_version: str) -> None: ...
    def annotate_identifier(self, apex_name: str, apex_type: str):
        """Records the identifier's type (but does NOT imply assignment)."""
    def assign_identifier(self, apex_name: str, apex_type: str):
        """Records the assignment of an identifier."""
    def identifier_assigned(self, apex_name: str) -> bool:
        """Checks if the identifier has been assigned (not just annotated)."""
    def identifier_type(self, apex_name: str) -> str:
        """Returns the identifier's type from an annotation or assigment."""

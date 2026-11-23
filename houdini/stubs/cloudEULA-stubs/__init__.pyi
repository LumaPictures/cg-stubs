EULA_AGREEMENT: str
EULA_HOUDINI_CLOUD_FAQ_URL: str
EULA_ACCEPTANCE_FILE_NAME: str
EULA_ACCEPTANCE_FILE_PREAMBLE: str

def isEULAAccepted() -> bool:
    """Checks if user license agreement has been accepted. If it has been in the
       past (ie, the file stamp is present), then this function returns True.
       Otherwise, EULA dialog is presented; if accepted, the file stamp is
       written and True returned, otherwise False is returned.
    """

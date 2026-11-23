from types import ModuleType

os: ModuleType

def currentUserName() -> str:
    '''Return the login name of the current user, or "unknown" if it couldn\'t
    be determined.
    '''

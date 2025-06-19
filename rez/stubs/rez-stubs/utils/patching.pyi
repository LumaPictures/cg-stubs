from rez.version import Requirement as Requirement

def get_patched_request(requires, patchlist):
    '''Apply patch args to a request.

    For example, consider:

        >>> print(get_patched_request(["foo-5", "bah-8.1"], ["foo-6"]))
        ["foo-6", "bah-8.1"]
        >>> print(get_patched_request(["foo-5", "bah-8.1"], ["^bah"]))
        ["foo-5"]

    The following rules apply wrt how normal/conflict/weak patches override
    (note though that the new request is always added, even if it doesn\'t
    override an existing request):

    PATCH  OVERRIDES: foo  !foo  ~foo
    -----  ---------- ---  ----  -----
    foo               Y    Y     Y
    !foo              N    N     N
    ~foo              N    N     Y
    ^foo              Y    Y     Y

    Args:
        requires (list of str or `version.Requirement`): Request.
        patchlist (list of str): List of patch requests.

    Returns:
        List of `version.Requirement`: Patched request.
    '''

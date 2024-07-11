# mypy: disable-error-code="misc, override, no-redef"

__MFB_FULL_PACKAGE_NAME: str

def GetConcurrencyLimit() -> int:
    """
    Return the current concurrency limit, always>= 1.


    This value is determined by the underlying concurrency subsystem. It
    may have been set by a third party, by a call to Work API below, or by
    Work itself if the PXR_WORK_THREAD_LIMIT env setting was set. If the
    PXR_WORK_THREAD_LIMIT env setting has been explicitly set to a non-
    zero value, Work will attempt to configure the underlying concurrency
    subsystem to use the specified limit and will ignore concurrency
    limits set via the API calls below.

    Note that this can return a value larger than
    WorkGetPhysicalConcurrencyLimit() if WorkSetConcurrencyLimit() was
    called with such a value, or if PXR_WORK_THREAD_LIMIT was set with
    such a value.
    """
def GetPhysicalConcurrencyLimit() -> int:
    """
    Return the number of physical execution cores available to the
    program.


    This is either the number of physical cores on the machine or the
    number of cores specified by the process's affinity mask, whichever is
    smaller.
    """
def HasConcurrency() -> bool:
    """
    Return true if WorkGetPhysicalConcurrencyLimit() returns a number
    greater than 1 and PXR_WORK_THREAD_LIMIT was not set in an attempt to
    limit the process to a single thread, false otherwise.
    """
def SetConcurrencyLimit(_n: int, /) -> None:
    """
    Set the concurrency limit to C{n}, if C{n} is a non-zero value.


    If C{n} is zero, then do not change the current concurrency limit.

    Note, calling this function with n> WorkGetPhysicalConcurrencyLimit()
    may overtax the machine.

    In general, very few places should call this function. Call it in
    places where the number of allowed threads is dictated, for example,
    by a hosting environment. Lower-level module code should never call
    this function.
    """
def SetConcurrencyLimitArgument(_n: int, /) -> None:
    """
    Sanitize C{n} as described below and set the concurrency limit
    accordingly.


    This function is useful for interpreting command line arguments.

    If C{n} is zero, then do not change the current concurrency limit.

    If C{n} is a positive, non-zero value then call
    WorkSetConcurrencyLimit(n). Note that calling this method with C{n}
    greater than the value returned by WorkGetPhysicalConcurrencyLimit()
    may overtax the machine.

    If C{n} is negative, then set the concurrency limit to all but abs(
    C{n}) cores. The number of cores is determined by the value returned
    by WorkGetPhysicalConcurrencyLimit() . For example, if C{n} is -2,
    then use all but two cores. If abs( C{n}) is greater than the number
    of physical cores, then call WorkSetConcurrencyLimit(1), effectively
    disabling concurrency.
    """
def SetMaximumConcurrencyLimit() -> None:
    """
    Set the concurrency limit to be the maximum recommended for the
    hardware on which it's running.


    Equivalent to: ::

      WorkSetConcurrencyLimit(WorkGetPhysicalConcurrencyLimit()).

    """

def platform_mapped(func):
    '''Decorates functions for lookups within a config.platform_map dictionary.

    The first level key is mapped to the func.__name__ of the decorated function.
    Regular expressions are used on the second level key, values.
    Note that there is no guaranteed order within the dictionary evaluation. Only the first matching
    regular expression is being used.
    For example:

    .. code-block:: python

       config.platform_map = {
           "os": {
               r"Scientific Linux-(.*)": r"Scientific-\\1",    # Scientific Linux-x.x -> Scientific-x.x
               r"Ubuntu-14.\\d": r"Ubuntu-14",                 # Any Ubuntu-14.x      -> Ubuntu-14
           },
           "arch": {
               "x86_64": "64bit",                             # Maps both x86_64 and amd64 -> 64bit (don\'t)
               "amd64": "64bit",
           },
       }
    '''

def getMyIPAddress() -> str | None:
    """Get my IP address from an external web server that displays it.

    Unfortunately, the only way to get this machine's externally-visible IP
    address is to get another machine on the internet to tell it to us.

    Return None if the IP address could not be determined.
    """
def getMyLatLong() -> tuple[float, float] | None:
    """Return a tuple of (latitude, longitude) values for our location, based
    off my IP address.

    Return None if the location could not be determined.
    """
def getMyTimezoneOffset() -> float | None:
    """Return the offset of this timezone from GMT, accounting for whether or
    not daylight savings time is in effect.
    """
def doesAddressMatchNetMask(address: str, mask: str) -> bool:
    """Returns True if the address (xxx.xxx.xxx.xxx) matches the given CIDR
    netmask (xxx.xxx.xxx.xxx/xx).
    """

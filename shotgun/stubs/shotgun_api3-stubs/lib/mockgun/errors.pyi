class MockgunError(Exception):
    """
    Base for all Mockgun related API Errors.
    These are errors that relate to mockgun specifically, for example
    relating to mockups setup and initialization. For operational errors,
    mockgun raises ShotgunErrors just like the Shotgun API.
    """

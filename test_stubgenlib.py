import stubgenlib

from mypy.stubdoc import FunctionSig, ArgSig

# def test_boost_docstrings():
#     docstr = """
# __init__( (object)arg1) -> None

# __init__( (object)arg1 [, (Camera)arg2]) -> None

# __init__( (object)arg1 [, (Matrix4d)transform=Gf.Matrix4d(1.0, 0.0, 0.0, 0.0,
#             0.0, 0.0, 0.0, 1.0) [, (object)projection=Gf.Camera.Perspective [, (float)horizontalAperture=20.955 [, (float)verticalAperture=15.290799999999999 [, (float)horizontalApertureOffset=0.0 [, (float)verticalApertureOffset=0.0 [, (float)focalLength=50.0 [, (Range1f)clippingRange=Gf.Range1f(1.0, 1000000.0) [, (object)clippingPlanes=[] [, (float)fStop=0.0 [, (float)focusDistance=0.0]]]]]]]]]]]) -> None"""


#     expected = """
# __init__( arg1: object) -> None

# __init__( arg1: object , arg2: Camera = ...) -> None

# __init__( arg1: object , transform: Matrix4d = ..., projection: object = ..., horizontalAperture: float = ..., verticalAperture: float = ..., horizontalApertureOffset: float = ..., verticalApertureOffset: float = ..., focalLength: float = ..., clippingRange: Range1f = ..., clippingPlanes: object = ..., fStop: float = ..., focusDistance: float = ...) -> None"""
#     print(stubgenlib.BoostDocstringSignatureGenerator.standardize_docstring(docstr))
#     assert stubgenlib.BoostDocstringSignatureGenerator.standardize_docstring(docstr) == expected

#     docstr = """
# __init__( (object)arg1, (object)arg2) -> None

# __init__( (object)arg1 [, (Path)arg2]) -> None"""

#     expected = """
# __init__( arg1: object, arg2: object) -> None

# __init__( arg1: object , arg2: Path = ...) -> None"""
#     print(stubgenlib.BoostDocstringSignatureGenerator.standardize_docstring(docstr))
#     assert stubgenlib.BoostDocstringSignatureGenerator.standardize_docstring(docstr) == expected


def test_boost_docstring_overloads():
    docstr = """
__init__( (object)arg1) -> None

__init__( (object)arg1 [, (Camera)arg2]) -> None :

__init__( (object)arg1 [, (Matrix4d)transform=Gf.Matrix4d(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0) [, (object)projection=Gf.Camera.Perspective [, (float)apertureOffset=0.0 [, (Range1f)clippingRange=Gf.Range1f(1.0, 10000.0) [, (object)clippingPlanes=[] [, (float)fStop=0.0]]]]]]) -> None"""

    result = stubgenlib.infer_sig_from_boost_docstring(docstr, "__init__")
    import pprint

    pprint.pprint(result)
    assert result == [
        FunctionSig(
            name='__init__',
            args=[ArgSig(name='arg1', type='object', default=False)],
            ret_type='None',
        ),
        FunctionSig(
            name='__init__',
            args=[
                ArgSig(name='arg1', type='object', default=False),
                ArgSig(name='arg2', type='Camera', default=True),
            ],
            ret_type='None',
        ),
        FunctionSig(
            name='__init__',
            args=[
                ArgSig(name='arg1', type='object', default=False),
                ArgSig(name='transform', type='Matrix4d', default=True),
                ArgSig(name='projection', type='object', default=True),
                ArgSig(name='apertureOffset', type='float', default=True),
                ArgSig(name='clippingRange', type='Range1f', default=True),
                ArgSig(name='clippingPlanes', type='object', default=True),
                ArgSig(name='fStop', type='float', default=True),
            ],
            ret_type='None',
        ),
    ]


def test_boost_docstring_existing_description():
    docstr = """
Find( (object)identifier [, (dict)args={}]) -> Layer :
    Find(filename) -> LayerPtr
    
    filename : string
    
    Returns the open layer with the given filename, or None.  Note that this is a static class method.
"""
    result = stubgenlib.infer_sig_from_boost_docstring(docstr, "Find")
    assert result == [
        FunctionSig(
            name='Find',
            args=[
                ArgSig(name='identifier', type='object', default=False),
                ArgSig(name='args', type='dict', default=True),
            ],
            ret_type='Layer',
        )
    ]

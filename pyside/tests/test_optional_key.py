from __future__ import absolute_import, print_function

import pytest


@pytest.mark.skip(reason="can't import pyside_stubgen")
def test_optiona_key():
    from stubgen_pyside import OptionalKey

    assert OptionalKey("foo") == None
    assert OptionalKey("foo") == "foo"
    assert OptionalKey("foo") == OptionalKey(None)
    {OptionalKey(None): "this"}[OptionalKey("foo")]
    {OptionalKey("foo"): "this"}[OptionalKey("foo")]
    # {(None, 'bar'): 'this'}[(OptionalKey('foo'), 'bar')]
    {OptionalKey(None): "this"}[OptionalKey("foo")]
    {(OptionalKey(None), "bar"): "this"}[(OptionalKey("foo"), "bar")]

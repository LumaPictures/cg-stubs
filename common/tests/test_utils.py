from __future__ import absolute_import, print_function

from mypy.stubgenc import ArgSig, FunctionSig

from stubgenlib.utils import merge_signatures


def test_merge():
    assert merge_signatures(
        FunctionSig(
            name="foo",
            args=[
                ArgSig("first"),
                ArgSig("second"),
            ],
            ret_type="str",
        ),
        FunctionSig(
            name="foo",
            args=[
                ArgSig("second", type="str"),
            ],
            ret_type="str",
        ),
    ) == FunctionSig(
        name="foo",
        args=[
            ArgSig("first"),
            ArgSig("second", type="str"),
        ],
        ret_type="str",
    )

    assert merge_signatures(
        FunctionSig(
            name="foo",
            args=[
                ArgSig("first"),
                ArgSig("second"),
            ],
            ret_type="str",
        ),
        FunctionSig(
            name="foo",
            args=[
                ArgSig("third", type="str"),
            ],
            ret_type="str",
        ),
    ) == FunctionSig(
        name="foo",
        args=[
            ArgSig("first"),
            ArgSig("second"),
        ],
        ret_type="str",
    )

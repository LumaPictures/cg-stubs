from __future__ import absolute_import, print_function

from mypy.stubgenc import ArgSig, FunctionSig

from stubgenlib.utils import merge_signature_kwargs, merge_signatures


def test_basic_merge():
    # ok if argument length does not match:
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

    # extra arguments in the second sig are not copied to the first
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


def test_special_merge():
    dest = FunctionSig(
        name="__getitem__",
        args=[
            ArgSig("self"),
            ArgSig("arg"),
        ],
        ret_type="str",
    )
    assert dest.is_special_method()

    assert merge_signatures(
        dest,
        FunctionSig(
            name="__getitem__",
            args=[
                ArgSig("self"),
                # different name
                ArgSig("item", type="str"),
            ],
            ret_type="str",
        ),
    ) == FunctionSig(
        name="__getitem__",
        args=[
            ArgSig("self"),
            ArgSig("arg", type="str"),
        ],
        ret_type="str",
    )

    assert merge_signatures(
        FunctionSig(
            name="__getitem__",
            args=[
                ArgSig("self"),
                ArgSig("arg"),
            ],
            ret_type="str",
        ),
        FunctionSig(
            name="__getitem__",
            args=[
                ArgSig("self"),
                # different number of args
                ArgSig("first"),
                ArgSig("second", type="str"),
            ],
            ret_type="str",
        ),
    ) == FunctionSig(
        name="__getitem__",
        args=[
            ArgSig("self"),
            ArgSig("arg"),
        ],
        ret_type="str",
    )


def test_kwarg_merge():
    assert merge_signature_kwargs(
        FunctionSig(
            name="foo",
            args=[
                ArgSig("*args", type="str"),
                ArgSig("**kwargs"),
            ],
            ret_type=None,
        ),
        FunctionSig(
            name="foo",
            args=[
                ArgSig("arg"),
                ArgSig("*"),
                ArgSig("keyword1", type="str"),
                ArgSig("keyword2", type="int"),
            ],
            ret_type="str",
        ),
        replace_kwargs=True,
    ) == FunctionSig(
        name="foo",
        args=[
            ArgSig("*args", type="str"),
            ArgSig("keyword1", type="str"),
            ArgSig("keyword2", type="int"),
        ],
        ret_type="str",
    )

    # No change in args, bc kwargs is missing
    assert merge_signature_kwargs(
        FunctionSig(
            name="foo",
            args=[
                ArgSig("*args", type="str"),
            ],
            ret_type=None,
        ),
        FunctionSig(
            name="foo",
            args=[
                ArgSig("arg"),
                ArgSig("*"),
                ArgSig("keyword1", type="str"),
                ArgSig("keyword2", type="int"),
            ],
            ret_type="str",
        ),
        replace_kwargs=True,
    ) == FunctionSig(
        name="foo",
        args=[
            ArgSig("*args", type="str"),
        ],
        ret_type="str",
    )

    assert merge_signature_kwargs(
        FunctionSig(
            name="foo",
            args=[
                ArgSig("arg"),
                ArgSig("**kwargs"),
            ],
            ret_type=None,
        ),
        FunctionSig(
            name="foo",
            args=[
                ArgSig("*"),
                ArgSig("keyword1", type="str"),
                ArgSig("keyword2", type="int"),
            ],
            ret_type="str",
        ),
        replace_kwargs=True,
    ) == FunctionSig(
        name="foo",
        args=[
            ArgSig("arg"),
            ArgSig("*"),
            ArgSig("keyword1", type="str"),
            ArgSig("keyword2", type="int"),
        ],
        ret_type="str",
    )

    assert merge_signature_kwargs(
        FunctionSig(
            name="foo",
            args=[
                ArgSig("pos_only"),
                ArgSig("/"),
                ArgSig("pos_or_kw"),
                ArgSig("*"),
                ArgSig("kw_only"),
                ArgSig("**kwargs"),
            ],
            ret_type=None,
        ),
        FunctionSig(
            name="foo",
            args=[
                ArgSig("*"),
                ArgSig("keyword1", type="str"),
                ArgSig("keyword2", type="int"),
            ],
            ret_type="str",
        ),
        replace_kwargs=True,
    ) == FunctionSig(
        name="foo",
        args=[
            ArgSig("pos_only"),
            ArgSig("/"),
            ArgSig("pos_or_kw"),
            ArgSig("*"),
            ArgSig("kw_only"),
            ArgSig("keyword1", type="str"),
            ArgSig("keyword2", type="int"),
        ],
        ret_type="str",
    )

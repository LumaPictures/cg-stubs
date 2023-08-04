from __future__ import absolute_import, division, print_function


import hou


class SizedItems(object):
    """
    This is the bare minimum object required to instantiate data objects in Houdini.

    Possibly other types of objects as well.
    """

    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        return self._data[item]

    # def __iter__(self):
    #     return iter(self._data)


def test_matrix2():
    hou.Matrix2(
        SizedItems(
            [
                SizedItems(range(2)),
                SizedItems(range(2)),
            ]
        )
    )

    hou.Matrix2(SizedItems(range(4)))


def test_matrix3():
    hou.Matrix3(
        SizedItems(
            [
                SizedItems(range(3)),
                SizedItems(range(3)),
                SizedItems(range(3)),
            ]
        )
    )
    hou.Matrix3(SizedItems(range(9)))


def test_matrix4():
    hou.Matrix4(
        SizedItems(
            [
                SizedItems(range(4)),
                SizedItems(range(4)),
                SizedItems(range(4)),
                SizedItems(range(4)),
            ]
        )
    )
    hou.Matrix4(SizedItems(range(16)))

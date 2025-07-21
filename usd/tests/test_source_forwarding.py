#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A demonstration of how to get the leaf-target values of a USD relationship."""

# IMPORT THIRD-PARTY LIBRARIES
from pxr import Usd


def test():
    """Run the main execution of the current script."""
    stage = Usd.Stage.Open("fixtures/source_forwarding.usda")
    prim = stage.GetPrimAtPath("/SomePrim")

    relationship = prim.GetRelationship("another")
    print('This is the raw target value "{}"'.format(relationship.GetTargets()))
    print(
        'But this is the true location "{}"'.format(relationship.GetForwardedTargets())
    )

    variant_sets = prim.GetVariantSets()
    variant_set = variant_sets.GetVariantSet("forwarding_variant_set")

    for variant in variant_set.GetVariantNames():
        variant_set.SetVariantSelection(variant)

        print('This is the raw target value "{}"'.format(relationship.GetTargets()))
        print(
            'But this is the true location "{}"'.format(
                relationship.GetForwardedTargets()
            )
        )


if __name__ == "__main__":
    test()

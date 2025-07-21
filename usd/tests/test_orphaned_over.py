#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT THIRD-PARTY LIBRARIES
from pxr import Usd

def test():
    """Run the main execution of the current script."""
    stage = Usd.Stage.Open("fixtures/over.usda")

    # Method 1: Search everything and filter out only what you need This
    # method is the "best" because it crosses composition arcs and finds
    # nested overs even if they're layered between concrete Prims
    #
    print(list(prim for prim in stage.TraverseAll() if not prim.IsDefined()))

    # Method 2: Search all Layers in the stage, recursively (follows
    # payloads and other composition arcs but does not follow all Prims)
    #
    print(list(stage.Traverse(~Usd.PrimIsDefined)))

    # Method 3: Search the opened stage Layer
    print(list(Usd.PrimRange.Stage(stage, ~Usd.PrimIsDefined)))


if __name__ == "__main__":
    test()

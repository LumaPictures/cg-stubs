# mypy: disable-error-code="misc, override, no-redef"

import pxr.Gf as Gf
import pxr.Ts as Ts
from pxr.Ts.TsTest_Comparator import TsTest_Comparator as TsTest_Comparator
from pxr.Ts.TsTest_Grapher import TsTest_Grapher as TsTest_Grapher

class _Baseliner:
    def __init__(self, testName, splineData, samples, precision) -> None: ...
    def Validate(self): ...
    def _ReadBaseline(self, infile, path): ...
    def _ValidateInputs(self): ...
    def _ValidateValues(self): ...
    def _WriteBaseline(self): ...
    def _WriteCandidates(self): ...
    def _WriteDiffGraph(self): ...
    def _WriteSingleGraph(self): ...

def TsTest_CompareBaseline(testName, splineData, samples, precision: int = ...):
    '''
    A test helper function for spline evaluation.  Compares samples against the
    contents of a baseline file, and returns whether they match within the
    specified precision.

    Precision is specified as a number of decimal digits to the right of the
    decimal point.

    One of the following will occur:

    - If there is no baseline file yet, a candidate baseline file will be
    written to the test run directory, along with a graph made from the spline
    data and samples.  If the graph looks right, both of these files should be
    copied into the test source, such that they are installed into a "baseline"
    subdirectory of the test run directory.  (The graph isn\'t necessary for
    operation of the test, but is a useful reference for maintainers.)  The
    function will return False in this case.

    - If the spline data, sample times, or precision differ from those recorded
    in the baseline file, that is an error in the test setup; it is a difference
    in the test inputs rather than the outputs.  Candidate baseline files will
    be written as in the above case, and the function will return False.  If the
    inputs are being changed deliberately, the new baseline files should be
    inspected and installed.

    - If any sample values differ from the baseline values by more than the
    specified precision, all differing samples will be listed on stdout,
    candidate baseline files will be written, a graph of the differences will
    also be written, and the function will return False.  If the change in
    output is expected, the diff graph should be inspected and the new baseline
    files installed.

    - Otherwise, no files will be written, and the function will return True.
    '''

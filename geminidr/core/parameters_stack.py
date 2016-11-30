# This parameter file contains the parameters related to the primitives located
# in the primitives_ccd.py file, in alphabetical order.

from geminidr import ParametersBASE

class ParametersStack(ParametersBASE):
    alignAndStack = {
        "check_if_stack"    : False,
    }
    stackFrames = {
        "suffix"            : "_stack",
        "mask"              : True,
        "nhigh"             : 1,
        "nlow"              : 1,
        "operation"         : "average",
        "reject_method"     : "avsigclip",
    }
    stackSkyFrames = {
        "suffix"            : "_skyStacked",
        "mask"              : True,
        "nhigh"             : 1,
        "nlow"              : 1,
        "operation"         : "median",
        "reject_method"     : "avsigclip",
    }
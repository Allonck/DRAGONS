# ------------------------------------------------------------------------------
from inspect import stack

from gempy.utils import logutils

# ------------------------------------------------------------------------------
class PrimitivesSoarBASE(object):

    tagset = None

    def __init__(self, adinputs, mode = 'sq', **kwargs):
        self.log      = logutils.get_logger(__name__)
        self.myself   = lambda: stack()[1][3]
        self.streams = {'main': adinputs}
        self._initialize(adinputs, mode=mode, **kwargs)
        self.adinputs = adinputs

    def _initialize(self, adinputs, mode='sq', **kwargs):
        # This is a general config file so we should load it now. Some of its
        # information may be overridden by other parameters passed here.

        self.streams          = {'main': adinputs}
        self.mode             = mode
        self.params           = {}
        self.log              = logutils.get_logger(__name__)

    def _inherit_params(self, params, primname, pass_suffix=False):
        """Create a dict of params for a primitive from a larger dict,
        using only those that the primitive needs

        Parameters
        ----------
        params: dict
            parent parameter dictionary
        primname: str
            name of primitive to be called
        pass_suffix: bool
            pass "suffix" parameter?
        """
        return {k: v for k, v in params.items()
                if k in list(self.params[primname]) and
                not (k == "suffix" and not pass_suffix)}

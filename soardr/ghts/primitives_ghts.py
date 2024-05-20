#
#                                                                         soardr
#
#                                                          primitives_ghts.py
# ------------------------------------------------------------------------------
from gempy.gemini import gemini_tools as gt
from soar_instruments.ghts import (lookup as adlookup)

from inspect import isclass, currentframe

from ..soar.primitives_soar import Soar
from . import parameters_ghts

from ..utils.logging_handlers import log_adjust
# ------------------------------------------------------------------------------

class GHTS(Soar):
    """
    This is the class containing the generic Gemini primitives.

    """
    tagset = {"GHTS"}

    def _initialize(self, adinputs, **kwargs):
        self.inst_lookups = 'soardr.ghst.lookups'
        self.inst_adlookup = adlookup
        super()._initialize(adinputs, **kwargs)
        self._param_update(parameters_ghts)

    def _param_update(self, module):
        """Create/update an entry in the primitivesClass's params dict;
        this will be initialized later"""
        for attr in dir(module):
            obj = getattr(module, attr)
            if isclass(obj) and issubclass(obj, config.Config):
                # Allow classes purely for inheritance purposes to be ignored
                # Wanted to use hasattr(self) but things like NearIR don't inherit
                if attr.endswith("Config"):
                    primname = attr.replace("Config", "")
                    self.params[primname] = obj()

    def gudayMate(self, adinputs=None, **params):

        log = self.log
        log.stdinfo(gt.log_message("primitive", self.myself(), "starting"))
        for ad in self.adinputs:
            log.stdinfo("Hello World! This is {}".format(ad.filename))
            log.stdinfo("Sporting a tagset: {}".format(ad.tags))
            log.stdinfo("Coming to you from {}.".format(self.myself()))

        return
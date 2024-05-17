#
#                                                                         soardr
#
#                                                          primitives_ghts.py
# ------------------------------------------------------------------------------
from gempy.gemini import gemini_tools as gt

from soar_instruments.ghts import lookup as adlookup

from ..soar.primitives_soar import Soar

from . import parameters_ghts

from ..utils.logging_handlers import log_adjust
# ------------------------------------------------------------------------------
@log_adjust
class GHTS(Soar):
    """
    This is the class containing the generic Gemini primitives.

    """
    tagset = {"GHTS"}

    def _initialize(self, adinputs, **kwargs):
        self.inst_lookups = 'soardr.ghts.lookups'
        self.inst_adlookup = adlookup
        super()._initialize(adinputs, **kwargs)
        self._param_update(parameters_ghts)

    def gudayMate(self, *args, **kwargs):

        log = self.log
        log.stdinfo(gt.log_message("primitive", self.myself(), "starting"))
        for ad in self.adinputs:
            log.stdinfo("Hello World! This is {}".format(ad.filename))
            log.stdinfo("Sporting a tagset: {}".format(ad.tags))
            log.stdinfo("Coming to you from {}.".format(self.myself()))

        return
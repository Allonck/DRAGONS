#
#                                                                         soardr
#
#                                                             primitives_soar.py
# ------------------------------------------------------------------------------
from gempy.gemini import gemini_tools as gt

from soardr import PrimitivesSoarBASE

from ..utils.logging_handlers import log_adjust
# ------------------------------------------------------------------------------

class Soar(PrimitivesSoarBASE):
    
    tagset = {"SOAR"}

    def _initialize(self, adinputs, **kwargs):
        super()._initialize(adinputs, **kwargs)
        #self._param_update(parameters_gemini)

    def helloWorld(self, *args, **params):
        log = self.log
        log.stdinfo(gt.log_message("primitive", self.myself(), "starting"))
        for ad in self.adinputs:
            log.stdinfo("Hello World! This is {}".format(ad.filename))
            log.stdinfo("Sporting a tagset: {}".format(ad.tags))
            log.stdinfo("Coming to you from {}.".format(self.myself()))

        return

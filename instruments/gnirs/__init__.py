__all__ = ['AstroDataF2']

from astrodata import factory
from ..gemini import addInstrumentFilterWavelengths
from .adclass import AstroDataGnirs
from .lookup import filter_wavelengths

factory.addClass(AstroDataGnirs)
addInstrumentFilterWavelengths('GNIRS', filter_wavelengths)

__all__ = ['AstroData', 'AstroDataError', 'TagSet',
           'astro_data_descriptor', 'astro_data_tag', 'keyword',
           'descriptor_list',
           'open', 'create']

from .core import *
from .fits import AstroDataFits, KeywordCallableWrapper

from .factory import AstroDataFactory

keyword = KeywordCallableWrapper

factory = AstroDataFactory()
# Let's make sure that there's at least one class that matches the data
# (if we're dealing with a FITS file)
factory.addClass(AstroDataFits)

open = factory.getAstroData
create = factory.createFromScratch

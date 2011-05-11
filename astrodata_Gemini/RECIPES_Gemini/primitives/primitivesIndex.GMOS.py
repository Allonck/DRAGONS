# this is added to the reduction object dictionary, but only one
# reduction object per astro data type.
# NOTE: primitives are the member functions of a Reduction Object.

localPrimitiveIndex = {
    # "GEMINI": ("primitives_GEMINI.py", "GEMINIPrimitives"),
    "GMOS": ("primitives_GMOS.py", "GMOSPrimitives"),
    "GMOS_IMAGE": ("primitives_GMOS_IMAGE.py", "GMOS_IMAGEPrimitives"),
    "GMOS_SPECT": ("primitives_GMOS_SPECT.py", "GMOS_SPECTPrimitives"),
    "GMOS_LS_ARC": ("primitives_GMOS_LS_ARC.py", "GMOS_LS_ARCPrimitives"),
    "GMOS_IMAGE": ("primitives_alignment_GMOS_IMAGE.py","GMOS_IMAGE_alignment_Primitives"),
    }

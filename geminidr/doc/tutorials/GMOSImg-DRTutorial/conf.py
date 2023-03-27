#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os

on_rtd = os.environ.get('READTHEDOCS') == 'True'

# relative_path = './../../../../'
# dragons_path = os.path.normpath(os.path.join(os.getcwd(), relative_path))
# sys.path.append(dragons_path)
#
# import astrodata
#
# print('\n Printing current working directory for debugging:')
# print((' Current working directory: {}'.format(os.getcwd())))
# print((' Dragons path: {}\n'.format(dragons_path)))


# -- Project information -----------------------------------------------------

project = 'DRAGONS Tutorial<br> GMOS Imaging Data Reduction'
copyright = '2023, Association of Universities for Research in Astronomy'
author = 'DRAGONS Team'

# The short X.Y version
#version = astrodata.version(short=True)
version = '3.1'

# The full version, including alpha/beta/rc tags
#release = astrodata.version()
release = '3.1.0'
rtdurl = 'v'+release
#release = '3.1.x'
#rtdurl = 'release-'+release
#rtdurl = 'latest'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = 'April 2023'
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# hello world
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DRAGONSTutorial-GMOStut'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'DRAGONSTutorial-GMOStut.tex', 'DRAGONS Tutorial - GMOS Data Reduction',
     'DRAGONS Team', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dragonstutorial-gmos', 'DRAGONS Tutorial - GMOS Data Reduction',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    master_doc,
    'DRAGONSTutorial-GMOSDataReduction',
    'DRAGONS Tutorial - GMOS Data Reduction',
    author,
    'DRAGONSTutorial-GMOS',
    'A quick tutorial on how to reduce GMOS images with the DRAGONS command line tools',
    'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
#    'astrodata': ('https://astrodata-user-manual.readthedocs.io/en/latest/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
    'gemini_instruments': ('https://dragons-recipe-system-programmers-manual.readthedocs.io/en/latest/', None),
    'geminidr': ('https://dragons-recipe-system-programmers-manual.readthedocs.io/en/latest/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Finishing with a setup that will run always -----------------------------
def setup(app):

    # -- Adding custom styles ---
    app.add_css_file('css/code.xref-styles.css')
    app.add_css_file('css/todo-styles.css')
    app.add_css_file('css/copy_code_block.css')

    # -- Adding custom behavior ---
    # -- Will leave this out for now until I manage to get the behavior I want
    # app.add_js_file('js/copy_code_block.js')
    # app.add_js_file('https://cdn.jsdelivr.net/npm/clipboard@1/dist/clipboard.min.js')

rst_epilog = """
.. role:: raw-html(raw)
   :format: html

.. |caldb| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/caldb.html" target="_blank">caldb</a>`
.. |dataselect| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/supptools.html#dataselect" target="_blank">dataselect</a>`
.. |descriptors| replace:: :raw-html:`<a href="https://astrodata.readthedocs.io/en/{v}/appendix_descriptors.html" target="_blank">descriptors</a>`
.. |descriptor| replace:: :raw-html:`<a href="https://astrodata.readthedocs.io/en/{v}/appendix_descriptors.html" target="_blank">descriptors</a>`
.. |reduce| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/reduce.html" target="_blank">reduce</a>`
.. |showd| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/supptools.html#showd" target"_blank">showd</a>`
.. |showrecipes| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/supptools.html#showrecipes" target="_blank">showrecipes</a>`
.. |showpars| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/supptools.html#showpars" target="_blank">showpars</a>`
.. |typewalk| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/supptools.html#typewalk" target="_blank">typewalk</a>`
.. |atfile| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/reduce.html#the-file-facility" target="_blank">"at-file" Facility</a>`
.. |astrodatauser| replace:: :raw-html:`<a href="https://astrodata.readthedocs.io/en/{v}/usermanual/index.html" target="_blank">Astrodata User Manual</a>`

.. |DRAGONS| replace:: :raw-html:`<a href="https://dragons.readthedocs.io/en/{v}/" target="_blank">DRAGONS</a>`
.. |RSUser|  replace:: :raw-html:`<a href="http://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/">Recipe System Users Manual</a>`

.. |suptools| replace:: :raw-html:`<a href="https://dragons-recipe-system-users-manual.readthedocs.io/en/{v}/supptools.html" target="_blank">Supplemental Tools</a>`

""".format(v = rtdurl)

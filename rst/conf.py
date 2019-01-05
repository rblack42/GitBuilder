# -*- coding: utf-8 -*-

import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'GitBuilder'
copyright = '2018, Roie R. Black'
author = 'Roie R. Black'

version = '0.0.1'
release = '0.0.1'
language = None
today_fmt = '%B %d, %Y'

# -- General configuration ---------------------------------------------------

extensions = [ 
    'sphinx.ext.imgmath',
    'sphinx.ext.githubpages',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_options = { }
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_use_smartypants = True
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
html_last_updated_fmt = '%b %d, %Y'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt',
    'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'GitBuilder.tex', 'Git Builder',
     'Roie R. Black', 'manual'),
]

# -- Extension configuration -------------------------------------------------

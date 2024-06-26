'''
Author: LetMeFly
Date: 2024-06-04 16:27:24
LastEditors: LetMeFly
LastEditTime: 2024-06-04 20:43:13
'''
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setup import version

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BUCTOJ'
copyright = '2024, Tisfy'
author = 'Tisfy'

release = version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
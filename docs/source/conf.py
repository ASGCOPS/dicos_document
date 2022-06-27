# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DiCOS Document'
copyright = '2022, ASGC'
author = 'Jing-Ya You, Felix Lee, Mike Yang, Chih-Ting Chao'

release = '1'
version = '0.3.0'

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

# ------ customize setting
html_logo = 'image/dicos.png'
html_context = {
    'display_github': False,
}
html_theme_options = {
    'style_nav_header_background' : "#CCCCCC"
}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os, sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'text-advanced'
copyright = '2026, Monil Darediya'
author = 'Monil Darediya'
release = '0.1.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'autodoc2',
    'sphinx.ext.napoleon'
]

autodoc2_packages = [
    "../../text_advanced"
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_theme_options = {
    "dark_code": True,
    "color_mode": "dark"
}
html_static_path = ['_static']

autodoc2_render_as_dir = "apidocs"
autodoc2_output_dir = "apidocs"
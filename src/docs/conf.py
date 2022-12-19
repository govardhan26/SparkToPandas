# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SparkToPandas'
copyright = '2022, Govardhan Selvaraj'
author = 'Govardhan Selvaraj'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
            ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


twine upload -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDlhMTc5YTBmLTRkMjItNDVhNC04MzQwLTgzYTkwODZjOGY5MQACKlszLCIyMjJkYWRjMy1hNzdkLTRkYmEtYjRjYi0zNjI3OTNmNGRkNDUiXQAABiAWSKj0vt-kgIcyaj2Bxw5O7f8hLifcpqKuFONJ9If2gg --repository-url https://upload.pypi.org/legacy/ dist/*

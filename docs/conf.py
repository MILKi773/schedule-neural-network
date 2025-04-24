# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('D:\Python\schedule-neural-network'))

project = 'Shedule Neural Network'
copyright = '2025, Stepan'
author = 'Stepan'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 4,       # Глубина навигации
    'show_nav_level': 1,         # Уровень отображения навигации
    'collapse_navigation': True, # Сворачивание навигации
    'logo_only': False,          # Показывать только логотип (если есть)
    'home_page_in_toc': True,    # Добавить главную страницу в оглавление
}

html_css_files = [
    'custom.css',  # Мы создадим этот файл для кастомизации
]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Для поддержки Google-style docstrings
    'sphinx.ext.viewcode',
]
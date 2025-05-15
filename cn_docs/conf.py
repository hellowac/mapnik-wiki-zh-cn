# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "mapnik-wiki-zh-cn"
copyright = "2025, hellowac"
author = "hellowac"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "zh_CN"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "furo"
html_static_path = ["_static"]


# 可选：支持 .md 文件
source_suffix = [".rst", ".md"]

# 可选：启用更多 MyST 功能（如 Sphinx 原生指令）
myst_enable_extensions = [
    "amsmath",  # 支持 LaTeX 数学公式
    "colon_fence",  # 允许 ::: 作为代码块分隔符
    "dollarmath",  # 更灵活的数学公式
]

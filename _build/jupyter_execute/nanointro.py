#!/usr/bin/env python
# coding: utf-8

# (myst-content/math)=
# #2. Nanotermodinamikara sarrera
# 
# Mekanika estatistikoak esku artean dugun sistemaren fisika bere osagai mikroskopikoen dinamikaren bidez deskribatzea du erronkatzat.
# Horretarako, sistemaren aldakiz (edo kopiaz) osaturiko multzo estatistikoez baliatzen da.
# Aldaki-kopurua oso handia bada, denboran geldikortasuna eta oreka estatistikoa bermatzen dira, azterketa termodinamikoa abian jartzeko ezinbesteko baldintzak, egiazki.
# Berebat, jakin dakigunez, kanpotik ezarritako askatasun-baldintzen arabera, multzoari berari izaera jakina eman diezaiokegu.
# 
# By default MathJax version 2 is currently used.
# If you are using a lot of math, you may want to try using version 3, which claims to improve load speeds by 60 - 80%:
# 
# ```yaml
# sphinx:
#   config:
#     mathjax_path: https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
# ```
# 
# See the [Sphinx documentation](sphinx:sphinx.ext.mathjax) for details.
# 
# :::
# 
# ## 2. Nanotermodinamikara sarrera
# 
# To insert in-line math use the `$` symbol within a Markdown cell.
# For example, the text `$this_{is}^{inline}$` will produce: $this_{is}^{inline}$.

# ## Math blocks
# 
# You can also include math blocks for separate equations. This allows you to focus attention
# on more complex or longer equations, as well as link to them in your pages. To use a block
# equation, wrap the equation in either `$$` or `\begin` statements.
# 
# For example,
# 
# results in:
# 
# $$
#  \mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V+\mu\mathrm{d}N
# $$

# (math:latex)=
# ### Latex-style math
# 
# You can enable parsing LaTeX-style math blocks with the `amsmath` MyST extension. Enable it by adding the following to `_config.yml`
# 
# ```yaml
# parse:
#   myst_enable_extensions:
#     # don't forget to list any other extensions you want enabled,
#     # including those that are enabled by default!
#     - amsmath
# ```
# 
# Once enabled, you can define math blocks like so:
# 
# ```latex
# \begin{equation}
# a_2=b_2+c_2-d_2+e_2
# \end{equation}
# 
# \begin{align}
# a_{11}& =b_{11}&
#   a_{12}& =b_{12}\\
# a_{21}& =b_{21}&
#   a_{22}& =b_{22}+c_{22}
# \end{align}
# ```
# 
# which results in:
# 
# \begin{equation}
# a_2=b_2+c_2-d_2+e_2
# \end{equation}
# 
# 
# :::{seealso}
# The MyST guides to [dollar math syntax](myst-parser:syntax/math), [LaTeX math syntax](myst-parser:syntax/amsmath), and [how MyST-Parser works with MathJax](myst-parser:syntax/mathjax).
# 
# For advanced use, also see how to [define MathJax TeX Macros](sphinx/tex-macros).
# :::

# ### Numbering equations
# 
# If you'd like to number equations so that you can refer to them later, use the **math directive**.
# It looks like this:
# 
# ````md
# ```{math}
# :label: my_label
# my_math
# ```
# ````
# 
# For example, the following code:
# 
# ````md
# ```{math}
# :label: my_label
# w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
# ```
# ````
# 
# will generate
# 
# ```{math}
# :label: my_label
# E=TS-pV```
# 
# Alternatively you can use the dollar math syntax with a prefixed label:
# 
# ```md
# $$
# E=TS-pV
# $$ (my_other_label)
# ```
# 
# which generates
# 
# $$
#   w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
# $$ (my_other_label)
# 
# :::{note}
# Labels cannot start with an integer, or they won't be able to be referenced and
# will throw a warning message if referenced. For example, `:label: 1` and `:label: 1eq` cannot
# be referenced.
# :::
# 
# ### Linking to equations
# 
# If you have created an equation with a label, you can link to it from within your text
# (and across pages!).
# 
# You can refer to the equation using the label that you've provided by using
# the `{eq}` role. For example:
# 
# ```md
# - A link to an equation directive: {eq}`my_label`
# - A link to a dollar math block: {eq}`my_other_label`
# ```
# 
# results in
# 
# - A link to an equation directive: {eq}`my_label`
# - A link to a dollar math block: {eq}`my_other_label`
# 
# :::{note}
# `\labels` inside LaTeX environment are not currently identified, and so cannot be referenced.
# We hope to implement this in a future update (see [executablebooks/MyST-Parser#202](https://github.com/executablebooks/MyST-Parser/issues/202))!
# :::

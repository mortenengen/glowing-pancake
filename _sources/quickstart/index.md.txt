(quickstart)=
# Quickstart

## Installation

You can install `glopan` with `pip`:

:::{code-block} pwsh
python -m pip install glopan
:::

Remeber to [configure](configuration) `glopan` to get access to all features!

## Basic usage

`glopan` can be imported as a regular Python package or used through the command line interface. You can find some examples of basic usage below.

:::::{tab-set}
::::{tab-item} Python
:sync: python

:::{code-block} python
import glopan
:::
::::

::::{tab-item} CLI
:sync: cli

:::{code-block} pwsh
glopan -h
:::
::::
:::::

Combine several PDFs into one:

:::::{tab-set}
::::{tab-item} Python
:sync: python

:::{code-block} python
glopan.combine_pdfs(['Report.pdf', 'Appendix.pdf'], 'Report_full.pdf')
:::
::::

::::{tab-item} CLI
:sync: cli

:::{code-block} pwsh
glopan combine Report.pdf Appendix.pdf -o Report_full.pdf
:::
::::
:::::

Convert a DOCX file to PDF:

:::::{tab-set}
::::{tab-item} Python
:sync: python

:::{code-block} python
glopan.docx_to_pdf('Report.docs')
:::
::::

::::{tab-item} CLI
:sync: cli

:::{code-block} pwsh
glopan convert Report.docx -tf pdf
:::
::::
:::::

Split a PDF and convert one of its pages into SVG:

:::{code-block} python
glopan.split_pdf('Report.pdf')
glopan.pdf_to_svg('Report_p_5.pdf')
:::

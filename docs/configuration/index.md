(configuration)=
# Configuration

To get access to all the features of `glopan` you need to set the paths to the Inkscape and PS2PDF executables. The easiest way to accomplish this is through the command line interface, e.g.:

:::{code-block} pwsh
glopan config set inkscape_path 'C:\\Program Files\\inkscape\\bin\\inkscape.exe'
:::

and

:::{code-block} pwsh
glopan config set ps2pdf_path 'C:\\Program Files\\gs\\gs9.26\\lib\\ps2pdf.bat'
:::

You can always `list` or `reset` the configuration by typing `glopan config list` or `glopan config reset`.

:::{note}
To get access to all the functionality in `glopan` you need to install the following dependencies:

* [Inkscape](https://inkscape.org/) >= v.1.0.1, for converting from PDF to various graphics formats.
* [Ghostscript](https://www.ghostscript.com/) >= v.9.26, for converting from Postscript to PDF.
* Microsoft Word, for converting from DOCX to PDF.
:::

:::{hint}
When you configure `glopan`, the settings are stored in `glowing-pancake.json` which is located in your home directory. You can always configure `glopan` by editing this file directly.
:::
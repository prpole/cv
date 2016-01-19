CV
==

This repository contains all of the files used to produce my curriculum vitae.  Includes:

* cv.md -- main markdown file for editing
* cv.pdf -- typeset PDF
* cv.html -- HTML output for [website version](http://wythoff.net/cv/)
* addind.py -- [pandoc filter](https://github.com/jgm/pandocfilters) for producing hanging indents
* compile.sh -- shell script for producing HTML and PDF from markdown via Pandoc in one command (i.e. `$ sh compile.sh`)

LaTeX and HTML templates for PDF and web output can be found in my [pandoc-templates](https://github.com/gwijthoff/pandoc-templates) github repository (cv.tex and cv-website.sty, respectively).

Workflow
=========

Edit cv.md directly, then run compile.sh to typeset a PDF and HTML version.

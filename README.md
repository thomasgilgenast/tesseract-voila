tesseract-voila
===============

A voila app to run OCR on images using tesseract.

Quickstart
----------

### Local

    conda env create
    conda activate tesseract-voila
    python -m ipykernel install --user --name tesseract-voila
    jupytext --to ipynb index.py --set-kernel -
    voila --theme dark index.ipynb

### Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/thomasgilgenast/tesseract-voila/HEAD?urlpath=voila%2Frender%2Findex.py)

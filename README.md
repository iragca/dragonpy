<h1 align="center">DragonPy</h1>
<h3 align="center"><a href="https://molab.marimo.io/notebooks/nb_XTP3X6RaGyBfnKMcYcSQvk">
  <img
    src="https://molab.marimo.io/molab-shield.svg"
    alt="Open in molab"
  />
</a></h3>

DragonPy is a lightweight dragonfi.ph API wrapper for Python. Recommended for Analysts and Scientists and great for personal use.

> [!IMPORTANT]
> DragonFi exposes most of their API for free without authentication. Please do not abuse their API. The maintainer(s) of this Python package are not liable for any malicious or abusive acts done.

# Installation

You can install the package with your favorite Python package manager [pip](https://pip.pypa.io/en/stable/installation/) or [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).
- `pip install dragonfipy`
- `uv add dragonfipy`

# Usage

```python
from dragonpy import DragonPy

dpy = DragonPy()

ticker = "ABC"

# Fetch stock metadata
profile = dpy.securities.get_stock_profile(ticker)

# Fetch price history
data = dpy.dashboard.get_delayed_bars(ticker, candleType="1D")
```

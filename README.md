# geo-rampup-project

A sandbox project for getting familiar with geospatial raster data in Python, using `rasterio` and `matplotlib`.

## Data

`data/` contains eVSH NDVI GeoTIFFs for Africa (3km resolution, 2026 day-of-year 213-222):

- `AF_eVSH_NDVI...VI_NDVI...tif` — NDVI band
- `AF_eVSH_NDVI...VI_ACQI...tif` — acquisition quality/index band
- `AF_eVSH_NDVI...VI_QUAL...tif` — quality flags band

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install rasterio matplotlib numpy
```

## Usage

```bash
python load-scene.py
```

Reads the NDVI band, prints its shape/CRS/bounds, and saves a grayscale preview to `first_plot.png`.

# geo-rampup-project

A sandbox project for getting familiar with geospatial raster data in Python, using `rasterio` and `matplotlib`.

## Data

`data/` contains eVSH NDVI GeoTIFFs for Africa (3km resolution, 2026 day-of-year 213-222):

- `AF_eVSH_NDVI...VI_NDVI...tif` — NDVI band
- `AF_eVSH_NDVI...VI_ACQI...tif` — acquisition quality/index band
- `AF_eVSH_NDVI...VI_QUAL...tif` — quality flags band

## Packages

- **rasterio** — reads/writes raster data (GeoTIFFs), giving access to pixel arrays, CRS, bounds, and transforms; also handles operations like clipping a raster to a vector boundary (`rasterio.mask`).
  Think of a raster as a giant grid of colored squares laid over a map, like a spreadsheet where every cell is a tiny square of the Earth with a value (e.g. "how green is this spot"). rasterio is the tool that opens that grid, tells you where on Earth it sits, and lets you cut out just the piece you want.
- **geopandas** — pandas-like DataFrames for vector data (shapefiles, GeoJSON, etc.), with geometry-aware operations like reprojecting (`.to_crs()`) and spatial filtering.
  Think of a shapefile as a table of shapes instead of numbers, like a spreadsheet where each row is a country or state outline instead of a value. geopandas is what reads that table and knows how to draw, move, and compare those shapes.
- **matplotlib** — plots raster arrays and vector layers for quick visual inspection (e.g. grayscale previews of NDVI bands).
  Think of matplotlib as the crayon box: once rasterio or geopandas hands you the grid of numbers or the table of shapes, matplotlib is what draws it on screen so you can actually see it.

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

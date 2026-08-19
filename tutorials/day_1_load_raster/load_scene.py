# Day 1: open a raster scene with rasterio and take a first look at it.
import rasterio
import matplotlib.pyplot as plt

# rasterio.open() doesn't load pixel data yet - it just reads the file's
# metadata (dimensions, CRS, geographic bounds) via the `src` handle.
with rasterio.open('../../data/US_eVSH_NDVI.2026.216-222.3KM.VI_NDVI.001.2026229161335.tif') as src:
    print(src.shape, src.crs, src.bounds)
    # .read(1) pulls band 1 into a numpy array (bands are 1-indexed, not 0-indexed).
    band1 = src.read(1)

# Quick grayscale preview of the band - useful as a sanity check before
# doing any real analysis.
plt.imshow(band1, cmap='gray')
plt.savefig('first_plot.png')
plt.show()
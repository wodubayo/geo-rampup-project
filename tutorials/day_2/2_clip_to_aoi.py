# Day 2, step 2: clip the raster to the AOI's boundary.
# rasterio.mask.mask() needs the AOI geometries in the raster's own CRS,
# so the reprojection below must happen before any masking.
import geopandas as gpd
import rasterio
from rasterio.mask import mask
import matplotlib.pyplot as plt

# AOI = Area Of Interest - the shape (here, the USA outline) we want to
# clip the raster down to, instead of keeping the whole global scene.
aoi = gpd.read_file('../../data/ne_10m_admin_0_countries_usa.shp')

with rasterio.open('../../data/US_eVSH_NDVI.2026.216-222.3KM.VI_NDVI.001.2026229161335.tif') as src:
    raster_crs = src.crs
    band1 = src.read(1)

# .to_crs() reprojects the AOI geometries to match the raster's CRS
# (confirmed mismatched in step 1) so the two line up spatially.
aoi_reprojected = aoi.to_crs(raster_crs)

# Reopen the raster to actually mask() it. mask() returns:
#  - clipped: a new pixel array containing only the AOI's footprint
#    (crop=True trims the array down to the AOI's bounding box instead of
#    keeping the original full-scene size with the outside blacked out)
#  - clipped_transform: the new affine transform describing where that
#    smaller array sits on the map (needed since cropping shifts the origin)
with rasterio.open('../../data/US_eVSH_NDVI.2026.216-222.3KM.VI_NDVI.001.2026229161335.tif') as src:
    clipped, clipped_transform = mask(src, aoi_reprojected.geometry, crop=True)
    clipped_meta = src.meta.copy()

# The clipped array has different dimensions/geolocation than the original,
# so its metadata (used when writing a valid GeoTIFF) must be updated too.
clipped_meta.update({
    "height": clipped.shape[1],
    "width": clipped.shape[2],
    "transform": clipped_transform
})

# Save the clipped result as its own GeoTIFF so it can be reused without
# re-running the clip.
with rasterio.open('../../data/clipped.tif', 'w', **clipped_meta) as dest:
    dest.write(clipped)

# Side-by-side comparison: full scene vs. AOI-clipped scene.
# clipped[0] selects band 1 out of the (bands, rows, cols) array mask() returns.
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(band1, cmap='gray')
axes[0].set_title('Original Raster')
axes[1].imshow(clipped[0], cmap='gray')
axes[1].set_title('Clipped to AOI')
plt.savefig('outputs/clipped_comparison.png')
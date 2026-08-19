# Day 2, step 1: before combining a vector AOI (Area Of Interest - the
# boundary you actually care about, here the USA outline) with a raster,
# always check that their CRSs (coordinate reference systems) match - if
# they don't, any overlay or clip between them will be silently misaligned.
import geopandas as gpd
import rasterio

# Vector layer (the AOI) - geopandas reports CRS as `aoi.crs`.
aoi = gpd.read_file('../../data/ne_10m_admin_0_countries_usa.shp')
print(aoi.crs)

# Raster layer - rasterio reports CRS on the dataset handle as `src.crs`.
with rasterio.open('../../data/US_eVSH_NDVI.2026.216-222.3KM.VI_NDVI.001.2026229161335.tif') as src:
    raster_crs = src.crs
    print(raster_crs)

# Here the AOI is EPSG:4326 (lat/lon) but the raster is in a Lambert
# Azimuthal Equal Area projection - they don't match, so step 2 reprojects
# the AOI into the raster's CRS before clipping.
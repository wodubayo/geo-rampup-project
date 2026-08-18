import rasterio
import matplotlib.pyplot as plt

with rasterio.open('data/AF_eVSH_NDVI.2026.213-222.3KM.VI_NDVI.001.2026229153959.tif') as src:
    print(src.shape, src.crs, src.bounds)
    band1 = src.read(1)
    
plt.imshow(band1, cmap='gray')
plt.savefig('first_plot.png')
plt.show()
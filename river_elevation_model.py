import numpy as np
import pandas as pd
import geopandas as gpd
import osmnx as ox

import rasterio as rio

from shapely.geometry import box
from scipy.spatial import cKDTree as KDTree 

import xarray as xr
import xrspatial
import rioxarray

import matplotlib.pyplot as plt
import earthpy as et
import earthpy.plot as ep

import geojson

path = '/home/doug/git/FloodRiskMapping/LiDAR/LIDAR-DTM-2m-2022-SU32ne/SU32ne_DTM_2m.tif'
# download LiDAR from Defra at https://environment.data.gov.uk/DefraDataDownload/?Mode=survey and read band 1 (elevation values)
SU32ne_DTM_2m = rio.open(path).read(1)
crs = rio.open(path).crs
# implement joining LiDAR tiles together

dem = rioxarray.open_rasterio(path)

# get GeoJSON for box at https://boundingbox.klokantech.com/
bounding_box = '''{"type": "Polygon", "coordinates":[[
                                        [-1.5384894204,50.9855417341],
                                        [-1.4770346474,50.9855417341],
                                        [-1.4770346474,51.0419166991],
                                        [-1.5384894204,51.0419166991],
                                        [-1.5384894204,50.9855417341]]]}'''

cropping_geometry = [geojson.loads(bounding_box)]
#cropped_lidar = lidar.rio.clip(geometries=cropping_geometry, crs=27700)
    # need to check crs here


fig, ax = plt.subplots()
dem.squeeze().plot.imshow(ax=ax)


river = ox.geocode_to_gdf('River Test', which_result=1)
river = river.to_crs(crs)
river.plot(ax=ax, color='blue')
plt.show()


# Have a read of this https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/open-lidar-raster-python/#:~:text=When%20you%20open%20raster%20data,input%20and%20generates%20a%20plot.
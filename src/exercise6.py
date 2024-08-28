import os

home_dir = os.path.expanduser("~")
data_dir = os.path.join(home_dir, "Downloads", "pyqgis_masterclass")

vector_layer = "seismic_zones.shp"
vector_layer_path = os.path.join(data_dir, vector_layer)
raster_layer = "srtm.tif"
raster_layer_path = os.path.join(data_dir, raster_layer)

# Fix invalid geometries
fix_geometry_params = {
    "INPUT": vector_layer_path,
    "METHOD": 0,
    "OUTPUT": "TEMPORARY_OUTPUT"
}
results = processing.run("native:fixgeometries", fix_geometry_params)
# Zonal statistics
zsParams = {
    'INPUT':results["OUTPUT"],
    'INPUT_RASTER':raster_layer_path,
    'RASTER_BAND':1,
    'COLUMN_PREFIX':'_',
    'STATISTICS':[2],
    'OUTPUT':'memory:'
    }
results = processing.runAndLoadResults("native:zonalstatisticsfb", zsParams)
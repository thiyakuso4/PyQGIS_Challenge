import os

home_dir = os.path.expanduser("~")
data_dir = os.path.join(home_dir, "Downloads", "pyqgis_masterclass")

filename = "seismic_zones.shp"
uri = os.path.join(data_dir, filename)

# iface.addVectorLayer(uri, "seismic_zones", "ogr")

filename = "sf.gpkg|layername=zoning"
uri = os.path.join(data_dir, filename)
iface.addVectorLayer(uri, "zoning", "ogr")

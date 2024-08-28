from qgis.core import QgsDistanceArea
from qgis.core import QgsPointXY

san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)
las_vegas = (36.1699, -115.1398)
d = QgsDistanceArea()

d.setEllipsoid("WGS84")
sf_pt = QgsPointXY(san_francisco[1], san_francisco[0])
ny_pt = QgsPointXY(new_york[1], new_york[0])
lv_pt = QgsPointXY(las_vegas[1], las_vegas[0])

distance_m = d.measureLine([ny_pt, lv_pt, sf_pt])

distance_km = distance_m/1000

print(d.convertLengthMeasurement(distance_m, Qgis.DistanceUnit.DistanceMiles))
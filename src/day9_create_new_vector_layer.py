mc = iface.mapCanvas()
extent = mc.extent()

vlayer = QgsVectorLayer("Polygon", "extent", "memory")
crs = QgsProject.instance().crs()
vlayer.setCrs(crs)

provider = vlayer.dataProvider()

f = QgsFeature()
geometry = QgsGeometry.fromRect(extent)
f.setGeometry(geometry)

provider.addFeature(f)
vlayer.updateExtents()

QgsProject.instance().addMapLayer(vlayer)
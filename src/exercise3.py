layer = iface.activeLayer()

if layer.name() == "zoning":
    iface.messageBar().pushMessage("Success: ", "You selected the right layer", 
    level=Qgis.Success)
else:
    iface.messageBar().pushMessage("Error: ", "Wrong layer selected", 
    level=Qgis.Critical, duration=5)
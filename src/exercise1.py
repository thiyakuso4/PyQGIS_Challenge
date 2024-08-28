import numpy as np

icon_path = "C:/Users/thiya/Downloads/pyqgis_masterclass/extent-svgrepo-com.svg"
icon = QIcon(icon_path)
action = QAction("Show Raster Statistics")
action.setIcon(icon)


def show_statistics():
    """Function to return statistics of active raster (Band 1) over current extent"""
    active_layer = iface.activeLayer()
    mc = iface.mapCanvas()
    extent = mc.extent()
    if iface.activeLayer() is None:
        iface.messageBar().pushMessage("Error", 
                                       "Please select a raster layer",
                                         level=Qgis.Critical)
    elif iface.activeLayer().type() == QgsMapLayer.RasterLayer:
        rasterBandStats = active_layer.dataProvider().bandStatistics(bandNo =1, 
                                                                     extent=QgsRectangle(extent))
        mean_value = round(rasterBandStats.mean, 2)
        if np.isnan(mean_value):
            iface.messageBar().pushMessage("Error",
                                           "No valid pixels in current extent",
                                           level=Qgis.Critical)
        else:
            iface.messageBar().pushMessage(f"Average value of Band 1 in current extent",
                                           str(mean_value))
    else:
        iface.messageBar().pushMessage("Error",
                                       "Please select a raster layer",
                                       level=Qgis.Critical)
        
action.triggered.connect(show_statistics)

iface.addToolBarIcon(action)
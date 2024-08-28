import os
from datetime import datetime

icon_path = "C:/Users/thiya/Downloads/pyqgis_masterclass/question.svg"
#icon = QIcon(icon_path)
action = QAction("Zoom to selection")
action.setIcon(icon)
def zoom_to_selection():
    # Get the active layer
    layer = iface.activeLayer()

    if not layer:
        print("No active layer found.")
    else:
        # Get the selected features
        selected_features = layer.selectedFeatures()

        if not selected_features:
            print("No features selected.")
        else:
            # Get the bounding box of the selected features
            extent = layer.boundingBoxOfSelected()

            # Zoom to the bounding box
            iface.mapCanvas().setExtent(extent)
            iface.mapCanvas().refresh()

    
    
action.triggered.connect(zoom_to_selection)

iface.addToolBarIcon(action)


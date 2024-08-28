crsToolbar = iface.addToolBar("Filter Toolbar")

label = QLabel("Enter an Country Code", parent=crsToolbar)
crsTextBox = QLineEdit("AO", parent=crsToolbar)
crsTextBox.setFixedWidth(80)
button = QPushButton("Go!", parent=crsToolbar)

crsToolbar.addWidget(label)
crsToolbar.addWidget(crsTextBox)
crsToolbar.addWidget(button)
# Function to zoom to the extent of the layer
def zoom_to_layer(layer):
    if layer:
        extent = layer.extent()
        iface.mapCanvas().setExtent(extent)
        iface.mapCanvas().refresh()
        print(f"Zoomed to layer: {layer.name()}")
    else:
        print("Layer is None, cannot zoom.")
        
        
def filterCountry(crsText):
    country_code = crsTextBox.text()
    layer_name = "conflict_count"
    # Get the active layer
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    if not layer:
        print("No active layer found.")
    else:
        # Apply the filter to select features
        layer.setSubsetString(f"iso_a2='{country_code}'")
        zoom_to_layer(layer)

    
button.clicked.connect(filterCountry)
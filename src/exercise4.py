crsToolbar = iface.addToolBar("CRS Toolbar")

label = QLabel("Enter an EPSG Code", parent=crsToolbar)
crsTextBox = QLineEdit("4326", parent=crsToolbar)
crsTextBox.setFixedWidth(80)
button = QPushButton("Go!", parent=crsToolbar)

crsToolbar.addWidget(label)
crsToolbar.addWidget(crsTextBox)
crsToolbar.addWidget(button)

def changeCrs(crsText):
    crs_text = crsTextBox.text()
    try:
        epsgCode = int(crs_text)
    except ValueError:
        iface.messageBar().pushMessage("ValueError:", f"Wrong EPSG code {crs_text} entered", 
        level=Qgis.Critical, duration=5)
        return 0
    newCrs = QgsCoordinateReferenceSystem.fromEpsgId(epsgCode)
    if newCrs.isValid():
        QgsProject.instance().setCrs(newCrs)
    else:
        iface.messageBar().pushMessage("ValueError:", f"Wrong EPSG code {crs_text} entered", 
        level=Qgis.Critical, duration=5)
    
button.clicked.connect(changeCrs)    
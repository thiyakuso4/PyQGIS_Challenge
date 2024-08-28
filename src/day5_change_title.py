title = iface.mainWindow().windowTitle()

print(title)
new_title = title.replace("QGIS", "My QGIS")

iface.mainWindow().setWindowTitle(new_title)

icon_path = "C:/Users/thiya/Downloads/pyqgis_masterclass/qgis-black.png"
new_icon = QIcon(icon_path)
iface.mainWindow().setWindowIcon(new_icon)
vector_menu = iface.vectorMenu()
raster_menu = iface.rasterMenu()
menubar = vector_menu.parentWidget()

menubar.removeAction(vector_menu.menuAction())

menubar.removeAction(raster_menu.menuAction())

# Change visibility
iface.pluginToolBar().setVisible(True)


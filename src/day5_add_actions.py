import webbrowser
def open_website():
    webbrowser.open("https://gis.stackexchange.com")

website_action = QAction("Go to gis.stackexchange.com")

website_action.triggered.connect(open_website)
iface.helpMenu().addSeparator()
iface.helpMenu().addAction(website_action)
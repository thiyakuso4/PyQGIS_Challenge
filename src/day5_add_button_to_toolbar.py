import os
from datetime import datetime

icon_path = "C:/Users/thiya/Downloads/pyqgis_masterclass/question.svg"
icon = QIcon(icon_path)
action = QAction("Show Time")
action.setIcon(icon)
def show_time_warning():
    now = datetime.now().strftime('%H:%M:%S')
    iface.messageBar().pushWarning("Current time", now)
    
def show_time_info():
    now = datetime.now().strftime('%H:%M:%S')
    iface.messageBar().pushMessage("Current time", now, duration=10)
    
action.triggered.connect(show_time_info)
action.triggered.connect(show_time_warning)

iface.addToolBarIcon(action)


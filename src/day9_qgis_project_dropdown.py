import os
from qgis.core import QgsProject

home_dir = os.path.expanduser("~")
data_dir = os.path.join(home_dir, "Downloads", "pyqgis_masterclass")

projectToolbar = iface.addToolBar("Project Selector")

label = QLabel("Select a proejct to load", parent=projectToolbar)
projectSelector = QComboBox(parent=projectToolbar)
projectSelector.addItem("sf.qgz")
projectSelector.addItem("places.qgz")

def loadProject(projectName):
    project =  QgsProject.instance()
    project_path = os.path.join(data_dir, projectName)
    project.read(project_path)
    
projectSelector.currentTextChanged.connect(loadProject)
projectToolbar.addWidget(label)
projectToolbar.addWidget(projectSelector)


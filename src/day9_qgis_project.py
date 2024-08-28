import os
from qgis.core import QgsProject
# Get the project instance
project = QgsProject.instance()

home_dir = os.path.expanduser("~")
data_dir = os.path.join(home_dir, "Downloads", "pyqgis_masterclass")

project_path = os.path.join(data_dir, "sf.qgz")
project.read(project_path)
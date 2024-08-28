import os
import pandas as pd

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

layer = iface.activeLayer()

# Check if layer is selected
if not layer:
    iface.messageBar().pushMessage(
    "Please select a layer", level=Qgis.Critical)
# Check if the selected layer is vector
elif layer.type() != QgsMapLayer.VectorLayer:
    iface.messageBar().pushMessage(
    "Please select a vector layer", level=Qgis.Critical)
else:
    output_name = "output.csv"
    output_path = os.path.join(data_dir, output_name)
    fields = layer.fields()

    # Get a list of field names
    fieldnames = [field.name() for field in layer.fields()]
    # Get a list of attributes for each feature
    data = [f.attributes() for f in layer.getFeatures()]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=fieldnames)

    # Save to  file
    df.to_csv(output_path)

    iface.messageBar().pushMessage(
    "Sucess:", f"Output file writeten at {output_path}", level=Qgis.Success)
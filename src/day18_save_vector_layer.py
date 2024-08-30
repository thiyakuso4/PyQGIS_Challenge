import os
import time

data_dir = os.path.join(os.path.expanduser("~"), "Downloads", "pyqgis_masterclass")

layer = iface.activeLayer()
# Check if a layer is selected
if not layer:
    iface.messageBar().pushMessage('Please select a layer',
                                   level=Qgis.Critical)
# Check if the selected layer is a vector layer
elif layer.type() != QgsMapLayer.VectorLayer:
    print("Here we go")
    iface.messageBar().pushMessage('Please select a vector layer',
                                   level=Qgis.Critical)
else:
    # Define parameters for QgsVectorFileWriter
    output_name = 'output.csv'
    output_path = os.path.join(data_dir, output_name)
    
    # Define the options for saving the layer
    save_options = QgsVectorFileWriter.SaveVectorOptions()
    save_options.driverName = "CSV"
    save_options.fileEncoding = "UTF-8"
    save_options.layerOptions = ["SEPERATOR=COMMA"]

    # Create the writer
    writer = QgsVectorFileWriter.create(
        fileName=output_path,
        fields=layer.fields(),
        geometryType=QgsWkbTypes.NoGeometry,
        srs=layer.crs(),
        transformContext=QgsProject.instance().transformContext(),
        options=save_options
    )
    print(writer.hasError())
    # Check if we were able to create the writer
    if writer.hasError() != QgsVectorFileWriter.NoError:
        iface.messageBar().pushMessage("Error: ", write.errorMessage,
                                       level=Qgis.Critical)
    else:
        # Add features
        for f in layer.getFeatures():
            writer.addFeature(f)

        # delete the write to flush features to disk
        del writer

        iface.messageBar().pushMessage("Success:", 
                                       f"Output file written at {output_path}",
                                       level=Qgis.Success)
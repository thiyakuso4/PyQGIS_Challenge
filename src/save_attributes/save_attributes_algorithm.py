"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterFileDestination,
                       QgsVectorFileWriter,
                       QgsWkbTypes,
                       QgsProject)
from qgis import processing


class SaveAttributesAlgorithm(QgsProcessingAlgorithm):
    """
    This is an algorithm to save attribute table of selected layers as csv.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return SaveAttributesAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'save_attributes'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Save attributes as CSV')

    def shortHelpString(self):
        """
        Re  turns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("This tools saves attribute table of selected vector layer as csv")

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSource(
        "INPUT",
        'Input Layer',
        [QgsProcessing.TypeVectorAnyGeometry]
        )) 
    
        self.addParameter(QgsProcessingParameterFileDestination(
        'OUTPUT',
        'Output CSV',
        'CSV files (*.csv)'))
    def processAlgorithm(self, parameters, context, feedback):
        layer = self.parameterAsVectorLayer(parameters, 'INPUT', context)
        output = self.parameterAsFileOutput(parameters, 'OUTPUT', context)
        
        total = layer.featureCount()
        
        # Define the options for saving the layer
        save_options = QgsVectorFileWriter.SaveVectorOptions()
        save_options.driverName = 'CSV'
        save_options.fileEncoding = 'UTF-8'
        
        # Create the writer
        writer = QgsVectorFileWriter.create(
            fileName=output,
            fields=layer.fields(),
            geometryType=QgsWkbTypes.NoGeometry,
            srs=layer.crs(),
            transformContext=QgsProject.instance().transformContext(),
            options=save_options
        )
        feedback.pushInfo('Starting to process layer')
        for index, f in enumerate(layer.getFeatures()):
            if feedback.isCanceled():
                break
            writer.addFeature(f)
            progress = int(100*(index/total))
            feedback.setProgress(progress)

        return {'OUTPUT': output}

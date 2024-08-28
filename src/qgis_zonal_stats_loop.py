import glob
import os

inDir = "C:/Users/thiya/Downloads/pyqgis_masterclass/batch_processing_tutorial/PRISM_ppt_stable_4kmM3_2017_all_bil"
inFiles = glob.glob(f"{inDir}/*2017??_*.bil")

result_layer = "C:/Users/thiya/Downloads/pyqgis_masterclass/batch_processing_tutorial/Zip_Codes/Zip_Codes.shp"
outDir = "C:/Users/thiya/Downloads/pyqgis_masterclass/batch_processing_tutorial"
root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
  print(layer.name())
for inFile in inFiles:
    inName = os.path.basename(inFile)
    inName = inName.replace('.bil', '')
    yyyymm = inName[23:29]
    zsParams = {'INPUT':result_layer,
                'INPUT_RASTER':inFile,
                'RASTER_BAND':1,
                'COLUMN_PREFIX':f'{yyyymm}_',
                'STATISTICS':[2],
                'OUTPUT':'memory:'}
    
    result = processing.run("native:zonalstatisticsfb", zsParams)
    result_layer = result['OUTPUT']
    print(result)
#    iface.addRasterLayer(inFile, inName, "gdal")

QgsProject.instance().addMapLayer(result_layer)
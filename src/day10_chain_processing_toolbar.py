demPath = "C:/Users/thiya/Downloads/pyqgis_masterclass/srtm.tif"
shpPath = "C:/Users/thiya/Downloads/pyqgis_masterclass/shoreline.shp"
clipParams = {'INPUT':demPath,
'MASK':shpPath,
'SOURCE_CRS':None,
'TARGET_CRS':None,
'TARGET_EXTENT':None,
'NODATA':None,
'ALPHA_BAND':False,
'CROP_TO_CUTLINE':True,
'KEEP_RESOLUTION':False,
'SET_RESOLUTION':False,
'X_RESOLUTION':None,
'Y_RESOLUTION':None,
'MULTITHREADING':False,
'OPTIONS':'',
'DATA_TYPE':0,
'EXTRA':'',
'OUTPUT':'TEMPORARY_OUTPUT'}
clipResults = processing.run("gdal:cliprasterbymasklayer", clipParams)

outPath = f"C:/Users/thiya/Downloads/pyqgis_masterclass/hillshade_clipped.tif"
params = {'INPUT':clipResults["OUTPUT"],
'Z_FACTOR':1,
'AZIMUTH':300,
'V_ANGLE':40,
'OUTPUT':outPath}
results = processing.runAndLoadResults("native:hillshade", params)

print(results)

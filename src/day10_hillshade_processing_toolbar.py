demPath = "C:/Users/thiya/Downloads/pyqgis_masterclass/srtm.tif"
    
for angle in range(10, 90, 10):
    outPath = f"C:/Users/thiya/Downloads/pyqgis_masterclass/hillshade_{angle}.tif"
    params = {'INPUT':demPath,
    'Z_FACTOR':1,
    'AZIMUTH':300,
    'V_ANGLE':angle,
    'OUTPUT':outPath}
    results = processing.runAndLoadResults("native:hillshade", params)

#print(results)

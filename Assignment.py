import os
import ogr
from osgeo import ogr, osr
#set your working directory if necessary:
os.chdir('/home/user/PythonProjects/assignment1')

# reset your working directory
os.chdir('data')

## lat/long definition
source = osr.SpatialReference()
source.ImportFromEPSG(4326)

# http://spatialreference.org/ref/sr-org/6781/
# http://spatialreference.org/ref/epsg/28992/
target = osr.SpatialReference()
target.ImportFromEPSG(28992)

transform = osr.CoordinateTransformation(source, target)

ptGaia = ogr.CreateGeometryFromWkt("POINT (5.6664 51.9875)")
ptRound = ogr.CreateGeometryFromWkt("POINT (5.6615 51.9766)")
ptList = [ptGaia, ptRound]

for x in ptList:
    x.Transform(transform)
    print x.ExportToWkt()

## Is the ESRI Shapefile driver available?
driverName = "ESRI Shapefile"
driver = ogr.GetDriverByName(driverName)

if driver is None:
    print "%s driver not available.\n" % driverName
else:
    print  "%s driver IS available.\n" % driverName

Wag = "WagPoints.shp"
layername = "Wageningen"


## Create shape file
ds = driver.CreateDataSource(Wag)
print ds.GetRefCount()

# Set spatial reference
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(28992)

## Create Layer
layer = ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)

layerDefinition = layer.GetLayerDefn()
feature1 = ogr.Feature(layerDefinition)
feature2 = ogr.Feature(layerDefinition)

feature1.SetGeometry(ptGaia)
feature2.SetGeometry(ptRound)


layer.CreateFeature(feature1)
layer.CreateFeature(feature2)

ds.Destroy()
print(layer.GetExtent())

##Wageningen = QgsVectorLayer("/home/user/PythonProjects/assignment1/data/Wageningen.shp", "Wageningen", "ogr")
##Wageningen.isValid()
##dest_crs = QgsCoordinateReferenceSystem(4326)
##QgsVectorFileWriter.writeAsVectorFormat(Wageningen, "/home/user/PythonProjects/assignment1/data/Wageningen.kml", "utf-8", dest_crs, "KML")
##

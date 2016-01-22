## Author: The Leopards (Samantha Krawczyk, Georgios Anastasiou)
## 18 January 2016
## creating a shapefile with 2 points in Wageningen, NL

## for the user: The script contains code to export to .kml. This section works only in QGIS.0

import os
from osgeo import ogr, osr
# set your working directory if necessary:
os.chdir('/home/user/PythonProjects/assignment1')

# reset your working directory
os.chdir('data')


## Is the ESRI Shapefile driver available?
driverName = "ESRI Shapefile"
driver = ogr.GetDriverByName( driverName )
if driver is None:
    print "%s driver not available.\n" % driverName
else:
    print  "%s driver IS available.\n" % driverName

## Set the name of the layer and the shapfile
fn = "Wageningen.shp"
layername = "Points"


## Create shape file
ds = driver.CreateDataSource(fn)
print ds.GetRefCount()

## Set spatial reference
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(4326)


## Create Layer
layer=ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)
print(layer.GetExtent())

layerDefinition = layer.GetLayerDefn()


def pointGeo(pointname, s, x, y):
    pointname = ogr.Geometry(ogr.wkbPoint)
    pointname.SetPoint(s, x, y)
    feature = ogr.Feature(layerDefinition)
    feature.SetGeometry(pointname)
    layer.CreateFeature(feature)
    return layer

print "The new extent"
print layer.GetExtent()


   
ds.Destroy()

coord1 = [0, 5.6664, 51.9875]
pointGeo("gaia", coord1[0], coord1[1], coord1[2])
coord2 = [0, 5.6615, 51.9766]
pointGeo("round", coord2[0], coord2[1], coord2[2])

## Exporting it to .kml
Wageningen = QgsVectorLayer("/home/user/PythonProjects/assignment1/data/Wageningen.shp", "Wageningen", "ogr")
Wageningen.isValid()
dest_crs = QgsCoordinateReferenceSystem(4326)
QgsVectorFileWriter.writeAsVectorFormat(Wageningen, "/home/user/PythonProjects/assignment1/data/Wageningen.kml", "utf-8", dest_crs, "KML")


## Author: The Leopards (Samantha Krawczyk, Georgios Anastasiou)
## 18 January 2016
## creating a shapefile with 2 points in Wageningen, NL

## for the user: The script contains code to export to .kml. This section works only in QGIS.0

import os
import ogr
from osgeo import ogr, osr

# create your output directory and set it as your working directory
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

## Set spatial reference
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(4326)


## Create Layer
layer=ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)

## Create a point
gaia = ogr.Geometry(ogr.wkbPoint)
roundW = ogr.Geometry(ogr.wkbPoint)

## SetPoint(self, int point, double x, double y, double z = 0)
gaia.SetPoint(0, 5.6664, 51.9875) 
roundW.SetPoint(0, 5.6615, 51.9766)

## Feature is defined from properties of the layer
layerDefinition = layer.GetLayerDefn()
feature1 = ogr.Feature(layerDefinition)
feature2 = ogr.Feature(layerDefinition)

## Add the points to the feature
feature1.SetGeometry(gaia)
feature2.SetGeometry(roundW)

## Store the feature in a layer
layer.CreateFeature(feature1)
layer.CreateFeature(feature2)


ds.Destroy()

print "Check the shapefile created in your data folder"

## creating the .kml file out of the shapefile

Wageningen = QgsVectorLayer("../data/Wageningen.shp", "Wageningen", "ogr")
Wageningen.isValid()
dest_crs = QgsCoordinateReferenceSystem(4326)
QgsVectorFileWriter.writeAsVectorFormat(Wageningen, "../data/Wageningen.kml", "utf-8", dest_crs, "KML")


#!/bin/sh

###################################
#Script to rasterise vector labels#
#Maintainer: Christopher Chan     #
#Date: 2021-01-19                 #
#Version: 0.1.0                   #
###################################

echo "This script rasterise the vector labels from .GPKG or .geojson to raster."

echo "Please specify path to targeted vector labels"
read -p "Vector path: " vector_path
vector_path=${vector_path:- }

echo "Please specify path to the pairing raster file"
echo "This is to extract meta information for the rasterisation"
read -p "Raster path: " raster_path
raster_path=${raster_path:- }

echo "Please specify the column NAME of the provided vector label classification of which you would like to parse"
read -p "Colume NAME of classification: " col_name
col_name=${col_name:- }

echo "Please specify desired output path."
read -p "Output path: " output_path
output_path=${output_path:- }

pixels=$(gdalinfo $raster_path | grep "Pixel Size" | xargs | sed "s/Pixel Size = (/ /g; s/,/ /g; s/-//g; s/)/ /g")

log_date=$(date +%y-%m-%d)

echo "Rasterising class output..."
echo "Date generated: $(date)"

gdal_rasterize -at -a $col_name -tr $pixels -of GTiff -a_srs EPSG:3857 -ot Float32 $vector_path $output_path"/"$log_date"_LBL.tif"

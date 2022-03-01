#!/bin/sh

##############################
#Script to split RGB         #
#Maintainer: Christopher Chan#
#Date: 2021-02-06            #
#Version: 0.1.0              #
##############################

echo "This script will split input RGB bands into separate tifs."
echo "Please make sure LBL are rasterised and RGB image have been NORMALISED."

echo "Please specify NORMALISED RGB raster path to be split"
read -p "Normalised RGB path: " RGB_path
RGB_path=${RGB_path:- }

echo "Please specify desired output path."
read -p "Output path: " output_path
output_path=${output_path:- }

gdal_translate -a_nodata 0 -b 1 -of GTiff -a_srs EPSG:3857 -ot Float32 $RGB_path $output_path"/Red.tif"

gdal_translate -a_nodata 0 -b 2 -of GTiff -a_srs EPSG:3857 -ot Float32 $RGB_path $output_path"/Green.tif"

gdal_translate -a_nodata 0 -b 3 -of GTiff -a_srs EPSG:3857 -ot Float32 $RGB_path $output_path"/Blue.tif"

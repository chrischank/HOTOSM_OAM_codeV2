#!/bin/sh

##################################
#Script to curl and transform OAM#
#Maintainer: Christopher Chan    #
#Date: 2021-01-04                #
#Version: 0.1.0                  #
##################################

echo "This script will download and reproject OAM raster to EPSG: 3857"

echo "Please provide OAM download link."
read -p "OAM link: " OAM_link
OAM_link=${OAM_link:- }

echo "Please specify desired output path."
read -p "Output path: " output_path
output_path=${output_path:- }

echo "Please specify output pixel size in meters, i.e. 10m = 10 1m = 1, 10cm = 0.1..."
read -p "Pixel size: " pixels
pixels=${pixels:- 0.1}

echo "Please specify desired output filename."
read -p "Filename: " filename
filename=${filename:- }

if [ -e $output_path"/"$filename".tif" ];
then
	echo " File exists, skipping download..."
else
	curl --progress-bar $OAM_link --output $output_path"/"$filename".tif"
fi

origin_epsg=$(gdalinfo $output_path"/"$filename".tif" | grep "EPSG" | tail -1 | grep -o "[[:digit:]]" | xargs | sed -e "s/ //g")

gdalwarp -s_srs EPSG:$origin_epsg -t_srs EPSG:3857 -tr $pixels $pixels -ot Float32 -r cubic -srcnodata 0 -dstnodata 0 \
	-multi -of GTiff -overwrite $output_path"/"$filename".tif" \
	$output_path"/3857_"$filename".tif"

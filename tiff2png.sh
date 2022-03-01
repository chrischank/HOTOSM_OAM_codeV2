#!/bin/sh

##########################################
#This script parse tif into IMG & LBL PNG#
#Maintainer: Christopher Chan            #
#Date: 2022-02-17                        #
#Version: 0.1.2                          #
##########################################

echo "This script parse .tif into IMG & LBL PNGs"

echo "Please specify IMG directory: "
read -p "IMG dir: " IMG_dir
IMG_dir=${IMG_dir:- }

echo "Please specify LBL directory: "
read -p "LBL dir: " LBL_dir
LBL_dir=${LBL_dir:- }

# Extract b4 to LBL directory
echo "Extracting band 4 to LBL directory..."

cd $IMG_dir

for i in *.tif;
do
  gdal_translate -of PNG -ot Byte -b 4 $i $LBL_dir"/"$i".png";
done

echo "Extracting band 1 2 3 to IMG directory..."

for i in *.tif;
do
  gdal_translate -of PNG -ot Byte -b 1 -b 2 -b 3 $i $IMG_dir"/"$i".png";
done

rm -rf *.tif

# Renaming files
for i in *;
do
  rename -v .tif "" $i;
done

cd $LBL_dir

for i in *;
do
  rename -v _IMG_ _LBL_ $i;
done

for i in *;
do
  rename -v .tif "" $i;
done

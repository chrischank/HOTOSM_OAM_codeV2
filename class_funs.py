##############################
#Callable class functions    #
#Maintainer: Christopher Chan#
#Date: 08/10/2020            #
#Version: 0.1.7              #
##############################

import os
import numpy as np
import rasterio
import rasterio as rio
import geopandas as gpd
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import matplotlib
import matplotlib.pyplot as plt
from osgeo import gdal
from rasterio import Affine
from rasterio.enums import Resampling
from rasterio.mask import mask
from rasterio.plot import show
from rasterio.plot import plotting_extent
        
class transform():
    def jp2tiff(jp2):
        '''
        Transform jp2 to tiff
        Run before using class indices
        '''
        name1, name2 = jp2.split('.', 1)
        print(name1)
        path = os.path.join(name1 + '.tif')
        src_ds = gdal.Open(jp2)
        format = "GTiff"
        driver = gdal.GetDriverByName(format)
        dst_ds = driver.CreateCopy(path, src_ds, 0)
        dst_ds = None
        src_ds = None
        print("The file is saved in: {}".format(path))
        print("\n")
    
    def resampling(raster, upscale_factor):
        '''
        Resampling image to factor
        Run before using class indices
        '''
        with rasterio.open(raster) as dataset:

            # resample data to target shape
            data = dataset.read(
                out_shape=(
                    dataset.count,
                    int(dataset.height * upscale_factor),
                    int(dataset.width * upscale_factor)
                ),
                resampling=Resampling.bilinear
            )

            # scale image transform
            transform = dataset.transform * dataset.transform.scale(
                (dataset.width / data.shape[-1]),
                (dataset.height / data.shape[-2])
            )
        
        name1, name2 = raster.split('.', 1)
        file1 = os.path.join(name1 + "_resamp.tif")
        
        band = rio.open(raster)
        profile = band.profile
        
        profile.update(transform=transform, driver='GTiff', height=(dataset.height * upscale_factor), width=(dataset.width * upscale_factor), crs=band.crs)

        with rio.open(file1,'w', **profile) as dst:
            dst.write(data)
        
        print("The file is Resampled in: {}".format(file1))
        print('Before the nROW & nCLO: ',(rio.open(raster)).shape)
        print('Now the nROW & nCLO: ',(rio.open(file1)).shape)
        print("\n")
        
    def fix(image1, shp_path):
        
        shp = gpd.read_file(shp_path)
        
        band = rio.open(image1)
        #plot.show(band)
        masked, mask_transform = mask(dataset = band, shapes = shp.geometry, crop = True)
        show(masked, transform = mask_transform)
        out_meta = band.meta.copy()
        out_meta.update({"driver": "GTiff","height": masked.shape[1],
                         "width": masked.shape[2],"transform": mask_transform})
        
        name1, name2 = image1.rsplit('_', 1)
        path_masked = os.path.join(name1 + "_fix.tif")
        
        with rio.open(path_masked, "w", **out_meta) as dest:
            dest.write(masked)
        
        print("The file is Cropped in: {}".format(path_masked))
        print('Before the nROW & nCLO: ',(rio.open(image1)).shape)
        print('Now the nROW & nCLO: ',(rio.open(path_masked)).shape)
        print("\n")
        
    def convert(fn, form):
        '''
        https://numpy.org/doc/stable/user/basics.types.html
        '''
        t = {'Byte' : gdal.GDT_Byte,
             'UInt16' : gdal.GDT_UInt16,
             'Int16' : gdal.GDT_Int16,
             'UInt32' : gdal.GDT_UInt32,
             'Int32' : gdal.GDT_Int32,
             'Float32' : gdal.GDT_Float32,
             'Float64' : gdal.GDT_Float64}
        
        kwargs = {'format': 'GTiff', 'outputType': t[form]}
        
        # Create output directory and the output path
        path_files = os.path.join(fn)
        name, name0 = path_files.rsplit('/', 1)
        output_dir = os.path.join(name, form)
        if os.path.isdir(output_dir) == False:
            os.mkdir(output_dir)
        
        band = gdal.Open(fn)
        name1, name2 = name0.split('.', 1)
        
        path_masked = os.path.join(name, form, name1 + "_" + form + ".tif")

        ds = gdal.Translate(path_masked, band, **kwargs)
        # do something with ds if you need
        ds = None # close and save ds
        
        plot_band = rio.open(fn)
        print("The original file is in: {}".format(fn))
        print('Type before: ',(rio.open(fn)).dtypes[0])
        show(plot_band)
        
        plot_band1 = rio.open(path_masked)
        print("The file is saved in: {}".format(path_masked))
        print('Type now: ',(rio.open(path_masked)).dtypes[0])
        show(plot_band1)
        print("\n")
        
    def stack(path, name, version):
        '''
        https://earthpy.readthedocs.io/en/latest/gallery_vignettes/plot_raster_stack_crop.html
        Atention in the order of the path to create for instance RGB images
        stack_path = [RED_path, GREEN_path, BLUE_path]
        version = 1 in case you want to plot image as RGB
        '''
        # Create output directory and the output path
        path_files = os.path.join(path[0])
        name1, name2 = path_files.rsplit('/', 1)
        output_dir = os.path.join(name1, "stack")
        if os.path.isdir(output_dir) == False:
            os.mkdir(output_dir)
        
        output_name = os.path.join(name1, "stack", name + ".tif")
        array, raster_prof = es.stack(path, out_path=output_name)
        
        if version == 0:
            
            name_path = []
            
            for i in range(len(path)):
                name3, name4 = path[i].rsplit('/', 1)
                name_path.append(name4)
                ep.plot_bands(array[i], title=name_path[i],)
                plt.show()
        
        elif version == 1:
            
            extent = plotting_extent(array[0], raster_prof["transform"])
            fig, ax = plt.subplots(figsize=(12, 12))
            ep.plot_rgb(array, ax=ax, stretch=True, extent=extent, str_clip=0.5, title=name,)
            plt.show()
        
        else:
            
            return print("No version were stacked. To plot each band select 0 and to plot image compose like RGB select 1")
        
        print("The bands stack are: {}".format(path))
        print("\n")
        print("The file is saved in: {}".format(output_name))
        print("\n")
                
class indices():
    def ndvi(NIR_PATH, RED_PATH):
        '''
        Normalised Difference Vegetation Index
        Calculates NDVI (NIR-RED)/(NIR+RED)
        E.g. Sentinel-2: NIR = Band8; RED = Band4
        '''
        RED = gdal.Open(RED_PATH)
        NIR = gdal.Open(NIR_PATH)
        RED_link = RED.ReadAsArray().astype(np.float)
        NIR_link = NIR.ReadAsArray().astype(np.float)
        NDVI = es.normalized_diff(NIR_link, RED_link)
        ep.plot_bands(NDVI, cmap="RdYlGn", cols=1, title='NDVI', vmin=-1, vmax=1)
        
        band = rio.open(RED_PATH)
        name1, name2 = RED_PATH.rsplit('/', 1)
        #print(name1)
        path = os.path.join(name1,'NDVI.tif')
        
        #export ndvi image
        ndviImage = rio.open(path,'w',driver='Gtiff',
                                  width=band.width, 
                                  height = band.height, 
                                  count=1, crs=band.crs, 
                                  transform=band.transform, 
                                  dtype='float64')
        ndviImage.write(NDVI,1)
        ndviImage.close()
        return NDVI
    
    def ndbi(SWIR_PATH, NIR_PATH):
        '''
        Normaised Difference Built-up Index
        Calculates NDBI (SWIR-NIR)/(SWIR+NIR)
        E.g. Sentinel-2: SWIR = Band11; NIR = Band8
        '''
        NIR = gdal.Open(NIR_PATH)
        SWIR = gdal.Open(SWIR_PATH)
        NIR_link = NIR.ReadAsArray().astype(np.float)
        SWIR_link = SWIR.ReadAsArray().astype(np.float)
        NDBI = es.normalized_diff(SWIR_link, NIR_link)
        ep.plot_bands(NDBI, cmap="RdYlGn", cols=1, title='NDBI', vmin=-1, vmax=1)
        
        band = rio.open(SWIR_PATH)
        name1, name2 = SWIR_PATH.rsplit('/', 1)
        #print(name1)
        path = os.path.join(name1,'NDBI.tif')
        
        #export ndbi image
        ndbiImage = rio.open(path,'w',driver='Gtiff',
                                  width=band.width, 
                                  height = band.height, 
                                  count=1, crs=band.crs, 
                                  transform=band.transform, 
                                  dtype='float64')
        ndbiImage.write(NDBI,1)
        ndbiImage.close()
        return NDBI
    
    def BU (RED_PATH, NIR_PATH, SWIR_PATH):
        '''
        Built-up = NDBI - NDVI
        '''
        from class_funs import indices
        BU = indices.ndvi(NIR_PATH, RED_PATH) - indices.ndbi(SWIR_PATH, NIR_PATH)
        ep.plot_bands(BU, cmap="RdYlGn", cols=1, title='BU', vmin=-1, vmax=1)
        
        band = rio.open(RED_PATH)
        name1, name2 = RED_PATH.rsplit('/', 1)
        #print(name1)
        path = os.path.join(name1,'BU.tif')
        
        #export BU image
        buImage = rio.open(path,'w',driver='Gtiff',
                                  width=band.width, 
                                  height = band.height, 
                                  count=1, crs=band.crs, 
                                  transform=band.transform, 
                                  dtype='float64')
        buImage.write(BU,1)
        buImage.close()
        return BU
    
    def sci(SWIR_PATH, nNIR_PATH):
        '''
        Soil Composition Index
        Calculates SCI (SWIR-nNIR)/(SWIR+nNIR)
        E.g. Sentinel-2: SWIR = Band 11; narrowNIR = Band8A
        '''
        nNIR = gdal.Open(nNIR_PATH)
        SWIR = gdal.Open(SWIR_PATH)
        nNIR_link = nNIR.ReadAsArray().astype(np.float)
        SWIR_link = SWIR.ReadAsArray().astype(np.float)
        SCI = es.normalized_diff(SWIR_link, nNIR_link)
        ep.plot_bands(SCI, cmap="RdYlGn", cols=1, title='SCI', vmin=-1, vmax=1)
        
        band = rio.open(nNIR_PATH)
        name1, name2 = nNIR_PATH.rsplit('/', 1)
        #print(name1)
        path = os.path.join(name1,'SCI.tif')
        
        #export SCI image
        sciImage = rio.open(path,'w',driver='Gtiff',
                                  width=band.width, 
                                  height = band.height, 
                                  count=1, crs=band.crs, 
                                  transform=band.transform, 
                                  dtype='float64')
        sciImage.write(SCI,1)
        sciImage.close()
        return SCI

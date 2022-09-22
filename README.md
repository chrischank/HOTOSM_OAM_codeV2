# Code produced for the academic abstract
["Investigating the capability of UAV imagery for AI-assisted mapping of Refugee Camps in East Africa"](https://zenodo.org/record/7004576#.Yv4xNRVBzt8)

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/183308388-a041ceea-fdee-4895-8655-4853b3dbb9d8.png"/>
</p>

This github repository is the code-base for the Master Thesis submitted for the Master der Naturwissenschaften in Applied Earth Observation and Geoanalysis of the Living Environment (EAGLE) at the Julius-Maximilians-Universität Würzburg. For Full Master thesis, please [click here](https://www.dropbox.com/s/bl478xo083aum31/Chris_MSc_s382722.pdf?dl=0)

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/166689718-e570c0f4-e09d-49da-80c3-58f062d04896.png"/>
</p>

This work of this thesis is partnered with the Humanitarian OpenStreetMap (HOTOSM) and supported by the German Aerospace Center / Deutsches Zentrum für Luft- und Raumfahrt (DLR).

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/166691521-16efc2f3-6aee-4e1b-9c89-15492dfdc7b3.png"/>
  <img src="https://user-images.githubusercontent.com/36608720/166690232-c61e3ee2-3a7b-4452-ac55-7a6b3e1c5e2f.png"/>
</p>

## Introduction
HOTOSM would like to develop a solution for assisted mapping which can predict buildings in refugee camps on the drone imagery provided by associated organisation OpenAerialMap. Refugee camps and informal settlements reside some of the most vulnerable population, the  majority of which are located in Sub-Saharan East Africa (UNHCR, 2016). Many of these  settlements often lack up-to-date maps of which we take for granted in developed cities. Having up-to-date maps are important for assisting administration (e.g. population estimates,  infrastructure development) in data impoverished environments and thereby encourages  economic productivity (Herfort et al., 2021). The data inequality between developed and  developing areas can be reduced using assisted mapping technology. To extract geospatial and imagery characteristics of dense urban enviornments, a combination of VHR satellite imagery and Machine Learning (ML) are commonly used. Recent advances in CV based Deep Learning might be able to address these issues. Convolutional Neural Networks (CNN) are a subtype of the Deep Learning (DL) family used in  CV tasks. Past studies using CNN have shown high accuracy and transferability in small  geographical setting (Kuffer et al., 2022). The datasets provided for this project consist of both highly structured, zoned newer refugee camps and chaotic, highly complex older camps. In  addition, roofing materials are highly heterogeneous, especially in older sites where thatched  roofs are often mixed with litter. This coupled with the complex spatial autocorrelation and  relation due to the lack of zoning in older sites hinder rule-based and conventional ML based  approach. Therefore, a CNN based approach might be able to simplify the task of selecting and  testing parameters, taking advantage of VHR textural information but also learning contextual  relations (Lang et al., 2022; Lehner & Blaschke, 2022). This study will be connected to a pilot project on testing the capabilities of building segmentation.

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/181209381-93c4d351-f530-4625-a497-246676a12848.png"/>
</p>

## Research Questions and Answers
### RQ1. Do state-of-the-art models allow for accurate detection of buildings from UAV data in refugee camps?\
### RQ2. What is the optimal mixture of accurate and less-accurate labels and how does that affect the segmentation output result?\
#### RQ2(a). How does the introduction of complex environment such as heterogeneous urban morphologies, roofing materials, and UAV drone artefacts affect result?\

Shallow EfficientNet encoders U-Nets performed slightly better in Precision, Dice Score, and IoU on less-complicated accurately labelled Kalobeyei dataset\

BUT, they suffer larger performace loss than classical U-Nets when complex data were introduced\

### RQ3. How do existing models pre-trained on classical CV datasets and/or building datasets response when applied to the setting of refugee camps?\

Further training of the EfficientNet B1 U-Net (OCC initalised) have largest improvement in Recall\

Architectures with ImageNet initialisation only saw improvement with EfficientNet B1 encoder but not B2\

Inconclusive

## Experimental setup

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/189320108-f0251dea-bec8-4f5b-b476-4c409edb4148.png"/>
</p>

## Pre-processing pipeline
### Before any process are ran, please ensure you have the capability to run shell scripts and have [gdal](https://gdal.org/), and [PyTorch](https://pytorch.org/) installed.

*1. Download, extract and reproject OpenAerialMap WMS raster using [curl_warp.sh](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/curl_warp.sh)\
*2. Rasterise available vector labels using [rasterise_LBL.sh](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/rasterise_LBL.sh)\
3. 2-step normalisation (z-score --> linear scale) using [labelmaker.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/labelmaker.ipynb)\
*4. Split the RGB into separate tif using [RGB_split.sh](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/RGB_split.sh)\
**5. Create virtual raster with 4 bands (R, G, B, Labels) using [gdalbuildvrt](https://gdal.org/programs/gdalbuildvrt.html)\
**6. From VRT make permenant raster tif using [gdal_translate](https://gdal.org/programs/gdal_translate.html)\
7. Return to labelmaker.ipynb and crop the stacked raster using [labelmaker.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/labelmaker.ipynb)\
8. Clean the stacked and cropped raster for no labels and non conformity using [KBY_clean.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/KBY_clean.ipynb)\
*9. Change the tiff to png, and delete the tiff using [tiff2png.sh](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/tiff2png.sh)

*.sh scripts are Unix instructed shell script. Run these scripts using ./NAME_OF_SHELL_SCRIPT.sh on your Linux terminal. If you are using windows machine, you can run these scripts using [Cygwin](https://www.cygwin.com/) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/about)
*Take extra care that many shell scrip have targetted reprojection EPSG projection automatically set to map projection [EPSG:3857](https://epsg.io/3857). You might want to change that depending on your usage.
**gdal is an open-source geospatial processing library. Which contains many shell and python scripts executing processes with good memory efficiency.

## Training pipeline
1. Dataloader [dataloader.py](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/dataloader.py)
2. Training loop [Train_loop.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/Train_loop.ipynb)
3. Some classical U-Nets are available as class objects through [Networks.py](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/Networks.py)
4. Otherwise, the rest of the CNNs are constructed using higher level API [segmentation-models-pytorch](https://segmentation-models-pytorch.readthedocs.io/en/latest/models.html)

## Exploratory Data Analysis
See example:
1. [EDA_BASEruns.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/EDA_BASEruns.ipynb)
2. [PR_delta.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/PR_delta.ipynb)

## Testing and Predicion
1. For single image testing on various networks see [ALLtest_model.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/ALLtest_model.ipynb)
2. For custom function to parse each camp and predict using a trained network, see [PredSeg_Camp.ipynb](https://github.com/chrischank/HOTOSM_OAM_codeV2/blob/master/PredSeg_Camp.ipynb)
  
## Baseline training results for Kalobeyei, Kakuma (perfect dataset)
- Dataset: 256x256 px. 0.15 m/px.
- Trainning data with augmentation: 5719
- Validation data with augmentation: 1224
- Testing data: 272
- Optimiser: Adam
- Learning rate: 1e-3
- Weight decay: 1e-5
- Batch size: 32, 16(OCC - 5 layer EB1-Unet)
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

![256KBYFour-UnetBASE](https://user-images.githubusercontent.com/36608720/182344718-42d07704-9fbe-4f47-8bc4-985d87a5ad49.png)
![256KBYFive-UnetBASE](https://user-images.githubusercontent.com/36608720/182344738-71dc0c72-5cb0-42a1-8c92-003fe7214638.png)
![256KBYEB1-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/182344864-51a2154f-5120-49ad-b367-20e8811cd517.png)
![256KBYEB1-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/182344824-4700ce1c-f3cc-43e1-b115-285e48231f92.png)
![256KBYEB1-UNet-OCCUNTRAINEDBASE](https://user-images.githubusercontent.com/36608720/182344912-1e15da1d-3f11-48a2-964f-245423f72420.png)
![256KBYEB1-UNet-OCCBASE](https://user-images.githubusercontent.com/36608720/182344944-49babf87-27e4-401a-bc0b-0d4a9e46e05c.png)

## Baseline training results for Kalobeyei + Dzaleka + Dzaleka North (full dataset)
- Dataset: 256x256 px. 0.15 m/px.
- Trainning data with augmentation: 18242
- Validation data with augmentation: 3909
- Testing data: 435
- Optimiser: Adam
- Learning rate: 1e-3
- Weight decay: 1e-5
- Batch size: 32, 16(OCC - 5 layer EB1-Unet)
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

![256ALLFour-UnetBASE](https://user-images.githubusercontent.com/36608720/182214024-858a851c-7cd0-48cb-bcbd-44bacf714f7e.png)
![256ALLFive-UnetBASE](https://user-images.githubusercontent.com/36608720/182214075-3caca019-e8b4-434e-b454-93ee4775292f.png)
![256ALLEB1-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/182214150-ccd3ad7d-5d1c-4902-91ac-488cccf469d1.png)
![256ALLEB1-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/182218635-186d4cc6-7c0c-46db-9be6-97272446d320.png)
![256ALLEB1-UNet-OCCUNTRAINEDBASE](https://user-images.githubusercontent.com/36608720/182214213-469c84c8-9286-4d7f-99a4-26c651075839.png)
![256ALLEB1-UNet-OCCBASE](https://user-images.githubusercontent.com/36608720/182218812-f2bcfa08-a5e7-4ea2-90e5-f622a0861fab.png)

## Class-based accuracy assesments
![cat_CAA](https://user-images.githubusercontent.com/36608720/183244569-3cb4c28a-92a6-4105-a29c-643b5e4e409a.png)

## EfficientNet B2 header performance
- Dataset: 256x256 px. 0.15 m/px.
- Trainning data with augmentation: 18242
- Validation data with augmentation: 3909
- Testing data: 435
- Optimiser: Adam
- Learning rate: 1e-3
- Weight decay: 1e-5
- Batch size: 32
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

<p align="center">
  EfficientNet B2 header U-Net ImageNet vs No ImageNet (Vanilla) weights, where: red = ImageNet and blue = No ImageNet
  <img src="https://user-images.githubusercontent.com/36608720/171561584-7696bc54-fe9b-4130-bf56-98a868d2b798.png"/> 
</p>

![256KBYEB2-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/182345044-bef97ab2-a1b7-41d8-b37d-bf11ff7721ca.png)
![256KBYEB2-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/182345337-89d379b5-e59a-423a-80cb-c7d0b13ddcb0.png)
![256ALLEB2-UNet-NoIMN](https://user-images.githubusercontent.com/36608720/171693413-a62c39f0-24c7-4ece-9932-89b329ca50c6.png)
![256ALLEB2-UNet-IMN](https://user-images.githubusercontent.com/36608720/171693400-c64623e9-472c-48d6-8d5b-15039f855d1d.png)

## Depth-wise Precision and Recall change

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/189317817-3848096a-20ae-498c-8eda-2abb8b391fd6.png"/>
  <img src="https://user-images.githubusercontent.com/36608720/189317885-1e32ab85-d6a3-4aa9-8a56-5056c3598d00.png"/>
</p>

## Dataset-wise Precision and Recall change

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/189317946-148ddab8-bde3-4371-b358-adecc3627170.png"/>
  <img src="https://user-images.githubusercontent.com/36608720/189318013-03466f2d-be3e-488d-b8e9-b50efcea3ea0.png"/>
</p>

## Weight-wise Precision and Recall change

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/189318135-dca2eb36-1fe3-497a-ab32-b7757b874950.png"/>
  <img src="https://user-images.githubusercontent.com/36608720/189318179-ea5819e6-2270-4cc4-9c75-feeebd880ed8.png"/>
</p>

## Key takeaways
1. Deeper network tends to reduce the classification of False Positive
2. Architectures trained with initialised weights from ImageNet tends to reduce the classification of False Negative
3. Transferability of competition winning network is limited
4. Models might have better precision than calculated due to Human labelling ambiguity

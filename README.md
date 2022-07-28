# HOTOSM_OAM_codeV2

This github repository is the code-base for the Master Thesis submitted for the Master der Naturwissenschaften in Applied Earth Observation and Geoanalysis of the Living Environment (EAGLE) at the Julius-Maximilians-Universität Würzburg.

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/166689718-e570c0f4-e09d-49da-80c3-58f062d04896.png"
 />
</p>

This work of this thesis is partnered with the Humanitarian OpenStreetMap (HOTOSM) and supported by the German Aerospace Center / Deutsches Zentrum für Luft- und Raumfahrt (DLR).

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/166691521-16efc2f3-6aee-4e1b-9c89-15492dfdc7b3.png"
 />
  <img src="https://user-images.githubusercontent.com/36608720/166690232-c61e3ee2-3a7b-4452-ac55-7a6b3e1c5e2f.png"
 />
</p>

## Introduction
HOTOSM would like to develop a solution for assisted mapping which can predict buildings in refugee camps on the drone imagery provided by associated organisation OpenAerialMap. Refugee camps and informal settlements reside some of the most vulnerable population, the  majority of which are located in Sub-Saharan East Africa (UNHCR, 2016). Many of these  settlements often lack up-to-date maps of which we take for granted in developed cities. Having up-to-date maps are important for assisting administration (e.g. population estimates,  infrastructure development) in data impoverished environments and thereby encourages  economic productivity (Herfort et al., 2021). The data inequality between developed and  developing areas can be reduced using assisted mapping technology. To extract geospatial and imagery characteristics of dense urban enviornments, a combination of VHR satellite imagery and Machine Learning (ML) are commonly used. Recent advances in CV based Deep Learning might be able to address these issues. Convolutional Neural Networks (CNN) are a subtype of the Deep Learning (DL) family used in  CV tasks. Past studies using CNN have shown high accuracy and transferability in small  geographical setting (Kuffer et al., 2022). The datasets provided for this project consist of both highly structured, zoned newer refugee camps and chaotic, highly complex older camps. In  addition, roofing materials are highly heterogeneous, especially in older sites where thatched  roofs are often mixed with litter. This coupled with the complex spatial autocorrelation and  relation due to the lack of zoning in older sites hinder rule-based and conventional ML based  approach. Therefore, a CNN based approach might be able to simplify the task of selecting and  testing parameters, taking advantage of VHR textural information but also learning contextual  relations (Lang et al., 2022; Lehner & Blaschke, 2022). This study will be connected to a pilot project on testing the capabilities of building segmentation.

<p align="center">
  <img src="https://user-images.githubusercontent.com/36608720/181209381-93c4d351-f530-4625-a497-246676a12848.png"
 />
</p>
  
## Baseline training results for Kalobeyei, Kakuma (perfect dataset)
- Dataset: 256x256 px. 0.15 m/px.
- Trainning data with augmentation: 5719
- Validation data with augmentation: 1224
- Testing data: 272
- Optimiser: Adam
- Learning rate: 1e-3
- Weight decay: 1e-5
- Batch size: 32, 16(qubvel - 5 layer EB1-Unet)
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

![256KBYFour-UnetBASE](https://user-images.githubusercontent.com/36608720/165932776-75ecdd33-7cb9-4660-8312-e8625a52c77b.png)
![256KBYEB1-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/165932771-60871747-23b4-46ac-83d6-a34626e52699.png)
![256KBYEB1-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/165932767-15b04c02-3b3c-4d1f-8999-5408248abaab.png)
![256KBYEB1-UNet-OCCUNTRAINEDBASE](https://user-images.githubusercontent.com/36608720/165932774-71b35a31-7b32-4026-a704-5a0f710e57f8.png)
![256KBYEB1-UNet-OCCBASE](https://user-images.githubusercontent.com/36608720/165932763-213326de-d973-45d3-89b3-8ce3b893fa49.png)

## Baseline training results for Kalobeyei + Dzaleka + Dzaleka North (full dataset)
- Dataset: 256x256 px. 0.15 m/px.
- Trainning data with augmentation: 18242
- Validation data with augmentation: 3909
- Testing data: 435
- Optimiser: Adam
- Learning rate: 1e-3
- Weight decay: 1e-5
- Batch size: 32, 16(qubvel - 5 layer EB1-Unet)
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

![256ALLFour-UnetBASE](https://user-images.githubusercontent.com/36608720/169056447-7e3729fe-ca00-4cde-b487-d6797e150104.png)
![256ALLEB1-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/169056436-a54ca6cd-d05d-4edd-bf66-41beff400702.png)
![256ALLEB1-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/169056430-b8d7b387-8f29-4c0e-b0bd-bbb6383f7acb.png)
![256ALLEB1-UNet-OCCUNTRAINEDBASE](https://user-images.githubusercontent.com/36608720/169056438-8695e156-5da8-4f39-a3b6-d047b6551053.png)
![256ALLEB1-UNet-OCCBASE](https://user-images.githubusercontent.com/36608720/169056421-59664ea0-6d7c-426b-907a-8201f8ec6d76.png)

## Class-based accuracy assesments
![cat_CAA](https://user-images.githubusercontent.com/36608720/181450347-a36cc55b-2882-4e0c-a7c0-02071fa70aef.png)


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
  <img src="https://user-images.githubusercontent.com/36608720/171561584-7696bc54-fe9b-4130-bf56-98a868d2b798.png" /> 
</p>

![256ALLEB2-UNet-NoIMN](https://user-images.githubusercontent.com/36608720/171693413-a62c39f0-24c7-4ece-9932-89b329ca50c6.png)
![256ALLEB2-UNet-IMN](https://user-images.githubusercontent.com/36608720/171693400-c64623e9-472c-48d6-8d5b-15039f855d1d.png)

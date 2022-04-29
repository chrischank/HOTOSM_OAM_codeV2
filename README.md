# HOTOSM_OAM_codeV2

## Introduction
HOTOSM would like to develop a solution for assisted mapping which can predict buildings in refugee camps on the drone imagery provided by associated organisation OpenAerialMap. Refugee camps and informal settlements reside some of the most vulnerable population, the  majority of which are located in Sub-Saharan East Africa (UNHCR, 2016). Many of these  settlements often lack up-to-date maps of which we take for granted in developed cities. Having up-to-date maps are important for assisting administration (e.g. population estimates,  infrastructure development) in data impoverished environments and thereby encourages  economic productivity (Herfort et al., 2021). The data inequality between developed and  developing areas can be reduced using assisted mapping technology. To extract geospatial and imagery characteristics of dense urban enviornments, a combination of VHR satellite imagery and Machine Learning (ML) are commonly used. Recent advances in CV based Deep Learning might be able to address these issues. Convolutional Neural Networks (CNN) are a subtype of the Deep Learning (DL) family used in  CV tasks. Past studies using CNN have shown high accuracy and transferability in small  geographical setting (Kuffer et al., 2022). The datasets provided for this project consist of both highly structured, zoned newer refugee camps and chaotic, highly complex older camps. In  addition, roofing materials are highly heterogeneous, especially in older sites where thatched  roofs are often mixed with litter. This coupled with the complex spatial autocorrelation and  relation due to the lack of zoning in older sites hinder rule-based and conventional ML based  approach. Therefore, a CNN based approach might be able to simplify the task of selecting and  testing parameters, taking advantage of VHR textural information but also learning contextual  relations (Lang et al., 2022; Lehner & Blaschke, 2022). This study will be connected to a pilot project on testing the capabilities of building segmentation.

![ETL_flow2](https://user-images.githubusercontent.com/36608720/165942666-2a05cde2-62be-4fad-b298-a8680b07122c.png)

## Baseline training results for Kalobeyei, Kakuma (perfect dataset)
- Dataset: 256x256 px. 0.15 m/px.
- Trainning data with augmentation: 5719
- Validation data with augmentation: 1224
- Testing data: 435
- Optimiser: Adam
- Learning rate: 1e-3
- Weight decay: 1e-5
- Batch size: 32, 16(qubvel - 5 layer EB1-Unet)
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

![256KBYFour-UnetBASE](https://user-images.githubusercontent.com/36608720/165932776-75ecdd33-7cb9-4660-8312-e8625a52c77b.png)
![256KBYEB1-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/165932767-15b04c02-3b3c-4d1f-8999-5408248abaab.png)
![256KBYEB1-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/165932771-60871747-23b4-46ac-83d6-a34626e52699.png)
![256KBYEB1-UNet-OCCUNTRAINEDBASE](https://user-images.githubusercontent.com/36608720/165932774-71b35a31-7b32-4026-a704-5a0f710e57f8.png)
![256KBYEB1-UNet-OCCBASE](https://user-images.githubusercontent.com/36608720/165932763-213326de-d973-45d3-89b3-8ce3b893fa49.png)

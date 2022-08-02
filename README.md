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
- Batch size: 32, 16(qubvel - 5 layer EB1-Unet)
- Scheduler: Reduce Learning Rate on Plateau(min 1e-8) [Patient: 20 epochs, factor: 0.1]

![256ALLFour-UnetBASE](https://user-images.githubusercontent.com/36608720/182214024-858a851c-7cd0-48cb-bcbd-44bacf714f7e.png)
![256ALLFive-UnetBASE](https://user-images.githubusercontent.com/36608720/182214075-3caca019-e8b4-434e-b454-93ee4775292f.png)
![256ALLEB1-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/182214150-ccd3ad7d-5d1c-4902-91ac-488cccf469d1.png)
![256ALLEB1-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/182218635-186d4cc6-7c0c-46db-9be6-97272446d320.png)
![256ALLEB1-UNet-OCCUNTRAINEDBASE](https://user-images.githubusercontent.com/36608720/182214213-469c84c8-9286-4d7f-99a4-26c651075839.png)
![256ALLEB1-UNet-OCCBASE](https://user-images.githubusercontent.com/36608720/182218812-f2bcfa08-a5e7-4ea2-90e5-f622a0861fab.png)

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

![256KBYEB2-UNet-NoIMNBASE](https://user-images.githubusercontent.com/36608720/182345044-bef97ab2-a1b7-41d8-b37d-bf11ff7721ca.png)
![256KBYEB2-UNet-IMNBASE](https://user-images.githubusercontent.com/36608720/182345337-89d379b5-e59a-423a-80cb-c7d0b13ddcb0.png)
![256ALLEB2-UNet-NoIMN](https://user-images.githubusercontent.com/36608720/171693413-a62c39f0-24c7-4ece-9932-89b329ca50c6.png)
![256ALLEB2-UNet-IMN](https://user-images.githubusercontent.com/36608720/171693400-c64623e9-472c-48d6-8d5b-15039f855d1d.png)

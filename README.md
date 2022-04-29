# HOTOSM_OAM_codeV2

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

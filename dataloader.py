###############################
#Data Loading Script and Class#
#Maintainer: Christopher Chan #
#Date: 2022-02-11             #
#Version: 0.0.3               #
###############################

import os
import torch
import PIL
import torchvision.transforms.functional as transform
from torch.utils.data import Dataset

class BuildingDataset(Dataset):
    def __init__(self, png_dir, lbl_dir, transform=None):
        self.png_dir = png_dir
        self.lbl_dir = lbl_dir
        self.transform = transform

    def __len__(self):
        return len(self.png_dir) + len(self.lbl_dir)

    def __getitem__(self, idx):

        # Since gdal can only output format to UInt16
        # We use the dataset building to format to UInt8
        image_iter = self.png_dir[idx]
        label_iter = self.lbl_dir[idx]

        P_image = PIL.Image.open(image_iter)
        P_label = PIL.Image.open(label_iter)

        image = transform.to_tensor(P_image)
        label = transform.to_tensor(P_label)

        if self.transform: # What are these things?
            image = self.transform(image)
            label = self.transform(label)

        return image, label

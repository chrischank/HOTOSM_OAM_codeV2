###############################
#Data Loading Script and Class#
#Maintainer: Christopher Chan #
#Date: 2022-02-11             #
#Version: 0.0.3               #
###############################

import os
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.io import read_image, ImageReadMode

class BuildingDataset(Dataset):
    def __init__(self, png_dir, lbl_dir, transform=None):
        self.png_dir = png_dir
        self.lbl_dir = lbl_dir
        self.transform = transform

    def __len__(self):
        return len(self.png_dir), len(self.lbl_dir)

    def __getitem__(self, idx):
        img_path = os.path.join(self.png_dir)
        lbl_path = os.path.join(self.lbl_dir)

        # Since gdal can only output format to UInt16
        # We use the dataset building to format to UInt8
        image = read_image(img_path[idx], mode = ImageReadMode.RGB)
        label = read_image(lbl_path[idx], mode = ImageReadMode.GRAY)
        if self.transform: # What are these things?
            image = self.transform(image)
            label = self.transform(label)

        return image, label

###############################
#Data Loading Script and Class#
#Maintainer: Christopher Chan #
#Date: 2022-03-13             #
#Version: 0.2.2               #
###############################

import os
import torch
import PIL
import torchvision
import torchvision.transforms.functional as transform
import numpy as np
from torch.utils.data import Dataset

class BuildingDataset(Dataset):
    def __init__(self, png_dir, lbl_dir, transform = None):
        self.png_dir = png_dir
        self.lbl_dir = lbl_dir
        self.transform = transform

    def __len__(self):
        return len(self.png_dir)

    def __getitem__(self, idx):
        image_iter = self.png_dir[idx]
        label_iter = self.lbl_dir[idx]

        P_image = PIL.Image.open(image_iter)
        P_label = PIL.Image.open(label_iter)

        image = transform.to_tensor(P_image)
        label = transform.to_tensor(P_label)

        if transform is not None:
            if self.transform == "Hflip":
                image = transform.hflip(image)
                label = transform.hflip(label)

            elif self.transform == "Vflip":
                image = transform.vflip(image)
                label = transform.vflip(label)

            elif self.transform == "InRGB":
                image = transform.invert(image)
                label = label

        return image, label

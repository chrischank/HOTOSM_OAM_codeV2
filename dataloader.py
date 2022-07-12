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
import torchvision.transforms.functional as f
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

        image = f.to_tensor(P_image)
        label = f.to_tensor(P_label)

        if self.transform is not None:
            if self.transform == "Hflip":
                image = f.hflip(image)
                label = f.hflip(label)

            elif self.transform == "Vflip":
                image = f.vflip(image)
                label = f.vflip(label)

            elif self.transform == "InRGB":
                image = f.invert(image)
                label = label

            elif self.transform == "Grayscale":
                image = f.rgb_to_grayscale(image)
                label = label

            elif self.transform == "Blur":
                image = f.gaussian_blur(image, 25)
                label = label

            elif self.transform == "Contrast":
                image = f.autocontrast(image)
                label = label

            elif self.transform == "Solarize":
                image = f.solarize(image, 0)
                label = label

        return image, label

class PredictionDataset(Dataset):
    def __init__(self, png_dir, transform = None):
        self.png_dir = png_dir

    def __len__(self):
        return len(self.png_dir)

    def __getitem__(self, idx):
        image_iter = self.png_dir[idx]

        P_image = PIL.Image.open(image_iter)

        image = f.to_tensor(P_image)
        
        return image

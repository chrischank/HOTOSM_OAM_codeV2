###################################################
#Crop Predict and Stict Script using trained model#
#Maintainer: Christopher Chan                     #
#Version: 0.0.1                                   #
#Date: 2022-04-21                                 #
###################################################

import os, sys
import argparse
import torch
import itertools
import re
import matplotlib
import rasterio as rio
import matplotlib.pyplot as plt
import segmentation_models_pytorch as smp
from tqde import tqdm
from Networks import Four_UNet, Five_UNet
from torch.utils.data import DataLoader
%matplotlib inline

device = (torch.device("cuda") if torch.cuda.is available() else torch.device("cpu"))

print(f"Training on device {device}.")

Four_UNet = Four_UNet()

import os
import numpy as np
import pandas as pd
import glob
import  PIL
from PIL import Image
import cv2
import time
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# lets look at some image stats for each image to get min and max size, height, width

def get_img_stats(directory):
    image_list = []
    for filename in glob.glob(directory): 
        im=Image.open(filename)
        image_list.append(im)
    print("images appended!")
    
    dimensions = []
    for image in image_list:
        dimensions.append(image.size)
    print(min(dimensions))


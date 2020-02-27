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

# reshape the images using Keras 

# get all the data in the directory split/test (230 images), and reshape them
test_generator = ImageDataGenerator(rescale=1./255).flow_from_directory('split/test/', 
        target_size=(140, 100), batch_size = 230)

# get all the data in the directory split/train (570 images), and reshape them
train_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
    'split/train/', 
    target_size=(140, 100), batch_size=570)

# get all the data in the directory split/validation (160 images), and reshape them
val_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
    'split/validation/', 
    target_size=(140, 100), batch_size = 160)

# create the train test and validation data sets
train_images, train_labels = next(train_generator)
test_images, test_labels = next(test_generator)
val_images, val_labels = next(val_generator)

# creat train, test, and validation image sets
train_img = train_images.reshape(train_images.shape[0], -1)
test_img = test_images.reshape(test_images.shape[0], -1)
val_img = val_images.reshape(val_images.shape[0], -1)

# reshape the ys
train_y = np.reshape(train_labels[:,0], (542,1))
test_y = np.reshape(test_labels[:,0], (180,1))
val_y = np.reshape(val_labels[:,0], (200,1))
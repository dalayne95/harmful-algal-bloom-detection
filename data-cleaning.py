import os
import numpy as np
import pandas as pd
import  PIL
from PIL import Image
import time
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# lets look at some image stats for each image to get min and max size, height, width

def get_size_stats(DIR):
    heights=[]
    widths=[]
    for image in os.walk(DIR): # os.path.walk goes into a directory and recurses into subdirectories 
        path = os.path.join(DIR, image) # os.path.join "joins path componenets intelligently" 
        data = np.array(Image.open(path)) # image.open(path) opens the image at the specified path
        heights.append(data.shape[0]) # append the height to the heights list
        widths.append(data.shape[1]) # append the width to the widths list
    #height_avg = np.mean(heights)
    #width_avg = np.mean(widths )

    print("Max Height: " + str(max(heights)))
    print("Min Height: " + str(min(heights)))
    print('\n')
    print("Max Width: " + str(max(widths)))
    print("Min Width: " + str(min(widths)))



# reshape the images
# ImageDataGenerator "Generate batches of tensor image data with real-time data augmentation. The data will be looped over (in batches)."

""" train_generator = ImageDataGenerator(rescale=None).flow_from_directory(
    train_folder, 
    target_size=(64,64), batch_size=(570))

test_generator = ImageDataGenerator(rescale=None).flow_from_directory(
    test_folder,
    target_size=(64,64), batch_size=(230))

val_generator = ImageDataGenerator(rescale=None).flow_from_directory(
    val_folder,
    target_size=(64,64), batch_size=(160) """

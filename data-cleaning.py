import numpy as np
import pandas as pd
#from PIL import image
import time
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from split import *
from PIL.Image import Image

# lets look at some image stats for each image to get min and max size, height, width

def get_size_stats(directory):
    heights=[]
    widths=[]
    for image in os.listdir(directory):
        path = os.path.join(directory, image)
        data = np.array(Image.open(path)) # Need to get PIL working ugh 
        heights.append(data.shape[0])
        widths.append(data.shape[1])
    height_avg = sum(heights) / len(heights)
    width_avg = sum(widths) / len(widths)

    print("Average Height: " + str(height_avg))
    print("Max Height: " + str(max(heights)))
    print("Min Height: " + str(min(heights)))
    print('\n')
    print("Average Width: " + str(width_avg))
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

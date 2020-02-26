import numpy as np
import pandas as pd
#from PIL import image
import time
import matplotlib.pyplot as plt
import scipy
#from PIL import Image
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from split import *

# reshape the images
# ImageDataGenerator "Generate batches of tensor image data with real-time data augmentation. The data will be looped over (in batches)."

train_generator = ImageDataGenerator(rescale=None).flow_from_directory(
    train_folder, 
    target_size=(64,64), batch_size=(570))

test_generator = ImageDataGenerator(rescale=None).flow_from_directory(
    test_folder,
    target_size=(64,64), batch_size=(230))

val_generator = ImageDataGenerator(rescale=None).flow_from_directory(
    val_folder,
    target_size=(64,64), batch_size=(160)

import pandas as pd
import numpy as np
#from PIL import image
import os, shutil

# first step is to split the data into train and test and validate sets 

# make a new object for each existing directory + a new split one
img_algae_bloom = 'images/algae-blooms/'
img_not_algae_bloom = 'images/not-algae-blooms/'
new_dir = 'split/'

# create an object that stores all relevant image names 
ext = [".jpg", ".jpeg", ".png"]
imgs_algae= [file for file in os.listdir(img_algae_bloom) if file.endswith(tuple(ext))]
imgs_not_algae = [file for file in os.listdir(img_not_algae_bloom) if file.endswith(tuple(ext))]

# how many img are there in the algae directory?
print("There are", len(imgs_algae), "with algae in them")
print("There are", len(imgs_not_algae), "without algae in them")

# Make a new directory called "new_dir"
os.mkdir(new_dir)

# use os.path.join to join a new multi-level directory together
train_folder = os.path.join(new_dir, 'train')
train_algae = os.path.join(train_folder, 'algae')
train_not_algae = os.path.join(train_folder, 'not_algae')

test_folder = os.path.join(new_dir, 'test')
test_algae = os.path.join(test_folder, 'algae')
test_not_algae = os.path.join(test_folder, 'not_algae')

val_folder = os.path.join(new_dir, 'validation')
val_algae = os.path.join(val_folder, 'algae')
val_not_algae = os.path.join(val_folder, 'not_algae')

# Make the directories
os.mkdir(train_folder)
os.mkdir(train_algae)
os.mkdir(train_not_algae)

os.mkdir(test_folder)
os.mkdir(test_not_algae)
os.mkdir(test_not_algae)

os.mkdir(val_folder)
os.mkdir(val_algae)
os.mkdir(val_not_algae)

# build your train, test, and val image sets for algae  

# build a train algae set of 285 images 
imgs_atrain = imgs_algae[:285]
for image in imgs_atrain:
    origin = os.path.join(img_algae_bloom, image)
    destination = os.path.join(train_algae, image)
    shutil.copyfile(origin, destination)

# build a test algae set of 115 imgs
imgs_atest = imgs_algae[285:400]
for image in imgs_atest:
    origin = os.path.join(img_algae_bloom, image)
    destination = os.path.join(test_algae, image)
    shutil.copyfile(origin, destination)

# build a validation algae set of 95 imgs
imgs_aval = imgs_algae(400:)
for image in imgs_aval:
    origin = os.path.join(img_algae_bloom, image)
    destination = os.path.join(val_algae, image)
    shutil.copyfile(origin, destination)

#  build your train image sets for not_algae
imgs_natrain = imgs_not_algae[:285]
for image in imgs_natrain:
    origin = os.path.join(img_not_algae_bloom, image)
    destination - os.path.join(imgs_natrain, image)

#  build your test image sets for not_algae
imgs_natest = imgs_not_algae[285:400]
for image in imgs_natest:
    origin = os.path.join(img_not_algae_bloom, image)
    destination - os.path.join(imgs_natest, image)

#  build your val image sets for not_algae
imgs_naval = imgs_not_algae[400:]
for image in imgs_naval:
    origin = os.path.join(img_not_algae_bloom, image)
    destination - os.path.join(imgs_naval, image)

print('There are', len(os.listdir(train_algae)), 'algae images in the training set')
print('There are', len(os.listdir(test_algae)), 'algae images in the test set')
print('There are', len(os.listdir(val_algae)), 'algae images in the validation set')
print('There are', len(os.listdir(train_not_algae)), 'not algae images in the training set')
print('There are', len(os.listdir(test_not_algae)), 'not algae images in the test set')
print('There are', len(os.listdir(val_not_algae)), 'not algae images in the validation set')

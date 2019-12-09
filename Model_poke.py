#!/usr/bin/env python

###Modules###

import os
os.getcwd()
#os.chdir('Documents/FirstDeeplearningProject')
import time
import numpy as np
from functions import DataPreparation,PlotImages,CreateModel
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.preprocessing.image import ImageDataGenerator

###Data Path###

categories = ['Morty','Rick']
data_dir = '/home/machinelearning/Documents/FirstDeepLearningProject/Rick_And_Morty_Dataset/'
train = os.path.join(data_dir,'Train')
validation =  os.path.join(data_dir,'Validation')

###Data Preparation###
batch_size = 20
img_size = 100

start = time.time()

print('###################')
print('###### START ######')
print('###################')

###DataPreparation###

train_data_gen, sample_train_images,categories_train_images = DataPreparation(
		batch_size,train,categories,img_size,b=True)
val_data_gen, sample_val_images,categories_val_images = DataPreparation(
		batch_size,validation,categories,img_size,b=False)
#show train and val data

print('Train data')
PlotImages(sample_train_images,categories_train_images)
print('Validation data')
PlotImages(sample_val_images,categories_val_images)

###Create the model###

model = CreateModel(img_size)
name = 'Rick-Morty-CNN'
tensorboard = TensorBoard(log_dir="logs/{}".format(name))
epochs = 100

###Train the model###

hist = model.fit_generator(
	train_data_gen ,
	steps_per_epoch=int(np.ceil(train_data_gen.n) / float(batch_size)),
	epochs=epochs,
	validation_data=val_data_gen,
	validation_steps=int(np.ceil(val_data_gen.n)  / float(batch_size)),
	callbacks=[tensorboard]
)

###Save the model###
model.save(name+'.model')


print('#################')
print('#####  DONE #####')
print('#################')
print('')
print("- t_read = %s s -" % (time.time() - start))

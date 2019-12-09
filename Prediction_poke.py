#!/usr/bin/env python
###Modules###
import os
#os.chdir('Documents/FirstDeeplearningProject')
import numpy as np
import pandas as pd
import time
from functions import PlotImages,DataPreparation
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

###Data preparation###
print('###################')
print('###### START ######')
print('###################')
start = time.time()
data_test = '/home/machinelearning/Documents/FirstDeeplearningProject/Rick_And_Morty_Dataset/Test'

categories = ['Morty','Rick']
img_size = 100
batch_size = 40

test_data_gen,sample_test_images,categories_test_images = DataPreparation(
        batch_size,
        data_test,
        categories,
        img_size,
        b = False)
#print(sorted(test_data_gen))
print('Test:')
PlotImages(sample_test_images,categories_test_images)

###Prediction###
model = tf.keras.models.load_model("Rick-Morty-CNN.model")
pred = model.predict_generator(test_data_gen,steps=len(test_data_gen),verbose=1)
#test_data_gen.reset()
predicted_class_indices = np.argmax(pred,axis=1)
predictions = [categories[k] for k in predicted_class_indices]
filenames = sorted(test_data_gen.filenames)
results = pd.DataFrame({"Filenames":filenames,"labels":categories_test_images,"Predictions":predictions})

print(results)
print('#################')
print('#####  DONE #####')
print('#################')
print('')
print("- t_read = %s s -" % (time.time() - start))

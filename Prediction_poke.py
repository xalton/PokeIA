#!/usr/bin/env python
###Modules###
import os
import numpy as np
import pandas as pd
import time
from functions_poke import PlotImages,DataPreparation
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

###Data preparation###
print('###################')
print('###### START ######')
print('###################')
start = time.time()
data_test = '/home/machinelearning/Documents/PokeIA/Dataset/Test'

categories = sorted(os.listdir(data_test))
categories
img_size = 100
batch_size = 32

test_data_gen,sample_test_images,categories_test_images = DataPreparation(
        batch_size,
        data_test,
        categories,
        img_size,
        b = False)
#print(len(test_data_gen.filenames))
print('Test:')
filenames = sorted(test_data_gen.filenames)
nb_samples = len(filenames)
PlotImages(sample_test_images,categories_test_images)

###Prediction###
model = tf.keras.models.load_model("PokeIA-CNN.model/")
pred = model.predict_generator(test_data_gen,steps=np.ceil(nb_samples/batch_size))
#test_data_gen.reset()
predicted_class_indices = np.argmax(pred,axis=1)
predictions = [categories[k] for k in predicted_class_indices]
results = pd.DataFrame({"Filenames":filenames,"Predictions":predictions})

print(results)
print('#################')
print('#####  DONE #####')
print('#################')
print('')
print("- t_read = %s s -" % (time.time() - start))

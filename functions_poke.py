import os
import re
import time
import pandas as pd
import numpy as np
import tensorflow
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

def DataPreparation(batch_size,path,categories,img_size,b):
    if b == True:
        image_gen_train = ImageDataGenerator(
        	rescale=1/255,
        	rotation_range=45,
        	shear_range=0.2,
        	width_shift_range=0.2,
        	height_shift_range=0.2,
        	horizontal_flip=True,
        	fill_mode='nearest')
        train_data_gen = image_gen_train.flow_from_directory(
            batch_size=batch_size,
            directory=path,
            shuffle=True,
            target_size=(img_size,img_size),
            class_mode= "binary")
        sample_train_images, labels_train = next(train_data_gen)
        categories_train_images = [categories[int(l)] for l in labels_train]
        return train_data_gen,sample_train_images,categories_train_images
    elif b == False:
        image_gen_val = ImageDataGenerator(rescale=1/255)
        val_data_gen = image_gen_val.flow_from_directory(
            batch_size=batch_size,
            directory=path,
            shuffle=False,
            target_size=(img_size,img_size ),
        	class_mode='binary')
        sample_val_images, labels_val = next(val_data_gen)
        categories_val_images = [categories[int(l)] for l in labels_val]
        return val_data_gen,sample_val_images,categories_val_images

def PlotImages(images_arr,labels):
    fig, axes = plt.subplots(1, 5, figsize=(20,20))
    axes = axes.flatten()
    for img, ax,l in zip( images_arr, axes,labels ):
        ax.imshow(img)
        ax.set_title(l,fontsize='30')
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def CreateModel(img_size):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
    		activation='relu',
            input_shape=(img_size, img_size, 3)))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
    		loss='sparse_categorical_crossentropy',
    		metrics=['accuracy'])
    model.summary()
    return model


def sav(name):
    model.save(name+'.model')

def TrainModel(name):
    data_dir = '/home/machinelearning/Documents/PokeIA/Dataset/'
    train = os.path.join(data_dir,'Train')
    validation =  os.path.join(data_dir,'Validation')
    categories = sorted(os.listdir(train))
    categories
    ###Data Preparation###
    batch_size = 32
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
    #print('Train data')
    #PlotImages(sample_train_images,categories_train_images)
    #print('Validation data')
    #PlotImages(sample_val_images,categories_val_images)
    ###Create the model###
    model = CreateModel(img_size)
    tensorboard = TensorBoard(log_dir="logs/{}".format(name))
    file_writer = tensorflow.summary.create_file_writer('logs/{}'.format(name))
    epochs = 100

    ###Train the model###
    hist = model.fit_generator(
    	train_data_gen ,
    	steps_per_epoch=int(np.ceil(train_data_gen.n) / float(batch_size)),
    	epochs=epochs,
    	validation_data=val_data_gen,
    	validation_steps=int(np.ceil(val_data_gen.n)  / float(batch_size)),
    	callbacks=[tensorboard],
        verbose = 1,
    )

    ###Save the model###
    model.save(name+'.model')
    print('#################')
    print('#####  DONE #####')
    print('#################')
    print('')
    print("- t_read = %s s -" % (time.time() - start))

def Predic(image_path,name):
    ###Data preparation###
    print('###################')
    print('###### START ######')
    print('###################')
    start = time.time()
    path_test = '/home/machinelearning/Documents/PokeIA/Dataset/Test'
    categ = sorted(os.listdir(path_test))
    categ
    path = image_path.split("/")
    for label in categ:
        if label in image_path:
            poke = label
            print('Oh you see ' + poke)

    img_size = 100
    batch_size = 1
    img = load_img(image_path, target_size = (img_size, img_size))
    img = img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    #test_data_gen,sample_test_images,categories_test_images = DataPreparation(
    #        batch_size,
    #        image_path,
    #        poke,
    #        img_size,
    #        b = False)
    #print(len(test_data_gen.filenames))
    print('Test:')
    #filenames = sorted(test_data_gen.filenames)
    #nb_samples = len(filenames)

    ###Prediction###
    model = tensorflow.keras.models.load_model(name+".model/")
    #pred = model.predict_generator(test_data_gen,steps=np.ceil(nb_samples/batch_size))
    #test_data_gen.reset()
    predicted = model.predict(img)
    predicted_class_indices = np.argmax(predicted,axis=1)
    print(predicted_class_indices)
    pred = categ[predicted_class_indices[0]]
    if pred == poke:
        print('Success!')
        print(pred)

    return pred
    #results = pd.DataFrame({"Filenames":filenames,"Predictions":predictions})

    #print(results)
    print('#################')
    print('#####  DONE #####')
    print('')
    print('#################')
    print("- t_read = %s s -" % (time.time() - start))

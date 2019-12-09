from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
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

    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer='adam',
    		loss='sparse_categorical_crossentropy',
    		metrics=['accuracy','mean_squared_error'])
    model.summary()
    return model

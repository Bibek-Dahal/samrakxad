
import os
import os.path
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.layers import Dense,Flatten,Conv2D,MaxPooling2D,Dropout,Rescaling
from keras.models import Sequential
from keras.optimizers import Adam
from keras.models import load_model
from pathlib import Path,WindowsPath





"""  
    train_dataset = keras.preprocessing.image_dataset_from_directory('images/Set1/1.57-Red_Deer', \
    validation_split=0.2, subset="training", seed=123, batch_size=64, image_size=(200, 200))

    test_dataset = keras.preprocessing.image_dataset_from_directory('images/Set1/1.57-Red_Deer', validation_split=0.2,\
    subset="validation", seed=123, batch_size=64, image_size=(200, 200))




model = Sequential([
    
    Rescaling(1./255),
    Conv2D(64,(3,3),activation='relu',input_shape=(200,200,3)),
    MaxPooling2D(2,2),
    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128,(3,3),activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128,(3,3),activation='relu'),
    MaxPooling2D(2,2),
    #Flatten the results to feed into DNN
    Flatten(),
    Dropout(0.5),
    Dense(512,activation='relu'),
    Dense(100,activation='softmax')
    
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = model.fit(train_dataset,epochs=10,validation_data=test_dataset)

def performance_graph():
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(10)

    plt.figure(figsize=(40,40))
    plt.subplot(5,5,1)
    plt.plot(epochs_range,acc,c='red',label='Training Accuracy')
    plt.plot(epochs_range,val_acc,c='green',label='Validation Accuracy')
    plt.legend(loc='lower right')

    plt.subplot(5,5,2)
    plt.plot(epochs_range,loss,c='red',label='Training Loss')
    plt.plot(epochs_range,val_loss,c='green',label='Validation Loss')
    plt.legend(loc='upper right')


if os.path.isfile('models/wildlife_monitoring.h5') is False:
    model.save('models/wildlife_monitoring.h5')
if os.path.isfile('models/wildlife_monitoring_weights.h5') is False:
    model.save_weights('models/wildlife_monitoring_weights.h5')


def display(display_list):
    plt.figure(figsize = (20,20))
    for images,labels in display_list.take(1):
        for i in range(9):
            plt.subplot(3,3,i+1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")

"""

def testModel(image):
    # pretrained_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    
    # pretrained_model.load_weights("/home/bibek/dev/projects/python_projects/wildlife_project/mysite/seqmodel/wildlife_monitoring_weights.h5")
    # pretrained_model=load_model(f"{os.getcwd()}/seqmodel/wildlife_monitoring.h5")
    file_path = f"{os.getcwd()}/wildlife/seqmodel/wildlife_monitoring.h5"
    pretrained_model=load_model(f"{os.getcwd()}/wildlife/seqmodel/wildlife_monitoring.h5")
    print("hello 000000000000000000000")
    print()
    print()
    print(pretrained_model)
    from django.core.files.storage import FileSystemStorage
    # pretrained_model.set_weights()
    fs = FileSystemStorage()
    # img_name = image.name
    file = fs.save('randomimagename', image)
    file_url = fs.url(file)
    type(file_url)
    print(file_url)
    img = keras.preprocessing.image.load_img(
        f"{os.getcwd()}{file_url}"
        , target_size=(200,200,3)
    )

    fs.delete(f"{os.getcwd()}{file_url}")
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = pretrained_model.predict(img_array)
    score = predictions[0]

    print(
        "This image most likely belongs to tiger with a {:.2f} percent confidence."
        .format( 100 * np.max(score))
    )
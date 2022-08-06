
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
from django.core.files.storage import FileSystemStorage
from .file_upload import upload_file

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
    
    
    # pretrained_model.set_weights()
    # fs = FileSystemStorage()
    # # img_name = image.name
    # file = fs.save('randomimagename', image)
    # file_url = fs.url(file)
    file_url = upload_file(image)
    
    
    type(file_url)
    print(file_url)
    img = keras.preprocessing.image.load_img(
        f"{os.getcwd()}{file_url}"
        , target_size=(224,224,3)
    )

    FileSystemStorage().delete(f"{os.getcwd()}{file_url}")
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = pretrained_model.predict(img_array)
    score = predictions[0]
    
    print(
        "This image most likely belongs to tiger with a {:.2f} percent confidence."
        .format(100 * np.max(score))
    )
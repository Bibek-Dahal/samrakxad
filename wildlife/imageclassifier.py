import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing import image

mobile = tf.keras.applications.mobilenet.MobileNet()

def prepare_image(file):
    img = image.load_img(file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

def disp_image(file_url):
    preprocessed_image = prepare_image(file_url)
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    return results
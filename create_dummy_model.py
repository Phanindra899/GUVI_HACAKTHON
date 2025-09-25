import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, InputLayer
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Function to preprocess any image to 3-channel RGB
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)  # Load image
    if img.mode != 'RGB':  # Convert grayscale or other modes to RGB
        img = img.convert('RGB')
    img_array = img_to_array(img) / 255.0  # Scale pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Create dummy model
def create_dummy_model(input_shape=(224, 224, 3), num_classes=10):
    model = Sequential()
    model.add(InputLayer(input_shape=input_shape))
    model.add(Conv2D(32, (3,3), activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Example usage:
# model = create_dummy_model()
# img_array = preprocess_image('path_to_your_image.jpg')
# predictions = model.predict(img_array)

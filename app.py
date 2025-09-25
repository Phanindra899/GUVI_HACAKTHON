from flask import Flask, render_template, request
import os
import numpy as np
import tensorflow as tf
import json
from PIL import Image

app = Flask(__name__)

# Load the trained model
# It's good practice to handle potential file-not-found errors
try:
    model = tf.keras.models.load_model('model/model.h5')
except OSError:
    print("Error: The model file 'model/model.h5' was not found.")
    print("Please make sure you have run create_dummy_model.py to generate the model.")
    # Exit or handle the error gracefully
    exit()

# Load remedies from JSON
try:
    with open('data/remedies.json', 'r') as f:
        remedies = json.load(f)
except FileNotFoundError:
    print("Error: The remedies.json file was not found.")
    print("Please create the file in the 'data' directory.")
    exit()

# This is the most reliable way to preprocess the image
def preprocess_image(image_path):
    """
    Preprocesses an image for model prediction. 
    It ensures the image is always in a 3-channel RGB format.
    """
    # Force 3 channels (RGB) to handle RGBA or other formats
    image = Image.open(image_path).convert("RGB")  
    image = image.resize((128, 128))  # Resize to model input
    
    img_array = np.array(image).astype("float32") / 255.0
    
    # Explicitly check and handle the channel dimension
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]  # Keep only the first 3 channels
        
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension: (1, 128, 128, 3)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image = request.files['image']
    if image.filename == '':
        return "No selected file", 400

    image_path = os.path.join('static', image.filename)
    image.save(image_path)

    try:
        # Preprocess and predict
        image_array = preprocess_image(image_path)
        prediction = model.predict(image_array)[0]
        predicted_class = np.argmax(prediction)

        # Dummy labels (update if you add more classes)
        labels = ['Healthy', 'Leaf Blight']
        label = labels[predicted_class]

        # Remedy lookup
        remedy = remedies.get(label, "No remedy found.")

        return render_template('result.html', label=label, remedy=remedy, image_path=image_path)

    except Exception as e:
        # This will catch any remaining errors and print them to the user
        return f"Error during prediction: {str(e)}", 500

if __name__ == '__main__':
    # Make sure you are in the correct directory before running
    app.run(debug=True)

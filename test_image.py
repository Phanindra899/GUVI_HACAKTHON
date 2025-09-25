import numpy as np
from PIL import Image

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    img_array = np.array(image).astype("float32")
    return img_array

# Replace 'path_to_your_image.png' with the actual path to your image
image_path = 'path_to_your_image.png' 

try:
    image_array = preprocess_image(image_path)
    print(f"Image loaded and converted. Shape: {image_array.shape}")
    print("The conversion was successful. The issue is with the Flask app.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("The issue is with the image file or the Pillow installation.")
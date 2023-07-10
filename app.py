# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import tensorflow as tf
from PIL import Image
import numpy as np
import boto3

s3 = boto3.client('s3')

# Download the human model file from S3
human_model = s3.download_file('imageclassificationbucket', 'human_and_non_human_.h5', 'human_and_non_human_.h5')

# Download the food delivery model file from S3
food_delivery_model = s3.download_file('imageclassificationbucket', 'delivery_guy_classification.h5', 'delivery_guy_classification.h5')


# Load the human/non-human classification model
# human_model = tf.keras.models.load_model('human_and_non_human_.h5')

# Load the zomato/swiggy/dunzo/other classification model
# food_delivery_model = tf.keras.models.load_model('delivery_guy_classification.h5')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Handle the uploaded image here
    image = request.files['image']
    img = Image.open(image)
    img = img.resize((150, 150))  # Resize the image to the input size expected by the model
    img = img.convert('RGB')  # Convert the image to RGB if it's not already
    
    # Perform the human/non-human classification
    human_prediction = human_model.predict(np.array([np.array(img)]))
    if human_prediction[0] < 0.5:
        return "Non-human"
    
    else:
        # Perform the zomato/swiggy/dunzo/other classification
        food_delivery_prediction = food_delivery_model.predict(np.array([np.array(img)]))
        class_names = ['zomato', 'swiggy', 'dunzo', 'other']
        max_prob_index = np.argmax(food_delivery_prediction)
        return class_names[max_prob_index]


if __name__ == '__main__':
    app.run(debug=True)



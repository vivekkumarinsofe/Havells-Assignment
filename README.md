# Havells-Assignments

# Assignment - 1:
Data for human-non_human classification was downloaded from https://www.kaggle.com/code/aliasgartaksali/human-vs-non-human-binary-classification/input

Data for delivery person classification was made by self by downloading data for swiggy/zomato/dunzo from google.

## human_and_non_human_.h5 Model:
A model to classify an image into human and non-human with 99.41% accuracy on training set and 99.81% accuracy on validation set

## delivery_guy_classification.h5 Model:
A model to classify a human image into swiggy/zomato/dunzo/other category - a multi class classification problem with 93.33% accuracy on training set and 90.00% accuracy on validation set

## References:
https://www.kaggle.com/code/aliasgartaksali/human-vs-non-human-binary-classification/

## Outcome:
A Web application is built and deployed on cloud to be accessed publicly at the URL: http://107.21.132.59:5000/
The web app will have an option to upload an image and will pass through first model. Once a non-human is detected, it will show non-human on the webpage. If the image is of a human, the same image will pass through the second model which will classify the same image into nay one of zomato/swiggy/dunzo or other categories.

The web app is able to handle multiple requests (>100) at any given time.

## Deployment:
EC2 machine from AWS (Free Trial) is used to deploy the app using flask.

# Assignment - 2:
The solution to assignment - 2 is attached in a pdf file in the file section.


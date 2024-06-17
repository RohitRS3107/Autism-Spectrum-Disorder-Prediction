# Autism-Spectrum-Disorder-Prediction
Autism Spectrum Disorder (ASD) Prediction using Machine Learning
Autism Spectrum Disorder (ASD) Prediction using Machine Learning
Overview

This project focuses on detecting Autism Spectrum Disorder (ASD) in children using machine learning techniques. It involves preparing the dataset, preprocessing the data, training a VGG model, and deploying a Flask web application for prediction.
Project Structure

bash

.
├── prepareData.py           # Script for preparing the dataset
├── data_preprocessing.py    # Script for preprocessing the dataset
├── vggModelUnit.py          # Unit tests for VGG model
├── vgg_model.py             # Script defining the VGG model architecture
├── app3.py                  # Flask application script for ASD prediction
├── README.md                # This README file
└── requirements.txt         # List of dependencies

Technologies Used

    Python
    Flask (for web application)
    TensorFlow / Keras (for machine learning)
    HTML, CSS, JavaScript (for web interface)

Getting Started
Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/your-repository.git
cd your-repository

Install dependencies:

    pip install -r requirements.txt

Steps to Run

Follow these steps in sequence to prepare the dataset, preprocess the data, train the VGG model, and run the Flask web application:

    Prepare Dataset

        Execute prepareData.py to gather and organize the dataset. Ensure the dataset is structured appropriately for further processing.

        bash

    python prepareData.py

Data Preprocessing

    Use data_preprocessing.py to preprocess the dataset, including data cleaning, feature extraction, and normalization.

    bash

    python data_preprocessing.py

VGG Model Unit Tests

    Run vggModelUnit.py to execute unit tests for the VGG model. Ensure that the model architecture and functionalities are working correctly.

    bash

    python vggModelUnit.py

Train VGG Model

    Train the VGG model using vgg_model.py to learn from the preprocessed dataset. Adjust hyperparameters as necessary for optimal performance.

    bash

    python vgg_model.py

Run Flask Application

    Finally, run app3.py to start the Flask web application for ASD prediction.

    bash

python app3.py

Access the application via a web browser at http://localhost:5000.

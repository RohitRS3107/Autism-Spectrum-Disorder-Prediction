# Autism-Spectrum-Disorder-Prediction
Autism Spectrum Disorder (ASD) Prediction using Machine Learning
Autism Spectrum Disorder (ASD) Prediction using Machine Learning

# Table of Contents

    Overview
    Demo
    Features
    Technologies Used
    Installation
    Usage
    Contributing
    License

Overview

This project focuses on detecting Autism Spectrum Disorder (ASD) in children using machine learning techniques. It utilizes facial analysis to predict ASD based on input images. The prediction model is built using a VGG architecture and deployed as a Flask web application.
Demo

Link to Live Demo
Features

    Detects ASD based on facial features extracted using computer vision techniques.
    Provides a web interface for uploading images and viewing prediction results.
    Utilizes a pre-trained VGG model for accurate prediction.
    Includes CSS and JavaScript for interactive front-end design.

Technologies Used

    Python
    TensorFlow / Keras
    Flask
    HTML, CSS, JavaScript

# Installation

# Clone the repository:


    git clone https://github.com/your-username/asd-prediction.git
    cd asd-prediction

# Install dependencies:



    pip install -r requirements.txt

# Usage

Prepare Dataset: Execute prepareData.py to gather and organize the dataset.

    

    python prepareData.py

Data Preprocessing: Use data_preprocessing.py to preprocess the dataset.



    python data_preprocessing.py

Train VGG Model: Train the VGG model using vgg_model.py.



    python vgg_model.py

Run Flask Application: Start the Flask web application for ASD prediction.



    python app3.py

    Access the application at http://localhost:5000.

# Contributing

Contributions are welcome! Please fork the repository and submit pull requests.
License

This project is licensed under the MIT License. See the LICENSE file for more details.

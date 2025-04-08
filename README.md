# PneumoniaResnet50
Project Description
This project aims to develop an artificial intelligence model for the automated diagnosis of pneumonia from chest X-ray images. The dataset used is the "Chest X-Ray Pneumonia" dataset available on Kaggle.

Dataset and Preparation
The dataset is organized into 3 folders (train, test, validation), each containing subfolders for the image categories "Pneumonia" and "Normal." It comprises 5,863 chest X-ray images (JPEG format). The images were retrospectively collected from pediatric patients aged 1 to 5 years at the Guangzhou Women and Children’s Medical Center, Guangzhou, as part of routine clinical care. For quality control, low-quality or unreadable scans were removed. Diagnoses were initially graded by two expert physicians and subsequently verified by a third expert for the evaluation set to address potential grading errors. During the data preprocessing phase, class imbalances were addressed, and detailed analyses were conducted to optimize the dataset for model training.

Developed Model and Application
For pneumonia diagnosis, a ResNet50 deep learning model was trained using the preprocessed dataset. The model was optimized with the training images, and its performance was evaluated on the test set. Subsequently, the model was integrated with the Python Flask framework to create a web application. A detailed website was designed using HTML, JavaScript, and CSS to provide a user-friendly interface, enabling users to upload chest X-ray images and receive pneumonia diagnoses.

Objective and Contribution
This study seeks to enable rapid and accurate pneumonia diagnosis from chest X-ray images. The developed model and web application are designed to assist healthcare professionals and streamline diagnostic processes. By sharing this project, the aim is to inspire and provide a technical guide for others working in similar domains.
dataset:
https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

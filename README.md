# CellScope AI

## Overview
CellScope AI is a machine learning project aimed at automating the segmentation and classification of cellular structures in high-throughput screening images. Using advanced neural network models, this project seeks to accurately identify and analyze cellular phenotypes in response to various treatments, facilitating faster and more efficient biological research.

## Objectives
- Develop a deep learning model for accurate segmentation of cellular structures.
- Classify segmented cells based on phenotypic responses to different chemical treatments.
- Evaluate model performance using appropriate metrics and validate against ground truth annotations.

## Dataset
The project utilizes images from the Broad Bioimage Benchmark Collection (BBBC), specifically the dataset [BBBC039](https://bbbc.broadinstitute.org/BBBC039), focusing on nuclei of U2OS cells under chemical treatment. The dataset includes images for training, validation, and testing, along with ground truth annotations for segmentation.

## Methodology
- **Preprocessing**: Images are normalized and augmented to improve model training efficacy.
- **Model Architecture**: We employ a Convolutional Neural Network (CNN), potentially leveraging architectures like U-Net for segmentation tasks, followed by a classification model for phenotypic analysis.
- **Training**: The model is trained on the provided dataset, with a split for validation to monitor overfitting.
- **Evaluation**: Performance is evaluated using metrics such as accuracy, precision, recall, and F1-score for classification, and Intersection over Union (IoU) for segmentation.

## Requirements
- Python 3.8+
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib
- OpenCV (for image preprocessing)
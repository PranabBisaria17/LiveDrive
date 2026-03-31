🚗 Real-Time Drivable Space Segmentation
📌 Project Overview

This project detects drivable road areas in real time using deep learning–based semantic segmentation. It processes input road images and predicts safe driving regions, helping autonomous vehicles understand where they can move safely.

The system uses a trained neural network model to classify each pixel in an image into drivable and non-drivable regions, improving navigation accuracy in real-world environments.

Key features:

Real-time road segmentation
Deep learning–based prediction
Supports custom image input
Works on GPU (optional) and CPU
Beginner-friendly implementation for hackathons
🧠 Model Architecture

The project uses a semantic segmentation neural network implemented with PyTorch.

Architecture highlights:

Encoder–decoder structure
Convolutional layers for feature extraction
Upsampling layers for pixel-level prediction
Binary segmentation output (drivable vs non-drivable)

Workflow:

Input Image → Feature Extraction → Segmentation Layers → Output Mask

The model predicts a segmentation mask highlighting drivable road regions.

📊 Dataset Used

Dataset used for training:
The model is trained using the BDD100K (Berkeley DeepDrive) dataset, which is a large-scale dataset designed for autonomous driving research. It contains diverse driving scenes captured in urban roads, highways, and different environmental conditions such as daytime, nighttime, and varying weather scenarios. The dataset provides pixel-level annotations that enable supervised training for semantic segmentation tasks, making it highly suitable for detecting drivable road regions accurately.

Dataset features:

Large-scale driving dataset
Real-world road scenes
Pixel-level annotations
Supports autonomous driving research

Dataset includes:

Urban roads
Highways
Night/day conditions
Different weather environments

Setup and Installation Instructions

To run this project locally, first clone the repository from GitHub to your system and navigate to the project directory. After cloning, install the required dependencies including PyTorch, torchvision, OpenCV, NumPy, and Matplotlib using pip. If GPU acceleration is required, install the CUDA-compatible version of PyTorch from the official PyTorch website. Once dependencies are installed successfully, the environment will be ready for running segmentation inference on road scene images. ⚙️

How to Run the Code

After completing installation, execute the prediction script from the project directory using the command python predict.py. If you want to test the model on a custom image, provide the image path as an argument while running the script. The program processes the input image and generates a segmentation mask highlighting drivable areas, which is automatically saved in the output folder for visualization and evaluation.

Example Outputs / Results

The model produces segmentation outputs in the form of binary masks that clearly highlight drivable road regions from the original input image. These results demonstrate the system’s capability to distinguish safe navigation areas from obstacles and non-drivable surfaces. Example input and output images can be added to the repository README file to visually present the effectiveness of the segmentation model and improve clarity for evaluators reviewing the project. 📊

🚗 DriveVision: Real-Time Drivable Space Segmentation

DriveVision is a deep learning–based semantic segmentation system that detects drivable road areas from camera images using DeepLabV3 with a ResNet50 backbone. The model is trained from scratch to classify drivable vs non-drivable regions and generate binary segmentation masks with overlay visualization highlighting safe driving areas.

This project demonstrates an efficient pipeline for road scene understanding and can be applied to autonomous vehicles, Advanced Driver Assistance Systems (ADAS), robotics navigation, and intelligent transportation systems.

📌 Features
Real-time drivable space detection from road images
DeepLabV3-based semantic segmentation model
Training from scratch (no pretrained weights)
Automatic road mask generation using HSV filtering
Custom PyTorch dataset loader
Binary segmentation output (road vs non-road)
GPU acceleration support (CUDA)
Overlay visualization of predicted drivable regions
🧠 Model Details

The system uses DeepLabV3 with a ResNet50 backbone, modified for binary segmentation of drivable areas.

Loss Function: Binary Cross Entropy with Logits Loss
Optimizer: Adam Optimizer
Input Resolution: 256 × 256 images
Output: Binary segmentation mask highlighting drivable regions

🚗 Applications

This project can be used in:

Autonomous driving systems
Driver assistance technologies (ADAS)
Robotics navigation
Smart mobility solutions
Road scene understanding research


📈 Future Improvements
Real-time video segmentation support
Multi-class road scene understanding
Lightweight deployment for edge devices
FPS optimization for embedded systems

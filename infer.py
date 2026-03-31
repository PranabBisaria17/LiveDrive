import torch
import torchvision
import cv2
import numpy as np
import os

# 🔥 SELECT DEVICE (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# 🔥 LOAD MODEL (NO pretrained weights allowed)
model = torchvision.models.segmentation.deeplabv3_resnet50(weights=None)

# change output to 1 class
model.classifier[4] = torch.nn.Conv2d(256, 1, kernel_size=1)

# 🔥 LOAD TRAINED MODEL FILE SAFELY
model_path = os.path.join(os.path.dirname(__file__), "deeplab_model.pth")

if not os.path.exists(model_path):
    raise Exception("❌ deeplab_model.pth not found in project folder")
import os

model_path = os.path.join(os.path.dirname(__file__), "deeplab_model.pth")
model.load_state_dict(torch.load(model_path), strict=False)

model.to(device)
model.eval()

print("✅ Model loaded successfully")

# 🔥 LOAD IMAGE
img_path = os.path.join(os.path.dirname(__file__), "test.jpg")

img = cv2.imread(img_path)

if img is None:
    raise Exception("❌ test.jpg not found! Check filename")

print("✅ Image loaded")

original = img.copy()

# 🔥 PREPROCESS IMAGE
img = cv2.resize(img, (256, 256))
img = img / 255.0
img = np.transpose(img, (2, 0, 1))

img = torch.tensor(img, dtype=torch.float32).unsqueeze(0).to(device)

# 🔥 PREDICTION
with torch.no_grad():
    output = model(img)["out"][0][0]
    pred = torch.sigmoid(output).cpu().numpy()

# 🔥 CONVERT TO BINARY MASK
pred = (pred > 0.5).astype(np.uint8) * 255

# resize mask back to original image size
pred = cv2.resize(pred, (original.shape[1], original.shape[0]))

# 🔥 OVERLAY RESULT (GREEN DRIVABLE AREA)
overlay = original.copy()
overlay[pred == 255] = [0, 255, 0]

# 🔥 SAVE OUTPUT FILES
cv2.imwrite("original.png", original)
cv2.imwrite("mask.png", pred)
cv2.imwrite("overlay.png", overlay)

print("✅ Saved successfully:")
print(" - original.png")
print(" - mask.png")
print(" - overlay.png")
import cv2
import numpy as np
import os

# Input & Output folders
input_folder = "CAM_FRONT"
output_folder = "masks"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        print("Processing:", filename)

        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Check if image loaded properly
        if img is None:
            print("❌ Failed to load:", filename)
            continue

        h, w = img.shape[:2]

        # Convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Road color range (gray-ish)
        lower = np.array([0, 0, 40])
        upper = np.array([180, 60, 200])

        mask = cv2.inRange(hsv, lower, upper)

        # Focus on lower half (road area)
        roi = np.zeros_like(mask)
        roi[int(h * 0.4):, :] = 255
        mask = cv2.bitwise_and(mask, roi)

        # Clean mask
        kernel = np.ones((7, 7), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Save as PNG
        new_name = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, new_name)

        cv2.imwrite(output_path, mask)

# Done
print("✅ All masks saved in 'masks/' folder")
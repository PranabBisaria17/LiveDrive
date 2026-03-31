import os
import cv2
import numpy as np
import torch
from torch.utils.data import Dataset

class RoadDataset(Dataset):
    def __init__(self, img_dir, mask_dir):
        self.img_dir = img_dir
        self.mask_dir = mask_dir

        # handle jpg/png safely
        self.images = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(".jpg")])
        self.masks = sorted([f for f in os.listdir(mask_dir) if f.lower().endswith(".png")])

        # match lengths
        min_len = min(len(self.images), len(self.masks))
        self.images = self.images[:min_len]
        self.masks = self.masks[:min_len]

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.images[idx])
        mask_path = os.path.join(self.mask_dir, self.masks[idx])

        img = cv2.imread(img_path)
        img = cv2.resize(img, (256, 256)) / 255.0

        mask = cv2.imread(mask_path, 0)
        mask = cv2.resize(mask, (256, 256))
        mask = (mask > 0).astype(np.float32)

        img = np.transpose(img, (2, 0, 1))
        mask = np.expand_dims(mask, axis=0)

        return torch.tensor(img, dtype=torch.float32), torch.tensor(mask, dtype=torch.float32)
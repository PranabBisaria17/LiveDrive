import torch
import torchvision
from torch.utils.data import DataLoader
from dataloader import RoadDataset
from torchvision.models.segmentation import deeplabv3_resnet50, DeepLabV3_ResNet50_Weights

# -----------------------
# DEVICE
# -----------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------
# LOAD DATA
# -----------------------
dataset = RoadDataset("CAM_BACK_LEFT", "maps")
print("Dataset size:", len(dataset))

loader = DataLoader(dataset, batch_size=4, shuffle=True)

# -----------------------
# LOAD MODEL (UPDATED)
# -----------------------
# LOAD MODEL
model = deeplabv3_resnet50(weights=None)

# MODIFY OUTPUT (1 class)
model.classifier[4] = torch.nn.Conv2d(256, 1, kernel_size=1)

# LOAD MODEL (UPDATED)
weights = DeepLabV3_ResNet50_Weights.DEFAULT
model = deeplabv3_resnet50(weights=weights)

# MODIFY OUTPUT (1 class)
model.classifier[4] = torch.nn.Conv2d(256, 1, kernel_size=1)

# -----------------------
# OPTIMIZER + LOSS
# -----------------------
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
loss_fn = torch.nn.BCEWithLogitsLoss()

# -----------------------
# TRAIN
# -----------------------
model.train()

EPOCHS = 3

for epoch in range(EPOCHS):
    total_loss = 0

    for imgs, masks in loader:
        imgs = imgs.to(device)
        masks = masks.to(device).float()

        # Ensure mask shape [B,1,H,W]
        if masks.dim() == 3:
            masks = masks.unsqueeze(1)

        outputs = model(imgs)["out"]

        loss = loss_fn(outputs, masks)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {total_loss:.4f}")

# -----------------------
# SAVE MODEL
# -----------------------
torch.save(model.state_dict(), "deeplab_model.pth")

print("✅ Training complete")


torch.save(model.state_dict(), "road_model.pth")
print("Model saved successfully!")
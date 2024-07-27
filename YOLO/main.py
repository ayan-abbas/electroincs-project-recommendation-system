"""

code for training model

"""


import numpy as np
from ultralytics import YOLO

def train_model():
    model = YOLO('../yolov8n-cls.pt')

    augmentations = {
        'flipud': 0.5,   # Vertical flip probability
        'fliplr': 0.5,   # Horizontal flip probability
        'mosaic': 1.0,   # Mosaic augmentation
        'mixup': 0.2,    # Mixup augmentation
        'hsv_h': 0.015,  # HSV-Hue augmentation
        'hsv_s': 0.7,    # HSV-Saturation augmentation
        'hsv_v': 0.4     # HSV-Value augmentation
    }

    # model.train(data='electronics_dataset', epochs=30, imgsz=64, augment=True, device='cuda')

    model.train(
        data='electronics_dataset',
        epochs=50,  # Increase epochs if needed
        imgsz=128,  # Increase image size
        lr0=0.01,  # Learning rate
        lrf=0.01,  # Learning rate final
        weight_decay=0.0005,  # Regularization
        augment=True,
        device='cuda'
    )


if __name__ == '__main__':  # __name__ == '__main__' guard for multiprocesing
    train_model()

import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
source_dir = '../downloaded_images'
target_dir = '../electronics_dataset'
train_dir = os.path.join(target_dir, 'train')
val_dir = os.path.join(target_dir, 'val')

# Create target directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Iterate through each class folder in the source directory
for class_name in os.listdir(source_dir):
    class_dir = os.path.join(source_dir, class_name)

    if os.path.isdir(class_dir):
        images = os.listdir(class_dir)
        train_images, val_images = train_test_split(images, test_size=0.25, random_state=42)

        # Create class subdirectories in train and val directories
        os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)

        # Move training images
        for image in train_images:
            shutil.copy(os.path.join(class_dir, image), os.path.join(train_dir, class_name, image))

        # Move validation images
        for image in val_images:
            shutil.copy(os.path.join(class_dir, image), os.path.join(val_dir, class_name, image))

print("Dataset split completed successfully.")

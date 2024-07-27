import os
from ultralytics import YOLO

# Initialize the YOLO model with the trained weights
model = YOLO('../runs/classify/train7/weights/last.pt')

# Define the directory containing test images
test_dir = '../electronics_dataset/test'

# Iterate through all images in the test directory
for filename in os.listdir(test_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(test_dir, filename)

        # Predict the image
        results = model(image_path, device='cuda')

        # Extract top-3 predictions
        names_list = [results[0].names[i] for i in results[0].probs.top5]
        prob_list = results[0].probs.top5conf.tolist()
        top_predictions = list(zip(names_list[:3], prob_list[:3]))

        # Print the image filename and predictions
        print(f"Image: {filename}")
        for name, prob in top_predictions:
            print(f"  {name}: {prob * 100:.2f}%")
        print()  # Add a newline for better readability between images

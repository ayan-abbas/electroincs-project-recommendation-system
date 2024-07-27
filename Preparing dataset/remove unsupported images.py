from PIL import Image
import os

def verify_images(directory):
    supported_formats = {'jpg', 'jpeg', 'png', 'bmp'}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with Image.open(file_path) as img:
                    if img.format.lower() not in supported_formats:
                        print(f"Removing unsupported format: {file_path}")
                        os.remove(file_path)
            except Exception as e:
                print(f"Removing corrupt image: {file_path} due to {e}")
                os.remove(file_path)

verify_images("C:/Users/ayan5/PycharmProjects/electroincs project recommendation system/downloaded_images")

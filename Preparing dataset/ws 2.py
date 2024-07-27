import pandas as pd
import requests
import os
import concurrent.futures
import time


def download_image(url, output_folder, index):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            image_name = os.path.join(output_folder, f'image_{index}.jpg')
            with open(image_name, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded: {image_name}")
            return True
        else:
            print(f"Failed to download {url} with status code {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


def download_images(csv_file, base_output_folder, max_workers=10, max_retries=3):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Ensure the CSV file has the required columns
    if 'query' not in df.columns or 'imageUrl' not in df.columns:
        raise ValueError("CSV file must contain 'query' and 'imageUrl' columns")

    # Function to handle retries with exponential backoff
    def retry_download(url, output_folder, index, retries):
        for i in range(retries):
            if download_image(url, output_folder, index):
                return True
            else:
                sleep_time = 2 ** i  # Exponential backoff
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
        return False

    # Use ThreadPoolExecutor for concurrent downloads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for index, row in df.iterrows():
            query = row['query']
            url = row['imageUrl']
            query_folder = os.path.join(base_output_folder, query.replace(' ', '_'))
            if not os.path.exists(query_folder):
                os.makedirs(query_folder)
            futures.append(executor.submit(retry_download, url, query_folder, index, max_retries))

        for future in concurrent.futures.as_completed(futures):
            future.result()  # To catch any exceptions


# Example usage
csv_file = "C:\\Users\\ayan5\Downloads\dataset_google-images-scraper_2024-07-21_09-39-22-411 (3).csv"
base_output_folder = 'electronics dataset'
download_images(csv_file, base_output_folder, max_workers=10, max_retries=3)

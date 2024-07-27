import os


def list_folders_in_directory(directory_path):
    try:
        # List all entries in the directory
        entries = os.listdir(directory_path)

        # Filter out the directories
        folders = [entry for entry in entries if os.path.isdir(os.path.join(directory_path, entry))]

        return folders
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Example usage:
directory_path = "downloaded_images"
folders = list_folders_in_directory(directory_path)
print(folders)

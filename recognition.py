import os
import time
from deepface import DeepFace

# Specify the folder you want to monitor
folder_path = "/path/to/folder"

# Create a set to store the initial list of files in the folder
initial_files = set(os.listdir(folder_path))

while True:
    # Get the current list of files in the folder
    current_files = set(os.listdir(folder_path))

    # Calculate the set difference to find new files
    new_files = current_files - initial_files

    if new_files:
        print("New files detected:")
        for file in new_files:)
            fileone = "/path/to/image.jpg"
            filename = os.path.join(folder_path, file
            print(filename)
            print("\n=========================================\nInitializing Facial Recognition Algorithm\n=========================================")
            result = DeepFace.verify(img1_path = fileone, img2_path = filename)
            verified_value = result.get('verified', False)
            print("\nResult: " + str(verified_value) + "\n\n=========================================")
            print("\nWaiting for new files.....\n")

    # Update the initial files set
    initial_files = current_files

    # Sleep for a specified interval (e.g., 60 seconds)
    time.sleep(2)

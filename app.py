import os
import shutil

source_folder = "test_files"

file_types = {
    "Images": [".png", ".jpg", ".jpeg"],
    "PDFs": [".pdf"],
    "Documents": [".docx", ".txt"],
    "Videos": [".mp4"]
}

for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.endswith(tuple(extensions)):
                destination = os.path.join(source_folder, folder, file)
                shutil.move(file_path, destination)
                print(f"Moved: {file} → {folder}")

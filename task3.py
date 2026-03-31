import os
import shutil

source_folder = "source_files"
destination_folder = "moved_files"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in os.listdir(source_folder):
    shutil.move(
        os.path.join(source_folder, file),
        os.path.join(destination_folder, file)
    )
    print(file, "moved successfully")

print("All files moved!")
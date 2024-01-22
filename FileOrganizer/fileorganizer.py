import os
import time

# Directory to be monitored
directory = 'C:/Users/mjcab/Downloads'

categories = {
    'Images': ['jpeg', 'jpg', 'png'],
    'PDFs': ['pdf'],
    'Sheets&Datasets': ['csv', 'xlsx', 'json'],
    'Videos': ['mp4'],
    'Docs': ['docx', 'odt']
}

for category in categories.keys():
    os.makedirs(os.path.join(directory, category), exist_ok=True)

def classify_file(filename):
    extension = filename.split('.')[-1]

    for category, extensions in categories.items():
        if extension in extensions:
            source_path = os.path.join(directory, filename)
            dest_path = os.path.join(directory, category, filename)

            os.rename(source_path, dest_path)
            print(f'Moved {filename} to {category}')
            break

for filename in os.listdir(directory):
    classify_file(filename)

initial_files = os.listdir(directory)

while True:

    time.sleep(5)
    current_files = os.listdir(directory)

    new_files = list(set(current_files) - set(initial_files))

    for filename in new_files:
        classify_file(filename)
    
    initial_files = current_files
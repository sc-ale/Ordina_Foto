import os
import json
from datetime import datetime

NEW_DIR = 'NuovaOrganizzazione'
BASE_DIR = '/Users/alessandro/Desktop/Takeout/Google Foto/'
SPECIAL_DIR = '/Users/alessandro/Desktop/Takeout/Google Foto/NuovaOrganizzazione/NonTrovato'

def extract_date_and_title(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    timestamp = int(data['photoTakenTime']['timestamp'])
    date = datetime.fromtimestamp(timestamp)
    title = data['title']
    return date, title

def move_to_special_dir(file_path, special_dir):
    if os.path.exists(file_path):
        new_path = os.path.join(special_dir, os.path.basename(file_path))
        os.rename(file_path, new_path)
    else:
        print(f'Warning: File {file_path} not found when trying to move to special directory')

def rename_file(original_file_path, title, dir):
    extension = os.path.splitext(original_file_path)[1]
    new_name = os.path.join(dir, title)
    if not new_name.endswith(extension):
        new_name += extension
    counter = 1
    while os.path.exists(new_name):
        new_name = os.path.join(dir, f"{title}({counter})")
        if not new_name.endswith(extension):
            new_name += extension
        counter += 1
    os.rename(original_file_path, new_name)

def create_directories(date, base_dir):
    new_base_dir = os.path.join(base_dir, NEW_DIR)
    year_dir = os.path.join(new_base_dir, str(date.year))
    month_dir = os.path.join(year_dir, str(date.month))
    week_dir = os.path.join(month_dir, 'week' + str(date.isocalendar()[1]))
    for dir in [year_dir, month_dir, week_dir]:
        if not os.path.exists(dir):
            os.makedirs(dir)
    return week_dir

def main():
    print("INIZIO")
    base_dir = BASE_DIR
    special_dir = SPECIAL_DIR
    for dirpath, dirnames, filenames in os.walk(base_dir):
        for json_file in filenames:
            if json_file.endswith('.json'):
                json_file_path = os.path.join(dirpath, json_file)
                try:
                    date, title = extract_date_and_title(json_file_path)
                    new_dir = create_directories(date, base_dir)
                    original_file_name = os.path.splitext(json_file)[0]
                    file_found = False
                    for file in filenames:
                        if file.startswith(original_file_name) and file != json_file:
                            file_path = os.path.join(dirpath, file)
                            rename_file(file_path, title, new_dir)
                            file_found = True
                            break
                    if not file_found:
                        print(f'Warning: No media file found for {json_file}')
                except Exception as e:
                    print(f'Error processing {json_file}: {e}')
                    move_to_special_dir(json_file_path, special_dir)
    
    print("FINE")

if __name__=="__main__":
    main()
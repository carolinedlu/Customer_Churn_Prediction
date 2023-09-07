import os

raw_file_path = os.path.join('artifact_folder', 'raw_file_name')
os.makedirs(os.path.dirname(raw_file_path), exist_ok= True)
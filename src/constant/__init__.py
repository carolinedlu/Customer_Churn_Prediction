import os

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

url1 = "https://drive.google.com/file/d/1zGMX9kZQRon3MA3FUMS9PvwNuBEaRbgh/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url1.split('/')[-2]

TARGET_COLUMN = 'Churn'

parent_dir = os.path.join('..', '..', 'artifacts')

artifact_folder =  parent_dir
raw_file_name = 'raw_file.csv'

transformer_file= 'transformer.pkl'
train_file_name= 'train_file.csv'
test_file_name= 'test_file.csv'
user_file_name= 'user_file.csv'
model_file= 'model.pkl'

model_pkl_path = os.path.join(parent_dir , model_file )

train_csv_path = os.path.join(parent_dir, train_file_name)

user_csv_path = os.path.join(parent_dir, user_file_name)
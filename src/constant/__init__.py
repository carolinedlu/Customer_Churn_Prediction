import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "pwskills"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
MONGO_DB_URL="mongodb+srv://snshrivas:Snshrivas@cluster0.u46c4.mongodb.net/?retryWrites=true&w=majority"

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

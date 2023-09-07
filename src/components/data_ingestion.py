import os, sys
import pandas as pd
from dataclasses import dataclass #type:ignore
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exceptions import CustomException
from src.constant import *

# Creating a data class having the configuration details
@dataclass
class DataIngestionConfig:
    raw_file_path = os.path.join(artifact_folder, raw_file_name)
    
# A class for data ingestion.
class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    # This function will read the data and then split it into test and train and then save it.
    def injectData(self):
        try:
            logging.info('Data Ingestion begins...')
            # Reading th eexcel file
            
            # Adding Data set throught link

            # Naming our dataset
            url1 = "https://drive.google.com/file/d/1zGMX9kZQRon3MA3FUMS9PvwNuBEaRbgh/view?usp=drive_link"
            url='https://drive.google.com/uc?id=' + url1.split('/')[-2]
            cc_df =  pd.read_csv(url,  encoding= 'unicode_escape')
            
            os.makedirs(os.path.dirname(self.config.raw_file_path), exist_ok= True)
            cc_df.to_csv(self.config.raw_file_path, index = False)
            
            logging.info(f'Datafiles are succcesfully stored in {os.path.dirname(self.config.raw_file_path)} folder.')
            return self.config.raw_file_path 
        except Exception as e:
            logging.info('Error occured while reading the data files.')
            raise CustomException(e, sys) #type:ignore
import os, sys 
from src.exceptions import CustomException
from src.components.data_transformation import DataTransformation
from src.utils.main_utils import MainUtils
from src.logger import logging
import pandas as pd
from src.constant import *

class ModelPrediction:
    def __init__(self):
        pass
    
    def prediction(self, input_data):
        try:
            # Creating the path for locating all the pickle files
            logging.info('-----------------------------------Recieved User dataframe-----------------------------------')
            model_pkl_path = os.path.join(artifact_folder,model_file)
            
            self.utils =  MainUtils()
            # Loading the pickle files
            model =  self.utils.load_object(model_pkl_path)
            logging.info('-----------------------------------Model loaded for prediction-----------------------------------')
            
            # user_csv_path = os.path.join(parent_dir, user_file_name) in constant --> __init__.py
            os.makedirs(os.path.dirname(user_csv_path), exist_ok= True)
            input_data.to_csv(user_csv_path, index = False)
            
            logging.info(f' USER CSV is succcesfully stored in {os.path.dirname(user_csv_path)} folder.')
            
            # Preprocessing
            # Data Transforming
            transform_user = DataTransformation(user_csv_path)
            # train_csv_path = os.path.join(parent_dir, train_file_name) in constant --> __init__.py
            
            X_user = transform_user.user_transformer(train_csv_path)
            
            print('Data Transformed successfully')
            logging.info('-----------------------------------User Data Transformed-----------------------------------')



            # Predicting
            prediction = model.predict(X_user)
            
            logging.info('-----------------------------------User prediction DONE-----------------------------------')
            
            
            return prediction
            

        
        except Exception as e:
            logging.info('Error occured in Prediction Pipeline')
            raise CustomException(e, sys) #type:ignore



import os, sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining
from src.logger import logging

def run_pipeline():
    # Data Ingestion
    inject_data = DataIngestion()
    raw_file_path = inject_data.injectData()
    print('Data Ingestion Succesfull')
    logging.info('-----------------------------------Final Data Ingested-----------------------------------')
 

    # Data Transforming
    transform_obj = DataTransformation(raw_file_path)
    X_train, X_test, y_train, y_test , data = transform_obj.save_transformation()
    print('Data Transformed successfully')
    logging.info('-----------------------------------Final Data Transformer-----------------------------------')

    # Model Training
    trainer_obj = ModelTraining()
    trainer_obj.train_model(X_train, X_test, y_train, y_test)
    print('Model Trained successfully')
    logging.info('-----------------------------------Final trained-----------------------------------')
    
if __name__ == '__main__':
    run_pipeline()
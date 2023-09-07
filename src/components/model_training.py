import os, sys #type:ignore 
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score
from src.utils.main_utils import MainUtils
from src.exceptions import CustomException
from src.logger import logging
from dataclasses import dataclass #type:ignore
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import precision_score
from src.constant import *
from src.utils.main_utils import MainUtils
import pickle

@dataclass
class ModelTrainingConfig:
    model_path = os.path.join(artifact_folder, model_file )


class ModelTraining:
    def __init__(self):
        self.config = ModelTrainingConfig()
    
    def train_model(self, X_train, X_test, y_train, y_test):
        try:
            logging.info('Model Training initiated...')
            
            
            # Neural Network model
            input_dim = X_train.shape[1]

            NN_model = keras.Sequential()
            NN_model.add(layers.Input(shape=(input_dim,)))
            NN_model.add(layers.Dense(64, activation='relu'))
            NN_model.add(layers.Dense(1, activation='sigmoid'))
            
            
            
            NN_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

            early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
            
            
            # Convert X_train and y_train to NumPy arrays with dtype=int
            X_train = np.array(X_train, dtype=int)
            y_train = np.array(y_train, dtype=int)
            X_test = np.array(X_test, dtype=int)
            y_test = np.array(y_test, dtype=int)


            # Train the neural network model with early stopping
            epochs = 100
            batch_size = 64
            history = NN_model.fit(
                X_train, y_train,
                epochs=epochs,
                batch_size=batch_size,
                validation_data=(X_test, y_test),
                callbacks=[early_stopping]  # Include the EarlyStopping callback here
            )
            
            logging.info('Neural Network Model Trained successfully.')
            
            # Evaluate the model on the test dataset
            test_loss, test_accuracy = NN_model.evaluate(X_test, y_test)
            logging.info(f"Test Loss: {test_loss}")
            logging.info(f"Test Accuracy: {test_accuracy}")
            
            
            y_pred = NN_model.predict(X_test)
            # Convert predicted probabilities to binary class labels (0 or 1) based on a threshold
            threshold = 0.5
            y_pred_binary = (y_pred > threshold).astype(int)

            # Calculate precision using scikit-learn
            precision = precision_score(y_test, y_pred_binary)
            logging.info(f"Test Precision: {precision}")

            # Save the trained model for future use

            
            self.utils =  MainUtils()
            
            os.makedirs(os.path.dirname(self.config.model_path), exist_ok= True)
            self.utils.save_object(
                file_path=self.config.model_path,
                obj=NN_model)
            
            
            with open(self.config.model_path, 'wb') as model_file:
                pickle.dump(NN_model, model_file)
            
        except Exception as e:
            logging.info('Error occurred while model training')
            raise CustomException(e, sys)  # type: ignore
        
    # def model_predict(self, x_test):
    #         self.NN_model


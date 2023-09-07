import os, sys #type:ignore
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from src.constant import TARGET_COLUMN
from dataclasses import dataclass
from src.exceptions import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
import pickle
from dataclasses import dataclass #type:ignore
from src.constant import *

@dataclass
class DataTransformationConfig:
    pkl_path = os.path.join(artifact_folder, transformer_file)
    raw_file_path = os.path.join(artifact_folder, raw_file_name)
    train_file_path = os.path.join(artifact_folder, train_file_name)
    test_file_path = os.path.join(artifact_folder, test_file_name)



class DataTransformation:
    def __init__(self, feature_store_file_path):
        self.feature_store_file_path = feature_store_file_path
        self.config = DataTransformationConfig()
    
        # Add other initialization parameters if needed

    def load_data(self):
        try:
            # Read the data from the specified feature store file path
            data = pd.read_csv(self.feature_store_file_path)
            
            # Drop unnecessary columns
            data.drop(['CustomerID', 'Name'], axis=1, inplace=True)

            # Encode categorical variables
            data = pd.get_dummies(data, columns=['Gender'], prefix='Gender')
            data = pd.get_dummies(data, columns=['Location'], prefix='Location')

            # Define age ranges and create age-related features
            age_ranges = [(0, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 200)]
            age_labels = ["Age_0_20", "Age_21_30", "Age_31_40", "Age_41_50", "Age_51_60", "Age_61_200"]

            for age_range, age_label in zip(age_ranges, age_labels):
                data[age_label] = ((data['Age'] >= age_range[0]) & (data['Age'] <= age_range[1])).astype(int)

            # Define subscription length threshold and create a related feature
            subscription_length_threshold = 12
            data['Subscription_Category'] = data['Subscription_Length_Months'].apply(
                lambda x: 'Short-Term' if x <= subscription_length_threshold else 'Long-Term'
            )

            data = pd.get_dummies(data, columns=['Subscription_Category'], prefix='Subscription_Category')

            # Create additional features
            data['Billing_to_Usage_Ratio'] = data['Monthly_Bill'] / data['Total_Usage_GB']
            data['Total_Paid'] = data['Subscription_Length_Months'] * data['Monthly_Bill']
            data['Per_GB_Price'] = data['Monthly_Bill'] * data['Subscription_Length_Months'] / data['Total_Usage_GB']
            
            
            data.to_csv(self.config.raw_file_path, index = False) 
            return data

        except Exception as e:
            # Handle exceptions and log errors here
            print(f"Error during data loading and transformation: {e}")
            return None

    def split_data(self):
        try:
            data= self.load_data()
            # Split data into train and test sets
            X = data.drop('Churn', axis=1)
            y = data['Churn']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            # Again concating the X and y of train and test data to make two complete datasets
            # Concatenate X_train and y_train along axis=1
            train_df = pd.concat([X_train, y_train], axis=1)

            # Concatenate X_test and y_test along axis=1
            test_df = pd.concat([X_test, y_test], axis=1)

            
            train_df.to_csv(self.config.train_file_path, index = False)
            test_df.to_csv(self.config.test_file_path, index = False)
        
            return X_train, X_test, y_train, y_test , data
        

        

        except Exception as e:
            # Handle exceptions and log errors here
            logging.info('Error in split data of dataset')
            raise CustomException(e, sys) # type: ignore

    def preprocess_data(self):
        # ... (existing code for imputation and scaling)
        try:
            # Transformation and scaling on specified columns
            X_train, X_test, y_train, y_test , data= self.split_data()  # Get data from split_data method
            
            columns_to_transform = ['Billing_to_Usage_Ratio', 'Per_GB_Price']

            for col in columns_to_transform:
                if col in X_train.columns:
                    X_train[col] = np.log(X_train[col])
                    X_test[col] = np.log(X_test[col])
                    
            X_train['Total_Paid']= np.sqrt(X_train['Total_Paid'])
            X_test['Total_Paid']= np.sqrt(X_test['Total_Paid'])

            # Additional scaling on numerical features
            numerical_features = ['Age', 'Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB', 'Billing_to_Usage_Ratio', 'Total_Paid', 'Per_GB_Price']

            scaler = MinMaxScaler()
            X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
            X_test[numerical_features] = scaler.transform(X_test[numerical_features])

            return X_train, X_test, y_train, y_test , data    
        
        except Exception as e:
            logging.info('Error while preprocessing of dataset')
            raise CustomException(e, sys) # type: ignore
        
    def save_transformation(self):
        # Save the instance of the transformation class to a pickle file
        try :
            X_train, X_test, y_train, y_test , data= self.preprocess_data()
            
            self.utils =  MainUtils()
            
            os.makedirs(os.path.dirname(self.config.pkl_path), exist_ok= True)
            self.utils.save_object(
                file_path=self.config.pkl_path,
                obj=self)

            return X_train, X_test, y_train, y_test , data
    
        except Exception as e:
            logging.info('Error while saving of transformer pickle file')
            raise CustomException(e, sys) # type: ignore
        
if __name__ == "__main__":
    feature_store_file_path = "your_data.csv"  # Replace with your data file path
    transformation = DataTransformation(feature_store_file_path)

    # Perform data transformation and preprocessing
    X_train, X_test, y_train, y_test, data = transformation.preprocess_data()

    # Save the transformation object to a pickle file
    output_pickle_path = "transformation.pkl"  # Specify the path where you want to save the pickle file
    transformation.save_transformation(output_pickle_path)
        # Create a preprocessing pipeline




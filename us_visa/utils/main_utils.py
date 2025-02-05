import os 
import sys 

import numpy as np
import dill  # used for serialization and deserialization 
import yaml 
import pandas as pd 

from us_visa.exception import USVisaException 
from us_visa.logger import logging 



def read_yaml_file(file_path: str) -> dict:

    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise USVisaException(e, sys)
    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:

    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # creating a directory if it doesn't exists
        with open(file_path, "w") as yaml_file:
            yaml.dump(content, yaml_file)
    
    except Exception as e:
        raise USVisaException(e, sys)
    


def load_object(file_path: str) -> object:
    logging.info("Invoking the load_object function from utils directory...")

    try:
        with open(file_path, "rb") as obj:
            obj = dill.load(obj)

        logging.info("Finished loading object using load_object function from utils directory..")

        return obj 
    
    except Exception as e:
        raise USVisaException(e, sys)



def save_object(file_path: str, obj: object) -> None:
    logging.info("Invoking the save_object method from utils directory...")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exiting the save_object method from utils directory...")

    except Exception as e:
        raise USVisaException(e, sys)
        


def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Function to save numpy array data into a file

    Args:
        file_path (str): Path of the file to store the array
        array (np.array): Data in format of numpy array
    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    
    except Exception as e:
        raise USVisaException(e, sys)
    


def load_numpy_array_data(file_path: str) -> np.array:
    """
    Function to load numpy array data from a file

    Args:
        file_path (str): Path of the file to load the numpy array
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
        
    except Exception as e:
        raise USVisaException(e, sys)



def drop_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """
    Function to drop the columns from a pandas DataFrame

    Args:
        df: Pandas DataFrame
        cols: list of columns to be dropped from pandas dataframe
    """
    logging.info("Invoking drop_columns method from utils directory")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils directory")
        
        return df 
    
    except Exception as e:
        raise USVisaException(e, sys)


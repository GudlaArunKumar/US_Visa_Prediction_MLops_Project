from us_visa.configuration.mongo_db_connection import MongoDBClient 
from us_visa.constants import DATABASE_NAME 
from us_visa.exception import USVisaException 

import pandas as pd 
import sys 
from typing import Optional 
import numpy as np 



class USVisaData:
    """
    This class helps to export entire mongo db record taken from collection as pandas dataframe
    """

    def __init__(self):
        try:
            self.mongodb_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USVisaException(e, sys) 
        

    def export_collection_as_dataframe(self, collection_name:str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        This function exports entire collection as a dataframe from removing
        Id column from the data

        Args:
            collection_name (str): MongoDB's collection name
            database_name (Optional[str], optional): MongoDB's Database Name. Defaults to None.

        Returns:
            pd.DataFrame: Dataframe
        """
        try:
            if database_name is None:
                collection = self.mongodb_client.database[collection_name]
            else:
                collection = self.mongodb_client[database_name][collection_name]  # get the DB name from MongoDBClient

            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)  # replacing any values with na as numpy NaN

            return df 

        except Exception as e:
            raise USVisaException(e,sys)
    



            



import sys
import os 
import certifi

from us_visa.constants import MONGODB_URL_KEY, DATABASE_NAME 
from us_visa.exception import USVisaException 
from us_visa.logger import logging

import pymongo

# to avoid time out issues 
ca = certifi.where()


class MongoDBClient:
    """
    This class exports the data from MongoDB feature store as dataframe
    
    Output:  connection to MongoDB database as Client object
    On Failure: Raise an exception
    """

    client = None 

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # pass this as env variable
                if mongo_db_url is None:
                    raise Exception(f"Environment variable for {MONGODB_URL_KEY} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client 
            self.database = self.client[DATABASE_NAME]
            self.database_name = database_name 
            logging.info("MongoDB Connection Successful.")

        except Exception as e:
            raise USVisaException(e, sys)



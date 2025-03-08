import os 
import sys 

import pandas as pd 
from sklearn.model_selection import train_test_split 

from us_visa.entity.config_entity import DataIngestionConfig 
from us_visa.entity.artifact_entity import DataIngestionArtifact 
from us_visa.exception import USVisaException 
from us_visa.logger import logging 
from us_visa.data_access.us_visa_data import USVisaData 



class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig):
        """
        Args:
            data_ingestion_config (DataIngestionConfig, optional): Defaults to DataIngestionConfig.
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise USVisaException(e, sys)
        
    
    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        This function exports from mongodb into feature store directory as a csv file

        Returns:
            pd.DataFrame: Returned as an artifact stored in feature store of data inhgestion
                          components
        """
        try:
            logging.info("Exporting the data from MongoDB database.")
            us_visa_data = USVisaData()
            dataframe = us_visa_data.export_collection_as_dataframe(collection_name=            \
                                                                    self.data_ingestion_config.collection_name)
            
            logging.info(f"Dataframe extracted with a shape of {dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving the export dataframe from MongoDB into feature store directory: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            
            return dataframe 
        
        except Exception as e:
            raise USVisaException(e, sys)
        

    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        """
        This function take dataframe as input and splits the dataframe into 
        train and test set based on split ratio

        Args:
            dataframe (pd.DataFrame): Pandas DataFrame exported from MongoDB database
        """

        logging.info("Entered split_data_as_train_test method of Data_Ingestion class")

        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            logging.info(f"Exporting train and test data into respective directories inside data ingestion.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported train and test file path.")

        except Exception as e:
            raise USVisaException(e, sys)
        

    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        This function is to trigger the data ingestion components of the training pipline
        and returns the file names of train and test path stored as artifacts.

        Returns:
            DataIngestionArtifact: Train dataset and test dataset are returned as artifacts from 
                                   data ingestion
        """
        try:
            dataframe = self.export_data_into_feature_store()

            logging.info("Exported Data from MongoDB")

            self.split_data_as_train_test(dataframe)

            logging.info("Data is splitted into train and test set")
            logging.info("Exited Data Ingestion process..")

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_file_path,
                                                            test_file_path=self.data_ingestion_config.testing_file_path)
            
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except Exception as e:
            raise USVisaException(e, sys)


    
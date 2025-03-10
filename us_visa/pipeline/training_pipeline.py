
import sys 

from us_visa.components.data_ingestion import DataIngestion 
from us_visa.exception import USVisaException 
from us_visa.logger import logging 

from us_visa.entity.config_entity import DataIngestionConfig 
from us_visa.entity.artifact_entity import DataIngestionArtifact 


class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig

    
    def run_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of Training Pipeline class is responsible for starting data ingestion component.
        """
        try:
            logging.info("Entered the run_data_ingestion method of TrainingPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the run_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact
        
        except Exception as e:
            raise USVisaException(e, sys) 
        
    
    def run_train_pipeline(self) -> None:
        """
        This method triggers the all the available components in the training pipeline.
        """

        try:
            data_ingestion_artifact = self.run_data_ingestion()

        except Exception as e:
            raise USVisaException(e, sys)

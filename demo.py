import sys 

from us_visa.components.data_ingestion import DataIngestion 
from us_visa.pipeline.training_pipeline import TrainingPipeline

ing_pipeline = TrainingPipeline()
ing_pipeline.run_train_pipeline()

from   housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainigPipelineConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
import os, sys
from housing.constant import *
from housing.exception import HousingException

from housing.logger import logging

class Configuration:
    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str =CURRENT_TIME_STAMP)-> None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.get_training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        pass
    
    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)-> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)->TrainigPipelineConfig:
        try:
            trainig_piepeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            trainig_piepeline_config[TRAINING_PIPELINE_NAME_KEY],
            trainig_piepeline_config[TRAINIG_PIPELINE_ARTIFACT_DIR_KEY]
            )


            trainig_piepeline_config = TrainingPipelineConfig(artifact_dir= artifact_dir)
            logging.info(f"Training pipeline config:{trainig_pipeline_config}")
            return trainig_piepeline_config

        except Exception as e:
            raise HousingException (e,sys) from e
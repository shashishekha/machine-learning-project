
from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])


ModelTrainingConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])

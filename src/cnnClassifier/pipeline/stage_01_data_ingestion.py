# from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion

from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigManager

STAGE_NAME = "Data Ingestion Stage"

# Pipeline class for data ingestion stage
class DataIngestionPipeline:
    def __init__(self):
        pass

    # Main method to execute data ingestion steps
    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        # logger.info(f"Data Ingestion config: {data_ingestion_config}")
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

# Entry point for running the pipeline
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
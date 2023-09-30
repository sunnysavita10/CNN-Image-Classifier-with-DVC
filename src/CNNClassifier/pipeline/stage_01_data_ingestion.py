from CNNClassifier.components.stage_01_data_ingestion import DataIngestion
from CNNClassifier.config import ConfigurationManager
from CNNClassifier import logger



logger.info(f"data ingesiton stage started")

config=ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()

data_ingesiton=DataIngestion(config=data_ingestion_config)

data_ingesiton.download_file()

data_ingesiton.unzip_and_clean()


logger.info(f"data ingesiton stage completed")
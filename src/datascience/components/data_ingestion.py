import os
import urllib.request as requests
from src.datascience.logging.logger import logger
import zipfile

from src.datascience.entity.config_entity import DataIngestionConfig

## components of data ingestion

class DataIngestion:
    def __init__(self,
                 config: DataIngestionConfig,
                 ):
        self.config = config

    # Downloading ZIP file from source URL and saving it to local data file path
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = requests.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"Data file already exists at {self.config.local_data_file}. Skipping download.")

    # Unzipping the downloaded file to the specified unzip directory
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
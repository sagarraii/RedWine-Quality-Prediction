import os
import pandas as pd
from src.datascience.logging.logger import logger
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(
            self,
            config = DataValidationConfig
    ):
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            df = pd.read_csv(self.config.unzipped_data_dir)
            cols_list = list(df.columns)

            all_schema = self.config.all_schema.keys()

            for cols in cols_list:
                if cols not in all_schema:
                    validation_status = False

                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True

                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
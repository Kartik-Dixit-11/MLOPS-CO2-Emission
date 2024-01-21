from Regression.constants import *
from Regression.utils.shared import get_yamlcontent,create_directories
from dataclasses import dataclass

@dataclass(frozen=True)
class Dataingestconfig:
    Source: Path
    Destination: Path

@dataclass(frozen=True)
class Model_Config:
    Test: Path
    Train:Path
    Load: Path
    mlflow_uri: str

class ConfigurationManager:
        def __init__(self,config_filepath = CONFIG_FILE_PATH):
            self.config = get_yamlcontent(config_filepath)
            create_directories([self.config.artifacts_root])

    
        def get_model_config(self):
                config = self.config.Model_Prepartion

                create_directories([config.path])

                data_ingestion_config = Model_Config(Test=config.test_path,Train=config.train_path,Load=config.path,mlflow_uri=config.MLFLOW_URI)

                return data_ingestion_config
        

        def get_data_ingestion_config(self) -> Dataingestconfig:
            config = self.config.data_ingestion

            create_directories([config.create])

            data_ingestion_config = Dataingestconfig(Source=config.path,Destination=config.create)

            return data_ingestion_config
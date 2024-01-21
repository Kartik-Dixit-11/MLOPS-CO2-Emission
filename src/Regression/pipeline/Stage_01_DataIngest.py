from Regression.config.configuration import ConfigurationManager
from Regression import logger
from Regression.components.Dataingestion import DataIngestion 

BUILD_STAGE='Dataingestion and Sagrigation'

class DataIngetiontrainingpipeline:
            def __init__(self):
                    pass
            def main(self):
                    Details=ConfigurationManager()
                    variables=Details.get_data_ingestion_config()
                    Ingest=DataIngestion(variables)
                    Ingest.start_ingestion()

if __name__ == '__main__':
    try:
        logger.info(f"--------- Starting {BUILD_STAGE} -----------")
        obj = DataIngetiontrainingpipeline()
        obj.main()
        logger.info(f"------Completed {BUILD_STAGE} -----------\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



from Regression.components.Model import Trainer
from Regression.config.configuration import ConfigurationManager
from Regression import logger

BUILD_STAGE='Training and Evaluation'

class ModelBuildTraningPipeline:
    def __init__(self):
        pass

    def run(self):
        config=ConfigurationManager()
        model_param=config.get_model_config()
        Model=Trainer(model_param)
        Model.Model_Training()
        Model.Model_Evaluation()

if __name__=="__main__":
    try:
        logger.info(f"------ Staring {BUILD_STAGE} --------")
        instance=ModelBuildTraningPipeline()
        instance.run()
        logger.info(f'-------- Completed {BUILD_STAGE}-------')
    except Exception as e:
        logger.info(e)
        raise e

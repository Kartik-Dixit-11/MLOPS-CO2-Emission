from Regression import logger

from Regression.pipeline.Stage_01_DataIngest import DataIngetiontrainingpipeline
from Regression.pipeline.Stage_02_Training import ModelBuildTraningPipeline

if __name__=="__main__":
    try:
        Ingest=DataIngetiontrainingpipeline()
        Train=ModelBuildTraningPipeline()

        Ingest.main()

        Train.run()
    except Exception as e:
        raise e
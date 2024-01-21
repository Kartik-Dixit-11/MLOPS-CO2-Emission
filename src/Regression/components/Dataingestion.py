from Regression import logger
from Regression.utils.shared import *
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestion:
    def __init__(self,config):
        try:
            self.paths=config
        except Exception as e:
            raise e

    def start_ingestion(self):
        try:
            fp=self.paths.Destination
            df=pd.read_csv((self.paths.Source))

            X=df.drop('CO2 Emissions(g/km)',axis=1)
            Y=df['CO2 Emissions(g/km)']
           
            X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
            Training_Data=pd.concat([X_train,Y_train],axis=1)
            Testing_Data=pd.concat([X_test,Y_test],axis=1)


            Training_Data.to_csv(os.path.join(fp,"training.csv"))
            Testing_Data.to_csv(os.path.join(fp,'testing.csv'))
            logger.info("Training and Testing Split was Successful")
        
        except Exception as e:
            raise e
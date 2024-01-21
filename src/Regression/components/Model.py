from Regression.utils.shared import create_directories,get_yamlcontent
from Regression.constants import *
from Regression import logger
from pathlib import Path
from dataclasses import dataclass
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score,mean_squared_error
import pickle
import mlflow


@dataclass
class Trainer:
    def __init__(self,config_data):   
        self.test_p=Path(config_data.Test)
        self.train_p=Path(config_data.Train)
        self.model_loc=Path(config_data.Load)
        self.mlflow_uri=config_data.mlflow_uri
    
    def Model_Training(self):
        try:
            test_df=pd.read_csv(self.test_p)
            train_df=pd.read_csv(self.train_p)
            Data=pd.concat([train_df,test_df],axis=0)
            Data.reset_index(inplace=True)

            Data.drop_duplicates(inplace=True)
            cat=Data.select_dtypes(include='object')
            num=Data.select_dtypes(exclude='object')

            ## Encoding
            encoder=LabelEncoder()
            for column in cat.columns:
                cat[column]=pd.Series(encoder.fit_transform(cat[column]))
            
            self.df=pd.concat([cat,num],axis=1)
        except Exception as e:
            raise e
        
    def Model_Evaluation(self):  
        try:
            X=self.df.drop('CO2 Emissions(g/km)',axis=1)
            Y=self.df['CO2 Emissions(g/km)']

            test_size=0.25

            X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=test_size,random_state=32)
            Std=StandardScaler()
            X_train=Std.fit_transform(X_train)
            X_test=Std.transform(X_test)

            with mlflow.start_run(run_name='mlflow_build'):
                n_estimator=120
                max_depth=7
                mlflow.log_param('max_depth',max_depth)
                mlflow.log_param('n_estimator',n_estimator)
                model=RandomForestClassifier(n_estimators=n_estimator,max_depth=max_depth)
                model.fit(X_train,Y_train)
                Y_pred=model.predict(X_test)
                r2=r2_score(Y_test,Y_pred)
                mse=mean_squared_error(Y_test,Y_pred)
                mlflow.log_metric('R2',r2)
                mlflow.log_metric('Mean Squared Error',mse)
                tu=mlflow.set_tracking_uri("")

                if tu != "file":
                    mlflow.sklearn.log_model(model, "model", registered_model_name="CO2Emission")
                
                else:
                    mlflow.sklearn.log_model(model, "model")
            
            mlflow.end_run()
            os.makedirs(self.model_loc,exist_ok=True)
            pickle.dump(model,open(os.path.join(self.model_loc,'model.pkl'),'wb'))

            logger.info('Successfully Submitted the model')
        except Exception as e:
        #pickle.load(open(os.path.join(self.model_loc,'model.pkl'),'rb'))
             raise e
        

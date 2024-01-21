import os
from pathlib import Path
import yaml
from ensure import ensure_annotations
from Regression import logger
from box import ConfigBox
import json

@ensure_annotations ## ensure the data type of arguments
def get_yamlcontent(yaml_path: Path):
    """Arg: Path to the YAML file
       returns the content of file
    """
    try:
        with open(yaml_path) as y:
            data=yaml.safe_load(y)
            logger.info(f'Loaded {y} Succesfully')
            return ConfigBox(data)
    except Exception as e:
        raise e
        
@ensure_annotations
def create_directories(location:list,verbose=True):
        """
            Use for creating a directory

            Arguments;
                location -> location where directory must be created
        """
        for loc in location:
             os.makedirs(loc,exist_ok=True)
             logger.info(f"File has been successfully created at {loc}")

@ensure_annotations
def save_json(location:str,details:dict):
    """Save json
       Args:
        location -> path where to store
        details  -> Json object
     """
    if(location):
        with open(location,'w') as j_file:
            json.dump(details,j_file)
    logger.info(f"Created Json file at {location}")




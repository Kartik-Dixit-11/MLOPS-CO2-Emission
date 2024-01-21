import os
import sys
import logging as log

msg="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

directory="Logs"
os.makedirs(directory,exist_ok=True)
file=os.path.join(directory,'log_data.log')

log.basicConfig(level=log.INFO,format=msg,handlers=[log.FileHandler(file)])

logger=log.getLogger('Regression')

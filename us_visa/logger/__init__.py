import logging 
import os 

from from_root import from_root 
from datetime import datetime 


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)  # this gives the path for log file to be stored 

os.makedirs(log_dir, exist_ok=True)  # creating a logs folder


# setting up logging 

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)



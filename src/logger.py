import logging
from datetime import datetime #type:ignore
import os

# log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
# file_path = os.path.join(os.getcwd(), 'logs', log_file)
# os.makedirs(os.path.dirname(file_path), exist_ok=True)

# logging.basicConfig(
#     filename=file_path,
#     format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
#     level = logging.INFO
# )



# Specify the relative path to the parent directory
parent_dir = os.path.join('..', '..', 'logs')

# Create the parent directory if it doesn't exist
# os.makedirs(parent_dir, exist_ok=True)

# Create a timestamped log file name
log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Create the full path to the log file within the parent directory
file_path = os.path.join(parent_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

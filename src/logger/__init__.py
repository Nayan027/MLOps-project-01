
import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime


# Constants for log configuration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Construct log file path

# here, Manually defined the project root (since my from_root() wasn't detecting "MLOps-project-01" but stored logs in "C:\Users\dell")
PROJECT_ROOT = r"C:\Users\dell\OneDrive\Desktop\MLOps-Projects-Folder\MLOps-project-01"
LOG_DIR = "logs"

# Define log path
log_dir_path = os.path.join(PROJECT_ROOT, LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)  # Create directory if it doesn’t exist
log_file_path = os.path.join(log_dir_path, LOG_FILE)

# print(f"Log Directory Path: {log_dir_path}")
# print(f"Log File Path: {log_file_path}")
# print(f"Detected Root Directory: {LOG_DIR}")
# -----------------------OUTPUTS IN TERMINAL--------------------------
# Log Directory Path ---------> C:\Users\dell\OneDrive\Desktop\MLOps-Projects-Folder\MLOps-project-01\logs
# Log File Path --------------> C:\Users\dell\OneDrive\Desktop\MLOps-Projects-Folder\MLOps-project-01\logs\03_04_2025_18_26_55.log
# Detected Root Directory-----> logs

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    """
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()
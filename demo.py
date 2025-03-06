# import sys
# sys.dont_write_bytecode = True
# Prevents `__pycache__` from being created, needs to be on the very top of the running script
# for an alternative or more info refer to the src related notes in learning-notes.


# # below code is to check the logging config

# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
import sys
sys.dont_write_bytecode = True
# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

# This code is to run the pipeline the check the proper working of pipeline at end of each phase
from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()
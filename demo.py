import sys
sys.dont_write_bytecode = True
# Prevents `__pycache__` from being created, needs to be on the very top of the running script
# for an alternative refer to the src.__init__.py 


# below code is to check the logging config
from src.logger import logging

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
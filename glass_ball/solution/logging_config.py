# Imports
import logging
import os

# Consts
LOGS_DIR = 'logs'
LOGGED_MODULES_NAME_LIST = ['binary_search', 'optimal_steps', 'optimal_steps_with_binary_search']

def setup_module_logger(module_name):
    # Create a logs directory if it doesn't exist
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, f'{module_name}.log'))
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

def configure_logging(debug_mode=False):
    level = logging.DEBUG if debug_mode else logging.WARNING

    # Configure root logger to suppress all logs
    logging.getLogger().setLevel(logging.WARNING)

    # Set the level for our custom module loggers
    for logger_name in logging.root.manager.loggerDict:
        if logger_name in LOGGED_MODULES_NAME_LIST:
            logging.getLogger(logger_name).setLevel(level)
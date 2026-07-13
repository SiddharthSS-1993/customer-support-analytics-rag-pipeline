import logging
from pathlib import Path


LOG_DIRECTORY = Path("logs")
LOG_FILE_PATH = LOG_DIRECTORY / "bronze__pipeline.log"

def create_logger(logger_name: str) -> logging.Logger:
    """Create and configure a reusable application logger"""

    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

    application_logger = logging.getLogger(logger_name)
    application_logger.setLevel(logging.INFO)

    if application_logger.handlers:
        return application_logger
    
    log_formatter = logging.Formatter("%(asctime)s | %(levelname)s |%(name)s | %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
    file_handler.setFormatter(log_formatter)

    application_logger.addHandler(console_handler)
    application_logger.addHandler(file_handler)

    return application_logger

    

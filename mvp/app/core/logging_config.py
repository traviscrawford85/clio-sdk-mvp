import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logging(name: str = __name__) -> logging.Logger:
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "clio_service.log")

    # Create a file handler that rotates logs daily and keeps 7 backups
    file_handler = TimedRotatingFileHandler(
        filename=log_file_path,
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8",
        utc=True
    )

    # Define formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Set up root logger
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # Console
            file_handler              # Rotating log file
        ]
    )

    return logging.getLogger(name)

import logging
from pathlib import Path

try:
    from sysadmin_utils.utils.config import LOGS_DIR
except ImportError:
    # Fallback if run directly
    LOGS_DIR = Path("logs")
    LOGS_DIR.mkdir(exist_ok=True)


def setup_logger(name: str = "app", log_file: str = "app.log",
                 level=logging.INFO) -> logging.Logger:
    """
    Sets up a logger with file and console handlers.

    Args:
        name (str): Name of the logger.
        log_file (str): Filename for the log in the logs directory.
        level: Logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        msg_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(msg_fmt)

        # File Handler
        file_path = LOGS_DIR / log_file
        fh = logging.FileHandler(file_path)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


# Default logger
logger = setup_logger("sysadmin_utils")


if __name__ == "__main__":
    logger.info("Logger test: Info message")
    logger.warning("Logger test: Warning message")
    logger.error("Logger test: Error message")
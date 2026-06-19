import logging
import inspect
from pathlib import Path

class Log_details:

    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_FILE = BASE_DIR / "Logs" / "automation.log"

    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)

        if not logger.handlers:
            logger.setLevel(logging.DEBUG)

            Log_details.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(Log_details.LOG_FILE)
            file_handler.setLevel(logging.DEBUG)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(lineno)d | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

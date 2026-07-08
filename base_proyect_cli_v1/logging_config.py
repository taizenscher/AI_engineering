# logging_conf.py

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def configure_logging()->None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8"),
        ],
    )

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


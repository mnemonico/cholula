import os

API_BASE_URL = "http://v0.ovapi.nl"
ENDPOINT = "line"
PER_LINE_ENDPOINT_REQUEST = f"{API_BASE_URL}/{ENDPOINT}/"

WAIT_EXPONENTIAL_MIN = 4
WAIT_EXPONENTIAL_MAX = 10
WAIT_EXPONENTIAL_MULTIPLAYER = 1
MAX_ATTEPTS = 100

NAN_VALUE = "-"
MISSING_VALUE = "-"

DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "postgres")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "postgres")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "0.0.0.0")
DATABASE_PORT = 5432

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "console": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "WARNING", "propagate": False},  # root logger
        "default": {
            "handlers": ["console"],
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "propagate": False,
        },
        "dbapi.orm": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "apicalls.extract_to_db": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "utils.tools": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "configuration.setup_loggers": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "__main__": {  # if __name__ == '__main__'
            "handlers": ["console"],
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "propagate": False,
        },
    },
}

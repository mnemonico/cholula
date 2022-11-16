import logging
from logging.config import dictConfig
from ovapi.configuration.assets import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.debug('loggers are configured')

if __name__ == '__main__':
    pass

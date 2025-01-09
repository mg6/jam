import logging

import toml

logger = logging.getLogger(__name__)


def get_config():
    with open("config.toml", "r") as f:
        config = toml.load(f)
        logger.debug("using config: {config}")
        return config

import sys
import logging

from jam.client import client

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__package__)

def run():
    try:
        with client:
            logger.info("Jam time! Press Ctrl-C to quit.")
            input()
    except (KeyboardInterrupt, EOFError):
        pass

    logger.info("Bye!")
    sys.exit(0)


if __name__ == "__main__":
    run()

import sys
import logging

from jam.client import client

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

def run():
    try:
        with client:
            logging.info("Jam time! Press Ctrl-C to quit.")
            input()
    except (KeyboardInterrupt, EOFError):
        pass

    logging.info("Bye!")
    sys.exit(0)


if __name__ == "__main__":
    run()

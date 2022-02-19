import logging
import argparse
import os

LOG_FORMAT = "%(asctime)s — %(name)s — %(levelname)s: %(message)s"
logger = logging.getLogger(__name__)

def main():
    # Parse arguments
    scriptname = os.path.basename(__file__)
    parser = argparse.ArgumentParser(scriptname)
    log_levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    parser.add_argument('-l', '--log-level', help='Define o nível do log', default='INFO', choices=log_levels)
    options = parser.parse_args()

    logging.basicConfig(level=options.log_level, format=LOG_FORMAT)

    logger.warning("This is a test")

if __name__ == '__main__':
    main()
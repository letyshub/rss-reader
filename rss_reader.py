import json
import logging
import logging.handlers
import os
import sys

from emails import EmailSender
from feeds import FeedsReader
from helpers.time_helper import get_period


def configure_logging() -> None:
    """Function configures logging."""

    os.makedirs('logs', exist_ok=True)
    formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t\t%(message)s')
    handler = logging.handlers.TimedRotatingFileHandler(
        os.path.join('logs', 'app.log'), when="S", interval=30, backupCount=10)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def load_configuration() -> any:
    """Function loads configuration from config.json."""

    with open("config.json", "r", encoding="utf-8") as jsonfile:
        return json.load(jsonfile)


def main() -> int:
    """Main function."""

    configure_logging()
    logging.info('Starting application')
    config = load_configuration()
    rss_reader = FeedsReader(config['feeds'])
    feeds = rss_reader.get_feeds(get_period(config['period']))
    email_sender = EmailSender(config['feeds-email-sender'],
                               config['feeds-email-recipient'], config['smtp-host'], config['smtp-port'], config['smtp-user'], config['smtp-password'])
    email_sender.send_feeds_email(feeds)
    return 0


if __name__ == '__main__':
    sys.exit(main())

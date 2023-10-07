import json
import logging
import logging.handlers
import sys

from emails import EmailSender
from helpers.time_helper import get_period
from feeds_reader import FeedsReader


def configureLogging() -> None:
    formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t\t%(message)s')
    handler = logging.handlers.TimedRotatingFileHandler(
        'app.log', when="S", interval=30, backupCount=10)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def loadConfiguration() -> any:
    with open("config.json", "r") as jsonfile:
        return json.load(jsonfile)


def main() -> int:
    configureLogging()
    logging.info('Starting application')
    config = loadConfiguration()
    rss_reader = FeedsReader(config['feeds'])
    feeds = rss_reader.getFeeds(get_period(config['period']))
    email_sender = EmailSender(config['feeds-email-sender'],
                               config['feeds-email-recipient'], config['smtp-host'], config['smtp-port'], config['smtp-user'], config['smtp-password'])
    email_sender.sendFeedsEmail(feeds)
    return 0


if __name__ == '__main__':
    sys.exit(main())

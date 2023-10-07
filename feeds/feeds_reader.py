import datetime
import logging
from time import mktime
import feedparser


from feeds.feed import Feed


class FeedsReader:
    """Class representing a feeds reader"""

    def __init__(self, feed_urls) -> None:
        self.urls = feed_urls

    def get_feeds(self, from_date) -> []:
        """Function checks feeds and return posts since `from_date`."""

        feeds = []
        for url in self.urls:
            try:
                logging.info("Checking: %s since %s", url, from_date)
                d = feedparser.parse(
                    url_file_stream_or_string=url, modified=from_date)
                feed = Feed(d.feed.title, d.feed.subtitle)
                length = len(d.entries)
                logging.info("Downloaded %d entries", length)
                for i, entry in enumerate(d.entries):
                    logging.info(
                        "Checking %d entry of [%s]", i + 1, d.feed.title)
                    if datetime.datetime.fromtimestamp(mktime(entry.published_parsed)) >= from_date:
                        feed.add_entry(
                            entry.title, entry.summary, entry.link)
                feeds.append(feed)
            except Exception as e:
                logging.error("Something went wrong: %s", e, exc_info=True)
                continue

        return feeds

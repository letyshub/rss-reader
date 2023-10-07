import datetime
from time import mktime
import feedparser
import logging

from rssreader.feed import Feed


class RssReader:
    def __init__(self, feedUrls) -> None:
        self.urls = feedUrls

    def getFeeds(self, fromDate) -> []:
        feeds = []
        for url in self.urls:
            try:
                logging.info(f'Checking: {url} since {fromDate}')
                d = feedparser.parse(
                    url_file_stream_or_string=url, modified=fromDate)
                feed = Feed(d.feed.title, d.feed.subtitle)
                length = len(d.entries)
                logging.info(f'Downloaded {length} entries')
                for i in range(len(d.entries)):
                    if datetime.datetime.fromtimestamp(mktime(d.entries[i].published_parsed)) >= fromDate:
                        feed.addEntry(
                            d.entries[i].title, d.entries[i].summary, d.entries[i].link)
                feeds.append(feed)
            except Exception as e:
                logging.error(f'Something went wrong: {e}', exc_info=True)
                continue

        return feeds

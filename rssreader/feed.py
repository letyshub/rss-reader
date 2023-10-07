
from rssreader.feedEntry import FeedEntry


class Feed:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.entries = []

    def addEntry(self, title: str, summary: str, url: str):
        feedEntry = FeedEntry(title, summary, url)
        self.entries.append(feedEntry)

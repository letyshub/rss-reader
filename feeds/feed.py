
from attr import dataclass
from feeds.feed_entry import FeedEntry


class Feed:
    """Class representing a feed"""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.entries = []

    def add_entry(self, title: str, summary: str, url: str):
        """Function adds entry to feed's entries"""

        feed_entry = FeedEntry(title, summary, url)
        self.entries.append(feed_entry)

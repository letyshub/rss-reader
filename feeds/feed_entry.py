from attr import dataclass


class FeedEntry:
    """Class representing a feed's entry (post/article)"""

    def __init__(self, title: str, summary: str, url: str) -> None:
        self.title = title
        self.summary = summary
        self.url = url

import unittest

from feeds.feed import Feed


class TestFeedMethods(unittest.TestCase):
    """Class representing tests of feed.py"""

    def test_add_entry(self):
        """Tests add_entry method"""

        feed = Feed("test-name", "test-description")
        feed.add_entry("title 1", "summary 1", "url 1")
        feed.add_entry("title 2", "summary 2", "url 2")
        self.assertEqual(2, len(feed.entries))
        self.assertEqual("title 1", feed.entries[0].title)
        self.assertEqual("summary 1", feed.entries[0].summary)
        self.assertEqual("url 1", feed.entries[0].url)
        self.assertEqual("title 2", feed.entries[1].title)
        self.assertEqual("summary 2", feed.entries[1].summary)
        self.assertEqual("url 2", feed.entries[1].url)

from datetime import date, timedelta
import unittest

from helpers.time_helper import get_period


class TestTimeHelperMethods(unittest.TestCase):
    """Class representing tests of time_helper.py"""

    def test_get_period_week(self):
        """Tests get_period for week period. Should return last week's date"""

        actual = get_period('w')
        today = date.today()
        expected = today - timedelta(weeks=1)
        self.assertEqual(expected.year, actual.year)
        self.assertEqual(expected.month, actual.month)
        self.assertEqual(expected.day, actual.day)

    def test_get_period_day(self):
        """Tests get_period for day period. Should return yesterday's date"""

        actual = get_period('d')
        today = date.today()
        expected = today - timedelta(days=1)
        self.assertEqual(expected.year, actual.year)
        self.assertEqual(expected.month, actual.month)
        self.assertEqual(expected.day, actual.day)

    def test_get_period_default(self):
        """Tests get_period for default period. Should return yesterday's date"""

        actual = get_period('')
        today = date.today()
        expected = today - timedelta(days=1)
        self.assertEqual(expected.year, actual.year)
        self.assertEqual(expected.month, actual.month)
        self.assertEqual(expected.day, actual.day)

    def test_get_period_month(self):
        """Tests get_period for month period. Should return 30 days ago date"""

        actual = get_period('m')
        today = date.today()
        expected = today - timedelta(days=30)
        self.assertEqual(expected.year, actual.year)
        self.assertEqual(expected.month, actual.month)
        self.assertEqual(expected.day, actual.day)


if __name__ == '__main__':
    unittest.main()

from datetime import date
from datetime import timedelta
import datetime


def get_period(period: str):
    """Function return correct period's date for given `period` attribute."""

    today = date.today()
    period_date = today - timedelta(days=1)
    if period == 'w':
        period_date = today - timedelta(weeks=1)
    if period == 'm':
        period_date = today - timedelta(months=1)

    return datetime.datetime(period_date.year, period_date.month, period_date.day)

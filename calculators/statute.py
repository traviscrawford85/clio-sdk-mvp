# clio_sdk/calculators/statute.py
from datetime import datetime

from dateutil.relativedelta import relativedelta


def compute_limitations_date(incident_date_str: str) -> str:
    """
    Given an incident date string in 'YYYY-MM-DD', returns a limitations date 2 years in the future.
    Returns the computed date as a string in 'YYYY-MM-DD' format.
    """
    try:
        incident_date = datetime.strptime(incident_date_str, "%Y-%m-%d")
        limitations_date = incident_date + relativedelta(years=2)
        return limitations_date.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return ""

# clio/validators.py
# Validates phone numbers, custom fields like Date of Incident, Tort Deadline, Statute of Limitations.
import re
from typing import Any

E164_REGEX = r"^\+[1-9]\d{1,14}$"


def validate_phone_number(phone: str) -> bool:
    """
    Validates that the phone number is in E.164 format:
    - Starts with '+'
    - Country code (no leading zero)
    - Up to 15 digits total (including country code)
    - No spaces, parentheses, or punctuation
    """
    return bool(re.fullmatch(E164_REGEX, phone))


def validate_date_of_incident(custom_fields: dict[str, Any]) -> bool:
    return "Date of Incident" in custom_fields and bool(custom_fields["Date of Incident"])


def validate_matter_data(matter: dict[str, Any]) -> list[str]:
    errors = []

    # Validate phone number
    if "client" in matter and "phone" in matter["client"]:
        phone = matter["client"]["phone"]
        if not validate_phone_number(phone):
            errors.append("Client phone number is not in E.164 format.")
    else:
        errors.append("Client phone number is missing.")

    # Validate Date of Incident custom field
    custom_fields = matter.get("custom_fields", {})
    if not validate_date_of_incident(custom_fields):
        errors.append("Date of Incident is missing or improperly formatted.")

    return errors

from enum import Enum


class ContactindexType(str, Enum):
    COMPANY = "Company"
    PERSON = "Person"

    def __str__(self) -> str:
        return str(self.value)

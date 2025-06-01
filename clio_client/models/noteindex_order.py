from enum import Enum


class NoteindexOrder(str, Enum):
    AUTHORASC = "author(asc)"
    AUTHORDESC = "author(desc)"
    DATEASC = "date(asc)"
    DATEDESC = "date(desc)"
    DETAILASC = "detail(asc)"
    DETAILDESC = "detail(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    SUBJECTASC = "subject(asc)"
    SUBJECTDESC = "subject(desc)"

    def __str__(self) -> str:
        return str(self.value)

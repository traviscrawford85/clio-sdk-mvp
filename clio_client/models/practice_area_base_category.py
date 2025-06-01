from enum import Enum


class PracticeAreaBaseCategory(str, Enum):
    AUTO_ACCIDENT = "auto_accident"
    GENERAL_NEGLIGENCE = "general_negligence"
    MEDICAL_MALPRACTICE = "medical_malpractice"
    OTHER = "other"
    PERSONAL_INJURY = "personal_injury"
    PREMISES_LIABILITY = "premises_liability"
    SCHOOL_INJURY = "school_injury"
    WORKERS_COMPENSATION = "workers_compensation"

    def __str__(self) -> str:
        return str(self.value)

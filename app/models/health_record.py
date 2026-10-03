"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Health Record Model
Description  : Defines the HealthRecord class used to
               represent livestock health information.
------------------------------------------------------------
"""


class HealthRecord:
    """Represents a health record for livestock."""

    VALID_STATUSES = {
        "Healthy": "Healthy",
        "Under Observation": "Under Observation",
        "Under Treatment": "Under Treatment",
        "Recovered": "Recovered",
    }

    def __init__(
        self,
        health_record_id,
        livestock_id,
        health_status,
        treatment,
        record_date,
    ):
        self.__health_record_id = health_record_id
        self.livestock_id = livestock_id
        self.health_status = health_status
        self.treatment = treatment
        self.record_date = record_date

    @property
    def health_record_id(self):
        """Return the health record's unique identifier."""
        return self.__health_record_id

    def display_info(self):
        """Return health record information as formatted text."""
        return (
            f"Health Record ID: {self.health_record_id}\n"
            f"Livestock ID: {self.livestock_id}\n"
            f"Health Status: {self.health_status}\n"
            f"Treatment: {self.treatment}\n"
            f"Record Date: {self.record_date}"
        )

    def update_status(self, health_status):
        """Update the health status of the livestock."""
        self.health_status = health_status

    @classmethod
    def create_basic(
        cls,
        health_record_id,
        livestock_id,
        health_status,
        treatment,
        record_date,
    ):
        """Create a basic HealthRecord object."""
        return cls(
            health_record_id,
            livestock_id,
            health_status,
            treatment,
            record_date,
        )

    @staticmethod
    def is_valid_status(health_status):
        """Check whether a health status is supported."""
        return health_status in HealthRecord.VALID_STATUSES
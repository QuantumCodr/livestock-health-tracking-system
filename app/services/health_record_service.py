"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Health Record Service
Description  : Handles business operations related to
               livestock health records.
------------------------------------------------------------
"""

from app.models import HealthRecord


class HealthRecordService:
    """Provides application operations for health records."""

    def __init__(
        self,
        health_record_repository,
        livestock_repository
    ):
        self.health_record_repository = health_record_repository
        self.livestock_repository = livestock_repository

    def record_health(
        self,
        livestock_id,
        health_status,
        treatment,
        record_date
    ):
        """Create and save a new livestock health record."""

        livestock = self.livestock_repository.find_by_id(
            livestock_id
        )

        if livestock is None:
            raise ValueError("Livestock not found.")

        health_status = health_status.strip()
        treatment = treatment.strip()
        record_date = record_date.strip()

        if not HealthRecord.is_valid_status(health_status):
            raise ValueError("Invalid health status.")

        if not treatment:
            raise ValueError("Treatment cannot be empty.")

        if not record_date:
            raise ValueError("Record date cannot be empty.")

        health_record_id = (
            self.health_record_repository.generate_id()
        )

        health_record = HealthRecord.create_basic(
            health_record_id,
            livestock_id,
            health_status,
            treatment,
            record_date,
        )

        self.health_record_repository.save(health_record)

        return health_record

    def get_health_record(self, health_record_id):
        """Return a health record by ID."""
        return self.health_record_repository.find_by_id(
            health_record_id
        )

    def get_all_health_records(self):
        """Return all registered health records."""
        return self.health_record_repository.find_all()

    def get_health_record_details(self, health_record_id):
        """Return a health record together with livestock details."""

        health_record = (
            self.health_record_repository.find_by_id(
                health_record_id
            )
        )

        if health_record is None:
            return None

        livestock = self.livestock_repository.find_by_id(
            health_record.livestock_id
        )

        return {
            "health_record": health_record,
            "livestock": livestock,
        }

    def get_all_health_record_details(self):
        """Return all health records with livestock details."""

        health_records = (
            self.health_record_repository.find_all()
        )

        health_record_details = {}

        for key, health_record in health_records.items():
            livestock = self.livestock_repository.find_by_id(
                health_record.livestock_id
            )

            health_record_details[key] = {
                "health_record": health_record,
                "livestock": livestock,
            }

        return health_record_details

    def update_health_status(
        self,
        health_record_id,
        health_status
    ):
        """Update the status of an existing health record."""

        health_status = health_status.strip()

        if not HealthRecord.is_valid_status(health_status):
            raise ValueError("Invalid health status.")

        health_record = (
            self.health_record_repository.find_by_id(
                health_record_id
            )
        )

        if health_record is None:
            raise ValueError("Health record not found.")

        health_record.update_status(health_status)

        self.health_record_repository.update(
            health_record
        )

        return health_record
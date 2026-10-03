"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Health Record Repository
Description  : Handles JSON storage and retrieval of
               HealthRecord objects.
------------------------------------------------------------
"""

import json

from app.models import HealthRecord


class HealthRecordRepository:
    """Handles persistence of HealthRecord objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next available health record ID."""
        data = self._load()

        if not data:
            return 1

        return max(int(key) for key in data.keys()) + 1

    def save(self, health_record):
        """Save a HealthRecord object to the JSON file."""
        data = self._load()

        data[str(health_record.health_record_id)] = {
            "health_record_id": health_record.health_record_id,
            "livestock_id": health_record.livestock_id,
            "health_status": health_record.health_status,
            "treatment": health_record.treatment,
            "record_date": health_record.record_date,
        }

        self._write(data)

    def find_by_id(self, health_record_id):
        """Return a HealthRecord by ID, or None if not found."""
        data = self._load()
        record_data = data.get(str(health_record_id))

        if record_data is None:
            return None

        return HealthRecord(
            record_data["health_record_id"],
            record_data["livestock_id"],
            record_data["health_status"],
            record_data["treatment"],
            record_data["record_date"],
        )

    def find_all(self):
        """Return all stored HealthRecord objects."""
        data = self._load()

        health_records = {}

        for key, record_data in data.items():
            health_records[key] = HealthRecord(
                record_data["health_record_id"],
                record_data["livestock_id"],
                record_data["health_status"],
                record_data["treatment"],
                record_data["record_date"],
            )

        return health_records

    def update(self, health_record):
        """Update an existing HealthRecord object."""
        data = self._load()
        record_key = str(health_record.health_record_id)

        if record_key not in data:
            return False

        data[record_key] = {
            "health_record_id": health_record.health_record_id,
            "livestock_id": health_record.livestock_id,
            "health_status": health_record.health_status,
            "treatment": health_record.treatment,
            "record_date": health_record.record_date,
        }

        self._write(data)

        return True

    def _load(self):
        """Load health record data from the JSON file."""
        try:
            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:
                return json.load(file)

        except FileNotFoundError:
            return {}

    def _write(self, data):
        """Write health record data to the JSON file."""
        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(data, file, indent=4)
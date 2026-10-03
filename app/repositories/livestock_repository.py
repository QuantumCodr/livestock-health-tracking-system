"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Livestock Repository
Description  : Handles JSON storage and retrieval of
               Livestock objects.
------------------------------------------------------------
"""

import json

from app.models import Livestock


class LivestockRepository:
    """Handles persistence of Livestock objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next available livestock ID."""
        data = self._load()

        if not data:
            return 1

        return max(int(key) for key in data.keys()) + 1

    def save(self, livestock):
        """Save a Livestock object to the JSON file."""
        data = self._load()

        data[str(livestock.livestock_id)] = {
            "livestock_id": livestock.livestock_id,
            "farmer_id": livestock.farmer_id,
            "animal_type": livestock.animal_type,
            "breed": livestock.breed,
            "gender": livestock.gender,
        }

        self._write(data)

    def find_by_id(self, livestock_id):
        """Return a Livestock object by ID, or None if not found."""
        data = self._load()
        livestock_data = data.get(str(livestock_id))

        if livestock_data is None:
            return None

        return Livestock(
            livestock_data["livestock_id"],
            livestock_data["farmer_id"],
            livestock_data["animal_type"],
            livestock_data["breed"],
            livestock_data["gender"],
        )

    def find_all(self):
        """Return all stored Livestock objects."""
        data = self._load()

        livestock_records = {}

        for key, livestock_data in data.items():
            livestock_records[key] = Livestock(
                livestock_data["livestock_id"],
                livestock_data["farmer_id"],
                livestock_data["animal_type"],
                livestock_data["breed"],
                livestock_data["gender"],
            )

        return livestock_records

    def update(self, livestock):
        """Update an existing Livestock object."""
        data = self._load()
        livestock_key = str(livestock.livestock_id)

        if livestock_key not in data:
            return False

        data[livestock_key] = {
            "livestock_id": livestock.livestock_id,
            "farmer_id": livestock.farmer_id,
            "animal_type": livestock.animal_type,
            "breed": livestock.breed,
            "gender": livestock.gender,
        }

        self._write(data)

        return True

    def _load(self):
        """Load livestock data from the JSON file."""
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
        """Write livestock data to the JSON file."""
        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(data, file, indent=4)
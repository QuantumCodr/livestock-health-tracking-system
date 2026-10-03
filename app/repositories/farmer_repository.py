"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Farmer Repository
Description  : Handles JSON storage and retrieval of
               Farmer objects.
------------------------------------------------------------
"""

import json

from app.models import Farmer


class FarmerRepository:
    """Handles persistence of Farmer objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next available farmer ID."""
        data = self._load()

        if not data:
            return 1

        return max(int(key) for key in data.keys()) + 1

    def save(self, farmer):
        """Save a Farmer object to the JSON file."""
        data = self._load()

        data[str(farmer.farmer_id)] = {
            "farmer_id": farmer.farmer_id,
            "name": farmer.name,
            "location": farmer.location,
        }

        self._write(data)

    def find_by_id(self, farmer_id):
        """Return a Farmer object by ID, or None if not found."""
        data = self._load()
        farmer_data = data.get(str(farmer_id))

        if farmer_data is None:
            return None

        return Farmer(
            farmer_data["farmer_id"],
            farmer_data["name"],
            farmer_data["location"],
        )

    def find_all(self):
        """Return all stored Farmer objects."""
        data = self._load()

        farmers = {}

        for key, farmer_data in data.items():
            farmers[key] = Farmer(
                farmer_data["farmer_id"],
                farmer_data["name"],
                farmer_data["location"],
            )

        return farmers

    def _load(self):
        """Load farmer data from the JSON file."""
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
        """Write farmer data to the JSON file."""
        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(data, file, indent=4)
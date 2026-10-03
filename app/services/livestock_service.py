"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Livestock Service
Description  : Handles business operations related to
               livestock registration and retrieval.
------------------------------------------------------------
"""

from app.models import Livestock


class LivestockService:
    """Provides application operations for livestock."""

    def __init__(
        self,
        livestock_repository,
        farmer_repository
    ):
        self.livestock_repository = livestock_repository
        self.farmer_repository = farmer_repository

    def register_livestock(
        self,
        farmer_id,
        animal_type,
        breed,
        gender
    ):
        """Create and save a new livestock record."""

        farmer = self.farmer_repository.find_by_id(farmer_id)

        if farmer is None:
            raise ValueError("Farmer not found.")

        animal_type = animal_type.strip()
        breed = breed.strip()
        gender = gender.strip()

        if not Livestock.is_valid_animal_type(animal_type):
            raise ValueError("Invalid animal type.")

        if not breed:
            raise ValueError("Livestock breed cannot be empty.")

        if not Livestock.is_valid_gender(gender):
            raise ValueError("Invalid livestock gender.")

        livestock_id = self.livestock_repository.generate_id()

        livestock = Livestock.create_basic(
            livestock_id,
            farmer_id,
            animal_type,
            breed,
            gender,
        )

        self.livestock_repository.save(livestock)

        return livestock

    def get_livestock(self, livestock_id):
        """Return livestock by ID."""
        return self.livestock_repository.find_by_id(
            livestock_id
        )

    def get_all_livestock(self):
        """Return all registered livestock."""
        return self.livestock_repository.find_all()

    def get_livestock_by_farmer(self, farmer_id):
        """Return all livestock belonging to a farmer."""
        livestock_records = (
            self.livestock_repository.find_all()
        )

        farmer_livestock = {}

        for key, livestock in livestock_records.items():
            if livestock.farmer_id == farmer_id:
                farmer_livestock[key] = livestock

        return farmer_livestock

    def update_livestock(
        self,
        livestock_id,
        breed,
        gender
    ):
        """Update the breed and gender of existing livestock."""

        livestock = self.livestock_repository.find_by_id(
            livestock_id
        )

        if livestock is None:
            raise ValueError("Livestock not found.")

        breed = breed.strip()
        gender = gender.strip()

        if not breed:
            raise ValueError("Livestock breed cannot be empty.")

        if not Livestock.is_valid_gender(gender):
            raise ValueError("Invalid livestock gender.")

        livestock.breed = breed
        livestock.gender = gender

        self.livestock_repository.update(livestock)

        return livestock
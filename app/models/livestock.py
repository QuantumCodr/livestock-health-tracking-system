"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Livestock Model
Description  : Defines the Livestock class used to represent
               animals owned and tracked by farmers.
------------------------------------------------------------
"""


class Livestock:
    """Represents livestock registered in the system."""

    # Supported animal types used by the system.
    VALID_ANIMAL_TYPES = {
        "Cattle": "Cattle",
        "Goat": "Goat",
        "Sheep": "Sheep",
        "Pig": "Pig",
        "Chicken": "Chicken",
        "Other": "Other",
    }

    # Supported livestock genders used by the system.
    VALID_GENDERS = {
        "Male": "Male",
        "Female": "Female",
    }

    def __init__(
        self,
        livestock_id,
        farmer_id,
        animal_type,
        breed,
        gender,
    ):
        self.__livestock_id = livestock_id
        self.farmer_id = farmer_id
        self.animal_type = animal_type
        self.breed = breed
        self.gender = gender

    @property
    def livestock_id(self):
        """Return the livestock's unique identifier."""
        return self.__livestock_id

    def display_info(self):
        """Return livestock information as formatted text."""
        return (
            f"Livestock ID: {self.livestock_id}\n"
            f"Farmer ID: {self.farmer_id}\n"
            f"Animal Type: {self.animal_type}\n"
            f"Breed: {self.breed}\n"
            f"Gender: {self.gender}"
        )

    @classmethod
    def create_basic(
        cls,
        livestock_id,
        farmer_id,
        animal_type,
        breed,
        gender,
    ):
        """Create a basic Livestock object."""
        return cls(
            livestock_id,
            farmer_id,
            animal_type,
            breed,
            gender,
        )

    @staticmethod
    def is_valid_animal_type(animal_type):
        """Check whether an animal type is supported."""
        return animal_type in Livestock.VALID_ANIMAL_TYPES

    @staticmethod
    def is_valid_gender(gender):
        """Check whether a livestock gender is supported."""
        return gender in Livestock.VALID_GENDERS
"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Farmer Model
Description  : Defines the Farmer class used to represent
               farmers who own livestock in the system.
------------------------------------------------------------
"""


class Farmer:
    """Represents a farmer in the livestock tracking system."""

    def __init__(self, farmer_id, name, location):
        self.__farmer_id = farmer_id
        self.name = name
        self.location = location

    @property
    def farmer_id(self):
        """Return the farmer's unique identifier."""
        return self.__farmer_id

    def display_info(self):
        """Return the farmer's information as formatted text."""
        return (
            f"Farmer ID: {self.farmer_id}\n"
            f"Name: {self.name}\n"
            f"Location: {self.location}"
        )

    @classmethod
    def create_basic(cls, farmer_id, name, location):
        """Create a basic Farmer object."""
        return cls(farmer_id, name, location)

    @staticmethod
    def is_valid_name(name):
        """Check whether a farmer name is valid."""
        return bool(name and name.strip())

    @staticmethod
    def is_valid_location(location):
        """Check whether a farmer location is valid."""
        return bool(location and location.strip())
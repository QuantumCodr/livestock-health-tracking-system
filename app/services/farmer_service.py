"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Farmer Service
Description  : Handles business operations related to
               farmer registration and retrieval.
------------------------------------------------------------
"""


class FarmerService:
    """Provides application operations for farmers."""

    def __init__(self, farmer_repository):
        self.farmer_repository = farmer_repository

    def register_farmer(self, name, location):
        """Create and save a new farmer."""
        if not name.strip():
            raise ValueError("Farmer name cannot be empty.")

        if not location.strip():
            raise ValueError("Farmer location cannot be empty.")

        farmer_id = self.farmer_repository.generate_id()

        from app.models import Farmer

        farmer = Farmer.create_basic(
            farmer_id,
            name.strip(),
            location.strip(),
        )

        self.farmer_repository.save(farmer)

        return farmer

    def get_farmer(self, farmer_id):
        """Return a farmer by ID."""
        return self.farmer_repository.find_by_id(farmer_id)

    def get_all_farmers(self):
        """Return all registered farmers."""
        return self.farmer_repository.find_all()
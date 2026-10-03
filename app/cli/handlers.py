"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Handlers
Description  : Handles user input and presentation for the
               Livestock Health & Tracking System.
------------------------------------------------------------
"""


class CLIHandlers:
    """Handles user interaction with application services."""

    def __init__(
        self,
        farmer_service,
        livestock_service,
        health_record_service
    ):
        self.farmer_service = farmer_service
        self.livestock_service = livestock_service
        self.health_record_service = health_record_service

    def register_farmer(self):
        """Register a new farmer."""
        print("\n--- Register Farmer ---")

        name = input("Enter farmer name: ").strip()
        location = input("Enter farmer location: ").strip()

        try:
            farmer = self.farmer_service.register_farmer(
                name,
                location,
            )

            print("\nFarmer registered successfully.")
            print(farmer.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def register_livestock(self):
        """Register new livestock."""
        print("\n--- Register Livestock ---")

        farmer_id = self._read_id(
            "Enter farmer ID: "
        )

        print("\nSelect animal type:")
        print("1. Cattle")
        print("2. Goat")
        print("3. Sheep")
        print("4. Pig")
        print("5. Chicken")
        print("6. Other")

        animal_choices = {
            "1": "Cattle",
            "2": "Goat",
            "3": "Sheep",
            "4": "Pig",
            "5": "Chicken",
            "6": "Other",
        }

        animal_choice = input(
            "Enter animal choice: "
        ).strip()

        animal_type = animal_choices.get(animal_choice)

        if animal_type is None:
            print("\nInvalid animal choice.")
            return

        breed = input("Enter livestock breed: ").strip()

        print("\nSelect gender:")
        print("1. Male")
        print("2. Female")

        gender_choices = {
            "1": "Male",
            "2": "Female",
        }

        gender_choice = input(
            "Enter gender choice: "
        ).strip()

        gender = gender_choices.get(gender_choice)

        if gender is None:
            print("\nInvalid gender choice.")
            return

        try:
            livestock = (
                self.livestock_service.register_livestock(
                    farmer_id,
                    animal_type,
                    breed,
                    gender,
                )
            )

            print("\nLivestock registered successfully.")
            print(livestock.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def record_health(self):
        """Record a livestock health record."""
        print("\n--- Record Livestock Health ---")

        livestock_id = self._read_id(
            "Enter livestock ID: "
        )

        print("\nSelect health status:")
        print("1. Healthy")
        print("2. Under Observation")
        print("3. Under Treatment")
        print("4. Recovered")

        status_choices = {
            "1": "Healthy",
            "2": "Under Observation",
            "3": "Under Treatment",
            "4": "Recovered",
        }

        status_choice = input(
            "Enter health status choice: "
        ).strip()

        health_status = status_choices.get(status_choice)

        if health_status is None:
            print("\nInvalid health status choice.")
            return

        treatment = input(
            "Enter treatment or health action: "
        ).strip()

        record_date = input(
            "Enter record date: "
        ).strip()

        try:
            health_record = (
                self.health_record_service.record_health(
                    livestock_id,
                    health_status,
                    treatment,
                    record_date,
                )
            )

            print("\nHealth record created successfully.")
            print(health_record.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def view_farmer(self):
        """Display a farmer by ID."""
        print("\n--- View Farmer ---")

        farmer_id = self._read_id(
            "Enter farmer ID: "
        )

        farmer = self.farmer_service.get_farmer(
            farmer_id
        )

        if farmer is None:
            print("\nFarmer not found.")
            return

        print("\n" + farmer.display_info())

    def view_all_farmers(self):
        """Display all registered farmers."""
        print("\n--- All Farmers ---")

        farmers = self.farmer_service.get_all_farmers()

        if not farmers:
            print("\nNo farmers found.")
            return

        for farmer in farmers.values():
            print("\n" + farmer.display_info())
            print("-" * 40)

    def view_livestock(self):
        """Display livestock by ID."""
        print("\n--- View Livestock ---")

        livestock_id = self._read_id(
            "Enter livestock ID: "
        )

        livestock = self.livestock_service.get_livestock(
            livestock_id
        )

        if livestock is None:
            print("\nLivestock not found.")
            return

        print("\n" + livestock.display_info())

    def view_all_livestock(self):
        """Display all registered livestock."""
        print("\n--- All Livestock ---")

        livestock_records = (
            self.livestock_service.get_all_livestock()
        )

        if not livestock_records:
            print("\nNo livestock found.")
            return

        for livestock in livestock_records.values():
            print("\n" + livestock.display_info())
            print("-" * 40)

    def view_livestock_by_farmer(self):
        """Display livestock belonging to a specific farmer."""
        print("\n--- Livestock by Farmer ---")

        farmer_id = self._read_id(
            "Enter farmer ID: "
        )

        farmer = self.farmer_service.get_farmer(
            farmer_id
        )

        if farmer is None:
            print("\nFarmer not found.")
            return

        livestock_records = (
            self.livestock_service.get_livestock_by_farmer(
                farmer_id
            )
        )

        if not livestock_records:
            print("\nNo livestock found for this farmer.")
            return

        print(
            f"\nLivestock owned by {farmer.name}:"
        )

        for livestock in livestock_records.values():
            print("\n" + livestock.display_info())
            print("-" * 40)

    def view_health_record(self):
        """Display a health record with livestock details."""
        print("\n--- View Health Record ---")

        health_record_id = self._read_id(
            "Enter health record ID: "
        )

        details = (
            self.health_record_service
            .get_health_record_details(
                health_record_id
            )
        )

        if details is None:
            print("\nHealth record not found.")
            return

        health_record = details["health_record"]
        livestock = details["livestock"]

        print(
            f"\nHealth Record ID: "
            f"{health_record.health_record_id}\n"
            f"Livestock ID: "
            f"{health_record.livestock_id}\n"
            f"Animal Type: "
            f"{livestock.animal_type}\n"
            f"Breed: "
            f"{livestock.breed}\n"
            f"Health Status: "
            f"{health_record.health_status}\n"
            f"Treatment: "
            f"{health_record.treatment}\n"
            f"Record Date: "
            f"{health_record.record_date}"
        )

    def view_all_health_records(self):
        """Display all health records with livestock details."""
        print("\n--- All Health Records ---")

        details = (
            self.health_record_service
            .get_all_health_record_details()
        )

        if not details:
            print("\nNo health records found.")
            return

        for record_details in details.values():
            health_record = record_details["health_record"]
            livestock = record_details["livestock"]

            print(
                f"\nHealth Record ID: "
                f"{health_record.health_record_id}\n"
                f"Livestock ID: "
                f"{health_record.livestock_id}\n"
                f"Animal Type: "
                f"{livestock.animal_type}\n"
                f"Breed: "
                f"{livestock.breed}\n"
                f"Health Status: "
                f"{health_record.health_status}\n"
                f"Treatment: "
                f"{health_record.treatment}\n"
                f"Record Date: "
                f"{health_record.record_date}"
            )

            print("-" * 40)

    def update_livestock(self):
        """Update existing livestock information."""
        print("\n--- Update Livestock ---")

        livestock_id = self._read_id(
            "Enter livestock ID: "
        )

        breed = input(
            "Enter new breed: "
        ).strip()

        print("\nSelect new gender:")
        print("1. Male")
        print("2. Female")

        gender_choices = {
            "1": "Male",
            "2": "Female",
        }

        gender_choice = input(
            "Enter gender choice: "
        ).strip()

        gender = gender_choices.get(gender_choice)

        if gender is None:
            print("\nInvalid gender choice.")
            return

        try:
            livestock = (
                self.livestock_service.update_livestock(
                    livestock_id,
                    breed,
                    gender,
                )
            )

            print("\nLivestock updated successfully.")
            print(livestock.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def update_health_status(self):
        """Update the health status of a health record."""
        print("\n--- Update Health Status ---")

        health_record_id = self._read_id(
            "Enter health record ID: "
        )

        print("\nSelect new health status:")
        print("1. Healthy")
        print("2. Under Observation")
        print("3. Under Treatment")
        print("4. Recovered")

        status_choices = {
            "1": "Healthy",
            "2": "Under Observation",
            "3": "Under Treatment",
            "4": "Recovered",
        }

        status_choice = input(
            "Enter health status choice: "
        ).strip()

        health_status = status_choices.get(status_choice)

        if health_status is None:
            print("\nInvalid health status choice.")
            return

        try:
            health_record = (
                self.health_record_service
                .update_health_status(
                    health_record_id,
                    health_status,
                )
            )

            print("\nHealth status updated successfully.")
            print(health_record.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    @staticmethod
    def _read_id(prompt):
        """Read and validate a positive integer ID."""
        try:
            value = int(input(prompt).strip())

            if value <= 0:
                raise ValueError

            return value

        except ValueError:
            raise ValueError(
                "ID must be a positive integer."
            )
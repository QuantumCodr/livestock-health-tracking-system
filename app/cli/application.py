"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Application
Description  : Coordinates the command-line interface and
               application services.
------------------------------------------------------------
"""

from app.cli.handlers import CLIHandlers
from app.cli.menu import Menu


class Application:
    """Runs the Livestock Health & Tracking System CLI."""

    def __init__(
        self,
        farmer_service,
        livestock_service,
        health_record_service
    ):
        self.handlers = CLIHandlers(
            farmer_service,
            livestock_service,
            health_record_service,
        )
        self.menu = Menu()

    def run(self):
        """Start the command-line application."""

        while True:
            self.menu.display()

            choice = input(
                "Enter your choice: "
            ).strip()

            if choice == "1":
                self.handlers.register_farmer()

            elif choice == "2":
                self.handlers.register_livestock()

            elif choice == "3":
                self.handlers.record_health()

            elif choice == "4":
                self.handlers.view_farmer()

            elif choice == "5":
                self.handlers.view_all_farmers()

            elif choice == "6":
                self.handlers.view_livestock()

            elif choice == "7":
                self.handlers.view_all_livestock()

            elif choice == "8":
                self.handlers.view_livestock_by_farmer()

            elif choice == "9":
                self.handlers.view_health_record()

            elif choice == "10":
                self.handlers.view_all_health_records()

            elif choice == "11":
                self.handlers.update_livestock()

            elif choice == "12":
                self.handlers.update_health_status()

            elif choice == "0":
                print("\nThank you for using the system.")
                break

            else:
                print("\nInvalid menu choice.")
"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Menu
Description  : Defines the menu displayed by the
               Livestock Health & Tracking System.
------------------------------------------------------------
"""


class Menu:
    """Displays the application menu."""

    def display(self):
        """Display the main application menu."""
        print("\n" + "=" * 55)
        print("       LIVESTOCK HEALTH & TRACKING SYSTEM")
        print("=" * 55)
        print("1. Register Farmer")
        print("2. Register Livestock")
        print("3. Record Livestock Health")
        print("4. View Farmer")
        print("5. View All Farmers")
        print("6. View Livestock")
        print("7. View All Livestock")
        print("8. View Livestock by Farmer")
        print("9. View Health Record")
        print("10. View All Health Records")
        print("11. Update Livestock")
        print("12. Update Health Status")
        print("0. Exit")
        print("=" * 55)
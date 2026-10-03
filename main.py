"""
------------------------------------------------------------
Program Name : Livestock Health & Tracking System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Main Application
Description  : Application entry point for the Livestock
               Health & Tracking System.
------------------------------------------------------------
"""

from app.cli import Application
from app.repositories import (
    FarmerRepository,
    LivestockRepository,
    HealthRecordRepository,
)
from app.services import (
    FarmerService,
    LivestockService,
    HealthRecordService,
)


def main():
    """Configure dependencies and start the application."""

    farmer_repository = FarmerRepository(
        "data/farmers.json"
    )

    livestock_repository = LivestockRepository(
        "data/livestock.json"
    )

    health_record_repository = HealthRecordRepository(
        "data/health_records.json"
    )

    farmer_service = FarmerService(
        farmer_repository
    )

    livestock_service = LivestockService(
        livestock_repository,
        farmer_repository,
    )

    health_record_service = HealthRecordService(
        health_record_repository,
        livestock_repository,
    )

    application = Application(
        farmer_service,
        livestock_service,
        health_record_service,
    )

    application.run()


if __name__ == "__main__":
    main()
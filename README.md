# Livestock Health & Tracking System

A Python-based Livestock Health & Tracking System developed as an Object-Oriented Programming 1 assignment.

## Problem

Livestock farmers need a simple way to keep track of their animals and monitor their health information. Manual records can make it difficult to organize livestock information and follow changes in animal health.

This system provides a simple command-line solution for registering farmers, tracking livestock, recording health information, and updating livestock health status.

## System Relationship

The system is based on three main entities:

```text
Farmer
   ↓ owns
Livestock
   ↓ has
HealthRecord
```

A farmer can own multiple livestock, and each livestock can have health records associated with it.

## Main Features

* Register farmers
* Register livestock
* Record livestock health information
* View individual farmers
* View all farmers
* View individual livestock
* View all livestock
* View livestock belonging to a farmer
* View individual health records
* View all health records
* Update livestock information
* Update livestock health status
* Automatically generate unique IDs
* Persist data using JSON files

## Livestock Types

The system supports the following animal types:

* Cattle
* Goat
* Sheep
* Pig
* Chicken
* Other

## Health Statuses

The system supports the following health statuses:

* Healthy
* Under Observation
* Under Treatment
* Recovered

## Object-Oriented Programming Concepts

### Classes and Objects

The system contains three main domain classes:

* `Farmer`
* `Livestock`
* `HealthRecord`

Objects are created from these classes to represent real-world farmers, animals, and health records.

### Instance Methods

Instance methods operate on individual objects.

Examples include:

```python
farmer.display_info()
livestock.display_info()
health_record.display_info()
health_record.update_status()
```

### Class Methods

Class methods are used to provide alternative object creation methods.

Examples include:

```python
Farmer.create_basic()
Livestock.create_basic()
HealthRecord.create_basic()
```

### Static Methods

Static methods provide validation functionality that does not depend on a particular object instance.

Examples include:

```python
Livestock.is_valid_animal_type()
Livestock.is_valid_gender()
HealthRecord.is_valid_status()
```

## Data Structure

The system uses **one main data structure: the dictionary**.

Each record is stored using its unique ID as the dictionary key.

Example:

```python
{
    "1": {
        "livestock_id": 1,
        "farmer_id": 1,
        "animal_type": "Cattle",
        "breed": "N'Dama",
        "gender": "Female"
    }
}
```

Using a unique ID as the key makes it possible to retrieve individual records efficiently.

## Data Persistence

The system uses JSON files for simple data persistence.

```text
data/
├── farmers.json
├── livestock.json
└── health_records.json
```

The repositories are responsible for reading and writing these files.

## Project Architecture

The project follows a simple layered structure:

```text
User
  ↓
CLI
  ↓
Services
  ↓
Repositories
  ↓
JSON Files
```

### Models

The model classes represent the main objects in the system.

```text
app/models/
├── farmer.py
├── livestock.py
└── health_record.py
```

### Repositories

Repositories handle JSON storage and retrieval.

```text
app/repositories/
├── farmer_repository.py
├── livestock_repository.py
└── health_record_repository.py
```

### Services

Services contain the application's business rules and operations.

```text
app/services/
├── farmer_service.py
├── livestock_service.py
└── health_record_service.py
```

### CLI

The command-line interface handles user input and displays results.

```text
app/cli/
├── application.py
├── menu.py
└── handlers.py
```

## Project Structure

```text
livestock-health-tracking-system/
├── README.md
├── main.py
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── farmer.py
│   │   ├── livestock.py
│   │   └── health_record.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── farmer_repository.py
│   │   ├── livestock_repository.py
│   │   └── health_record_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── farmer_service.py
│   │   ├── livestock_service.py
│   │   └── health_record_service.py
│   └── cli/
│       ├── __init__.py
│       ├── application.py
│       ├── menu.py
│       └── handlers.py
├── data/
│   ├── farmers.json
│   ├── livestock.json
│   └── health_records.json
└── docs/
    └── report.md
```

## Digital Public Goods Alignment

### Open Source

The project is developed in Python and can be published openly on GitHub so that other students and developers can study and improve the source code.

### Inclusive and Accessible

The application uses a simple command-line interface with clear numbered options and text-based interaction.

### Privacy Respecting

The system is designed to use basic livestock and farming information. It does not require sensitive personal information such as passwords, financial information, or government identification numbers.

### Modular and Reusable

The system separates models, services, repositories, and the CLI. This makes individual components easier to understand, maintain, and reuse.

## Example Usage

Example menu:

```text
=======================================================
       LIVESTOCK HEALTH & TRACKING SYSTEM
=======================================================
1. Register Farmer
2. Register Livestock
3. Record Livestock Health
4. View Farmer
5. View All Farmers
6. View Livestock
7. View All Livestock
8. View Livestock by Farmer
9. View Health Record
10. View All Health Records
11. Update Livestock
12. Update Health Status
0. Exit
=======================================================
Enter your choice:
```

Example livestock information:

```text
Livestock ID: 1
Farmer ID: 1
Animal Type: Cattle
Breed: N'Dama
Gender: Female
```

Example health record:

```text
Health Record ID: 1
Livestock ID: 1
Animal Type: Cattle
Breed: N'Dama
Health Status: Healthy
Treatment: Routine health monitoring
Record Date: 2026-09-25
```

## Requirements

* Python 3.x

No external Python packages are required.

## Running the Application

Open a terminal in the project directory and run:

```bash
python main.py
```

The application will display the main menu and wait for user input.

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

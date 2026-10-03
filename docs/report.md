# Livestock Health & Tracking System

## 1. Project Overview

The Livestock Health & Tracking System is a Python-based object-oriented application designed to help farmers record livestock information and monitor the health of individual animals.

The system allows users to register farmers, register livestock owned by farmers, record livestock health information, view stored records, and update livestock and health information.

The project demonstrates fundamental Object-Oriented Programming concepts including classes, objects, attributes, instance methods, class methods, and static methods.

---

## 2. Problem Statement

Livestock farmers need to keep track of the animals they own and monitor their health conditions. When livestock information is recorded manually, important information such as animal type, breed, ownership, health status, treatment, and health record dates can become difficult to manage.

The Livestock Health & Tracking System provides a simple digital solution for organizing this information.

The system connects farmers with their livestock and connects each livestock record with its health records.

---

## 3. Objectives

The main objectives of the system are to:

* Register farmers in the system.
* Register livestock owned by farmers.
* Record livestock health information.
* Track the health status of livestock.
* Record treatments and health record dates.
* View individual and multiple records.
* Update livestock information.
* Update livestock health status.
* Demonstrate Object-Oriented Programming principles in Python.
* Provide a simple and reusable modular application.

---

## 4. System Design

The system uses three main domain classes:

* `Farmer`
* `Livestock`
* `HealthRecord`

The relationship between the classes is:

```text
Farmer
   ↓ owns
Livestock
   ↓ has
HealthRecord
```

A farmer can own livestock, and each livestock record can have health information associated with it.

For example:

```text
Farmer
ID: 1
Name: Mohamed Kamara
Location: Waterloo
        │
        └── Livestock
            ID: 1
            Type: Cattle
            Breed: N'Dama
            Gender: Female
                    │
                    └── Health Record
                        Status: Healthy
                        Treatment: Routine health monitoring
                        Date: 2026-09-25
```

---

## 5. Classes and Responsibilities

### 5.1 Farmer Class

The `Farmer` class represents a farmer registered in the system.

### Attributes

* `farmer_id`
* `name`
* `location`

### Main Responsibilities

* Store farmer information.
* Provide farmer identification.
* Display farmer information.
* Validate basic farmer information.

---

### 5.2 Livestock Class

The `Livestock` class represents an animal owned by a farmer.

### Attributes

* `livestock_id`
* `farmer_id`
* `animal_type`
* `breed`
* `gender`

### Main Responsibilities

* Store livestock information.
* Associate livestock with a farmer.
* Validate supported animal types.
* Validate supported genders.
* Display livestock information.

Supported animal types include:

* Cattle
* Goat
* Sheep
* Pig
* Chicken
* Other

Supported genders include:

* Male
* Female

---

### 5.3 HealthRecord Class

The `HealthRecord` class represents health information associated with livestock.

### Attributes

* `health_record_id`
* `livestock_id`
* `health_status`
* `treatment`
* `record_date`

### Main Responsibilities

* Store livestock health information.
* Display health records.
* Update health status.
* Validate supported health statuses.

Supported health statuses include:

* Healthy
* Under Observation
* Under Treatment
* Recovered

---

## 6. Object-Oriented Programming Concepts

### 6.1 Classes and Objects

The system defines classes that represent real-world entities.

For example:

```python
farmer = Farmer(
    1,
    "Mohamed Kamara",
    "Waterloo"
)
```

This creates a `Farmer` object from the `Farmer` class.

Similarly, `Livestock` and `HealthRecord` objects are created to represent individual animals and their health information.

---

### 6.2 Attributes

Each class contains attributes that describe its object.

For example, a livestock object contains:

```python
livestock_id
farmer_id
animal_type
breed
gender
```

These attributes allow the system to represent the characteristics of a specific animal.

---

### 6.3 Instance Methods

Instance methods operate on individual objects.

For example:

```python
def display_info(self):
    ...
```

The `display_info()` method displays information belonging to a particular farmer, livestock record, or health record.

The `HealthRecord` class also contains:

```python
def update_status(self, health_status):
    ...
```

This updates the health status of a particular health record.

---

### 6.4 Class Methods

Class methods are used to create objects through the class itself.

For example:

```python
@classmethod
def create_basic(cls, farmer_id, name, location):
    return cls(
        farmer_id,
        name,
        location,
    )
```

The same pattern is used by the `Livestock` and `HealthRecord` classes.

This demonstrates how a class method can provide an alternative object creation method.

---

### 6.5 Static Methods

Static methods provide validation functionality that does not require an individual object.

For example:

```python
@staticmethod
def is_valid_status(health_status):
    return health_status in HealthRecord.VALID_STATUSES
```

Static methods are also used to validate farmer names, locations, animal types, genders, and health statuses.

---

## 7. Data Structure

The project uses **one primary data structure: the dictionary**.

Multiple records are stored using unique identifiers as dictionary keys.

For example:

```python
{
    "1": {
        "farmer_id": 1,
        "name": "Mohamed Kamara",
        "location": "Waterloo"
    }
}
```

The dictionary allows the system to associate each record with a unique ID.

The same approach is used for farmers, livestock, and health records.

This satisfies the requirement to use one data structure for storing multiple objects.

---

## 8. System Features

The system provides the following features:

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
13. Exit the application

These features allow the user to manage the main information required by the system.

---

## 9. Application Architecture

The application follows a simple layered architecture:

```text
main.py
   ↓
CLI
   ↓
Services
   ↓
Repositories
   ↓
JSON Data Files
```

### Models

The model layer represents the real-world entities:

* Farmer
* Livestock
* HealthRecord

### Repositories

The repository layer handles storing and retrieving objects from JSON files.

Repositories are responsible for persistence operations such as:

* Generate ID
* Save
* Find by ID
* Find all
* Update

### Services

The service layer contains the application's business logic.

For example, before livestock is registered, the service verifies that the associated farmer exists and that the livestock information is valid.

### CLI

The CLI layer handles interaction with the user.

It displays menus, accepts input, calls the appropriate services, and displays results.

This separation keeps user interaction, business logic, object representation, and data persistence independent from one another.

---

## 10. Data Persistence

The application uses JSON files for data persistence.

The project contains three main data files:

```text
data/
├── farmers.json
├── livestock.json
└── health_records.json
```

The JSON files allow information to remain available after the application is closed.

The repository layer is responsible for reading and writing these files.

The models and services do not directly interact with the JSON files.

---

## 11. DPG Standards Alignment

### 11.1 Open Source

The project is designed as an open-source Python application and can be published on GitHub.

The source code can be inspected, modified, and reused by other developers.

---

### 11.2 Inclusion and Accessibility

The application uses a simple command-line interface with clear menus and straightforward text-based interaction.

It does not require expensive hardware or advanced software to operate.

The simple interface makes the system suitable for basic computer environments.

---

### 11.3 Privacy

The system focuses on livestock management information and avoids unnecessary sensitive personal information.

The example data uses basic farmer information such as name and location for demonstration purposes.

The application does not require passwords, financial information, or sensitive personal records.

---

### 11.4 Modularity and Reusability

The application is separated into models, repositories, services, and CLI components.

This modular structure makes individual components easier to understand, maintain, and reuse.

For example, the `Livestock` model can be reused by another interface without requiring the model itself to handle user input or file storage.

---

## 12. Example Usage

A typical workflow is:

```text
1. Register Farmer
2. Register Livestock
3. Record Livestock Health
4. View Livestock
5. View Health Record
6. Update Health Status
```

Example:

```text
Enter livestock ID: 1

Livestock ID: 1
Farmer ID: 1
Animal Type: Cattle
Breed: N'Dama
Gender: Female
```

The user can then view the associated health record:

```text
Health Record ID: 1
Livestock ID: 1
Health Status: Healthy
Treatment: Routine health monitoring
Record Date: 2026-09-25
```

The health status can later be updated when the condition of the livestock changes.

---

## 13. Sample Data

The application includes sample records for demonstration.

### Farmers

```text
1. Mohamed Kamara - Waterloo
2. Mariama Sesay - Makeni
3. Abdul Rahman - Bo
```

### Livestock

```text
1. Cattle - N'Dama - Female
2. Goat - West African Dwarf - Male
3. Chicken - Local Breed - Female
```

### Health Records

```text
1. Healthy
2. Under Treatment
3. Recovered
```

These records demonstrate the relationship between farmers, livestock, and health records.

---

## 14. Project Structure

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

---

## 15. Conclusion

The Livestock Health & Tracking System demonstrates how Object-Oriented Programming can be applied to a real-world agricultural problem.

The system uses classes and objects to represent farmers, livestock, and health records. It demonstrates instance methods, class methods, and static methods while using a dictionary as the selected data structure for managing multiple records.

The layered architecture separates models, data persistence, business logic, and user interaction. JSON files provide simple persistent storage, while the command-line interface provides an accessible way to interact with the application.

The project also follows the required DPG principles by being designed for open-source development, accessibility, privacy-conscious data handling, and modularity.

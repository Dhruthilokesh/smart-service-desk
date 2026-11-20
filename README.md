# Smart Service Desk Management System

## Project Overview
The Smart Service Desk Management System is a command-line application developed using Python to manage employee service requests. It allows users to create, view, search, and resolve service requests while maintaining data in a JSON file.

The project demonstrates Object-Oriented Programming, custom exception handling, file handling, separation of responsibilities, basic Domain-Driven Design principles, and Git branching and merging.

## Features
- Create service requests with a unique Request ID
- Store employee name, issue description, and priority
- Support LOW, MEDIUM, and HIGH priorities
- Display all service requests
- Search requests using Request ID
- Resolve open requests
- Prevent duplicate Request IDs
- Prevent resolving an already resolved request
- Validate priority values
- Persist records using JSON
- Reload saved records when the application restarts
- Handle missing or empty data files safely

## Technologies Used
- Python 3
- JSON
- Git
- Linux / Ubuntu

## Project Structure

```text
smart-service-desk/
├── domain/
│   ├── __init__.py
│   ├── service_request.py
│   └── exceptions.py
├── application/
│   ├── __init__.py
│   └── request_service.py
├── infrastructure/
│   ├── __init__.py
│   └── file_repository.py
├── data/
│   └── requests.json
├── tests/
│   ├── __init__.py
│   └── test_service_request.py
├── main.py
├── README.md
└── .gitignore
```

## Application Architecture

### Domain Layer
Contains the core business logic.

- `service_request.py`: Defines the ServiceRequest class, request attributes, priority validation, resolution behavior, and serialization.
- `exceptions.py`: Defines custom exceptions for duplicate requests, missing requests, invalid priority, and already-resolved requests.

### Application Layer
- `request_service.py`: Manages application operations such as creating, searching, viewing, resolving, and saving service requests.

### Infrastructure Layer
- `file_repository.py`: Handles JSON file reading and writing for persistent storage.

### CLI Layer
- `main.py`: Provides the interactive menu and handles user input and output.

## Concepts Demonstrated

### Object-Oriented Programming (OOP)
The ServiceRequest class encapsulates request data and behavior. Objects represent individual service requests.

### Exception Handling
Custom exceptions provide meaningful error handling for invalid priorities, duplicate IDs, missing requests, and repeated resolution attempts.

### File Handling
JSON is used to store request records. Data is loaded at startup and saved after changes, allowing records to persist across program restarts.

### Separation of Responsibilities
The domain, application, infrastructure, and user-interface layers have separate responsibilities, making the code easier to understand, test, and maintain.

### SOLID Principles
The project demonstrates the Single Responsibility Principle by separating business logic, application operations, file persistence, and user interaction into different modules.

### Domain-Driven Design (DDD)
The ServiceRequest acts as a domain model. The RequestService manages operations, while FileRepository handles persistence. The domain model contains the rules governing request priorities and status transitions.

### Git Workflow
Development was carried out on a separate `development` branch using multiple meaningful commits. The completed work is merged into `main` to maintain a stable version of the project.

## How to Run

1. Clone the repository and navigate into the project directory.
2. Run the application:

```bash
python3 main.py
```

## Menu Options

```text
1. Create Service Request
2. View All Requests
3. Search Request
4. Resolve Request
5. Exit
```

## Data Storage

Service request records are stored in:

```text
data/requests.json
```

Each record contains:

- Request ID
- Employee Name
- Issue Description
- Priority
- Status

Example:

```json
{
    "request_id": "SR101",
    "employee_name": "Rahul",
    "issue": "laptop not working",
    "priority": "HIGH",
    "status": "RESOLVED"
}
```

## Running Unit Tests

Execute the unit tests using:

```bash
python3 -m unittest discover -s tests -v
```

The tests validate request creation, priority validation, request resolution, and preventing repeated resolution.

## Git Branch and Merge Workflow

The project uses two branches:

- `main`: stable branch containing the project setup and final version
- `development`: branch used for implementation, testing, and updates

The development workflow:

```bash
git checkout development
# Make changes and commit

git checkout main
git merge development
```

## Conclusion

This project provides a simple and practical service desk solution while demonstrating fundamental Python development concepts, structured application design, automated testing, JSON persistence, and version control using Git.

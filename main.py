from application.request_service import RequestService
from infrastructure.file_repository import FileRepository
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError,
    InvalidPriorityError,
    RequestAlreadyResolvedError
)


def display_menu():
    print("\n" + "=" * 40)
    print("       SMART SERVICE DESK SYSTEM")
    print("=" * 40)
    print("1. Create Service Request")
    print("2. View All Requests")
    print("3. Search Request")
    print("4. Resolve Request")
    print("5. Exit")
    print("=" * 40)


def create_request(service):
    print("\n--- Create Service Request ---")

    request_id = input("Enter Request ID: ").strip()
    employee_name = input("Enter Employee Name: ").strip()
    issue = input("Enter Issue Description: ").strip()
    priority = input("Enter Priority (LOW/MEDIUM/HIGH): ").strip()

    if not request_id or not employee_name or not issue:
        print("Request ID, Employee Name and Issue cannot be empty.")
        return

    try:
        request = service.create_request(
            request_id,
            employee_name,
            issue,
            priority
        )
        print("\nService Request created successfully!")
        print(f"Request ID : {request.request_id}")
        print(f"Status    : {request.status}")

    except DuplicateRequestError as error:
        print(f"\nError: {error}")

    except InvalidPriorityError as error:
        print(f"\nError: {error}")


def view_requests(service):
    print("\n--- All Service Requests ---")

    requests = service.view_requests()

    if not requests:
        print("No service requests available.")
        return

    for request in requests:
        print(
            f"{request.request_id} | "
            f"{request.employee_name} | "
            f"{request.issue} | "
            f"{request.priority} | "
            f"{request.status}"
        )


def search_request(service):
    print("\n--- Search Service Request ---")

    request_id = input("Enter Request ID to search: ").strip()

    try:
        request = service.search_request(request_id)

        print("\nRequest Found")
        print("-" * 30)
        print(f"Request ID     : {request.request_id}")
        print(f"Employee Name  : {request.employee_name}")
        print(f"Issue         : {request.issue}")
        print(f"Priority       : {request.priority}")
        print(f"Status        : {request.status}")

    except RequestNotFoundError as error:
        print(f"\n{error}")


def resolve_request(service):
    print("\n--- Resolve Service Request ---")

    request_id = input("Enter Request ID to resolve: ").strip()

    try:
        request = service.resolve_request(request_id)
        print(f"\nRequest {request.request_id} resolved successfully.")

    except RequestNotFoundError as error:
        print(f"\n{error}")

    except RequestAlreadyResolvedError as error:
        print(f"\n{error}")


def main():
    repository = FileRepository()
    service = RequestService(repository)

    print("Welcome to Smart Service Desk Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            create_request(service)

        elif choice == "2":
            view_requests(service)

        elif choice == "3":
            search_request(service)

        elif choice == "4":
            resolve_request(service)

        elif choice == "5":
            print("\nThank you for using Smart Service Desk System.")
            print("Exiting application...")
            break

        else:
            print("\nInvalid menu choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
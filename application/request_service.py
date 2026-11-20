from domain.service_request import ServiceRequest
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError
)


class RequestService:
    def __init__(self, repository):
        self.repository = repository
        saved_data = self.repository.load_all()

        self.requests = [
            ServiceRequest.from_dict(item)
            for item in saved_data
        ]

    def create_request(self, request_id, employee_name, issue, priority):
        request_id = request_id.strip().upper()

        if self.search_request(request_id, raise_error=False):
            raise DuplicateRequestError(
                f"Request ID {request_id} already exists."
            )

        request = ServiceRequest(
            request_id,
            employee_name,
            issue,
            priority
        )

        self.requests.append(request)
        self._save()

        return request

    def view_requests(self):
        return self.requests

    def search_request(self, request_id, raise_error=True):
        request_id = request_id.strip().upper()

        for request in self.requests:
            if request.request_id == request_id:
                return request

        if raise_error:
            raise RequestNotFoundError(
                f"Request {request_id} not found."
            )

        return None

    def resolve_request(self, request_id):
        request = self.search_request(request_id)
        request.resolve()
        self._save()
        return request

    def _save(self):
        data = [request.to_dict() for request in self.requests]
        self.repository.save_all(data)
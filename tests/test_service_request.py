import unittest
from domain.service_request import ServiceRequest
from domain.exceptions import (
    InvalidPriorityError,
    RequestAlreadyResolvedError
)


class TestServiceRequest(unittest.TestCase):

    def test_create_request(self):
        request = ServiceRequest(
            "SR101", "Rahul", "Laptop not working", "HIGH"
        )
        self.assertEqual(request.request_id, "SR101")
        self.assertEqual(request.status, "OPEN")

    def test_invalid_priority(self):
        with self.assertRaises(InvalidPriorityError):
            ServiceRequest(
                "SR102", "Ananya", "Keyboard issue", "URGENT"
            )

    def test_resolve_request(self):
        request = ServiceRequest(
            "SR103", "Kiran", "Monitor issue", "MEDIUM"
        )
        request.resolve()
        self.assertEqual(request.status, "RESOLVED")

    def test_resolve_twice(self):
        request = ServiceRequest(
            "SR104", "Ravi", "Network issue", "LOW"
        )
        request.resolve()

        with self.assertRaises(RequestAlreadyResolvedError):
            request.resolve()


if __name__ == "__main__":
    unittest.main()
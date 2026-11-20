class ServiceRequest:
    def __init__(self, request_id, employee_name, description, priority):
        self.request_id = request_id
        self.employee_name = employee_name
        self.description = description
        self.priority = priority.upper()
        self.status = "OPEN"

    def resolve(self):
        if self.status == "RESOLVED":
            return False

        self.status = "RESOLVED"
        return True

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        request = cls(
            data["request_id"],
            data["employee_name"],
            data["description"],
            data["priority"]
        )
        request.status = data["status"]
        return request
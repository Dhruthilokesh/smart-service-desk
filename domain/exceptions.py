class ServiceDeskError(Exception):
    """Base exception for service desk application errors."""
    pass


class DuplicateRequestError(ServiceDeskError):
    """Raised when a duplicate request ID is entered."""
    pass


class RequestNotFoundError(ServiceDeskError):
    """Raised when a requested service ID does not exist."""
    pass


class InvalidPriorityError(ServiceDeskError):
    """Raised when an invalid priority is provided."""
    pass


class RequestAlreadyResolvedError(ServiceDeskError):
    """Raised when an already resolved request is resolved again."""
    pass
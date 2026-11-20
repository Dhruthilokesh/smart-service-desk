class DuplicateRequestError(Exception):
    """Raised when a request ID already exists."""
    pass


class RequestNotFoundError(Exception):
    """Raised when a service request cannot be found."""
    pass


class InvalidPriorityError(Exception):
    """Raised when an invalid priority is provided."""
    pass


class RequestAlreadyResolvedError(Exception):
    """Raised when an already resolved request is resolved again."""
    pass
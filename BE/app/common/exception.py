from typing import Optional, Any
from fastapi import Request, status

class AppError(Exception):
    """Base class for application-specific exceptions."""

    def __init__(self,
                 status_code: int,
                 message: str = "An unexpected error occurred.",
                 error_code: Optional[str] = None,
                 details: Optional[list[Any]] = None
    ):
        super().__init__(message)
        self.status_code = status_code
        self.message = message
        self.error_code = error_code
        self.details = details

class BadRequestException(AppError):
    """Exception raised for bad requests."""

    def __init__(self, message: str = "Bad request.", error_code: Optional[str] = "BAD_REQUEST"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, message=message, error_code=error_code)

class UnAuthorizedError(AppError):
    """Exception raised for unauthorized access."""

    def __init__(self, message: str = "Unauthorized access.", error_code: Optional[str] = "UNAUTHORIZED"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, message=message, error_code=error_code)

class ForbiddenError(AppError):
    """Exception raised for forbidden access."""

    def __init__(self, message: str = "Forbidden access.", error_code: Optional[str] = "FORBIDDEN"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, message=message, error_code=error_code)

class NotFoundError(AppError):
    """Exception raised when a requested resource is not found."""

    def __init__(self, message: str = "Resource not found.", error_code: Optional[str] = "RESOURCE_NOT_FOUND"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, message=message, error_code=error_code)

class ConflictError(AppError):
    """Exception raised for conflict errors."""

    def __init__(self, message: str = "Conflict error.", error_code: Optional[str] = "CONFLICT"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, message=message, error_code=error_code)

class ValidationError(AppError):
    """Exception raised for validation errors."""

    def __init__(self, message: str = "Validation error.", error_code: Optional[str] = "VALIDATION_ERROR", details: Optional[list[Any]] = None):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, message=message, error_code=error_code, details=details)

class InternalServerError(AppError):
    """Exception raised for internal server errors."""

    def __init__(self, message: str = "Internal server error.", error_code: Optional[str] = "INTERNAL_SERVER_ERROR"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=message, error_code=error_code)

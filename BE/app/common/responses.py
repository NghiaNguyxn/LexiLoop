from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    code: int
    message: str
    result: T | None = None
    error_code: str | None = None
    errors: list[Any] | None = None

def create_success_response(
    code: int,
    message: str = "Successful",
    result: T | None = None
) -> BaseResponse[T]:
    """Create response for successful operation"""

    return BaseResponse[T](
        code=code,
        message=message,
        result=result
    )

def create_error_response(
    code: int,
    message: str,
    error_code: str | None = None,
    errors: list[Any] | None = None
) -> BaseResponse[T]:
    """Create response for error"""

    return BaseResponse[T](
        code=code,
        message=message,
        error_code=error_code,
        errors=errors
    )

from typing import TypeVar
from pydantic import BaseModel


ReturnModelType = TypeVar("ReturnModelType", bound=BaseModel)
class ApiResponse:
    def __init__(self, data_model: ReturnModelType) -> None:
        self.data_model = data_model    
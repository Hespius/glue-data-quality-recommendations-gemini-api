from pydantic import BaseModel
from typing import Optional, List


class AttributeModel(BaseModel):
    name: str
    type: str
    length: int


class RequestModel(BaseModel):
    type: str
    model: Optional[str] = None
    attributes : List[AttributeModel]

from pydantic import BaseModel
from typing import Optional, List


class AttributeModel(BaseModel):
    name: str
    type: str
    primary_key: Optional[bool] = False


class GeminiRequestModel(BaseModel):
    model: Optional[str] = None
    attributes : List[AttributeModel]


class ManualRequestModel(BaseModel):
    attributes : List[AttributeModel]

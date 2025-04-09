from pydantic import BaseModel
from typing import List


class GeminiResponseModel(BaseModel):
    rules: List[str]
    count_prompt_tokens: int
    count_response_tokens: int
    count_total_tokens: int

class ManualResponseModel(BaseModel):
    rules: List[str]

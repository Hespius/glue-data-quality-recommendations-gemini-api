from pydantic import BaseModel
from typing import List


class ResponseModel(BaseModel):
    rules: List[str]
    count_prompt_tokens: int
    count_response_tokens: int
    count_total_tokens: int

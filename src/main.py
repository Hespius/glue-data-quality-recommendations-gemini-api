import json
from typing import List

import config

from schemas import RequestModel, AttributeModel, ResponseModel

from fastapi import FastAPI
import google.generativeai as genai


app = FastAPI()


def __build_prompt(attributes: List[AttributeModel]) -> str:
    prompt = config.PROMPT
    table_attributes = ""

    for attribute in attributes:
        table_attributes += f"attribute name:{attribute.name}" 
        table_attributes += " | attribute type:{attribute.type}"
        table_attributes += " | attribute length:{attribute.length}\n"

    prompt = prompt.format(table_attributes)

    return prompt


@app.post("/glue-data-quality-recommendations-rules/")
async def recommendations_rules(request_body: RequestModel):
  genai.configure(api_key=config.GEMINI_API_KEY)

  model = genai.GenerativeModel(
    model_name=request_body.model,
    generation_config=config.GENERATION_CONFIG,
    system_instruction=config.INSTRUCTIONS
  )

  prompt = __build_prompt(request_body.attributes)

  response = model.generate_content(prompt)

  response_json = json.loads(response.text)

  return ResponseModel(
    rules=response_json["Rules"],
    count_prompt_tokens=response.usage_metadata.prompt_token_count,
    count_response_tokens=response.usage_metadata.candidates_token_count,
    count_total_tokens=response.usage_metadata.total_token_count
  )

import json
from typing import List

from fastapi import FastAPI
import google.generativeai as genai

import config
from schemas import *


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


@app.post("/glue-data-quality-recommendations-rules-with-gemini")
async def gemini_recommendations_rules(request_body: GeminiRequestModel):
  genai.configure(api_key=config.GEMINI_API_KEY)

  model = genai.GenerativeModel(
    model_name=request_body.model,
    generation_config=config.GENERATION_CONFIG,
    system_instruction=config.INSTRUCTIONS
  )

  prompt = __build_prompt(request_body.attributes)

  response = model.generate_content(prompt)

  response_json = json.loads(response.text)

  return GeminiResponseModel(
    rules=response_json["Rules"],
    count_prompt_tokens=response.usage_metadata.prompt_token_count,
    count_response_tokens=response.usage_metadata.candidates_token_count,
    count_total_tokens=response.usage_metadata.total_token_count
  )


def __build_manual_rules(attributes: List[AttributeModel]) -> List[str]:
    LIST_ACCEPTED_TYPES = ["BOOLEAN", "DATE", "TIMESTAMP", "INTEGER", "DOUBLE", "FLOAT", "LONG"]

    list_rules = []

    for attribute in attributes:
        if attribute.type.upper() in LIST_ACCEPTED_TYPES:
            list_rules.append(f'ColumnDataType \"{attribute.name.upper()}\" = \"{attribute.type.upper()}\"')

        list_rules.append(f'ColumnLength \"{attribute.name.upper()}\" >= \"{attribute.length}\"')

    return list_rules


@app.post("/glue-data-quality-recommendations-rules")
async def recommendations_rules(request_body: ManualRequestModel):
  rules = __build_manual_rules(request_body.attributes)

  return ManualResponseModel(
    rules= rules
  )

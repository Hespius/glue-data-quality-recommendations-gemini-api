import os
import re
import json

from dotenv import load_dotenv
from fastapi import FastAPI
import google.generativeai as genai

load_dotenv()

app = FastAPI()

@app.get("/glue-data-quality-recommendations-rules")
def read_root(model_name: str = "gemini-2.0-flash-exp"):
  genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    

  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
  }

  instructions = """
  Act as a data engineer specializing in data quality. Your primary tool is AWS Glue, and you use AWS Glue Data Quality to monitor the data quality of your tables.

  Respond only with the data quality rules I can apply to the table following the syntax of AWS Glue Data Quality's DQDL, according to the example below:

  Rules = [
    'IsComplete "COLUMN_NAME"',
    'IsUnique "COLUMN_NAME"'
  ]
  """

  model = genai.GenerativeModel(
    model_name=model_name,
    generation_config=generation_config,
    system_instruction=instructions
  )

  prompt = """
  I have a table with the following attributes:

  id: integer
  nome: string
  idade: integer
  email: string
  data_cadastro: string

  I would like to know what data quality rules I can apply to the table.

  """

  response = model.generate_content(prompt)
  response_json = json.loads(response.text)

  return {
    "rules": response_json["Rules"],
    "count_prompt_tokens": response.usage_metadata.prompt_token_count,
    "count_response_tokens": response.usage_metadata.candidates_token_count,
    "count_total_tokens": response.usage_metadata.total_token_count
  }

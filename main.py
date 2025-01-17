import os
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
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
  model_name="gemini-2.0-flash-exp",
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

print(response.text)
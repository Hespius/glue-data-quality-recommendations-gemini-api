import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GENERATION_CONFIG = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

INSTRUCTIONS = """
Act as a data engineer specializing in data quality. Your primary tool is AWS Glue, and you use AWS Glue Data Quality to monitor the data quality of your tables.

Respond only with the data quality rules I can apply to the table following the syntax of AWS Glue Data Quality's DQDL, according to the example below:

Rules = [
    'IsComplete "COLUMN_NAME"',
    'IsUnique "COLUMN_NAME"'
]
"""

PROMPT = """
  I have a table with the following attributes:

  {}

  I would like to know what data quality rules I can apply to the table.

  """
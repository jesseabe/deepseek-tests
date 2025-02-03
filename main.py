from openai import OpenAI   
import os
from dotenv import load_dotenv

load_dotenv(".env")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("KEY"),
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)
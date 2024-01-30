import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("What is the meaning of life?")
response = model.generate_content("日本に有名なところを言ってください。")

print(response.text)
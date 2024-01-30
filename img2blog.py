import os
from dotenv import load_dotenv
import PIL.Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

img = PIL.Image.open('test1.png')
genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)
response.resolve()
print(response.text)
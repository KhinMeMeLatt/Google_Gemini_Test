import os
from dotenv import load_dotenv
import PIL.Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

img = PIL.Image.open('img2.jpg')
genai.configure(api_key='AIzaSyB0DrN5nr19Rb_SXiw1BZ2N52XYK6K3lOA')

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

print(response.text)
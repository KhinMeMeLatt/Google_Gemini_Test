import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
response = chat.send_message("In one sentence, explain how a computer works to a young child.")
response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)
response.resolve()
for message in chat.history:
  print(message.role+": "+message.parts[0].text)
#   display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
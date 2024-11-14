from pcpartpicker import API as api
from openai import OpenAI as openai
from dotenv import load_dotenv
import os

load_dotenv()

pc_api = api(region="us")

import cohere

client = cohere.Client(os.getenv("COHERE_KEY_NATAS"))

def generate_response(prompt):
    response = client.generate(
        model="command-xlarge",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.generations[0].text.strip()

def get_part_info(part_type):
  try:
    part_data = pc_api.retrieve(part_type)
    return part_data
  except Exception as e:
    return str(e)

def chatbot_response(user_input):
  if "understand computer parts" in user_input.lower():
    return generate_response("You are a specialized assistant in understanding computer parts. " + user_input)
  
  elif "select parts" in user_input.lower():
    parts_data = get_part_info("cpu")  # Example part type
    if parts_data:
      return f"Here are some CPUs you can consider: {parts_data}"
    
    else:
      return "Sorry, I couldn't retrieve parts data at the moment."
  
  elif "build a system" in user_input.lower():
    return generate_response("You are a specialized assistant in building computer systems. " + user_input)
  
  else:
    return generate_response("You are a specialized assistant in computer specifications. " + user_input)

def main():
  print("Welcome to the Computer Hardware Chatbot!")
  print("Type 'exit' to end the chat.")
  while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
      print("Goodbye!")
      break
    response = chatbot_response(user_input)
    print("Assistant:", response)

if __name__ == "__main__":
  main()

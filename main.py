from pcpartpicker import API as api
from openai import OpenAI as openai
from dotenv import load_dotenv
import os

load_dotenv()
# GPT_KEY_LEO
# GPT_KEY_NATAS
client = openai(api_key = os.getenv("GPT_KEY_NATAS")) 
pc_api = api(region="us")

specialization_prompt = "You are a specialized assistant for computer specifications."

def generate_response(prompt):
  response = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content":
          {
            "type": "text",
            "text": specialization_prompt
          }
      },
      {
        "role": "user",
        "content":
          {
            "type": "text",
            "text": prompt
          }
      }
    ],
    model="gpt-3.5-turbo",
    max_tokens=150,
    temperature=0.5
  )
  return response['choices'][0]['message']['content'].strip()

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

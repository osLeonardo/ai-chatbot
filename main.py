from dotenv import load_dotenv
from pcpartpicker import API
import cohere
import os

load_dotenv()

pc_api = API("us")
client = cohere.Client(os.getenv("COHERE_KEY"))
part_categories = {'wireless-network-card', 'case-fan', 'cpu', 'cpu-cooler', 'headphones', 'motherboard', 'monitor', 'internal-hard-drive', 'external-hard-drive', 'ups', 'fan-controller', 'case', 'keyboard', 'mouse', 'wired-network-card', 'sound-card', 'video-card', 'speakers', 'optical-drive', 'power-supply', 'thermal-paste', 'memory'}

def clear_terminal():
  os.system('clear')

def generate_response(prompt):
  response = client.generate(
    model="command-xlarge",
    prompt=prompt,
    max_tokens=1500,
    temperature=0.5
  )
  return response.generations[0].text.strip()

def get_part_info(part_type):
  try:
    part_data = pc_api.retrieve(part_type)
    return part_data
  except Exception as e:
    return str(e)

def identify_part_category(user_input):
  for category in part_categories:
    if category.replace('-', ' ') in user_input.lower():
      return category
  return None

def chatbot_response(user_input):
    part_category = identify_part_category(user_input)
    if part_category:
        parts_data = get_part_info(part_category)
        if parts_data:
            return f"Here are some {part_category.replace('-', ' ')}s you can consider: {parts_data}"
        else:
            return "Sorry, I couldn't retrieve parts data at the moment."
    else:
        return generate_response("You are a specialized assistant in computer parts. " + user_input)

def main():
  clear_terminal()
  print("\033[1;36m=========================================")
  print("\n\033[1;35mWelcome to the Computer Hardware Chatbot!")
  print("\n\033[1;36m=========================================")
  print("\n\033[1;31m\n- Type '\033[0;33mexit\033[1;31m' to end the chat.")
  while True:
    user_input = input("\033[1;32m\n> You: \033[0m")
    if user_input.lower() == 'exit':
      print("\n\033[1;36m> Assistant: \033[0mGoodbye!\n")
      break
    response = chatbot_response(user_input)
    print("\n\033[1;36m> Assistant: \033[0m", response)

if __name__ == "__main__":
  main()

# Computer Hardware Chatbot

# Contributors
- Natanael Alves
- Leonardo Spilere

## Overview

The Computer Hardware Chatbot is a specialized assistant designed to help users with questions about computer parts and PC building. It uses the `pcpartpicker` library to retrieve data about various computer components and provides relevant information based on user queries. The chatbot can answer general questions about computers and provide specific details about different parts.

## Features

- Answers general questions about computer parts and PC building.
- Retrieves data from the `pcpartpicker` library.
- Supports a wide range of part categories, including CPUs, GPUs, motherboards, and more.
- Provides a user-friendly chat interface with colored text for better readability.

## Part Categories Supported

The chatbot supports the following part categories:
- `wireless-network-card`
- `case-fan`
- `cpu`
- `cpu-cooler`
- `headphones`
- `motherboard`
- `monitor`
- `internal-hard-drive`
- `external-hard-drive`
- `ups`
- `fan-controller`
- `case`
- `keyboard`
- `mouse`
- `wired-network-card`
- `sound-card`
- `video-card`
- `speakers`
- `optical-drive`
- `power-supply`
- `thermal-paste`
- `memory`

## Installation

1. Clone the repository:
    ```sh
    # Using HTTPS
    git clone https://github.com/osLeonardo/ai-chatbot.git
    cd ai-chatbot
    ```

    ```sh
    # Using SSH
    git clone git@github.com:osLeonardo/ai-chatbot.git
    cd ai-chatbot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a Cohere API key:
    - Go to the [Cohere website](https://cohere.ai/) and sign up for an account.
    - Navigate to the API section and generate a new API key.

4. Edit the `.env` file in the root directory with your Cohere API key:
    ```env
    COHERE_KEY="your_cohere_api_key"
    ```

## Usage

1. Run the chatbot:
    ```sh
    python main.py
    ```

2. Interact with the chatbot by typing your questions about computer parts and PC building. For example:
    ```sh
    > You: What are some good CPUs?
    ```

3. To exit the chat, type `exit`.

## Example
  ```sh
  =========================================
  Welcome to the Computer Hardware Chatbot!
  =========================================

  - Type 'exit' to end the chat.
  
  > You: What are some good CPUs?
  
  > Assistant: Here are some CPUs you can consider: [list of CPUs]
```

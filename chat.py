#!/usr/bin/env python3

import requests
import json

# Define your Cloudflare Workers URL
WORKER_URL = 'https://worker-au-hackathon.campbrown123.workers.dev'

def chatbot(input_text):
    # Define the payload
    payload = {
        'text': input_text
    }

    try:
        # Send a POST request to the Cloudflare Worker
        response = requests.post(WORKER_URL, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return 'Error: Failed to process request'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    # Get input from the user
    user_input = input('You: ')

    # Call the chatbot function
    bot_response = chatbot(user_input)

    # Print the response
    print('Bot:', bot_response)

    # Write the bot response to a text file
    with open('bot_response.txt', 'w') as file:
        file.write('You: ' + user_input + '\n')
        file.write('Bot: ' + bot_response + '\n')

    print('Bot response has been saved to bot_response.txt')
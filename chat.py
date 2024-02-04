import openai

openai.api_key = ''

def response(user_input, initialization):
    messages = [{"role": "system", "content":
                 initialization}]

    messages.append({"role": "user", "content": user_input})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content

    with open('bot_response.txt', 'a') as file:
        file.write('You: ' + user_input + '\n')
        file.write('Bot: ' + reply + '\n')

    return reply
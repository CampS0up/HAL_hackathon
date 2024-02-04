import openai
import sys

openai.api_key = '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'

def response(user_input):
    messages = [{"role": "system", "content":
                 "You are an intelligent assistant modeled after HAL."}]

    if len(sys.argv) != 2:
        print("Usage: python3 chat.py 'TEXT'")
        sys.exit(1)

    messages.append({"role": "user", "content": user_input})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    print(reply)
    return reply
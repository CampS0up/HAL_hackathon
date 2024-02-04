import openai

openai.api_key = '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'

def response(user_input):
    messages = [{"role": "system", "content":
                 "You are an intelligent assistant modeled after HAL."}]

    messages.append({"role": "user", "content": user_input})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    print(reply)
    return reply
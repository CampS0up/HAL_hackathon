import openai
import sys

openai.api_key = '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'

def main():
    messages = [{"role": "system", "content":
                 "You are an intelligent assistant modeled after HAL."}]

    if len(sys.argv) != 2:
        print("Usage: python3 chat.py 'TEXT'")
        sys.exit(1)

    user_input = sys.argv[1]
    messages.append({"role": "user", "content": user_input})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    print(reply)

if __name__ == "__main__":
    main()
import openai

openai.api_key = "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"

def Chat_with_gpt(promt):
    response = openai.ChatCompletion.create(
        model="gpt3.5-turbo",
        messages=[{"role": "user", "content": promt}]
    )

    return response.choices[0].message.content.strip()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit","exit","bye"]:
        break

    response = Chat_with_gpt(user_input)
    print("Chatbot: ", response)

from google import genai
client = genai.Client(api_key="AIzaSyDpP6nok-UeFyw-Li_hTtDIgJDUUvfwfDg")

chat = client.chats.create(model = "gemini-2.5-flash")


print("Gemini Chatbot (type 'exit' to quit)\n")


while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)

    print("Bot: ", response.text)


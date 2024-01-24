from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from openai.types.chat.chat_completion import ChatCompletion

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()


response : ChatCompletion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format= {"type" : "json_object"},
    messages= [
        # 'messages' must contain the word 'json', otherwise error
        {"role" : "system", "content" : "You are a helpful assistant. Output must be in JSON."},
        {"role" : "user", "content" : "List of months that have 31 days"}
        # { 
        # "months": ["January", "March", "May", "July", "August", "October", "December"
        # }
    ]
)

print(response.choices[0].message.content)
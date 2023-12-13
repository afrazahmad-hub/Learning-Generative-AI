from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from openai.types.chat.chat_completion import ChatCompletion

# following is the community standerd
# when return something from a function, but do not use it
# we ue _ sign
_ : bool = load_dotenv(find_dotenv())

client : OpenAI = OpenAI()

stream : ChatCompletion = client.chat.completions.create(
    model = "gpt-3.5-turbo-1106",
    messages =[ {
        "role":"user", "content" : "Say this is a streaming test"
    }],
    stream= True
)

for part in stream:
    print(part.choices[0].delta.content or "")

# This
#  is 
#  a        
#  streaming
#  test
# .
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
from openai.types.chat.chat_completion import ChatCompletion

# print(find_dotenv()) # It will find the path of enviornment file


# following is the community standerd
# when return something from a function, but do not use it
# we ue _ sign
_ : bool = load_dotenv(find_dotenv()) 
client : OpenAI = OpenAI()

# print(os.environ["MY_NAME"]) # AFRAZ AHMAD

def chat_completion(prompt : str) -> str:
    response : ChatCompletion = client.chat.completions.create(
        messages=[
            {"role" : "user",
            "content" : prompt}
        ],
        model = "gpt-3.5-turbo-1106",
    )
    # print(response)
    # print(response.choices[0].message.content)
    return response.choices[0].message.content

result = chat_completion("What is 1 + 1 ?")
print(result)


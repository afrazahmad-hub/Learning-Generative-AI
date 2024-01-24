from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import os

from openai.types.chat.chat_completion import ChatCompletion

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

def chat_completion() -> str:
    completion : ChatCompletion = client.chat.completions.create(
        model = "gpt-3.5-turbo-1106",
        messages = [
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
        )
    # print(completion)
    return completion.choices[0].message.content


result = chat_completion()
print(result)

# In the world of code, recursive might sound divine, 
# A function that calls itself, like a dance in time. 

# From its humble start, it ventures into the unknown,
# Solving problems in a way, truly of its own.        

# Like a Russian doll, nested within its own grasp,   
# It repeats its steps, until the problem's clasped.

# A mystical loop, echoing through the night,
# Unraveling complexities, with each recursive flight.

# Through the branches of logic, it travels without cease,
# And with each iteration, a solution it will release.

# In the realm of code, recursion stands tall,
# A poetic dance of function, answering the call.
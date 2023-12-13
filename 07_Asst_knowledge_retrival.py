from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import json

from openai.types.beta import Assistant, Thread


_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()


file = client.files.create(
    file = open("C.V.Afraz to use in step 7.pdf", "rb"),
    purpose="assistants"
)
print(file.id)


# assistant = Assistant = client.beta.assistants.create(
#     name = ""
#     instructions= ""
#     model = "gpt-3.5-turbo-1106"
# )
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import json

from openai.types.beta import Assistant, Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads.run import Run

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()


file = client.files.create(
    file = open("CV_Afraz_use_step7.pdf", "rb"),
    purpose="assistants"
)

# 2 extra arguments in assistant
# tools, and file_id
assistant : Assistant = client.beta.assistants.create(
    name = "My Assistant",
    instructions= "You use the given knowledge base, to anwser the queries about Afraz Ahmad",
    model = "gpt-3.5-turbo-1106",
    tools = [{"type" : "retrieval"}],
    file_ids= [file.id]
)

thread : Thread = client.beta.threads.create()


message = client.beta.threads.messages.create(
    thread_id= thread.id,
    role = "user",
    content= "What is the father name of Afraz Ahmad?"
)

run : Run = client.beta.threads.runs.create(
    thread_id= thread.id,
    assistant_id= assistant.id,
    instructions= "Please consider the user as Pakistani."
)
# check the run status
run : Run = client.beta.threads.runs.retrieve(
    thread_id= thread.id,
    run_id= run.id
)
print(" Run status", run)

# display assistant response
messages : list[ThreadMessage] = client.beta.threads.messages.list(
    thread_id= thread.id
)

for m in reversed(messages.data):
    # print(f"""Answer: \n {m.role} : {m.content[0].text.value} """)
    print(m.role + ":" + m.content[0].text.value)
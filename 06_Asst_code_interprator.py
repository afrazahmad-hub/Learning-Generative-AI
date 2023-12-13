from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from openai.types.beta import Assistant, Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads.run import Run

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

# step 1: create an assistant
assistant : Assistant = client.beta.assistants.create(
    name =  "Math Tuoter",
    instructions= "You are a math teacher.",
    model="gpt-3.5-turbo-1106"
)

# step 2: create a thread
thread : Thread = client.beta.threads.create()

# step 3: add messages to the thread
message1 = client.beta.threads.messages.create(
    thread_id= thread.id,
    role= "user",
    content= "Answer of 8 * 8 ?"
)

message2 = client.beta.threads.messages.create(
    thread_id= thread.id,
    role= "user",
    content= "Answer of 4 * 4 ?"
)


# Step 4: Run the Assistant
run: Run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

# step 5: Check the run status
run : Run = client.beta.threads.runs.retrieve(
    thread_id= thread.id,
    run_id= run.id
)

# step 6: Display the Assistant's Response
messages : list[ThreadMessage] = client.beta.threads.messages.list(
    thread_id= thread.id
)

for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)

# user: Answer of 8 * 8 ?
# assistant: 8 multiplied by 8 equals 64.


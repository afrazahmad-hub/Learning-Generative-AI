from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import json
import time

from openai.types.beta import Assistant, Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads.run import Run

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def getCurrentWeather(location:str, unit:str="fahrenheit")->str | dict | None:
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": "celsius"})
    elif "los angeles" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})
    

def getNickname(location:str)->str:
    """Get the nickname of a city"""
    if "tokyo" in location.lower():
        return "tk"
    elif "los angeles" in location.lower():
        return "la"
    elif "paris" in location.lower():
        return "py"
    else:
        return location

def show_json(message, obj):
    print(message, json.loads(obj.model_dump_json()))


assistant : Assistant = client.beta.assistants.create(
    instructions = "You are a weather bot. Use the provided functions to answer questions.",
    model= "gpt-3.5-turbo-1106",
    tools = [{
        "type" : "function",
        "function" : {
            "name" : "getCurrentWeather",
            "description" : "Get the weather in location.",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "location" : {"type" :  "string", "description" : "The city and state e.g. San Francisco, CA"},
                    "unit" : {"type" : "string", "enum" : ["c", "f"]}
                },
                "required" : ["location"]
            }
        }
    },{
        "type" : "function", 
        "function" : {
            "name": "getNickname",
            "description" : "Get the nickname of a city",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "location" : {"type" :  "string", "description" : "The city and state e.g. San Francisco, CA"}
                },
                "required" : ["location"]
            }
        }
    }]
)


thread : Thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id= thread.id,
    role="user",
    content= "How is the current weather in tokyo ?"
)

run : Run = client.beta.threads.runs.create(
    thread_id= thread.id,
    assistant_id= assistant.id
)

#  dictionary for functions
available_functions = {
    "getCurrentWeather" : getCurrentWeather,
    "getNickname" : getNickname
}


# Final step
# Polling for Updates and Calling Functions
while True:
    # check the status of run, i.e. in-progress, complete, or action_required etc.
    runStatus = client.beta.threads.runs.retrieve(thread_id=thread.id,
                                                   run_id=run.id)
    # for debugging, add run steps
    run_steps = client.beta.threads.runs.steps.list(thread_id=thread.id,
                                              run_id = run.id)
    
    # This means run is making a function call
    if runStatus.status == "requires_action":
        print(runStatus.status, ".........")
        show_json("Submit tools output", runStatus.required_action)
        # validate "submit_tool_outputs" and "tool_calls"
        if runStatus.required_action.submit_tool_outputs and runStatus.required_action.submit_tool_outputs.tool_calls:
            
            # we will use it to to extract function and function arguments
            toolCalls = runStatus.required_action.submit_tool_outputs.tool_calls

            tool_outputs = []
            for toolCall in toolCalls:
                function_name = toolCall.function.name
                function_args = json.load(toolCall.function.arguments)

                if function_name in available_functions:
                    function_to_call = available_functions[function_name]
                    print(function_to_call.name)

                    if function_to_call.name == "getCurrentWeather":
                        response = function_to_call(
                            location = function_args.get("location"),
                            unit = function_args.get("unit"),
                        )

                        tool_outputs.append({
                            "toolCall_id" : toolCall.id,
                            "output" : response
                        })
                    elif function_to_call.name == "getNickname":
                        response = function_to_call(
                            location = function_args.Get("location")                            
                        )

                        tool_outputs.append({
                            "toolCall_id" : toolCall.id,
                            "output" : response
                        })
            print(tool_outputs)
            # Submit tool outputs and update the run
            client.beta.threads.runs.submit_tool_outputs(
                thread_id= thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs)
    
    # =========== if COMPLETED
    elif runStatus.status == "completed":

        # List the messages to get the response
        messages : list[ThreadMessage] = client.beta.threads.messages.list(thread_id=thread.id)

        for m in messages.data:
            role_label = "User" if m.role == "user" else "Assistant"
            message_contant = m.content[0].value.text
            print(f"""{role_label} : {message_contant}\n """)
        break # Exit the loop after processing the completed run
    
    # =========== if FAILED
    elif runStatus.status == "failed":
        print("Run failed.")
        break

    # =========== if IN-PROGRESS, QUEUED
    elif runStatus.status == ["in_progress", "queued"]:
        print(f"Run is {runStatus.status}. Waiting...")
        time.sleep(5)  # Wait for 5 seconds before checking again

    else:
      print(f"Unexpected status: {runStatus.status}")
      break
 











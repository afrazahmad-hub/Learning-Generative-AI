from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import json
from openai.types.chat.chat_completion import ChatCompletion, ChatCompletionMessage

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

# Example dummy function
# In production, this could be your backend API or an external API
def get_current_weather(location: str, unit:str="fahrenheit") ->str:
    """Get the Current weather for the given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location" : "Tokyo", "temprature" : "10", "unit" : "celsius"})
    elif "san francisco" in location.lower():
        return json.dumps({"location" : "san francisco", "temprature" : "72", "unit" : "fahrenheit"})
    elif "paris" in location.lower():
        return json.dumps({"location" : "Paris", "temprature" : "22", "unit" : "celsius"})
    else:
        return json.dumps({"location" : location, "temprature" : "unknown"})


# Step 1: send the conversation and available functions to the model
def run_conversation(main_req : str) ->str:
    messages = [{"role" : "user", "content" : main_req}]
    tools = [
        { 
            "type" : "function",
            "function" : {
                "name" : "get_current_weather",
                # Must write this description
                "description" : "Get the current weather in given location",
                "parameters" : {
                    "type" : "object",
                    "properties" : {
                        "location" : {
                            "type" : "string",
                            "description" : "The city and state, e.g. San Francisco, CA"},
                        "unit" : {"type" : "string", "enum" : ["celsius", "fahrenheit"]},
                    },
                    "required" : ["location"]
                }
            }
        }
    ]

    # First Request
    response : ChatCompletion = client.chat.completions.create(
        model = "gpt-3.5-turbo-1106",
        messages = messages,
        tools = tools,
        tool_choice = "auto")
    
    response_message : ChatCompletionMessage = response.choices[0].message
    # print("First Output: ", dict(response_message))
    # First Output:  {'content': None, 'role': 'assistant', 'function_call': None, 'tool_calls': 
    # [ChatCompletionMessageToolCall(id='call_evQa5jUUwDiZ79vwB7KJcNvr', 
    # function=Function(arguments='{"location": "San Francisco", "unit": "celsius"}', 
    # name='get_current_weather'), type='function'), 
    # ChatCompletionMessageToolCall(id='call_O7J6aJg7QFwxqBN7PAgoV9qI', 
    # function=Function(arguments='{"location": "Tokyo", "unit": "celsius"}', 
    # name='get_current_weather'), type='function'), 
    # ChatCompletionMessageToolCall(id='call_qFwTikgVCH07xGztOF3rU55Y', 
    # function=Function(arguments='{"location": "Paris", "unit": "celsius"}', 
    # name='get_current_weather'), type='function')]}

    tool_calls = response_message.tool_calls
    # print("Tool call output: ", tool_calls)
    # Tool call output:  [ChatCompletionMessageToolCall(id='call_kfdMX6m4MSbDU4Ax2MRcXsDd', 
    # function=Function(arguments='{"location": "San Francisco, CA", "unit": "celsius"}', 
    # name='get_current_weather'), type='function'), 
    # ChatCompletionMessageToolCall(id='call_NEr40uKvdWEbH2RWd45yGuJv', 
    # function=Function(arguments='{"location": "Tokyo, Japan", "unit": "celsius"}', 
    # name='get_current_weather'), type='function'), 
    # ChatCompletionMessageToolCall(id='call_8n93HByEUIhLd1AQ1cACsAOQ', 
    # function=Function(arguments='{"location": "Paris, France", "unit": "celsius"}', 
    # name='get_current_weather'), type='function')]

    # Step 2: check if the model wanted to call a function
    if tool_calls:
        available_functions = {
            "get_current_weather" : get_current_weather,
        } # only one function in this example, but could be multiple

        messages.append(response_message) # extend conversation with assistant's reply

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location = function_args.get('location'),
                unit = function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id" : tool_call.id,
                    "role" : "tool",
                    "name" : function_name,
                    "content" : function_response
                }
            ) # extend conversation with function response
        
        # print("Second Response: ", list(messages))
        # Second Response:  [{'role': 'user', 'content': "What's the weather like in San Francisco, Tokyo, and Paris?"}, 
        # ChatCompletionMessage(content=None, role='assistant', 
        # function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_4hrGWX5QOhpnwxg95QqsvhZ5', 
        # function=Function(arguments='{"location": "San Francisco", "unit": "celsius"}', 
        # name='get_current_weather'), type='function'), 
        # ChatCompletionMessageToolCall(id='call_WbA2ZjXRXAYss4cmRrzSHC5f', 
        # function=Function(arguments='{"location": "Tokyo", "unit": "celsius"}', 
        # name='get_current_weather'), type='function'), 
        # ChatCompletionMessageToolCall(id='call_7jCMXASvXYvOGfw9YNtLkc9E', 
        # function=Function(arguments='{"location": "Paris", "unit": "celsius"}', 
        # name='get_current_weather'), type='function')]), {'tool_call_id': 
        # 'call_4hrGWX5QOhpnwxg95QqsvhZ5', 'role': 'tool', 'name': 'get_current_weather', 'content': 
        # '{"location": "san francisco", "temprature": "72", "unit": "fahrenheit"}'}, 
        # {'tool_call_id': 'call_WbA2ZjXRXAYss4cmRrzSHC5f', 'role': 'tool', 
        # 'name': 'get_current_weather', 'content': '{"location": "Tokyo", "temprature": "10", 
        # "unit": "celsius"}'}, {'tool_call_id': 'call_7jCMXASvXYvOGfw9YNtLkc9E', 'role': 'tool',
        #  'name': 'get_current_weather', 'content': '{"location": "Paris", "temprature": "22", 
        # "unit": "celsius"}'}]

        final_response : ChatCompletion = client.chat.completions.create(
            messages=messages,
            model= "gpt-3.5-turbo-1106"
        )
        return final_response.choices[0].message.content


result = run_conversation("What's the weather like in San Francisco, Tokyo, and Paris?")
print(result)
# The current weather in San Francisco is 72°F, in Tokyo it's 10°C, and in Paris it's 22°C.

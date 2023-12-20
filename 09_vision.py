from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

response = client.chat.completions.create(
    model= "gpt-4-vision-preview",
    messages=[
        {
            "role" : "user",
            "content" : [
                { "type" : "text", "text" : "What is in this picture ?" },
                {"type" : "image_url",
                "image_url" :{
                                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                }}
            ],

        }
    ],
    max_tokens=300
)

print(response.choices[0])
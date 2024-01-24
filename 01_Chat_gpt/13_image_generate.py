from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import requests
from PIL import Image


_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

file_name:str = "image.png"

response = client.images.generate(
    model= "dall-e-3",
    prompt="Create a newborn baby surrounded by white flowers ",
    size= "1024x1024",
    quality= "standard",
    n=1
)

image_URL : str = response.data[0].url
print("Image URL", image_URL)

# limit exceed :(

res = requests.get(image_URL)

# save image to file    
with open(file_name, 'wb') as f:
    f.write(res.content)

# open image
image: Image = Image.open(file_name)
image.show()
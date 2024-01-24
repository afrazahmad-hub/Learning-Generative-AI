from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()


# different voices (alloy, echo, fable, onyx, nova, and shimmer)
speech_file_path : str = "speech1.mp3"

response = client.audio.speech.create(
    model = "tts-1",
    voice= "alloy",
    input= "Mera naam Afraz Ahmad hai"
    # input= "My name is Afraz Ahmad."
)

print(response.stream_to_file(speech_file_path))
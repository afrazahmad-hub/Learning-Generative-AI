from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()
# The translations API takes as input the audio file in any of the supported languages and transcribes, 
# if necessary, the audio into English. This differs from our /Transcriptions endpoint since the output 
# is not in the original input language and is instead translated to English text.

audio_file = open("tts_Urdu.mp3", "rb")

translation = client.audio.translations.create(
    model= "whisper-1",
    file= audio_file
)

print(translation)
# Translation(text='My name is Afraz Ahmad.')
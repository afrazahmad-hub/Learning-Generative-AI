from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()


# The Audio API provides two speech to text endpoints, transcriptions and translations, 
# based on our state-of-the-art open source large-v2 Whisper model. They can be used to:

# Transcribe audio into whatever language the audio is in.

# Translate and transcribe the audio into english.
# File uploads are currently limited to 25 MB and the following input file types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.


audio_file = open("tts_Urdu.mp3", "rb")

transcript = client.audio.transcriptions.create(
    model= "whisper-1",
    file= audio_file,
    response_format= "text"
)

print(transcript)

# Maranam Afraz Ahmad Hay.
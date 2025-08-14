import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


with open("Recording.mp3", "rb") as audio_file:
    response = openai.Audio.translate(
        model="whisper-1",
        file=audio_file,
        response_format="text",
        language="en"
    )
print(response)

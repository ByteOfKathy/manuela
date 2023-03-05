import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")
openai.api_key = os.getenv("OPENAIAPIKEY")

import moodDetection as md
def responseGenerator(emotion, context) -> str:
    """

    Parameters
    ----------
    emotion
    context

    Returns a response to the given emotion and context
    -------

    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{context}. I am feeling {emotion}. Help them feel good about themselves.",
        max_tokens=200,
    )
    while response["choices"][0]["text"][-1] not in [".", "!", "?"]:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{context}. I am feeling {emotion}. Help them feel good about themselves.",
            max_tokens=200,
        )

    return response["choices"][0]["text"]

if __name__ == "__main__":
    emote = md.detectEmotion("images/nice-man-smiling.jpg")
    print(emote)
    print(responseGenerator(emote, "I am having a great day"))
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


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

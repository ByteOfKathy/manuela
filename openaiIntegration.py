import os
import openai
from dotenv import load_dotenv

load_dotenv("openapi.env")
openai.api_key = os.getenv("OPENAPIKEY")


def responseGenerator(emotion, context) -> str:
    """
    Generates a response based on the emotion and context
    :param emotion: The emotion to generate a response for
    :param context: The context to generate a response for
    :return: The generated response
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

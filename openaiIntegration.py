import os
import openai
from dotenv import load_dotenv

load_dotenv("openAPI.env")

openai.api_key = os.getenv("OPENAIAPIKEY")


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
    return response["choices"][0]["text"]


# create a main
if __name__ == "__main__":
    print(responseGenerator("happy", "What a day I had today."))
    print("\n")
    print(responseGenerator("sad", "What a day I had today."))
    print("\n")
    print(responseGenerator("disgust", "What a day I had today."))
    print("\n")
    print(responseGenerator("neutral", "What a day I had today."))
    print("\n")
    print(responseGenerator("angry", "What a day I had today."))
    print("\n")
    print(responseGenerator("fear", "What a day I had today."))
    print("\n")
    print(responseGenerator("surprise", "What a day I had today."))
    print("\n")

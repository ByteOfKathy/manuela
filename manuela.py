import random
from nltk.parse.dependencygraph import malt_demo
import text2emotion as te
import textRecognizer as tr
import numpy as np
import moodDetection as md
import openaiIntegration as oi


def get_emotion_helper() -> dict:
    """
    Gets the emotion from the user
    :return: the emotion from the user
    """
    tr.tts("Hello! I'm Manuela. What's your name? ")
    name = input()
    tr.tts("Hello " + name + ", how are you feeling today?")

    talk_to_manuela()


def talk_to_manuela():
    """
    Responds to the emotion
    :param emotion: the emotion to respond to
    """

    # Prompt from the user
    userInput = input()
    emotion_weights: dict = te.get_emotion(userInput)
    emotion_weights["neutral"] = 0
    emotion = md.interpret_emotion(emotion_weights).lower()

    tr.tts(
        f"It seems you're mostly feeling {emotion}. Is that correct? Please respond yes or no"
    )

    correct_response = input()
    if correct_response.lower() == "yes":
        if len(md.available_emotions) == 1 and emotion == "neutral":
            tr.tts(
                oi.responseGenerator(emotion, userInput)
            )  # To change later to some custom respone for not understanding the user's emotion
        elif emotion in md.available_emotions:
            tr.tts(oi.responseGenerator(emotion, userInput))
        else:
            tr.tts(
                "I'm sorry, I don't understand that emotion. Could you explain further?"
            )
            talk_to_manuela()
    else:
        tr.tts("I'm sorry, I must have misunderstood. Could you tell me more?")
        if emotion != "neutral":
            md.available_emotions.remove(emotion)
        talk_to_manuela()


get_emotion_helper()

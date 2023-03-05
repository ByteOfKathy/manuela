import random
from nltk.parse.dependencygraph import malt_demo
import text2emotion as te
import textRecognizer as tr
import numpy as np

happyResponses = [
    "That's great! I'm happy for you!",
    "I'm glad you're feeling happy!",
    "I'm glad you're feeling good!",
]
sadResponses = [
    "Keep your chin up, it'll be alright!",
    "I'm sorry to hear that. That must be really upsetting. I'm here for you!",
    "I'm sorry about that. Everything will be alright!",
]
madResponses = [
    "I'm sorry to hear that. That must be frustrating. I'm here for you!",
    "I'm sorry about that. I hope you feel better soon!",
]
fearResponses = [
    "I can see how you feel worried. It's okay, I'm here for you!",
    "I'm sorry to hear that. I hope you feel better soon!",
    "I'm sorry about that. I hope you feel better soon!",
]
surpriseResponses = [
    "Oh, that was unexpected!",
    "Wow, that's surprising!",
    "I'm surprised by that!",
]
disgustResponses = [
    "I'm sorry to hear that. That must have been icky. I'm here for you!",
    "I'm sorry about that. I hope you feel better soon!",
]
neutralResponses = ["Ah, it seems it's a so-so day for you. That's okay!"]


def get_emotion_helper() -> dict:
    tr.tts("Hello! I'm Manuela. What's your name? ")
    name = input()
    tr.tts("Hello " + name + ", how are you feeling today?")
    return te.get_emotion(input())


def interpret_emotion(emotion: dict, a_emotions : set(str)) -> dict:
    """
    Returns the emotion with the highest value
    :param emotion: the emotion dictionary
    :return: the emotion with the highest value
    """

    strongest_emotions = max(emotion[a_emotions], key = emotion[a_emotions].get) # Needs to be replaced with get_strongest_emotion later
    return strongest_emotions if emotion[strongest_emotions] > 0.2 else "Neutral"


def respond_to_emotion(emotion: str, a_emotions : set(str)):
    """
    Responds to the emotion with a (currently) predetermined message
    :param emotion: the emotion to respond to
    :param a_emotions: the available emotions not already disproven
    :return: None

    """

    tr.tts(
        f"It seems you're mostly feeling {emotion}. Is that correct? Please respond yes or no"
    )

    correct_response = input()

    if correct_response.lower() == "yes":
        if emotion == "Happy":
            tr.tts(random.choice(happyResponses))
        elif emotion == "Sad":
            tr.tts(random.choice(sadResponses))
        elif emotion == "Angry":
            tr.tts(random.choice(madResponses))
        elif emotion == "Fear":
            tr.tts(random.choice(fearResponses))
        elif emotion == "Surprise":
            tr.tts(random.choice(surpriseResponses))
        elif emotion == "Disgust":
            tr.tts(random.choice(disgustResponses))
        elif emotion == "Neutral":
            tr.tts(random.choice(neutralResponses))
        else:
            tr.tts(
                "I'm sorry, I don't understand that emotion. Could you explain further?"
            )
            respond_to_emotion(interpret_emotion(te.get_emotion(input()), a_emotions))
    elif correct_response.lower() == "no":
        tr.tts("I'm sorry, I must have misunderstood. Could you tell me more?")
        a_emotions.remove(emotion)
        respond_to_emotion(interpret_emotion(te.get_emotion(input()), a_emotions))


def get_strongest_emotion(t_emotions: dict, i_emotions: dict, a_emotions: set(str)) -> str:
    """
    Gets the strongest emotions from an average of likelihoods from different sources
    :param t_emotions: the emotion likelihoods derived from text input
    :param i_emotions: the emotion likelihoods derived from facial(image) input
    :param a_emotions: the available emotions not already disproven
    :return: the strongest emotion

    """

    norm_emotions = dict()
    for t_emotion, t_value in t_emotions.items():
        norm_emotions[t_emotion] = (t_value + i_emotions[t_emotion]) / 2
    return max(norm_emotions[a_emotions], key = norm_emotions[a_emotions].get)

available_emotions = {"Happy", "Sad", "Angry", "Fear", "Surprise", "Disgust", "Neutral"}
emotion = get_emotion_helper()
respond_to_emotion(interpret_emotion(emotion), available_emotions)

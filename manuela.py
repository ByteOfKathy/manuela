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
neutralResponses = ["Ah, it seems it's a so-so day for you. That's okay!"]
manuelaIsConfused = [
    "I'm sorry, but the emotion you're feeling is not in my databases."
]

global available_emotions
available_emotions = set(["Happy", "Sad", "Angry", "Fear", "Surprise", "Neutral"])


def get_emotion_helper() -> dict:
    tr.tts("Hello! I'm Manuela. What's your name? ")
    name = input()
    tr.tts("Hello " + name + ", how are you feeling today?")
    emotion_weights: dict = te.get_emotion(input())
    emotion_weights["Neutral"] = 0
    return emotion_weights


def interpret_emotion(emotion: dict) -> str:
    """
    Returns the emotion with the highest value
    :param emotion: the emotion dictionary
    :return: the emotion with the highest value
    """

    if "Neutral" not in emotion:
        emotion["Neutral"] = 0.0
    max_emotion = ["Neutral", 0.0]
    for emo in available_emotions:
        if emotion[emo] > max_emotion[1]:
            max_emotion = emo, emotion[emo]

    return max_emotion[0] if max_emotion[1] > 0.2 else "Neutral"


def respond_to_emotion(emotion: str):
    """
    Responds to the emotion with a (currently) predetermined message
    :param emotion: the emotion to respond to
    :param available_emotions: the available emotions not already disproven
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
        elif len(available_emotions) == 1 and emotion == "Neutral":
            tr.tts(random.choice(manuelaIsConfused))
        elif emotion == "Neutral":
            tr.tts(random.choice(neutralResponses))

        else:
            tr.tts(
                "I'm sorry, I don't understand that emotion. Could you explain further?"
            )
            respond_to_emotion(interpret_emotion(te.get_emotion(input())))
    elif correct_response.lower() == "no":
        tr.tts("I'm sorry, I must have misunderstood. Could you tell me more?")
        if emotion != "Neutral":
            available_emotions.remove(emotion)
        respond_to_emotion(interpret_emotion(te.get_emotion(input())))


def get_strongest_emotion(t_emotions: dict, i_emotions: dict) -> str:
    """
    Gets the strongest emotions from an average of likelihoods from different sources
    :param t_emotions: the emotion likelihoods derived from text input
    :param i_emotions: the emotion likelihoods derived from facial(image) input
    :param available_emotions: the available emotions not already disproven
    :return: the strongest emotion

    """

    norm_emotions = dict()
    for t_emotion, t_value in t_emotions.items():
        norm_emotions[t_emotion] = (t_value + i_emotions[t_emotion]) / 2
    return max(
        norm_emotions[available_emotions], key=norm_emotions[available_emotions].get
    )


emotion = get_emotion_helper()
top_emotion = interpret_emotion(emotion)
respond_to_emotion(top_emotion)

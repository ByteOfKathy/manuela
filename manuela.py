import random
from nltk.parse.dependencygraph import malt_demo
import text2emotion as te
import textRecognizer as tr
import numpy as np
import moodDetection as md


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

def get_emotion_helper() -> dict:
    """
    Gets the emotion from the user
    :return: the emotion from the user
    """
    tr.tts("Hello! I'm Manuela. What's your name? ")
    name = input()
    tr.tts("Hello " + name + ", how are you feeling today?")

    userInput = input()
    emotion_weights: dict = te.get_emotion(userInput)
    emotion_weights["Neutral"] = 0
    return emotion_weights



def respond_to_emotion(emotion: str):
    """
    Responds to the emotion
    :param emotion: the emotion to respond to
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
        elif len(md.available_emotions) == 1 and emotion == "Neutral":
            tr.tts(random.choice(manuelaIsConfused))
        elif emotion == "Neutral":
            tr.tts(random.choice(neutralResponses))

        else:
            tr.tts(
                "I'm sorry, I don't understand that emotion. Could you explain further?"
            )
            respond_to_emotion(md.interpret_emotion(te.get_emotion(input())))
    elif correct_response.lower() == "no":
        tr.tts("I'm sorry, I must have misunderstood. Could you tell me more?")
        if emotion != "Neutral":
            md.available_emotions.remove(emotion)
        respond_to_emotion(md.interpret_emotion(te.get_emotion(input())))


emotion = get_emotion_helper()
top_emotion = md.interpret_emotion(emotion)
respond_to_emotion(top_emotion)

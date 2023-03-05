from deepface import DeepFace
import cv2

global available_emotions
available_emotions = set(["happy", "sad", "angry", "fear", "surprise", "neutral"])


def detectEmotion(image: cv2.imread) -> str:
    """
    Detects emotion in image
    parameters
    ----------
    image: image to detect emotion in
    returns
    -------
    emotion
    """

    try:
        emotion = DeepFace.analyze(image, actions=["emotion"])
        return emotion[0]["dominant_emotion"]
    except ValueError as e:
        return "neutral"


def combine_emotions(t_emotions: dict, i_emotions: dict) -> dict:
    """
    Combines the emotions from the text and the image
    :param t_emotions: the emotions from the text
    :param i_emotions: the emotions from the image
    :return: the combined emotions
    """
    for i_emotion, i_value in i_emotions.items():
        i_emotions[i_emotion] = i_value / (1 - i_emotions["disgust"])

    del i_emotions["disgust"]

    norm_emotions = dict()
    for t_emotion, t_value in t_emotions.items():
        norm_emotions[t_emotion] = (t_value + i_emotions[t_emotion]) / 2

    return norm_emotions


def interpret_emotion(emotion: dict) -> str:
    """
    Interprets the emotion
    :param emotion: the emotion to interpret
    :return: the emotion that is the strongest
    """
    if "neutral" not in emotion:
        emotion["neutral"] = 0.0
    max_emotion = ["neutral", 0.0]

    lowercase_emotion: dict = {}
    for e in emotion:
        lowercase_emotion[e.lower()] = emotion[e]

    emotion = lowercase_emotion
    for emo in available_emotions:
        if emotion[emo] > max_emotion[1]:
            max_emotion = emo, emotion[emo]

    return max_emotion[0] if max_emotion[1] > 0.2 else "neutral"

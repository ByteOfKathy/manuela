from deepface import DeepFace
import videoDetection as vd
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


def combine_emotions(t_emotions: dict, i_emotion: str) -> dict:
    """
    Combines the emotions from the text and the image
    :param t_emotions: the emotions from the text
    :param i_emotions: the emotions from the image
    :return: the combined emotions
    """

    t_emotions[i_emotion] += 0.7

    return t_emotions


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

    image_emotions = vd.getEmotion()
    emotion = combine_emotions(emotion, image_emotions)

    return max_emotion[0] if max_emotion[1] > 0.2 else "neutral"

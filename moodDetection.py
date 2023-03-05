from deepface import DeepFace
import cv2

global available_emotions
available_emotions = set(["Happy", "Sad", "Angry", "Fear", "Surprise", "Neutral"])


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
        i_emotions[i_emotion] = i_value / (1 - i_emotions["Disgust"])

    del i_emotions["Disgust"]

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
    if "Neutral" not in emotion:
        emotion["Neutral"] = 0.0
    max_emotion = ["Neutral", 0.0]
    for emo in available_emotions:
        if emotion[emo] > max_emotion[1]:
            max_emotion = emo, emotion[emo]

    return max_emotion[0] if max_emotion[1] > 0.2 else "Neutral"

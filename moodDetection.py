from deepface import DeepFace
import cv2


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
    emotion = DeepFace.analyze(image, actions=['emotion'])
    return emotion[0]['dominant_emotion']

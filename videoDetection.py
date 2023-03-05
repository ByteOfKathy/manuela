import time
import cv2
import moodDetection as md


def startVideo():
    """
    Starts video capture
    """
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame


def getEmotion() -> str:
    """
    Gets emotion from video
    """
    frame = startVideo()
    emotion = md.detectEmotion(frame)
    return emotion

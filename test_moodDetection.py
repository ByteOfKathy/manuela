import pytest
import moodDetection as md
import cv2


def test_moodDetection():
    """
    Returns True if the emotion detected in image is happy
    """
    testImg = cv2.imread("images/nice-man-smiling.jpg")
    assert md.detectEmotion(testImg) == "happy"


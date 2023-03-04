import pytest
import moodDetection as md
import cv2


def test_moodDetection():
    """
    Returns True if the emotion detected in image is happy
    """
    test_img = cv2.imread("images/nice-man-smiling.jpg")
    assert md.detectEmotion(test_img) == "happy"

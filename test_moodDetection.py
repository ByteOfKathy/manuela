import pytest
import moodDetection as md
import cv2


def test_moodDetection():
    """
    Returns True if there is at least 1 smile detected in image
    """
    testImg = cv2.imread("images/nice-man-smiling.jpg")
    assert md.detectSmile(testImg) is not None

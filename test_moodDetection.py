import pytest
import moodDetection as md
import cv2


def test_moodDetection():
    testImg = cv2.imread("images/nice-man-smiling.jpg")
    assert md.detectSmile(testImg) is not None

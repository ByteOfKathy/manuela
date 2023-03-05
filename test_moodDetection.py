import pytest
import cv2


# only run this locally or it will fail GHA
try:
    import moodDetection as md
except ImportError:
    pass


@pytest.mark.skipif("md" not in globals(), reason="moodDetection not imported")
def test_moodDetection():
    """
    Returns True if the emotion detected in image is happy
    """
    test_img = cv2.imread("images/nice-man-smiling.jpg")
    assert md.detectEmotion(test_img) == "happy"

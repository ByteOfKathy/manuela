import textRecognizer
import pytest


def test_tts():
    """
    test tts function
    """
    debug = True
    assert textRecognizer.tts("test", debug) == True

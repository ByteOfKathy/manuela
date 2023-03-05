import pytest
import cv2
import openaiIntegration as oi


def test_openaiIntegration():
    """
    test openai integration
    """
    response = oi.responseGenerator("happy", "I had a great day at school today!")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("sad", "I got bullied today by my coworkers.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("disgust", "I cannot believe what she did on TV.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("neutral", "How are you doing today?")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator(
        "angry", "I hate my boss he is so annoying. He took away my PHONE."
    )
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("fear", "I am so scared of the dark.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator(
        "surprise", "Oh my god! I cannot believe what I just saw!"
    )
    assert response[-1] in [".", "!", "?"]

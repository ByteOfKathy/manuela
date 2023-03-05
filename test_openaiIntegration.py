import pytest
import cv2
import openaiIntegration as oi


def test_openaiIntegration():
    """
    test openai integration
    """
    response = oi.responseGenerator("happy", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("sad", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("disgust", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("neutral", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("angry", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("fear", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]
    response = oi.responseGenerator("surprise", "What a day I had today.")
    assert response[-1] in [".", "!", "?"]

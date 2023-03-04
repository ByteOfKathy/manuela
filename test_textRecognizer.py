import textRecognizer
import pytest


def test_OfferSuggestions():
    """
    test all different moods
    """

    # testing happy mood
    assert (
        textRecognizer.offerSuggestion(textRecognizer.Mood.HAPPY)
        in textRecognizer.happySuggestions
    )
    # testing sad mood
    assert (
        textRecognizer.offerSuggestion(textRecognizer.Mood.SAD)
        in textRecognizer.sadSuggestions
    )
    # testing angry mood
    assert (
        textRecognizer.offerSuggestion(textRecognizer.Mood.ANGRY)
        in textRecognizer.angrySuggestions
    )
    # testing neutral mood
    assert (
        textRecognizer.offerSuggestion(textRecognizer.Mood.NEUTRAL)
        in textRecognizer.neutralSuggestions
    )
    # testing unrecognized mood
    assert (
        textRecognizer.offerSuggestion("test")
        == "Uh oh, this is a new one! Unrecognized mood!"
    )


def test_tts():
    """
    test tts function
    """
    assert textRecognizer.tts("test") == True

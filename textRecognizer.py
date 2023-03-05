from enum import Enum

# imports related to output
import random
import playsound
from gtts import gTTS
import os

# imports related to input
import speech_recognition as sr


class Mood(Enum):
    HAPPY = 1
    SAD = 2
    ANGRY = 3
    NEUTRAL = 4


happySuggestions = ["Keep it up!", "Keep smiling!"]
sadSuggestions = ["Try to cheer up!", "Turn that frown upside down!"]
angrySuggestions = ["Try to calm down!", "Something bothering you?"]
neutralSuggestions = ["Try to smile more!", "What would make you happy?"]

# functions related to output


def tts(text: str, debug=False) -> bool:
    """
    Converts text to speech
    parameters
    ----------
    text: text to convert to speech
    debug: if true, prints text instead of speaking it (still tries to make speech file, but won't play it)
    returns
    -------
    True if successful, False otherwise
    """

    try:
        # convert text to speech
        speech = gTTS(text=text, lang="en", slow=False)
        speech.save("manuelaOut.mp3")
        os.chmod("manuelaOut.mp3", 0o777)

        # play speech if not silenced
        # os check for windows
        if not debug:
            if os.name.lower() == "nt":
                playsound.playsound("manuelaOut.mp3")
            else:
                # use aplay for linux
                os.system("aplay manuelaOut.mp3")
        else:
            print(text)

        os.remove("manuelaOut.mp3")
        return True
    except Exception as e:
        print(str(e))
        return False


# functions related to input


def recognizeSpeech(debug=False) -> str | None:
    """
    Recognizes speech
    parameters
    ----------
    debug: if true, prints recognized speech and what Google thinks you said
    returns
    -------
    recognized speech
    """
    # initialize recognizer
    r = sr.Recognizer()
    # open microphone
    with sr.Microphone() as source:
        tts("Hang on, I'm adjusting for ambient noise")
        r.adjust_for_ambient_noise(source, duration=1)
        tts("Ok, now I'm listening")
        # TODO: adjust listening parameters
        audio = r.listen(source, phrase_time_limit=10)
    # recognize speech
    try:
        txt = r.recognize_google(audio)
        if debug:
            tts("Google Speech Recognition thinks you said:")
            tts(txt)
        return txt
    except sr.UnknownValueError:
        tts("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
        return None


if __name__ == "__main__":
    # output tests

    # tts("Starting mood tests")

    # tts("Testing happy mood")
    # tts(offerSuggestion(Mood.HAPPY))

    # tts("Testing sad mood")
    # tts(offerSuggestion(Mood.SAD))

    # tts("Testing angry mood")
    # tts(offerSuggestion(Mood.ANGRY))

    # tts("Testing neutral mood")
    # tts(offerSuggestion(Mood.NEUTRAL))

    # tts("Testing unrecognized mood")
    # tts(offerSuggestion("test"))

    # input tests
    debug = True
    tts("Starting speech recognition tests in debug mode")
    recognizeSpeech(debug)

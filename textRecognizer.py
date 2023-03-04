from enum import Enum
import random
import playsound
from gtts import gTTS
import os


class Mood(Enum):
    HAPPY = 1
    SAD = 2
    ANGRY = 3
    NEUTRAL = 4


happySuggestions = ["Keep it up!", "Keep smiling!"]
sadSuggestions = ["Try to cheer up!", "Turn that frown upside down!"]
angrySuggestions = ["Try to calm down!", "Something bothering you?"]
neutralSuggestions = ["Try to smile more!", "What would make you happy?"]


def offerSuggestion(mood: Mood) -> str:
    """
    Returns a suggestion based on mood
    parameters
    ----------
    mood: mood to offer suggestion for
    returns
    -------
    suggestion
    """
    # case of moods
    if mood == Mood.HAPPY:
        return random.choice(happySuggestions)
    elif mood == Mood.SAD:
        return random.choice(sadSuggestions)
    elif mood == Mood.ANGRY:
        return random.choice(angrySuggestions)
    elif mood == Mood.NEUTRAL:
        return random.choice(neutralSuggestions)
    else:
        return "Uh oh, this is a new one! Unrecognized mood!"


def tts(text: str) -> bool:
    """
    Converts text to speech
    parameters
    ----------
    text: text to convert to speech
    returns
    -------
    True if successful, False otherwise
    """

    try:
        # convert text to speech
        speech = gTTS(text=text, lang="en", slow=False)
        speech.save("manuelaOut.mp3")
        os.chmod("manuelaOut.mp3", 0o777)

        # play speech
        # os check for windows
        if os.name.lower() == "nt":
            playsound.playsound("manuelaOut.mp3")
        else:
            # use aplay for linux
            os.system("aplay manuelaOut.mp3")

        os.remove("manuelaOut.mp3")
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == "__main__":
    tts("Starting mood tests")

    tts("Testing happy mood")
    tts(offerSuggestion(Mood.HAPPY))

    tts("Testing sad mood")
    tts(offerSuggestion(Mood.SAD))

    tts("Testing angry mood")
    tts(offerSuggestion(Mood.ANGRY))

    tts("Testing neutral mood")
    tts(offerSuggestion(Mood.NEUTRAL))

    tts("Testing unrecognized mood")
    tts(offerSuggestion("test"))

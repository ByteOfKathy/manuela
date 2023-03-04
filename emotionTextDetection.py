import text2emotion as te

def get_emotion_helper() -> dict:
    name = input("Hello! I'm Manuela. What's your name? \n")
    return get_emotion(input("Hello " + name + ", how are you feeling today? \n"))


def get_emotion(text: str) -> dict:
    """
    Returns a dictionary with the emotion and its value as a percentage 0.0-1.0
    :param text: the text to analyze
    :return: a dictionary with the emotion and its value

    Example:
    >>> get_emotion("I am happy")
    """
    return te.get_emotion(text)

def interpret_emotion(emotion: dict) -> dict:
    strongest_emotions = max(emotion, key=emotion.get)
    return strongest_emotions

def respond_to_emotion(emotion: str): 
    correct_response = input("It seems you're mostly feeling " + emotion + ". Is that correct? (Y/N) \n")

    if correct_response == "Y":
        if emotion == "Happy":
            print("That's great! I'm happy for you!")
        elif emotion == "Sad":
            print("I'm sorry to hear that. That must be really upsetting. I'm here for you!")
        elif emotion == "Angry":
            print("I'm sorry to hear that. That must be frustrating. I'm here for you!")
        elif emotion == "Fear":
            print("I can see how you feel worried. It's okay, I'm here for you!")
        elif emotion == "Surprise":
            print("Oh, that was unexpected! what do you think about that? \n")
            respond_to_emotion(interpret_emotion(get_emotion(input())))
        elif emotion == "Disgust":
            print("I'm sorry to hear that. That must have been icky. I'm here for you!")
        elif emotion == "Neutral":
            print("Ah, it seems it's a so-so day for you. That's okay!")
        else:
            print("I'm sorry, I don't understand that emotion. Could you explain further? \n")
            respond_to_emotion(interpret_emotion(get_emotion(input())))
    else: 
        respond_to_emotion(interpret_emotion(get_emotion(input("Hmm, I'm sorry, could you explain further? \n"))))
        
    


emotion = get_emotion_helper()
respond_to_emotion(interpret_emotion(emotion))
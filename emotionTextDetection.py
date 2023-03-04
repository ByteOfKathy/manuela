import text2emotion as te

def get_emotion(text: str)-> dict:
    """
    Returns a dictionary with the emotion and its value as a percentage 0.0-1.0
    :param text: the text to analyze
    :return: a dictionary with the emotion and its value

    Example:
    >>> get_emotion("I am happy")
    """
    return te.get_emotion(text)



import openai


# get your API key from https://beta.openai.com/account/api-keys
def responseGenerator(emotion, context):
    response = openai.Completion.create(
        engine="davinci",
        # create a prompt that responds to someone with a given emotion and context
        prompt="Given someone is "
        + emotion
        + " and "
        + context
        + " what would you say to them to make them feel good?",
    )
    return response

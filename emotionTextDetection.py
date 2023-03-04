import text2emotion as te

# Text input
text = "Hello, my name is John. I am very happy to be here! I am so excited to learn about text2emotion. I am so happy!"
# Detect emotion
emotion = te.get_emotion(text)

print(emotion)


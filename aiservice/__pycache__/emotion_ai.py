import cv2
import numpy as np

emotion_labels = ["Angry","Happy","Neutral","Sad","Surprise"]

def detect_emotion(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    resized = cv2.resize(gray,(48,48))

    img = resized / 255.0

    img = np.reshape(img,(1,48,48,1))

    # fake prediction (random)
    prediction = np.random.randint(0,5)

    emotion = emotion_labels[prediction]

    return emotion
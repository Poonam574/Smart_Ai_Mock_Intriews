import speech_recognition as sr

def record_answer():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Speak your answer...")

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text

    except:
        return "Not understood"
import speech_recognition as sr
r=sr.Recognizer()
#give your audio file as input in .wav format
file=input()
with sr.AudioFile(file) as source:
    audio=r.record(source)
    try:
        text=r.recognize_google(audio)
        print("you said {}".format(text))
    except sr.UnknownValueError:
        print("couldn't recognize")

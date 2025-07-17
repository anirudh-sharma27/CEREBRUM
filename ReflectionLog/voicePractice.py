import speech_recognition as sr



#absolute shit recognition


r = sr.Recognizer()
with sr.Microphone() as source:
    print("🎙️ Speak now...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print(" Couldn't understand")

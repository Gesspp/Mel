import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('rate', 170)  # Скорость речи
    engine.setProperty('volume', 1)  # Громкость (от 0.0 до 1.0)
    engine.setProperty('voice', voice.id)
    engine.say("otkrivayu brauzer")
    engine.runAndWait()
    engine.stop()
import speech_recognition as sr
import time
import pyaudio

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)


print('Start: ')

while True:
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = r.record(source, duration=2)
            print("Recognizing your text.............")
            text = r.recognize_google(audio_data)
            print(text)
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")

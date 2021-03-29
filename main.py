import speech_recognition as sr
import wikipedia


r = sr.Recognizer()
mic = sr.Microphone(device_index=2)


print('Start: ')

while True:
    with sr.Microphone() as source:
        try:
            audio_data = r.record(source, duration=3)
            print("Recognizing your text...")
            text = r.recognize_google(audio_data)
            print(text.split())
            if text.split()[0] == 'Legion':
                print("Yes?")
                audio = r.record(source, duration=3)
                command = r.recognize_google(audio)
                print(command)
                if 'wikipedia' in command.lower():
                    command = command.replace("wikipedia", "")
                    print(command)
                    results = wikipedia.summary(command, sentences=3)
                    print("According to Wikipedia")
                    print(results)
            print(text)
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")

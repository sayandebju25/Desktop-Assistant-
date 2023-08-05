import os
import sys

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold=0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, there was an issue with the speech recognition service."
        except Exception as e:
            return "Sorry, some error occurred. Please try again."
if __name__ == '__main__':
    print('pycharm')
    say("Hello, I am Jarvis AI. How can I help you?")

    while True:
        print("Listening....")
        query = takeCommand()
        sites = [['youtube', "https://youtube.com"], ['wikipedia', "https://wikipedia.com"],
                 ['google', "https://google.com"]]
        if any(site[0] in query.lower() for site in sites):
            for site in sites:
                if site[0] in query.lower():
                    say(f"Opening {site[0]}...")
                    webbrowser.open(site[1])

            if "open music" in query:
                musicPath=" D:\song"
                os.system(f"open {musicPath}")
            if "the time" in query:
                strftime=datetime.datetime.now().strftime("%H:%M:%S ")
                say(f"sir the time is {strftime}")
 
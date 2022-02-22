import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am David. How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising..")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say it again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('faizankalam567@gmail.com','password')
    server.sendmail('faizankalam567@gmail.com',to, content)
    server.close()

if __name__ == '__main__':
    # speak("Faizan")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            # results = wikipedia.summary(query,auto_suggest=True)
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'search' in query:
            # search = query.rsplit("search ")
            search = query.replace(" ", "+")
            url = f"https://www.google.com.tr/search?q={search}"
            webbrowser.open_new(url)
        elif 'play music' in query:
            music_dir = "D:\\Faizan\\MP3"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is{strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\kalam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open brave' in query:
            bravePath ="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravePath)
        elif 'email to faizan' in query:
            try:
                speak("What should the content be?")
                content = takeCommand()
                to = "faizankalam24@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak(f"Exception occured {e}")
        elif 'quit' in query:
            exit()
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening (voice)...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Voice: {query}")
        return query
    except:
        print("Could not understand voice. Try typing instead.")
        return None

def takeInput():
    print("\nSpeak OR Type your command:")
    text = input("Type here (or press Enter to use voice): ").strip()

    if text != "":
        print(f"Text: {text}")
        return text.lower()
    else:
        return takeVoiceCommand()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. You can talk to me or type commands.")

def getDate():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")
    print(today)

def tellJoke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the computer get cold? Because it forgot to close its windows.",
        "I told my computer I needed a break. It said no problem, it froze."
    ]
    joke = random.choice(jokes)
    speak(joke)
    print(joke)

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeInput()

        if query is None:
            continue
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com")

        elif 'search' in query:
            speak("What should I search for?")
            search_query = takeInput()
            if search_query:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow")
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query or 'open music' in query:
            speak("Opening YouTube Music")
            webbrowser.open("https://music.youtube.com/")

        elif 'time' in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The current time is {now}")
            speak(f"The current time is {now}")

        elif 'date' in query:
            getDate()

        elif 'open code' in query:
            codePath = "C:\\Users\\Lekana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")

        elif 'write note' in query or 'make a note' in query:
            speak("What should I write?")
            note = takeInput()
            if note:
                with open("notes.txt", "a") as f:
                    f.write(note + "\n")
                speak("Note saved")

        elif 'read note' in query or 'read notes' in query:
            if os.path.exists("notes.txt"):
                with open("notes.txt", "r") as f:
                    notes = f.read()
                print(notes)
                speak("Here are your notes")
                speak(notes)
            else:
                speak("No notes found")

        elif 'joke' in query:
            tellJoke()

        elif 'shutdown' in query:
            speak("Are you sure you want to shut down?")
            confirm = takeInput()
            if confirm and 'yes' in confirm:
                os.system("shutdown /s /t 5")

        elif 'restart' in query:
            speak("Are you sure you want to restart?")
            confirm = takeInput()
            if confirm and 'yes' in confirm:
                os.system("shutdown /r /t 5")

        elif 'stop' in query or 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Thank you for using me. Goodbye!")
            print("Jarvis stopped.")
            break

        else:
            print("No command matched.")

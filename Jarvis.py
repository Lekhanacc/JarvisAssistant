import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

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

        elif 'open code' in query:
            codePath = "C:\\Users\\Lekana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")

        elif 'stop' in query or 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Thank you for using me. Goodbye!")
            print("Jarvis stopped.")
            break

        else:
            print("No command matched.")

   
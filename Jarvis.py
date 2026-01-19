import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes

# ---------------- SETUP ----------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ---------------- GREETING ----------------

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning Lekhs!")
    elif hour < 18:
        speak("Good Afternoon Lekhs!")
    else:
        speak("Good Evening Lekhs!")
    speak("I am Jarvis. How can I help you?")

# ---------------- INPUT METHODS ----------------

def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except:
        speak("Say that again please...")
        return "none"
    return query.lower()

def takeTextCommand():
    return input("Type your command: ").lower()

def chooseInputMode():
    speak("Do you want to speak or type?")
    print("Choose input mode: voice / text")
    mode = input("Enter mode (voice/text): ").lower()
    return mode

# ---------------- FEATURES ----------------

def playMusic():
    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'  # change path if needed
    if not os.path.exists(music_dir):
        speak("Music directory not found")
        return
    songs = os.listdir(music_dir)
    song = random.choice(songs)
    os.startfile(os.path.join(music_dir, song))

def tellTime():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")

def tellDate():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {date}")

def takeNote(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    speak("I have saved your note")

# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    wishMe()
    mode = chooseInputMode()

    while True:
        if mode == "voice":
            query = takeVoiceCommand()
        else:
            query = takeTextCommand()

        if query == "none":
            continue

        # ---------------- COMMAND HANDLING ----------------

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except:
                speak("Could not find results")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'search google for' in query:
            query = query.replace("search google for", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'play music' in query:
            playMusic()

        elif 'time' in query:
            tellTime()

        elif 'date' in query:
            tellDate()

        elif 'take note' in query:
            speak("What should I write?")
            note = takeVoiceCommand() if mode == "voice" else takeTextCommand()
            takeNote(note)

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'switch mode' in query:
            speak("Switching input mode")
            mode = chooseInputMode()

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye Lekhs!")
            break

        else:
            speak("Sorry, I did not understand that.")


import speech_recognition as sr
import pyttsx3
import datetime , webbrowser

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognising...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def respond(query):
    if "hello" in query:
        speak("Hello! How may I help you right now ?")
    elif "time" in query:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time_now}")
    elif "date" in query:
        date_today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {date_today}")
    elif "search" in query:
        search_query = query.replace("search", "").strip()
        if search_query:
            speak(f"Looking up {search_query} on the internet")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("What would you like me to search for?")
    else:
        speak("I am sorry, I cannot do that yet.")



RUN_AS_SCRIPT = True  

def main():
    speak("Voice Assistant initialized. How can I help you?")
    while True:
        command = listen()
        if command:
            respond(command)
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

if RUN_AS_SCRIPT:
    main()

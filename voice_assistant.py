import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize TTS engine and speech recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    """Convert text to speech."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input and convert to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def open_application(app_name):
    """Launch desktop applications by name."""
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",  # update if path differs
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    }

    if app_name in apps:
        try:
            os.startfile(apps[app_name])
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Sorry, I couldn’t open {app_name}. Please check the path.")
            print(e)
    else:
        speak("I don't know how to open that application yet.")

def respond(query):
    """Process voice commands and respond accordingly."""
    if "hello" in query:
        speak("Hello! How may I help you right now?")
    
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
    
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        open_application(app_name)
    
    elif "exit" in query or "quit" in query or "stop" in query:
        speak("Goodbye! Have a nice day.")
        return False
    
    else:
        speak("I am sorry, I cannot do that yet.")
    
    return True

def main():
    """Main loop for the assistant."""
    speak("Voice Assistant initialized. How can I help you?")
    while True:
        command = listen()
        if command:
            if not respond(command):
                break

if __name__ == "__main__":
    main()

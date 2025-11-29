# jarvis_api.py
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def handle_command(cmd):
    cmd = cmd.lower()

    if "time" in cmd:
        time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {time}"

    elif "joke" in cmd:
        return pyjokes.get_joke()

    elif "play" in cmd:
        song = cmd.replace("play", "").strip()
        url = f"https://www.youtube.com/results?search_query={song}"
        webbrowser.open(url)
        return f"Playing {song} on YouTube"

    elif "who is" in cmd:
        person = cmd.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            return info
        except:
            return "Sorry, I couldn't find information."

    return "I didn't understand that command."

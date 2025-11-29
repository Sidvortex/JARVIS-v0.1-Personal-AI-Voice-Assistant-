# jarvis_basic.py
# Siddharth Ravada — Jarvis v0.1 (refined, robust)
# IMPORTANT: Do NOT name this file "code.py" (it shadows the stdlib 'code' module)

import os
import sys
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyttsx3
import logging
from urllib.parse import quote as urlquote

# --- optional speech deps, detected at runtime ---
_SR_AVAILABLE = False
_PYAUDIO_AVAILABLE = False
try:
    import speech_recognition as sr  # type: ignore
    _SR_AVAILABLE = True
    try:
        import pyaudio  # type: ignore
        _PYAUDIO_AVAILABLE = True
    except Exception:
        _PYAUDIO_AVAILABLE = False
except Exception:
    _SR_AVAILABLE = False
    _PYAUDIO_AVAILABLE = False

# --- logging (helps debugging) ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("jarvis")

# --- TTS setup ---
try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)  # prefer a female voice if present
    engine.setProperty("rate", 170)
except Exception as e:
    engine = None
    log.warning("pyttsx3 init failed: %s", e)

def talk(text: str, speak: bool = True):
    """Print + speak. Safe if TTS failed to init."""
    msg = str(text)
    print("JARVIS:", msg)
    if speak and engine is not None:
        try:
            engine.say(msg)
            engine.runAndWait()
        except Exception as e:
            log.warning("TTS error: %s", e)

# --- input handling ---
def keyboard_input(prompt: str = "Type command (or press Enter to use mic): ") -> str:
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        return "stop"

def listen(timeout: float = 5.0, phrase_time_limit: float = 6.0) -> str:
    """
    Prefer microphone if available, otherwise keyboard fallback.
    Returns lowercase command ('' when nothing recognized).
    """
    # If speech_recognition or PyAudio missing -> fallback immediately
    if not _SR_AVAILABLE or not _PYAUDIO_AVAILABLE:
        return keyboard_input().lower()

    # microphone path
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎧 Listening... (say 'jarvis' optionally)")
            r.pause_threshold = 0.8
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        try:
            cmd = r.recognize_google(audio)  # type: ignore
            cmd = cmd.lower().strip()
            # optional wake-word handling
            if "jarvis" in cmd:
                cmd = cmd.replace("jarvis", "").strip()
            return cmd
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            talk("Speech recognition network error. Using keyboard input.")
            return keyboard_input().lower()
    except Exception as e:
        log.warning("Microphone error: %s", e)
        return keyboard_input().lower()

# --- core helpers ---
MEM_FILE = "jarvis_memory.txt"

def save_memory(text: str):
    if not text:
        talk("Nothing to remember.")
        return
    try:
        os.makedirs(os.path.dirname(MEM_FILE) or ".", exist_ok=True)
        with open(MEM_FILE, "a", encoding="utf-8") as f:
            f.write(text.strip() + "\n")
        talk("Saved to memory.")
    except Exception as e:
        talk("Failed to save memory.")
        log.exception(e)

def read_memory():
    if not os.path.exists(MEM_FILE):
        talk("No memories found.")
        return
    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()
        if data:
            talk("You asked me to remember:")
            talk(data)
        else:
            talk("Memory file is empty.")
    except Exception as e:
        talk("Could not read memory.")
        log.exception(e)

def open_youtube_search(query: str):
    if not query:
        talk("What should I play?")
        return
    url = "https://www.youtube.com/results?search_query=" + urlquote(query)
    webbrowser.open(url)
    talk(f"Opened YouTube results for {query}")

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    talk("The current time is " + now)

def wiki_lookup(subject: str):
    if not subject:
        talk("Who should I search for?")
        return
    try:
        summary = wikipedia.summary(subject, sentences=1, auto_suggest=True, redirect=True)
        talk(summary)
    except wikipedia.DisambiguationError:
        talk("There are multiple results — be more specific.")
    except wikipedia.PageError:
        talk("No page found for that subject.")
    except Exception as e:
        talk("Wikipedia lookup failed.")
        log.exception(e)

# --- main function loop ---
def run_jarvis():
    talk("Initializing systems... (keyboard fallback available).")
    if not _SR_AVAILABLE:
        talk("SpeechRecognition package not installed. Using keyboard input.")
    elif not _PYAUDIO_AVAILABLE:
        talk("PyAudio not available. Install PyAudio for mic support or use keyboard input.")

    while True:
        command = listen()
        if not command:
            continue
        print("You said:", command)

        # Basic commands (trim and match)
        cmd = command.strip()

        if cmd.startswith("play "):
            open_youtube_search(cmd.replace("play", "", 1).strip())

        elif cmd == "play":
            talk("Say or type the song name.")
            q = listen()
            open_youtube_search(q)

        elif "time" in cmd:
            tell_time()

        elif cmd.startswith("who is ") or cmd.startswith("who's "):
            subj = cmd.split(" ", 2)[-1].strip()
            wiki_lookup(subj)

        elif "joke" in cmd:
            talk(pyjokes.get_joke())

        elif cmd.startswith("remember "):
            note = cmd.replace("remember", "", 1).strip()
            save_memory(note)

        elif "what did you remember" in cmd or "read memory" in cmd or "recall" in cmd:
            read_memory()

        elif cmd.startswith("open "):
            target = cmd.replace("open", "", 1).strip().lower()
            mapping = {
                "google": "https://www.google.com",
                "youtube": "https://www.youtube.com",
                "github": "https://github.com",
                "stackoverflow": "https://stackoverflow.com",
            }
            url = mapping.get(target) or ("https://www.google.com/search?q=" + urlquote(target))
            webbrowser.open(url)
            talk(f"Opening {target}")

        elif cmd in ("stop", "sleep", "exit", "quit"):
            talk("Going offline. Goodbye, sir.")
            break

        else:
            talk("Command not recognized. Try: play, time, who is, joke, remember, read memory, open, stop.")

if __name__ == "__main__":
    # protect against earlier 'code.py' issue
    if os.path.basename(__file__).lower() == "code.py":
        print("Rename this file — do NOT use the filename 'code.py'. Use 'jarvis_basic.py' instead.")
        sys.exit(1)
    try:
        run_jarvis()
    except KeyboardInterrupt:
        talk("Shutting down. Goodbye, sir.")
        # attempt a clean engine stop if possible
        try:
            if engine is not None:
                engine.stop()
        except Exception:
            pass
        sys.exit(0)

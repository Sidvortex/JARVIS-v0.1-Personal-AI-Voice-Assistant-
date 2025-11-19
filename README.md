
👥 Developers

Siddharth Ravada
Creator & Lead Developer
GitHub: https://github.com/sidvortex

Ishan Gupta
Collaborator
github: https://github.com/IshanGupta-Code


🚀 Features

✔ Speech-to-text (with fallback to keyboard if mic fails)

✔ Text-to-speech with pyttsx3

✔ Tell time

✔ Wikipedia summaries

✔ Play/search songs on YouTube (browser-based, no pywhatkit)

✔ Tell jokes

✔ Memory storage & recall (jarvis_memory.txt)

✔ Open common websites

✔ Clean error handling & logging

✔ Fully functional even without PyAudio or microphone

✔ Safe from Python filename conflicts (e.g., code.py issue)



📁 Project Structure

JARVIS-v0.1/
│

├── jarvis_basic.py          #Main JARVIS script (do NOT name this code.py)

├── requirements.txt         #Dependencies (minimal)

├── jarvis_memory.txt        #Created automatically — stores 'remember' notes

├── README.md                #Project documentation

│
├── .venv/                   #Virtual environment (ignored by Git)

│
└── assets/                  #Optional future folder for images/sounds/etc.


🛠️ Installation Guide (Windows)

1. Clone the Repository
git clone https://github.com/sidvortex/JARVIS-v0.1-Personal-AI-Voice-Assistant-.git
cd JARVIS-v0.1-Personal-AI-Voice-Assistant

2. Create a Virtual Environment
python -m venv .venv

3. Activate the Virtual Environment
Command Prompt
.\.venv\Scripts\activate.bat

PowerShell

If scripts are blocked:

powershell -ExecutionPolicy Bypass -File .\.venv\Scripts\Activate.ps1


Or permanently allow local scripts:

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force

4. Install Required Packages
pip install --upgrade pip
pip install -r requirements.txt

5. (Optional) Enable Microphone Support

Full mic support requires PyAudio.

⚠ Note: PyAudio does not install smoothly on Python 3.13.
Recommended → Use Python 3.11 for full speech recognition.

If using Python 3.11, you can run:

pip install pipwin
pipwin install pyaudio


If you stay on Python 3.13, the assistant will still work, but using keyboard input instead of mic.

6. Run JARVIS
python jarvis_basic.py

🧩 Commands You Can Use
Command	Action

play <song>	Opens YouTube search results for the song

time	Tells current time

who is <person>	Reads 1-line Wikipedia summary

joke	Tells a joke

remember <something>	Saves memory

what did you remember	Reads memory

open google / youtube / github / stackoverflow	Opens websites

stop / sleep / quit	Shuts down assistant


If microphone isn’t available, JARVIS will automatically ask you to type commands.


⚠️ Troubleshooting
1. Script Errors Involving code.py

If you see:

AttributeError: module 'code' has no attribute 'InteractiveConsole'


You named your file code.py.
→ Rename it to jarvis_basic.py.

Then remove cache:

rmdir /s /q __pycache__

2. PyAudio Not Found

If you see:

Could not find PyAudio; check installation


Microphone won’t work — use keyboard fallback OR install PyAudio (Python 3.11 recommended).

3. pipwin / js2py bytecode error

Happens only on Python 3.13:

RuntimeError: Your python version made changes to the bytecode


Solution → Use Python 3.11 virtual environment.

🔮 Future Improvements (Roadmap)

Add wake-word (“Jarvis”) hotword detection

Add AI-powered natural language model (offline or API-based)

Add system control features (open apps, music control, brightness, etc.)

Add GUI dashboard

Add custom “skills” architecture


🤝 Contributing

Pull requests are welcome.
Feel free to improve features, add modules, or polish the code!


📜 License

MIT License — you can modify, distribute, and use freely.

<div align="center">

# 🤖 JARVIS v0.1

### Personal AI Voice Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

*A lightweight, fully functional voice assistant with speech recognition, text-to-speech, and smart command handling — works even without a microphone!*

[Features](#-features) •
[Installation](#%EF%B8%8F-installation-guide-windows) •
[Commands](#-commands-you-can-use) •
[Troubleshooting](#%EF%B8%8F-troubleshooting) •
[Roadmap](#-future-roadmap)

---

<img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="200" alt="JARVIS Animation">

*"At your service."*

</div>

---

## 👥 Developers

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/sidvortex">
        <img src="https://github.com/sidvortex.png" width="100px;" alt="Siddharth Ravada"/><br />
        <sub><b>Siddharth Ravada</b></sub>
      </a>
      <br />
      <sub>Creator & Lead Developer</sub>
    </td>
    <td align="center">
      <a href="https://github.com/IshanGupta-Code">
        <img src="https://github.com/IshanGupta-Code.png" width="100px;" alt="Ishan Gupta"/><br />
        <sub><b>Ishan Gupta</b></sub>
      </a>
      <br />
      <sub>Collaborator</sub>
    </td>
  </tr>
</table>

---

## 📖 Overview

**JARVIS v0.1** is a personal AI voice assistant built in Python that can:

- 🎤 Listen to voice commands (or accept typed input)
- 🔊 Respond with natural text-to-speech
- 🌐 Search the web, play music, and fetch information
- 🧠 Remember things you tell it

> **Note:** Works perfectly even without a microphone — automatically falls back to keyboard input!

---

## 🚀 Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🎤 **Speech-to-Text** | Voice recognition with mic fallback to keyboard | ✅ |
| 🔊 **Text-to-Speech** | Natural responses using `pyttsx3` | ✅ |
| ⏰ **Tell Time** | Current time on demand | ✅ |
| 📚 **Wikipedia Summaries** | Quick information lookup | ✅ |
| 🎵 **YouTube Playback** | Play/search songs (browser-based) | ✅ |
| 😂 **Tell Jokes** | Random jokes for entertainment | ✅ |
| 🧠 **Memory System** | Store & recall notes (`jarvis_memory.txt`) | ✅ |
| 🌐 **Open Websites** | Quick access to common sites | ✅ |
| 🛡️ **Error Handling** | Clean logging and graceful failures | ✅ |
| ⌨️ **Keyboard Fallback** | Works without PyAudio or microphone | ✅ |
| 🔒 **Safe Naming** | No conflicts with Python modules | ✅ |

---

## 🏗️ Project Structure
    JARVIS-v0.1/
    │
    ├── 📄 jarvis_basic.py # Main JARVIS script (⚠️ do NOT name this code.py)
    ├── 📄 requirements.txt # Dependencies (minimal)
    ├── 📄 jarvis_memory.txt # Auto-created — stores 'remember' notes
    ├── 📄 README.md # Project documentation
    │
    ├── 📁 .venv/ # Virtual environment (ignored by Git)
    │
    └── 📁 assets/ # Optional: images, sounds, etc.

text


---

## 🛠️ Installation Guide (Windows)

### Prerequisites

    - Python 3.8+ (Python 3.11 recommended for full mic support)
    - Windows 10/11
    - Internet connection

### Step-by-Step Setup

**1️⃣ Clone the Repository**


    git clone https://github.com/sidvortex/JARVIS-v0.1-Personal-AI-Voice-Assistant-.git
cd JARVIS-v0.1-Personal-AI-Voice-Assistant-
2️⃣ Create a Virtual Environment



    python -m venv .venv
3️⃣ Activate the Virtual Environment

Shell	Command
Command Prompt	.venv\Scripts\activate.bat
PowerShell	.venv\Scripts\Activate.ps1
<details> <summary>⚠️ PowerShell Execution Policy Issue?</summary>
If scripts are blocked, run one of these:

PowerShell

    # Option 1: Bypass for this session
    powershell -ExecutionPolicy Bypass -File .venv\Scripts\Activate.ps1
    
    # Option 2: Permanently allow local scripts
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force
</details>
4️⃣ Install Required Packages

    Bash
    
    pip install --upgrade pip
    pip install -r requirements.txt
5️⃣ (Optional) Enable Microphone Support

⚠️ Important: PyAudio doesn't install smoothly on Python 3.13.
Recommended: Use Python 3.11 for full speech recognition.

    Bash
    
    # For Python 3.11 users
    pip install pipwin
    pipwin install pyaudio
💡 If you stay on Python 3.13, JARVIS will still work using keyboard input instead of mic.

6️⃣ Run JARVIS

    Bash
    
    python jarvis_basic.py
🎯 Commands You Can Use
Voice/Text Commands
Command	Action
play <song name>	Opens YouTube search results for the song
time	Tells the current time
who is <person>	Reads 1-line Wikipedia summary
joke	Tells a random joke
remember <something>	Saves to memory file
what did you remember	Reads all saved memories
open google	Opens Google
open youtube	Opens YouTube
open github	Opens GitHub
open stackoverflow	Opens Stack Overflow
stop / sleep / quit	Shuts down the assistant
Example Interaction
   text
    
    You: "What time is it?"
    JARVIS: "The current time is 3:45 PM"
    
    You: "Play Shape of You"
    JARVIS: "Playing Shape of You on YouTube"
    [Opens browser with YouTube search]
    
    You: "Remember my wifi password is secret123"
    JARVIS: "I'll remember that."
    
    You: "What did you remember?"
    JARVIS: "You asked me to remember: my wifi password is secret123"
💡 Tip: If microphone isn't available, JARVIS will automatically prompt you to type commands!

⚠️ Troubleshooting
🔴 Script Errors Involving code.py
Error:

    text
    
    AttributeError: module 'code' has no attribute 'InteractiveConsole'
Cause: You named your file code.py, which conflicts with Python's built-in module.

Solution:

    Bash
    
    # 1. Rename the file
    ren code.py jarvis_basic.py
    
    # 2. Remove cache
    rmdir /s /q __pycache__
    
    # 3. Run again
    python jarvis_basic.py
🔴 PyAudio Not Found
Error:

    text
    
    Could not find PyAudio; check installation
Cause: Microphone library not installed.

Solutions:

Python Version	Solution
3.11 or lower	pipwin install pyaudio
3.13	Use keyboard fallback (works automatically)
🔴 pipwin / js2py Bytecode Error
Error:

    text
    
    RuntimeError: Your python version made changes to the bytecode
Cause: Python 3.13 bytecode incompatibility.

Solution: Use Python 3.11 virtual environment:

    Bash
    
    # Create venv with Python 3.11
    py -3.11 -m venv .venv311
    .venv311\Scripts\activate
    pip install -r requirements.txt
🔮 Future Roadmap
Phase	Feature	Status
1	Core voice assistant	✅ Complete
2	Memory system	✅ Complete
3	YouTube integration	✅ Complete
4	Wake-word detection ("Jarvis")	📋 Planned
5	AI-powered NLP (offline/API)	📋 Planned
6	System control (apps, brightness, volume)	📋 Planned
7	GUI Dashboard	📋 Planned
8	Custom "skills" plugin architecture	📋 Planned
9	Integration with Project AES (emotion detection)	📋 Planned
🔗 Related Projects
Project	Description	Link
Project AES	Emotion detection system for JARVIS	GitHub
🤝 Contributing
Contributions are welcome! Here's how to get started:

Fork the repository
Create a feature branch
    Bash
    
    git checkout -b feature/AmazingFeature
Commit your changes
    Bash
    
    git commit -m "Add AmazingFeature"
Push to the branch
    Bash
    
    git push origin feature/AmazingFeature
Open a Pull Request
Ideas for Contributions
🎤 Better speech recognition
🧠 AI-powered responses
🎨 GUI interface
🔌 New command plugins
📱 Cross-platform support
📜 License
This project is licensed under the MIT License — you can modify, distribute, and use freely.

text

    MIT License
    
    Copyright (c) 2024 Siddharth Ravada
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software...
<div align="center">
⭐ Star this repo if you found it useful!
Built with ❤️ by Siddharth Ravada & Ishan Gupta

"I am JARVIS. At your service."

Visitors

</div> 

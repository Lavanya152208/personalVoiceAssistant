# PersonalVoiceAssistant
 🎙️ Cherry - Your Personal Voice Assistant

**Cherry** is a lightweight, customizable Python-based voice assistant designed to make your daily tasks hands-free and more productive. It uses speech recognition and text-to-speech (TTS) technologies to interact with the user and perform various tasks using simple voice commands.

> 🔊 “Yes Boss... I am your Cherry. Tell me, Boss.”

---

## 🚀 Features

- 🎧 **Speech Recognition** – Understands your voice commands using Google's Speech API.
- 🗣️ **Text to Speech** – Responds with a natural voice using `pyttsx3`.
- 🕒 **Time Telling** – Ask for the current time.
- 📺 **YouTube Playback** – Plays your requested videos on YouTube.
- 🔍 **Web Search** – Performs a Google search for any query.
- 📚 **Wikipedia Integration** – Fetches brief summaries from Wikipedia.
- 🙋 **Self-aware** – Knows its name and responds to greetings.
- 🛑 **Graceful Exit** – Say "close" to terminate the assistant politely.

---

## 🛠️ Tech Stack

| Technology      | Description                          |
|----------------|--------------------------------------|
| Python 3.x      | Core programming language             |
| SpeechRecognition | For voice input                    |
| pyttsx3         | For text-to-speech conversion         |
| datetime        | For current time functionality        |
| wikipedia       | For fetching brief information        |
| pywhatkit       | For YouTube and Google integration    |

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/cherry-voice-assistant.git
   cd cherry-voice-assistant
2.Create a Virtual Environment 

bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install Dependencies

bash

    pip install -r requirements.txt

4.Run the Assistant

bash

    python cherry.py

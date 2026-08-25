# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)



# 🎙️ Translator-AI
AI-powered voice translator that transcribes spoken Spanish and generates
translated audio in multiple languages, using OpenAI Whisper for speech
recognition and ElevenLabs for natural-sounding text-to-speech.
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![License](https://img.shields.io/badge/license-unspecified-lightgrey)
# Table of Contents
* About
* Features
* How It Works
* Tech Stack
* Prerequisites
* Installation
* Configuration
* Usage
* Project Structure
* Roadmap
* Contributing
* License
* Author
# About
Translator-AI is a voice translation tool that takes a spoken phrase in
Spanish and returns spoken translations in four other languages. It combines
speech recognition (Whisper), text translation, and text-to-speech
(ElevenLabs) into a single Gradio web app — no typing required, just record
and listen.
# Features
* 🎤 Record audio directly from the browser microphone
* 📝 Automatic Spanish speech-to-text transcription (Whisper)
* 🌍 Translation into English, Italian, French, and Portuguese
* 🔊 Natural-sounding voice output for every translation (ElevenLabs)
* 🖥️ Simple, no-code web interface via Gradio
# How It Works
1. Record — the user records audio through the browser microphone
(Spanish input).
2. Transcribe — OpenAI Whisper
converts the recorded speech into text.
3. Translate — the transcribed text is translated into English,
Italian, French, and Portuguese.
4. Synthesize — each translation is converted into spoken audio via the
ElevenLabs Text-to-Speech API.
5. Play back — the Gradio interface returns one playable audio clip per
language.

# Tech Stack
| :---- | :----: |
| Layer	| Technology | 
| UI	| Gradio |
| Speech-to-text	| OpenAI Whisper |
| Translation |	`translate` (Python package) | 
| Text-to-speech	| ElevenLabs API |
| Config |	`python-dotenv` |


# Prerequisites
Python 3.9+
An ElevenLabs account and API key
`ffmpeg` installed and available on your system PATH (required by Whisper)
# Installation
```bash
# Clone the repository
git clone https://github.com/Dev-Dorian/Translator-AI.git
cd Translator-AI

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
# Configuration
Create a `.env` file in the project root with your ElevenLabs API key:
```env
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```
> **Security note:** never commit your `.env` file or hardcode API keys
> directly in the source code. Add `.env` to `.gitignore` to keep your
> credentials out of version control.
# Usage
Run the app:
```bash
python main.py
```
Gradio will launch a local web interface. From there:
Click the microphone input and record a phrase in Spanish.
Wait for processing — the app will transcribe, translate, and generate
audio.
Listen to the translated output in English, Italian, French, and
Portuguese, each in its own audio player.
Generated audio files are saved locally in the `audios/` directory
(e.g. `audios/en.mp3`, `audios/it.mp3`, `audios/fr.mp3`, `audios/pt.mp3`).
# Project Structure
```
Translator-AI/
├── audios/              # Generated translated audio output
├── main.py              # Application entry point (Gradio UI + pipeline)
├── requirements.txt     # Python dependencies
└── .gitignore
```
# Roadmap
[ ] Load the ElevenLabs API key from environment variables only (remove
any hardcoded key from source)
[ ] Add error handling/UI feedback for unsupported audio formats
[ ] Allow the user to select which target languages to generate
[ ] Add a `.env.example` file to document required environment variables
[ ] Add automated tests
# Contributing
Contributions are welcome. To contribute:
Fork the repository
Create a feature branch (`git checkout -b feature/my-feature`)
Commit your changes (`git commit -m "Add my feature"`)
Push to the branch (`git push origin feature/my-feature`)
Open a Pull Request
# License
No license specified yet — add a `LICENSE` file if you intend to make this
project open source.
# Author
Dorian Hidalgo — GitHub

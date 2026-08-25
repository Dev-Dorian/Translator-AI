Translator-AI
AI-powered voice translator that transcribes spoken Spanish and generates
translated audio in multiple languages, using OpenAI Whisper for speech
recognition and ElevenLabs for natural-sounding text-to-speech.
How It Works
Record — the user records audio through the browser microphone
(Spanish input).
Transcribe — OpenAI Whisper
converts the recorded speech into text.
Translate — the transcribed text is translated into English,
Italian, French, and Portuguese.
Synthesize — each translation is converted into spoken audio via the
ElevenLabs Text-to-Speech API.
Play back — the Gradio interface returns
one playable audio clip per language.
Tech Stack
Python
Gradio — web UI for microphone input and audio playback
OpenAI Whisper — speech-to-text transcription
translate — text translation
ElevenLabs API — text-to-speech synthesis
python-dotenv — environment variable management
Prerequisites
Python 3.9+
An ElevenLabs account and API key
`ffmpeg` installed and available on your system PATH (required by Whisper)
Installation
```bash
# Clone the repository
git clone https://github.com/Dev-Dorian/Translator-AI.git
cd Translator-AI

# Install dependencies
pip install -r requirements.txt
```
Configuration
Create a `.env` file in the project root with your ElevenLabs API key:
```env
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```
> **Security note:** never commit your `.env` file or hardcode API keys
> directly in the source code. Add `.env` to `.gitignore` to keep your
> credentials out of version control.
Usage
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
Project Structure
```
Translator-AI/
├── audios/              # Generated translated audio output
├── main.py              # Application entry point (Gradio UI + pipeline)
├── requirements.txt     # Python dependencies
└── .gitignore
```
Roadmap / Possible Improvements
Load the ElevenLabs API key from environment variables only (remove any
hardcoded key from source).
Add error handling/UI feedback for unsupported audio formats.
Allow the user to select which target languages to generate.
Add a `.env.example` file to document required environment variables.
License
No license specified yet — add a `LICENSE` file if you intend to make this
project open source.

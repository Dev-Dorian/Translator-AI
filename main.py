import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings


# config = dotenv_values(".env")
# ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]
ELEVENLABS_API_KEY = ""


def translator(audio_file):
    transcription = transcribeAudio(audio_file)
    translations = translate_text(transcription)
    audio_files = generateTranslated(translations)

    return audio_files


def transcribeAudio(audio_file):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
        return transcription
    except Exception as e:
        raise gr.Error(
            f"An error occurred while transcribing the text: {str(e)}")
    print(f"Texto transcription: {transcription}")


def translate_text(transcription):
    languages = ["en", "it", "fr", "pt"]
    translations = {}
    try:
        for lang in languages:
            translator = Translator(from_lang="es", to_lang=lang)
            translations[lang] = translator.translate(transcription)
            print(f"Text translated into {lang}: {translations[lang]}")
        return translations
    except Exception as e:
        raise gr.Error(
            f"An error occurred while translating the text.: {str(e)}"
        )


def generateTranslated(translations):
    audioPaths = []

    try:
        for lang, text in translations.items():
            audio_path = textSpeech(text, lang)
            audioPaths.append(audio_path)
        return audioPaths
    except Exception as e:
        raise gr.Error(f"Error generating translated audio: {str(e)}")


def textSpeech(text: str, language: str):
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = f"audios/{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        return save_file_path
    except Exception as e:
        raise gr.Error(
            f"An error occurred while translating the text: {str(e)}"
        )


web = gr.Interface(
    fn=translator,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Spanish"
    ),
    outputs=[gr.Audio(label="English"),
             gr.Audio(label="Italian"),
             gr.Audio(label="French"),
             gr.Audio(label="Portuguese"),
             ],
    title="Voice Translator",
    description="AI Voice Translator for Multiple Languages"
)

web.launch()

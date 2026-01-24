import whisper
import streamlit as st
from pathlib import Path

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

def transcribe(audio_path, output_path):
    model = load_whisper_model()
    result = model.transcribe(audio_path)
    Path(output_path).write_text(result["text"], encoding="utf-8")
    return result["text"]

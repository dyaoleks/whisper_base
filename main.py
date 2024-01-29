import streamlit as st
import whisper
import torch


torch.cuda.empty_cache()

st.title("Перетворення звуку на текст")

# Завантажити аудіофайл зі стрімліт
audio_file = st.file_uploader("Завантажити аудіо", type=["wav", "mp3", "m4a", "ogg",])

model = whisper.load_model("base")
st.text("Модель завантажена")

if st.sidebar.button("Зчитати аудіо"):
    if audio_file is not None:
        st.sidebar.success("Зчитування аудіо")       

        transcription = model.transcribe(audio_file.name)
        st.sidebar.text("Зчитування завершене")
        st.markdown(transcription["text"])
       
    else:
        st.sidebar.error("Завантаж аудіо файл")

st.sidebar.header("Відтворити оригінальне аудіо")
st.sidebar.audio(audio_file)


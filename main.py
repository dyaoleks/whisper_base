import streamlit as st
import whisper
import torch

torch.cuda.empty_cache()

st.title("Перетворення звуку на текст")

# Завантажити аудіофайл зі стрімліт
audio_file = st.file_uploader("Завантажити аудіо", type=["wav", "mp3", "m4a", "ogg",])

# Завантаження моделі при запуску програми
model = whisper.load_model("base")
st.text("Модель завантажена")

if st.sidebar.button("Зчитати аудіо"):
    try:
        if audio_file is not None:
            st.sidebar.success("Зчитування аудіо")       
            transcription = model.transcribe(audio_file.name)
            st.sidebar.text("Зчитування завершене")
            st.markdown(transcription["text"])  # Замість st.markdown
        else:
            st.sidebar.error("Завантаж аудіо файл")
    except Exception as e:
        st.error(f"Помилка під час зчитування аудіо: {str(e)}")

with st.sidebar.expander("Відтворити оригінальне аудіо"):
    if audio_file is not None:
        st.audio(audio_file, format="audio/wav")
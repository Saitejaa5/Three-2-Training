import streamlit as st
from translate_model import load_translator

@st.cache_resource
def get_model():
    return load_translator()

translator = get_model()

st.title("English → Chinese Translator")

text = st.text_area("Enter English text")

if st.button("Translate"):
    if text.strip():
        result = translator(text)
        st.success(result[0]["translation_text"])
    else:
        st.warning("Please enter some text")

import streamlit as st
from transformers import pipeline

# Load model once (important for performance)
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest",
        tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

classifier = load_model()

# UI
st.set_page_config(page_title="Sentiment Analysis App", page_icon="😊")
st.title("💬 Sentiment Analysis (Positive / Neutral / Negative)")
st.write("Enter text below to analyze sentiment.")

# Input
text = st.text_area("Enter your text here:")

# Button
if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = classifier(text)[0]
        label = result["label"]
        score = result["score"]

        # Display result
        st.subheader("Result")
        st.write(f"**Sentiment:** {label.upper()}")
        st.write(f"**Confidence Score:** {score:.2f}")

        # Emoji feedback
        if label == "positive":
            st.success("😊 Positive sentiment detected")
        elif label == "neutral":
            st.info("😐 Neutral sentiment detected")
        else:
            st.error("😠 Negative sentiment detected")

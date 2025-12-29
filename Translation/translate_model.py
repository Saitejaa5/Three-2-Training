from transformers import pipeline

def load_translator():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-zh",
        framework="pt"
    )

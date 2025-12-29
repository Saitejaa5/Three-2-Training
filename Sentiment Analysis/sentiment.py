from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = "I love programming in Python!"
result = classifier(text)

print("Text:", text)
print("Sentiment:", result[0]['label'])
print("Score:", result[0]['score'])

from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI
app = FastAPI(title="Sentiment Analysis API",
              description="A simple API that uses a pretrained Hugging Face model to classify text sentiment",
              version="1.0")

# Load Hugging Face sentiment pipeline
sentiment_model = pipeline("sentiment-analysis")

# Input schema
class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API! Use /predict to analyze text."}

@app.post("/predict")
def predict(input: TextInput):
    """Classify sentiment of input text"""
    result = sentiment_model(input.text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"]),
        "text": input.text
    }

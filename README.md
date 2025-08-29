# Sentiment Analysis API

A lightweight **FastAPI service** that uses a pretrained **Hugging Face Transformer model** to classify the sentiment of input text.

---

## 🚀 Features

* REST API built with **FastAPI**
* Uses Hugging Face **`distilbert-base-uncased-finetuned-sst-2-english`** model
* Predicts sentiment (`POSITIVE` or `NEGATIVE`) of input text
* Returns model confidence score and original text
* Lightweight, simple, and easy to deploy

---

## 👂 Project Structure

```
ml-sentiment-api/
│── app.py               # Main FastAPI application
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YOURUSERNAME/ml-sentiment-api.git
cd ml-sentiment-api
```

2. **Create and activate a virtual environment (recommended)**

```powershell
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the API**

```bash
python -m uvicorn app:app --reload
```

By default, the API runs at `http://127.0.0.1:8000`.

---

## 🧑‍💻 Usage

### Health Check

Use PowerShell/cURL:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/
```

**Response:**

```json
{"message":"Welcome to the Sentiment Analysis API! Use /predict to analyze text."}
```

### Predict Sentiment

PowerShell example:

```powershell
$body = @{ text = "I love working with machine learning!" } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/predict -Method POST -Body $body -ContentType "application/json"
```

**Response:**

```json
label        : POSITIVE
score        : 0.9998
text         : I love working with machine learning!
```

---

## 💡 How It Works

1. **Pretrained Model:** The project uses Hugging Face’s **`distilbert-base-uncased-finetuned-sst-2-english`** sentiment model.
2. **API Endpoint:** `/predict` accepts JSON input with a `text` field.
3. **Pipeline:** Hugging Face `pipeline("sentiment-analysis")` processes the text and returns label + confidence.
4. **FastAPI:** Handles HTTP requests and returns JSON responses.

---


## 🛠 Dependencies

* `fastapi` – Web framework for Python
* `uvicorn` – ASGI server to run FastAPI
* `transformers` – Hugging Face library for pretrained models
* `torch` – Backend for model inference

Install with:

```bash
pip install -r requirements.txt
```

---

## 🌟 Potential Extensions

* Add support for **batch predictions**
* Add **logging** and **metrics**
* Deploy using **Docker** or **cloud service** (AWS, GCP, Azure)
* Extend to **multi-class sentiment** or **other text classification tasks**

# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from typing import Optional

app = FastAPI(title='Disaster Tweet Classifier')

class InputText(BaseModel):
    text: str

# lazy load models
VECT = None
CLF = None

def load_models():
    global VECT, CLF
    if VECT is None:
        VECT = joblib.load('models/tfidf_vect.joblib')
    if CLF is None:
        CLF = joblib.load('models/logreg_baseline.joblib')

@app.get('/')
def root():
    return {'status': 'ok', 'service': 'Disaster Tweet Classifier'}

@app.post('/predict')
def predict(payload: InputText):
    load_models()
    text = payload.text
    x = VECT.transform([text])
    pred = CLF.predict(x)[0]
    prob = float(CLF.predict_proba(x)[0, int(pred)]) if hasattr(CLF, 'predict_proba') else None
    return {'label': int(pred), 'probability': prob}
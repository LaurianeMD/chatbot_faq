from fastapi import FastAPI
from pydantic import BaseModel
from model import get_response

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/predict")
def predict(q: Question):
    response = get_response(q.question)
    return {"response": response}

from fastapi import APIRouter
from app.schema.user_input import UserInput
from app.schema.prediction_response import PredictionResponse
from app.services.prediction_services import run_prediction


router = APIRouter()

@router.post("/predict",response_model=PredictionResponse)
def predict(user_input:UserInput):
    result = run_prediction(user_input)
    return result 


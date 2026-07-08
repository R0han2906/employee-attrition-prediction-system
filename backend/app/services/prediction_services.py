from app.model.predict import predict_attrition
from app.schema.user_input import UserInput

def run_prediction(user_input:UserInput):
    
    input_dict = user_input.model_dump()
    result = predict_attrition(input_dict)
    return result

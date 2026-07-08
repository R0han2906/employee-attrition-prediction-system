import pandas as pd
from app.model.load_model import load_model
import numpy as np
from app.services.shap_service import generate_shap_explanation

def predict_attrition(user_input:dict) ->dict:
    # i forget to add this log transformation in pipeline this is mistake
    model,threshold = load_model()
    user_input["MonthlyIncome"] = np.log1p(user_input["MonthlyIncome"])

    input_df = pd.DataFrame([user_input]) 
    
    probabilities = model.predict_proba(input_df)[0]
    
    prob_yes = probabilities[1]
    prob_no = probabilities[0]
    
    prediction = "Yes" if prob_yes>=threshold else "No"
    
    shap_explanation = generate_shap_explanation(model,input_df)
    

    return {
        "prediction":prediction,
        "confidence_score" : float(max(prob_yes,prob_no)),
        "class_probabilities":{
            "Yes":float(prob_yes),
            "No":float(prob_no)
            },
        "top_contributors":shap_explanation
    }
    
from pydantic import BaseModel, Field
from typing import Annotated, Literal,List,Dict


class PredictionResponse(BaseModel):
    prediction: Annotated[
        Literal["Yes", "No"],
        Field(description="Predicted employee attrition status")
    ]

    confidence_score: Annotated[
        float,
        Field(
            ge=0,
            le=1,
            description="Confidence score of the predicted class"
        )
    ]

    class_probabilities: Annotated[
        dict[str, float],
        Field(
            description="Probability for each class"
        )
    ]
    
    top_contributors:Annotated[List[Dict],Field(description="Top contributors in shap explanation")]
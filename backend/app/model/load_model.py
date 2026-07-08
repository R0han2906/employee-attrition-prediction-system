import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "elasticnet_attrition_model.pkl"
THRESHOLD_PATH = Path(__file__).resolve().parent / "decision_threshold.pkl"

_model = None
_threshold = None

def load_model():
    global _model, _threshold

    if _model is None:
        _model = joblib.load(MODEL_PATH)

    if _threshold is None:
        _threshold = joblib.load(THRESHOLD_PATH)

    return _model, _threshold
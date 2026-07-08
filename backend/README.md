# 🔧 Backend — FastAPI ML Service

This backend serves a trained Elastic Net Logistic Regression model that predicts employee attrition risk and explains predictions using SHAP.

See the [root README](../README.md) for overall architecture and model results.

---

## Folder Structure

```
app/
├── config/
├── model/
├── routes/
├── schema/
├── services/
└── main.py
```

## Setup

```bash
python -m venv backend-env

# Windows
backend-env\Scripts\activate

# macOS / Linux
source backend-env/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Interactive API docs: `http://127.0.0.1:8000/docs`

## Model Pipeline

- Elastic Net Logistic Regression
- Preprocessing: scaling (numeric) + one-hot encoding (categorical)
- Log transform on `MonthlyIncome` to reduce skew
- SHAP `LinearExplainer` for per-prediction feature attribution

## API Reference

### `GET /health`
Basic liveness check.

**Response**
```json
{ "status": "ok" }
```

### `POST /api/predict`
Returns attrition prediction, confidence score, class probabilities, and SHAP explanation.

**Request**
```json
{
  "Age": 34,
  "MonthlyIncome": 5200,
  "OverTime": "Yes",
  "JobSatisfaction": 2,
  "YearsSinceLastPromotion": 4,
  "DistanceFromHome": 12
  // ... remaining model features — see schema/ for the full Pydantic model
}
```

**Response**
```json
{
  "prediction": "Yes",
  "confidence": 0.78,
  "probabilities": { "No": 0.22, "Yes": 0.78 },
  "top_factors": [
    { "feature": "OverTime", "impact": 0.31 },
    { "feature": "MonthlyIncome", "impact": -0.24 },
    { "feature": "JobSatisfaction", "impact": 0.15 }
  ]
}
```

**Error response** (invalid payload)
```json
{ "detail": [ { "loc": ["body", "Age"], "msg": "field required", "type": "value_error.missing" } ] }
```

## Why SHAP

SHAP gives feature-level attribution per prediction rather than only global feature importance — useful for explaining to a non-technical stakeholder *why* a specific employee was flagged, not just that the model is generally accurate.

## Deployment

Designed to run on Render, Railway, Fly.io, or as a standalone Docker container. `Dockerfile` — `[FILL IN if one exists yet]`.

## CORS

Frontend runs from a different origin (opened as a local file / different port). CORS is configured in `[FILL IN: app/config/... file name]` to allow `[FILL IN: allowed origins]`.

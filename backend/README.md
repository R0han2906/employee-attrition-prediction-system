# 🔧 Backend – FastAPI ML Service

This backend serves a trained Elastic Net model for predicting employee attrition risk.

---

## 🏗 Architecture
Request → Router → Service → Model → SHAP → Response


### Folder Structure
app/
├── config/
├── model/
├── routes/
├── schema/
├── services/
└── main.py

## 🚀 Run Locally

```bash
python -m venv backend-env
backend-env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Visit:
http://127.0.0.1:8000/docs

📦 Model Details
Elastic Net Logistic Regression
Preprocessing Pipeline (Scaling + Encoding)
Log Transformation for MonthlyIncome
SHAP for Explainability

🔍 Endpoints
✅ Health Check

GET /health
✅ Predict Attrition

POST /api/predict
Returns:

Prediction (Yes/No)
Confidence Score
Class Probabilities
Top SHAP Contributors
🧠 Why SHAP?
SHAP provides feature-level interpretability to understand why a particular employee is predicted to leave.

This improves business trust and transparency.

⚙️ Deployment
Backend is designed to be deployed on:

Render
Railway
Fly.io
Docker Containers
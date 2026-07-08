# 🧠 IBM HR Attrition Prediction System

An end-to-end machine learning application that predicts employee attrition risk and explains each prediction using SHAP interpretability. Built with a FastAPI backend and a lightweight HTML/CSS/JS frontend.

<!-- [FILL IN: Live demo link] · [FILL IN: Demo video/GIF] -->

---

## Architecture

```
Frontend (HTML + JS)
        ↓
FastAPI Backend
        ↓
Elastic Net Model
        ↓
SHAP Explanation Engine
```

## Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,fastapi,sklearn,numpy,pandas,js,html,css,git,docker" />
</p>

| Layer | Tools |
|---|---|
| ML | Elastic Net Logistic Regression, SHAP, GridSearchCV |
| Backend | FastAPI, Pydantic, Uvicorn, Joblib |
| Frontend | HTML5, CSS3, Vanilla JS (Fetch API) |

## Results

| Metric | Value |
|---|---|
| ROC-AUC | `0.81` |
| Recall (attrition class) | `0.64` |
| Precision | `0.43` |
| Decision threshold | `0.20 - tuned to prioritize recall over default 0.5 ` |

> Threshold was tuned away from the default 0.5 because false negatives (missing an employee who will actually leave) are more costly to the business than false positives. The model was optimized to balance recall and precision while maintaining strong ranking performance.



**Key Insights (SHAP Interpretability)**
**Top SHAP drivers of attrition:**
1. Monthly Income – Lower income significantly increases attrition risk
2. Overtime – Employees working overtime are more likely to leave
3. Job Satisfaction – Low satisfaction strongly increases risk
4. Years Since Last Promotion – Career stagnation correlates with attrition
5. Distance From Home – Long commute increases probability of leaving

The SHAP integration enables transparent, feature-level explanations for every prediction, improving trust and interpretability of the ML system.

## Project Structure

```
ibm-hr/
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── README.md
└── README.md
```

See [`backend/README.md`](./backend/README.md) and [`frontend/README.md`](./frontend/README.md) for setup instructions specific to each service.

## Quick Start

```bash
git clone https://github.com/R0han2906/ibm-hr.git
cd ibm-hr
```

Then follow the backend and frontend setup guides linked above — both need to run simultaneously (backend on `:8000`, frontend served or opened separately).

Engineering Highlights
- [ ] End-to-end ML pipeline (training → tuning → deployment)
- [ ] Elastic Net regularization with hyperparameter tuning
- [ ] Business-driven threshold optimization
- [ ] SHAP-based model explainability
- [ ] Modular FastAPI backend architecture
- [ ] Clean separation of routes, services, and model logic
- [ ] Frontend–Backend integration via Fetch API
- [ ] Reproducible environment with pinned dependencies

## Future Improvements

- [ ] Dockerize both services
- [ ] Migrate frontend to Next.js
- [ ] Add auth layer for API access
- [ ] Dashboard for aggregate attrition analytics
- [ ] CI/CD pipeline (GitHub Actions)

## Author

**[Your Name]**
GitHub: [R0han2906](https://github.com/R0han2906) 

Built as part of an applied ML engineering portfolio.

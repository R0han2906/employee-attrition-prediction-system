# 🎨 Frontend — HR Attrition Predictor UI

A minimal HTML/CSS/JS interface for the attrition prediction API — no framework, no build step.

See the [root README](../README.md) for overall architecture and model details.

---

## Preview

`[FILL IN: screenshot or GIF of the form + result view — this is the one section a recruiter will actually look at, don't skip it]`

## Features

- Structured form for entering employee attributes
- Calls the backend via `fetch()`
- Renders prediction result (Yes/No + confidence)
- Displays top SHAP factors behind the prediction
- Responsive layout

## Setup

The backend must be running first — see [`backend/README.md`](../backend/README.md).

```bash
cd frontend
# then open index.html directly, or serve it:
python -m http.server 5500
```

Backend expected at: `http://127.0.0.1:8000`

## API Connection

`script.js` calls:

```js
fetch("http://127.0.0.1:8000/api/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(formData)
})
```
Returned response includes:
{
  "prediction": "Yes",
  "confidence_score": 0.87,
  "class_probabilities": {...},
  "top_contributors": [...]
}

**The UI renders:**

- [ ] Final prediction
- [ ] Confidence level
- [ ] Human-readable SHAP contributors

If you open `index.html` as a plain file (`file://`) rather than serving it, some browsers block the fetch call under CORS — serve it locally instead if you hit that.

## Design Philosophy

- Minimal UI, no unnecessary chrome
- Clear hierarchy: input → result → explanation
- Interpretability foregrounded — SHAP factors are shown alongside the prediction, not buried
- Typography kept plain and legible over decorative

## Known Limitations

- No client-side advanced validation beyond HTML5 required
- Backend handles strict validation via Pydantic
- No authentication layer (intended as demo/portfolio project)
- Uses local backend URL (needs update for production deployment)

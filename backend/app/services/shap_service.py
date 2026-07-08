import shap
import numpy as np


def generate_shap_explanation(model, input_df, top_n=5):

    preprocessor = model.named_steps['preprocessor']
    clf = model.named_steps['model']

    X_transformed = preprocessor.transform(input_df)
    feature_names = preprocessor.get_feature_names_out()

    explainer = shap.LinearExplainer(clf, X_transformed)
    shap_values = explainer.shap_values(X_transformed)

    # If list (older SHAP behavior)
    if isinstance(shap_values, list):
        shap_values = shap_values[1]

    # Extract the first (and only) sample
    shap_values_single = shap_values[0]

    # Sort features by absolute impact
    indices = np.argsort(np.abs(shap_values_single))[::-1][:top_n]

    top_features = []
    for idx in indices:
        top_features.append({
            "feature": feature_names[idx],
            "impact": float(shap_values_single[idx])
        })

    return top_features
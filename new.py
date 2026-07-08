import joblib

# Load the trained model
model = joblib.load("models/elasticnet_attrition_model.pkl")

# Extract feature names
if hasattr(model, "feature_names_in_"):
    feature_names = list(model.feature_names_in_)
elif hasattr(model, "feature_names_"):
    feature_names = list(model.feature_names_)
elif hasattr(model, "feature_name"):
    feature_names = list(model.feature_name())
elif hasattr(model, "get_booster"):
    feature_names = model.get_booster().feature_names
else:
    feature_names = None

# Print results
if feature_names:
    print(f"Found {len(feature_names)} features:")
    print(feature_names)
else:
    print("Could not automatically extract feature names.")
    if hasattr(model, "n_features_in_"):
        print(f"Model expects {model.n_features_in_} features, but names were not saved.")
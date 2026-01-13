# predict_risk.py
def predict_student_risk(student_data):
    """
    Predict student risk based on input features.
    student_data: dict containing features
    Returns: risk label, probability percentage
    """

    # Feature limits
    limits = {
        'total_activity': (1, 100),
        'early_mid_late': (0, 100),
        'active_days': (1, 30),
        'activity_duration': (0, 1000),
        'video': (0, 50),
        'discussion': (0, 50),
        'problem': (0, 50)
    }

    # Check for out-of-bounds
    for key, (low, high) in limits.items():
        value = student_data.get(key, 0)
        if not (low <= value <= high):
            raise ValueError(f"{key.replace('_',' ').title()} should be between {low} and {high}.")

    # Load model
    import pickle
    import pandas as pd
    model = pickle.load(open('mooc_risk_model.pkl', 'rb'))

    df_input = pd.DataFrame([student_data])
    probability = model.predict_proba(df_input)[:,1][0] * 100

    if probability >= 70:
        risk = "High Risk"
    elif probability >= 40:
        risk = "Low Risk"
    else:
        risk = "Active"

    return risk, probability

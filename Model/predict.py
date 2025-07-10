import pickle
import pandas as pd

with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)


MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input):
    input_data = pd.DataFrame([user_input])
    
    predicated_class = model.predict(input_data)[0]
    probabliities = model.predict_proba(input_data)[0]
    confidence = max(probabliities)
    
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabliities)))
    model_prediction = model.predict(input_data)[0]
    
    return {
        "predicted_class": model_prediction,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs}
    
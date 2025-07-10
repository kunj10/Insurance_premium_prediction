from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from Model.predict import predict_output, model, MODEL_VERSION
   
app = FastAPI() 
         
@app.get("/")
def home():
    return JSONResponse(status_code=200, content={
        "message": "Welcome to the Health Risk Prediction API. Use the /predict endpoint to get predictions."
    })
  
@app.get("/health")
def health_check():
    return JSONResponse(status_code=200, content={
        "status": "healthy",
        "message": "The API is running smoothly.",
        "model_version": MODEL_VERSION
    })  
    
@app.post("/predict")
def predict_risk(user_input: UserInput):
    user_input = {
        
        'bmi': user_input.bmi,
        'age': user_input.age,
        'age_group': user_input.age_group,
        'lifestyle_risk': user_input.lifestyle_risk,  
        'city_tier': user_input.city_tier,
        'income_lpa': user_input.income_lpa,
        'occupation': user_input.occupation
        
        }
    
    try: 
        model_prediction = predict_output(user_input)
        
        return JSONResponse(status_code=200, content={
            "prediction": model_prediction,
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "error": "An error occurred while processing the request.",
            "details": str(e)
        })    
  
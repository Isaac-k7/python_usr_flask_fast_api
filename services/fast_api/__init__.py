from fastapi import FastAPI, HTTPException
import ml

app = FastAPI()

@app.get("/predict")
def get_predict():
    try:
         # Perform prediction with your model
        prediction = ml.predict('data to predict')
        
        # Return the prediction in JSON format
        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

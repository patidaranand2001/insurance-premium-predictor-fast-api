from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_premium



app = FastAPI()




@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

@app.get('/health')
def health_check(): 
    return JSONResponse(status_code=200, content={'message': 'OK'})

@app.post('/predict')
def predict_endpoint(data: UserInput):

    input_df = {
        'age': data.age,
        'sex': data.sex,
        'bmi': data.bmi,
        'children': data.children,
        'smoker': data.smoker,
        'region_northwest': data.region_northwest,
        'region_southeast': data.region_southeast,
        'region_southwest': data.region_southwest,
    }

    try:
        prediction = predict_premium(input_df)
        return JSONResponse(status_code=200, content={'total_premium': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})






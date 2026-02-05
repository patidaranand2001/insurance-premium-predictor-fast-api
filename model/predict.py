# import the ml model
from fastapi.responses import JSONResponse
import pandas as pd
import pickle

with open('model/insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)


def predict_premium(user_input:dict):

    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    return prediction





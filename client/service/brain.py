import joblib
import os

def read_model():
    print(os.getcwd())
    model, accuracy, scaler = joblib.load('../model/model.pkl')
    return model, accuracy, scaler

def predict(data):
    model, accuracy, scaler = read_model()
    data = scaler.transform(data)
    prediction = model.predict(data)
    return prediction[0], accuracy
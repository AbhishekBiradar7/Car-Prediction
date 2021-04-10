import pandas as pd 
from flask import Flask,jsonify,request
import joblib

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
    req = request.get_json()
    input_data =  req['data']
    input_data_df = pd.DataFrame.from_dict(input_data)

    model = joblib.load('model.pkl')

    prediction = model.predict(input_data_df)
    prediction = float(prediction[0])
   # if prediction<0:
    #    prediction_text='Sorry you cannot sell this car'
   # else:
     #   prediction_text='You Can Sell The Car at {}'.format(output)

    return jsonify({'output':{'prediction':prediction}})

@app.route('/')
def home():
    return "Welcome to Car-Prediction"
    
if __name__== '__main__':
    app.run(host='0.0.0.0', port='3000')

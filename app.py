from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        engine = int(request.form['engine'])
        max_power = int(request.form['max_power'])
        km_driven=int(request.form['km_driven'])
        km_driven=np.log(km_driven)
        owner=int(request.form['owner'])
        company_Nissan = int(request.form['company_Nissan'])
        if(company_Nissan=='Nissan'):
            company_Nissan=1
        else:
            company_Nissan = 0
        
        company_Ashok = int(request.form['company_Ashok'])
        if(company_Ashok=='Ashok'):
            company_Ashok=1
        else:
            company_Ashok=0
        
        company_Audi = int(request.form['company_Audi'])
        if(company_Audi=='Audi'):
            company_Audi=1
        else:
            company_Audi=0
        
        company_BMW = int(request.form['company_BMW'])
        if(company_BMW=='BMW'):
            company_BMW=1
        else:
            company_BMW=0
        
        company_Chevrolet = int(request.form['company_Chevrolet'])
        if(company_Chevrolet=='Chevrolet'):
            company_Chevrolet=1
        else:
            company_Chevrolet=0
        
        company_Daewoo = int(request.form['company_Daewoo'])
        if(company_Daewoo=='Daewoo'):
            company_Daewoo=1
        else:
            company_Daewoo=0

        company_Datsun = int(request.form['company_Datsun'])
        if(company_Datsun=='Datsun'):
            company_Datsun=1
        else:
            company_Datsun=0
        
        company_Fiat = int(request.form['company_Fiat'])
        if(company_Fiat=='Fiat'):
            company_Fiat=1
        else:
            company_Fiat=0
        
        company_Force = int(request.form['company_Force'])
        if(company_Force=='Force'):
            company_Force=1
        else:
            company_Force=0
        
        company_Ford = int(request.form['company_Ford'])
        if(company_Ford=='Ford'):
            company_Ford=1
        else:
            company_Ford=0
        
        company_Honda = int(request.form['company_Honda'])
        if(company_Honda=='Honda'):
            company_Honda=1
        else:
            company_Honda=0
        
        company_Hyundai = int(request.form['company_Hyundai'])
        if(company_Hyundai=='Hyundai'):
            company_Hyundai=1
        else:
            company_Hyundai=0

        company_Isuzu = int(request.form['company_Isuzu'])
        if(company_Isuzu=='Isuzu'):
            company_Isuzu=1
        else:
            company_Isuzu=0

        company_Jaguar = int(request.form['company_Jaguar'])
        if(company_Jaguar=='Jaguar'):
            company_Jaguar=1
        else:
            company_Jaguar=0
        
        company_Jeep = int(request.form['company_Jeep'])
        if(company_Jeep=='Jeep'):
            company_Jeep=1
        else:
            company_Jeep=0

        company_Kia = int(request.form['company_Kia'])
        if(company_Kia=='Kia'):
            company_Kia=1
        else:
            company_Kia=0
        
        company_Land = int(request.form['company_Land'])
        if(company_Land=='Land'):
            company_Land=1
        else:
            company_Land=0
        
        company_MG = int(request.form['company_MG'])
        if(company_MG=='MG'):
            company_MG=1
        else:
            company_MG=0
        
        company_Mahindra = int(request.form['company_Mahindra'])
        if(company_Mahindra=='Mahindra'):
            company_Mahindra=1
        else:
            company_Mahindra=0

        company_Maruti = int(request.form['company_Maruti'])
        if(company_Maruti=='Maruti'):
            company_Maruti=1
        else:
            company_Maruti=0
        
        company_Mercedes-Benz = int(request.form['company_Mercedes-Benz'])
        if(company_Mercedes-Benz=='Mercedes-Benz'):
            company_Mercedes-Benz=1
        else:
            company_Mercedes-Benz=0
        
        company_Mitsubishi = int(request.form['company_Mitsubishi'])
        if(company_Mitsubishi=='Mitsubishi'):
            company_Mitsubishi=1
        else:
            company_Mitsubishi=0
        
        company_Opel = int(request.form['company_Opel'])
        if(company_Opel=='Opel'):
            company_Opel=1
        else:
            company_Opel=0

        company_Renault = int(request.form['company_Renault'])
        if(company_Renault=='Renault'):
            company_Renault=1
        else:
            company_Renault=0
        
        company_Skoda = int(request.form['company_Skoda'])
        if(company_Skoda=='Skoda'):
            company_Skoda=1
        else:
            company_Skoda=0
        
        company_Tata = int(request.form['company_Tata'])
        if(company_Tata=='Tata'):
            company_Tata=1
        else:
            company_Tata=0
        
        company_Toyota = int(request.form['company_Toyota'])
        if(company_Toyota=='Toyota'):
            company_Toyota=1
        else:
            company_Toyota=0
        
        company_Volkswagen = int(request.form['company_Volkswagen'])
        if(company_Volkswagen=='Volkswagen'):
            company_Volkswagen=1
        else:
            company_Volkswagen=0
        
        company_Volvo = int(request.form['company_Volvo'])
        if(company_Volvo=='Volvo'):
            company_Volvo=1
        else:
            company_Volvo=0

    
        fuel_Petrol=request.form['fuel_Petrol']
        if(fuel_Petrol=='Petrol'):
                fuel_Petrol=1
        else:
            fuel_Petrol=0
        
        seller_type_Individual=request.form['seller_type_Individual']
        if(seller_type_Individual=='Individual'):
            seller_type_Individual=1
        else:
            seller_type_Individual=0

        transmission_Manual=request.form['transmission_Manual']
        if(transmission_Manual=='Manual'):
            transmission_Manual=1
        else:
            transmission_Manual=0
        
        prediction=model.predict([[km_driven, owner, mileage, engine, max_power,Age, fuel_Petrol, seller_type_Individual, transmission_Manual, company_Ashok, company_Audi, company_BMW,
        company_Chevrolet, company_Daewoo, company_Datsun, company_Fiat,company_Force, company_Ford, company_Honda, company_Hyundai,company_Isuzu, company_Jaguar, company_Jeep, company_Kia,
        company_Land, company_MG, company_Mahindra, company_Maruti,company_Mercedes-Benz, company_Mitsubishi, company_Nissan,company_Opel, company_Renault, company_Skoda, company_Tata,
        company_Toyota, company_Volkswagen, company_Volvo]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()


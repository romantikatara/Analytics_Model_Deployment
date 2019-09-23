
# A very simple Flask Hello World app for you to get started with...

# Import libraries
from flask import Flask, request, jsonify
import numpy as np
#import pickle
from sklearn.externals import joblib
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Load the model
# de-serialization
model = joblib.load(open('/home/romantikatara/mysite/modelcreditscoring.pkl','rb'))

@app.route('/api',methods=['POST']) #menerima masukan/POST/API
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred = []
    for data in datas:
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([data['AGE'], data['MARRIAGE'], data['PAY_1'], data['PAY_2'], data['PAY_3']])]) #model : sudah di state diatas -> pickle.load()

        # Take the first value of prediction
        output = float(prediction[0])
        out = 'Approved' if output==0 else 'Not Approved'
        pred.append(out)
    return jsonify(pred)
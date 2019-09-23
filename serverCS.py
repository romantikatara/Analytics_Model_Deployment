# Membuat API dari model Machine Learning dengan menggunakan flask
# Ingin mengeload model .pkl ke suatu server

'''
Code ini mengambil data JSON dengan POST request suatu tampilan prediksi menggunakan model yang telah di-load.
Kemudian mengeluarkan hasil dengan format JSON.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load Model Random Forest
# De-serialization
model = pickle.load(open('modelcreditscoring.pkl','rb'))

@app.route('/api',methods=['POST']) #menerima masukan/POST/API
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([np.array([data['AGE'],
                                          data['MARRIAGE'],
                                          data['PAY_1'],
                                          data['PAY_2'],
                                          data['PAY_3']])])

    # Take the first value of prediction
    output = int(prediction[0])

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


model = pickle.load(open('insurance_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker']) # 0=Hayır, 1=Evet
        region = int(request.form['region']) # 0=NE, 1=NW, 2=SE, 3=SW

        degerler = np.array([[age, bmi, children, smoker, region]])
        
      
        sonuc = model.predict(degerler)
        tahmin_fiyat = round(sonuc[0], 2) 

        return render_template('index.html', prediction_text=f'Tahmini Sigorta Tutarı: ${tahmin_fiyat}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Hata oluştu: {e}')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
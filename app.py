from flask import Flask, request
import joblib

model = joblib.load('./models/ml/jakesiewjk64_linearregression.joblib', 'rb')
app = Flask(__name__)

@app.route('/')
def hello():
    return {"message":"hello"}

@app.route('/predict/prediction')
def predict():
    res = request.json
    data = res["data"]
    response = list(model.predict(data))
    return ({"prediction":response})

if __name__ == '__main__':    
    app.run(debug=True)
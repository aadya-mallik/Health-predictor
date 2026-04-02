from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)
# Dummy training data
X = [
    [5,10,2,8],
    [7,30,3,4],
    [4,5,5,9],
    [8,40,2,3],
    [6,20,3,6]
]
y = [1,0,1,0,0]  # 1 = High Risk, 0 = Low Risk
model = LogisticRegression()
model.fit(X,y)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    sleep = float(data['sleep'])
    exercise = float(data['exercise'])
    junk = float(data['junk'])
    stress = float(data['stress'])
    prediction = model.predict([[sleep,exercise,junk,stress]])
    if prediction[0] == 1:
        result = "High Health Risk ⚠"
    else:
        result = "Low Health Risk ✅"
    return jsonify({"prediction": result})
if __name__ == '__main__':
    app.run(debug=True)
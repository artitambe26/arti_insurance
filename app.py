import seaborn as sns
import numpy as np
import sklearn
import pandas as pd


from flask import Flask, render_template,request,jsonify,url_for
import config
from utils import HealthInsurance

app = Flask(__name__)

@app.route("/")
def hello_insurance():
    return render_template("home.html")

@app.route("/insurance_price",methods =["GET","POST"])
def prediction():
    if request.method == "POST":
        data = request.form
        print("Data :",data)
     
        age = int(request.form["age"])
        sex = request.form["sex"]
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]

        price =  HealthInsurance(data)
        pred_amt = price.health_pred()
        print("Charges :",pred_amt)
        # return jsonify({"Insurance amount is :" : pred_amt})
        return render_template("home.html",predicted_price = pred_amt )

if __name__ == "__main__":
    app.run(host='0.0.0.0',port= config.PORT)


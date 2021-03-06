import pickle
lr = pickle.load(open("lr_c32.pkl",'rb'))


import numpy as np
from flask import Flask,request,jsonify,render_template
app = Flask(__name__)#
@app.route("/")
def homepage():
    return render_template("index.html")
    
@app.route("/predict",methods=['POST']) 
def predict():
    int_features = lr.predict([np.array([int(x) for x in request.form.values()])])
    return render_template("index.html",prediction_text="This is your predicted sal"+str(int_features))
    
   
    

if __name__=="__main__":
    app.run(port=5001,debug=True)
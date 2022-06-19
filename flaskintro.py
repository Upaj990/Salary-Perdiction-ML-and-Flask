#!pip install flask
from flask import Flask
# import numpy as np
# from sklearn.linear_model import LinearRegression   1
# --------------------------------------------------
# # create a instance of class object(reg) in below example  2
# reg = LinearRegression()
# ------------------------------------------------------
# reg.fit(x,y)  3

# # This is just for your reference




# Intialization of Flask
app = Flask(__name__) # Dir structure is required ,It take cares of dir structure to render the HTML page properly
#created a instance of Flask so that we can use any functionality of Flask class

@app.route("/top")# It binds the website with a specific url 
def hello():
    return "AKASH you are explaining this very perfectly ..!Hurray"
print("in first file")
print(__name__)

if __name__=="__main__":
    app.run(debug=True)
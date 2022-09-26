# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:13:31 2021

@author: Swaminathan ayyappan

"""
import numpy as np
from flask import Flask,request,render_template
import os
import json
import pickle

CropRecommendationApplication = Flask(__name__)
croprecommendationmodel = pickle.load(open('Croprecommendationmodel.pkl','rb'))
decoded_form={0:'apple',1:'banana',2:'blackgram',3:'chickpea',4:'coconut',5:'coffee',6:'cotton',7:'grapes',8:'jute',9:'kidneybeans',
              10:'lentil',11:'maize',12:'mango',13:'mothbeans',14:'mungbean',15:'muskmelon',16:'orange',17:'papaya',18:'pigeonpeas',
              19:'pomegranate',20:'rice',21:'watermelon'}

@CropRecommendationApplication.route('/')
def home():
    return render_template("webpage.html")

@CropRecommendationApplication.route('/predict',methods=['POST'])
def predict():
	features=[float(x) for x in request.form.values()]
	f_features=[np.array(features)]
	prediction=croprecommendationmodel.predict(f_features)
	out=int(prediction)
	return render_template('webpage.html',prediction=decoded_form[out])

@CropRecommendationApplication.route("/api", methods=["GET","POST"])
def api_call():
    if request.method == "GET":
    	response = {
			"Expected Payload":
			{
				"Nitrogen":"....",
				"Phosphorus":"....",
				"Potassium":"...",
				"Temperature":"....",
				"Humidity":"...",
				"Ph":"...",
				"Rainfall":"..."
			}
		}
    else:
        request_vals = request.get_json()
        required_params = ["Nitrogen","Phosphorus","Potassium","Temperature","Humidity","Ph","Rainfall"]
        if len(request_vals)==7:
            features=[float(request_vals["Nitrogen"]),float(request_vals["Phosphorus"]),float(request_vals["Potassium"]),float(request_vals["Temperature"]),float(request_vals["Humidity"]),float(request_vals["Ph"]),float(request_vals["Rainfall"])]
            f_features=[np.array(features)]
            prediction=croprecommendationmodel.predict(f_features)
            out=int(prediction)
            response = {
            "Best suitable crop is":str(decoded_form[out])
            }
        else:
            missing_params = []
            for x in required_params:
                if x not in list(request_vals.keys()):
                    missing_params.append(x)
            response = {"Message":"Error in producing results due to missing parameters",
                        "Missing parameters":missing_params
                        }
    return json.dumps(response)

        


if __name__=="__main__":
    	port = int(os.environ.get("PORT", 5000))
    	CropRecommendationApplication.run(host="0.0.0.0",port=port,debug=True)
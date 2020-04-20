from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import json
from joblib import load
import numpy as np

# curl -d "petal_length=2.2" -d "petal_width=5.1" -d "sepal_length=1.2" -d "sepal_width=2.2" http://127.0.0.1:5000/
# curl -d "petal_length=10" -d "petal_width=3.5" -d "sepal_length=2" -d "sepal_width=5" http://127.0.0.1:5000/

app = Flask(__name__)
api = Api(app)

class getPrediction(Resource):
	# resource let's you define get and put methods which coincide to http request here we want the
	def post(self):
		parser = reqparse.RequestParser()
		#parser.add_argument('petal_length', type = float, required = True)
		#parser.add_argument('petal_width', type = float, required = True)
		#parser.add_argument('sepal_length', type = float, required = True)
		#parser.add_argument('sepal_width', type = float, required = True)

		parser.add_argument('movie', type = float, required = True)

		# dictionary
		arguments = parser.parse_args()

		predictions = collaborative_filter(arguments["movie"])

		# 1M movvies in your database
		# compare movie to 1M items 1M calculations
		# find most similar
		# return results


		#model = load("model/irisDecisionTree.joblib") 
		#vector = [arguments["petal_length"], arguments["petal_width"], arguments["sepal_length"], arguments["sepal_width"]]
		#prediction = model.predict([vector]) # numpy array

		# returns an array so need to unpack
		# to make it flask friendly to return
		return {"prediction": prediction[0]} 

api.add_resource(getPrediction, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
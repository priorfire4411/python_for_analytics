#from functions import TestClass
#import functions as F
#from functions import test
#import argparse # https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
import yaml # https://rollout.io/blog/yaml-tutorial-everything-you-need-get-started/
import pandas as pd
#import functions as F
#import sklearn decisiontree

if __name__ == "__main__":

	import functions as F

	print(__name__)
	print(F.__name__)

	#if zscore_norm:
	#	df = zscore_norm(df)
	#parser = argparse.ArgumentParser()

	# name is how we pass it in on the command line
	# dest is the attribute it goes into
	#parser.add_argument('-path', type=int, help='an integer for param1', action="store", dest = "path", default = 5)
	#parser.add_argument('-save_path', type=str, help='an integer for param1', action="store", dest = "save_path")
	#parser.add_argument('-data_to_predict', type=str, help='an integer for param1', action="store", dest = "pred_data")
	#parser.add_argument('-nomralize_flag', type=str, help='an integer for param1', action="store", dest = "save_path")

	# put the arguments in results
	#results = parser.parse_args()

	#df = pd.load(results.path)

	#if results.nomralize_flag == True:
	#	df = df.normalize()
	#else:
	#	pass

	#dt = decisiontree()
	#df.fit(df)
	#dt.save(results.save_path)
	#dt.predict(result.pred_data)

	#with open('test.yaml') as f:
	#    data = yaml.load(f, Loader=yaml.FullLoader)

	#print(data)
	
	#model_type = "decision tree"

	#if data["modele_type"] == "decision tree":
	#	model = DecisionTree()
	#elif data["modele_type"] == "knn":
	#	model = KNNClassifier()

	#print(results.myparam1)
	#print(results.myparam2)

	#print(type(results.param1))
	#print("Param1:{}".format(results.myparam1))
	#print("Param2:{}".format(results.myparam2))
	#print("Param1 + 2:{}".format(results.myparam1+2))
	#print("Param1 Concat:{}".format(results.myparam2 + "-concat"))

	#print(results.load_path) 



	#t = TestClass()
	#print(t)
	#F.test()
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

def load_data(path):
	return pd.read_csv(path)

def get_y(df, column):
	return df[column]

def get_x(df, features):
	return df[features]

def train_tree(x, y):
	return DecisionTreeClassifier().fit(x,y)

def save_model(model, path):
	dump(model, path) 

if __name__ == '__main__':
	
	df = load_data("iris.csv")
	y = get_y(df, "species")
	x = get_x(df, ["sepal_length", "sepal_width", "petal_length", "petal_width"])
	model = train_tree(x,y)
	save_model(model, "/Users/conagrabrands/Documents/toyAPI/model/irisDecisionTree.joblib")
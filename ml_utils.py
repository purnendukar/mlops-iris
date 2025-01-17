from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

clf = GaussianNB()

clf2 = KNeighborsClassifier()

classes = {
    0: "Iris Setosa",
    1: "Iris Versicolour",
    2: "Iris Virginica"
}

def load_model():
	X, y = datasets.load_iris(return_X_y=True)

	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	clf.fit(X_train, y_train)
	clf2.fit(X_train, y_train)

	acc = accuracy_score(y_test, clf.predict(X_test))
	print(f"Model trained with accuracy (GaussianNB): {round(acc, 3)}")

	acc = accuracy_score(y_test, clf.predict(X_test))
	print(f"Model trained with accuracy (KNeighborsClassifier): {round(acc, 3)}")

def predict(query_data):
	x = list(query_data.dict().values())
	prediction = clf.predict([x])[0] 
	print(f"Model prediction: {classes[prediction]}")
	return classes[prediction]


def predict_v1(query_data):
	x = list(query_data.dict().values())
	prediction = clf2.predict([x])[0] 
	print(f"Model prediction: {classes[prediction]}")
	return classes[prediction]





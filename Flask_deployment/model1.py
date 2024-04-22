from sklearn import datasets
import joblib
import pickle

iris = datasets.load_iris()

x = iris.data
y = iris.target 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
clf = dtc.fit(X_train,y_train)

pickle.dump(clf,open('dtc2.pkl', 'wb'))
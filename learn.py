#Simple machine learning to tell an apple from an orange
from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict([[150, 0]]))
print (clf.predict([[150, 1]]))
print (clf.predict([[100, 1]]))

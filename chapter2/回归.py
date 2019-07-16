from sklearn import svm
X = [[0, 0,3],[2, 2,4]]
y = [[0.5],[1]]
clf = svm.SVR(kernel='poly',C = 1e3, gamma = 0.01)
clf.fit(X, y)
print(clf.predict([[1,1,3]]))
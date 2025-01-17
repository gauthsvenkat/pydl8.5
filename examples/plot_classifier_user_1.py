"""
=====================================================================================
DL8.5 classifier : user specific error function based on supports per class
=====================================================================================
PyDL8.5 allows users to write their own error function for classification tasks. 
This class shows how to write an error function that operates on supports per class.
For data that is not supervised, other supervised learning task, the DL85 predictor 
class should be used; check the plot_classifier_user_2.py and plot_cluster_user.py
examples.
"""
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from pydl85 import DL85Classifier

dataset = np.genfromtxt("../datasets/anneal.txt", delimiter=' ')
X, y = dataset[:, 1:], dataset[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


print("##########################################################################################\n"
      "#      DL8.5 classifier : user specific error function based on supports per class       #\n"
      "##########################################################################################")


# return the error and the majority class
def error(sup_iter):
    supports = list(sup_iter)
    maxindex = np.argmax(supports)
    return sum(supports) - supports[maxindex], maxindex


clf = DL85Classifier(max_depth=2, fast_error_function=error, time_limit=600)
start = time.perf_counter()
print("Model building...")
clf.fit(X_train, y_train)
duration = time.perf_counter() - start
print("Model built. Duration of building =", round(duration, 4))
y_pred = clf.predict(X_test)
print("Confusion Matrix below")
print(confusion_matrix(y_test, y_pred))
print("Accuracy DL8.5 on training set =", round(clf.accuracy_, 4))
print("Accuracy DL8.5 on test set =", round(accuracy_score(y_test, y_pred), 4))

# performance metrics for supervised learning models:

# y_true represents true/actual labels, y_pred represents predicted labels generated by classification model
y_true, y_pred = [], []

# 1. Accuracy = number of correct predictions / total number of predictions
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)


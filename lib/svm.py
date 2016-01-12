from sklearn import svm
from sklearn import cross_validation
import numpy as np


def vectorsAndLabels(arrayOfGenerators):
    '''Takes an array of generators and produces two lists X and y
    where len(X) = len(y),
    X is the vectors, y is their (numerical) labels.'''
    X = []
    y = []
    currentLabel = 0
    for generator in arrayOfGenerators:
        for vector in generator:
            # NB: feature vectors are serialized as strings sometimes
            # we map them to floats
            X.append(vector)
            y.append(currentLabel)
        currentLabel += 1
    return X, y


def crossValidate(X, y):
    "7-fold cross-validation with an SVM with a set of labels and vectors"
    clf = svm.LinearSVC()
    scores = cross_validation.cross_val_score(clf, np.array(X), y, cv=7)
    return scores.mean()

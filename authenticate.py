from lib.featurevectorgenerator import feature_vector_generator
from lib import labeler
from sklearn.svm import LinearSVC
from itertools import chain


def make_svm_classifier(tasks, subject, position, sessionnum="", sq=""):
    for i in range(len(tasks)):
        print('For subject ' + str(subject) + ', task ' + str(tasks[i]) + ':')
        taskX = feature_vector_generator(tasks[i], subject, position, sessionnum, sq)
        def f():
            return
            yield
        g = f()
        for j in range(i):
            # print(tasks[j])
            taskA = feature_vector_generator(tasks[j], subject, position, sessionnum, sq)
            g = chain(g, taskA)
        for k in range(i+1, len(tasks)):
            # print(tasks[k])
            taskB = feature_vector_generator(tasks[k], subject, position, sessionnum, sq)
            g = chain(g, taskB)
        X, y = labeler.vectorsAndLabels([taskX, g])
        '''Toggle the following for learner function or cross-validation.'''
        # lin_clf = LinearSVC()
        # target = lin_clf.fit(X, y)
        # return target
        comparison = tasks[i] + " vs. others cross-validation is: " + str(labeler.crossValidate(X, y))
        print(comparison)

tasks_list = ['breath', 'blink', 'ocular', 'song', 'hear', 'face', 'cube']
# make_svm_classifier(tasks_list, 2, 0, 1)
g = make_svm_classifier(tasks_list, 2, 0, 1)

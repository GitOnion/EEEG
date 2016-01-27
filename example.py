from lib.featurevectorgenerator import feature_vector_generator
from lib import labeler
from itertools import chain

'''
Using the cross-validation function in svm.py to demonstrate the classifiability of subjects and mental tasks.
Choose the dataset of interested user, interested electrode position(1 = anterior facing, 2 = superior facing),
among lists.

Note:
In test data (111,121,112,122,211,221,311,411,421), the dataset of the first session of the both positions of subject 1
(111, 121) were flawed due to error in the PsychoPy script, subeject 3 only have one position recorded (311), and the
second session of subject 1 (112, 122) only have two tasks(breath and cube) recorded. Other data (211, 221, 411, 421)
Only have 5 recordings per task.
'''


def compare_by_task(tasks, subject1, position, sessionnum="", sq=""):
    print('For subject ' + str(subject1) + ', position ' + str(position) + ':')
    for i in range(len(tasks)):
        for j in range(i+1, len(tasks)):
            for k in range(j+1, len(tasks)):
                for l in range(k+1, len(tasks)):
                    taskA = feature_vector_generator(tasks[i], subject1, position, sessionnum, sq)
                    taskB = feature_vector_generator(tasks[j], subject1, position, sessionnum, sq)
                    taskC = feature_vector_generator(tasks[k], subject1, position, sessionnum, sq)
                    taskD = feature_vector_generator(tasks[l], subject1, position, sessionnum, sq)
                    X, y = labeler.vectorsAndLabels([taskA, taskB, taskC, taskD])
                    comparison = tasks[i] + " vs. " + tasks[j] + " vs. " + tasks[k] + " vs. " + tasks[l] + " cross-validation is: " + str(labeler.crossValidate(X, y))
                    print(comparison)


def compare_by_subject(tasks, subjects, position, sessionnum=""):
    for i in range(len(tasks)):
        print('For task ' + tasks[i] + ', position ' + str(position) + ':')
        for j in range(len(subjects)):
            for k in range(j+1, len(subjects)):
                subA = feature_vector_generator(tasks[i], subjects[j], position, sessionnum)
                subB = feature_vector_generator(tasks[i], subjects[k], position, sessionnum)
                X, y = labeler.vectorsAndLabels([subA, subB])
                comparison = 'subject' + str(subjects[j]) + " vs. subject" + str(subjects[k]) + " cross-validation is: " + str(labeler.crossValidate(X, y))
                print(comparison)


def compare_across_all_tasks(tasks, subject, position, sessionnum="", sq=""):
    print('For subject ' + str(subject) + ':')
    for i in range(len(tasks)):
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
        comparison = tasks[i] + " vs. others cross-validation is: " + str(labeler.crossValidate(X, y))
        print(comparison)


tasks_list = ['breath', 'blink', 'ocular', 'song', 'hear', 'face', 'cube']
# tasks_list = ['breath', 'cube']
subjects_list = [1, 2, 3, 4]
positions_list = [1, 2]
sessions_list = [1, 2]

# compare_by_task(tasks_list, 1, 0, 1, sq=30)
compare_by_task(tasks_list, 1, 0, 1, sq=30)
compare_by_task(tasks_list, 2, 0, 1, sq=30)
# compare_by_subject(tasks_list, [2, 4], 1, 1)
# compare_by_subject(tasks_list, [2, 4], 2, 1)

compare_across_all_tasks(tasks_list, 2, 0, 1, sq=30)

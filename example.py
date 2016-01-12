from lib.featurevectorgenerator import feature_vector_generator
from lib import svm


# def compare_by_tasks(tasks, subject1, position, sessionnum=""):
#     # if subject1 is not int or position is not int:
#     #     raise ValueError("subject or position must be integer.")
#     task_holder = []
#     for task in tasks:
#         task_holder.append(feature_vector_generator(task, subject1, position, sessionnum))
#     for i in range(len(tasks)):
#         for j in range(i+1, len(tasks)):
#             print(tasks[i], tasks[j])
#             X, y = svm.vectorsAndLabels([task_holder[i], task_holder[j]])
#             comparison = 'For subject: '+ str(subject1) + ', ' + tasks[i] + " vs. " + tasks[j] + " cross-validation is: " + str(svm.crossValidate(X, y))
#             print(comparison)


def compare_by_task(tasks, subject1, position, sessionnum=""):
    print('For subject '+ str(subject1) + ', position ' + str(position) + ':')
    for i in range(len(tasks)):
        for j in range(i+1, len(tasks)):
            taskA = feature_vector_generator(tasks[i], subject1, position, sessionnum)
            taskB = feature_vector_generator(tasks[j], subject1, position, sessionnum)
            X, y = svm.vectorsAndLabels([taskA, taskB])
            comparison = tasks[i] + " vs. " + tasks[j] + " cross-validation is: " + str(svm.crossValidate(X, y))
            print(comparison)


def compare_by_subject(tasks, subjects, position, sessionnum=""):
    for i in range(len(tasks)):
        print('For task ' + tasks[i] + ':')
        for j in range(len(subjects)):
            for k in range(j+1, len(subjects)):
                subA = feature_vector_generator(tasks[i], subjects[j], position, sessionnum)
                subB = feature_vector_generator(tasks[i], subjects[k], position, sessionnum)
                X, y = svm.vectorsAndLabels([subA, subB])
                comparison = 'subject' + str(subjects[j]) + " vs. subject" + str(subjects[k]) + " cross-validation is: " + str(svm.crossValidate(X, y))
                print(comparison)


tasks_list = ['breath', 'blink', 'ocular', 'song', 'hear', 'face', 'cube']
# tasks_list = ['breath', 'cube']
subjects_list = [1, 2, 3, 4]
positions_list = [1, 2]
sessions_list = [1, 2]

# compare_by_task(tasks_list, 2, 2)
compare_by_subject(tasks_list, [2,4], 1)

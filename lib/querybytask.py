import json
import os.path as path


def dataset_path(subjectnum=1, positionnum=1, sessionnum=""):
    '''
    Choosing the csv file corresponding to specified subject, ear posision, and session.
    '''
    return path.join('dataset', str(subjectnum) + str(positionnum) + str(sessionnum) + '.csv')


def readings(tag, subjectnum, positionnum, sessionnum="", sq=0):
    '''
    Returns all of subject's readings with tag,
    sq defines minimum signal quality - 0, by default
    '''
    with open(dataset_path(subjectnum, positionnum, sessionnum), 'r') as f:
        for line in f.readlines():
            parsed = json.loads(line[:-2])
            if parsed['tag'] == tag and parsed['reading']['signal_quality'] <= sq:
                yield parsed['reading']

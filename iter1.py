import json
import os.path as path





def readings (subject, t0, t1, sq=0):
    '''Returns all of subject's readings between t0 and t1,
    not including t0, but including t1.
    sq defines minimum signal quality - 0, by default'''
    if t1 < t0:
        raise DatasetQueryError("First time must come before second time.")
    with open(dataset_path(subject), 'r') as f:
        reader = csv.DictReader(f)
        result = sorted(reader, key=lambda d: parse(d[time_field]))
        return [r for r in readings_in_range(result, t0, t1, sq)]

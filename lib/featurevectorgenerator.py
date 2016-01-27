from lib import querybytask
from lib import brainlib
from lib.grouper import grouper
import numpy as np
'''
make a generator of feature vectors
given a task, subject, electrode position, and session
'''


def parse_raw_values(reading):
    "make list of power spectra for all raw_values in a list"
    vals = reading['raw_values'].split(',')
    return np.array(vals).astype(np.float)


# get the power spectrum
def spectra(readings):
    "Parse + calculate the power spectrum for every reading in a list"
    return [brainlib.pSpectrum(parse_raw_values(r)) for r in readings]

# configure feature vector generation here:
vector_resolution = 3  # number of readings in an averaged feature vector


def make_feature_vector(readings):  # A function we apply to each group of power spectra
    '''
    Create 100, log10-spaced bins for each power spectrum.
    For more on how this particular implementation works, see:
    http://coolworld.me/pre-processing-EEG-consumer-devices/
    '''
    return brainlib.avgPowerSpectrum(brainlib.binnedPowerSpectra(spectra(readings), 100), np.log10)


# feature vector generator
def feature_vector_generator(task, subject, position, sessionnum="", sq=""):
    '''Returns a generator of feature vectors
    for a specific task, subject, position, and session. All returned vectors
    are guaranteed to be equal to or above signal quality sq.'''
    # get all the readings for subject between t0 and t1
    readings = querybytask.readings(task, subject, position, sessionnum, sq)
    # group readings into lists of length `vector_resolution`
    groups = grouper(vector_resolution, readings)
    for g in groups:
        readings = filter(None, g)
        # throw out readings with fewer signals than our desired resolution
        if len(readings) == vector_resolution:
            yield make_feature_vector(readings)

from array import array
from numpy import *
import operator


def createDataSet():
    group = array([1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1])
    label = ['A', 'B', 'C', 'D']
    return group, label

from array import array
from numpy import *
import operator


# k-邻近算法（kNN）
# 存在一个样本数据集合, 也称作训练样本集，并且样本集中每个数据都存在标签，
# 即我们知道样本集中每一数据与所属分类的对应关系。输入没有标签的新数据后，将新数据的每个特征与样本集中每一数据
#

def createDataSet():
    group = array([1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1])
    label = ['A', 'B', 'C', 'D']
    return group, label


group, label = createDataSet()

print(group)

print(label)

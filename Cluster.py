#Cluster class
from random import random

class Cluster:
    def __init__(self, id, numDim):
        #set the mean
        meanList = []
        for i in xrange(numDim):
            mean = random() * 150.0
            mean = mean - 75.0
            meanList.append(mean)

        #set the variance
        variance = random() * 10

        #
        self.mean = meanList
        self.variance = variance
        self.id = id
        self.member = 0
        self.numDim = numDim

    # Update the mean and variance
    def maximize(self, nodes):
        pass


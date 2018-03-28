#Cluster class
from random import random

class Cluster:
    def __init__(self, id, numDim, meanList, maxList, minList, varianceList):
        #set the mean
        self.mean = meanList

        #set the variance
        for i in xrange(numDim):
            variance = random() * 10

        #Take the variance of the entire distribution
        #base the variance on the nodes var/#cluster
        #PICK THE MEAN AND VARIANCE FORM THE NODES
        self.variance = variance    #Distribution
        self.id = id
        self.member = 0
        self.numDim = numDim

    # Update the mean and variance
    def maximize(self, nodes):
        pass


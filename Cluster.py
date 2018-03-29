#Cluster class
from random import random

class Cluster:
    def __init__(self, id, numDim, meanList, maxList, minList, varianceList):
        #set the mean
        self.mean = meanList
        variance = []
        #set the variance
        for i in xrange(numDim):
            randNum =  random() * 10
            variance.append(randNum)

        #Take the variance of the entire distribution
        #base the variance on the nodes var/#cluster
        #PICK THE MEAN AND VARIANCE FORM THE NODES
        self.variance = variance    #Distribution
        self.id = id
        self.member = 0
        self.numDim = numDim

    # Update the mean and variance
    def maximize(self, nodes):
        varianceList = []
        meanList = []

        # calculate new means
        for i in xrange(self.numDim):
            mean = 0
            prob = 0
            for j in xrange(len(nodes)):
                mean += nodes[j].coordinates[i] * nodes[j].probabilities[self.id][i]
                prob += nodes[j].probabilities[self.id]

            mean = mean/prob
            meanList.append(mean)
        self.mean = meanList

        # calculate new variance
        for i in xrange(self.numDim):
            square_diff = 0
            for j in xrange(len(nodes)):
                square_diff += (nodes[j].coordinates[i] - self.mean[i])**2

            variance = square_diff / len(nodes)
            varianceList.append(variance)

        self.variance = varianceList


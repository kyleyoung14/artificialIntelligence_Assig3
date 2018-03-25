#Cluster class
from random import random

class Cluster:
    def __init__(self, numNodes):
        #set the mean
        mean = random() * 150.0
        mean = mean - 75.0

        #set the variance
        variance = random() * 10

        self.mean = mean
        self.variance = variance
        self.probabilities = [0] * numNodes    #Probability Node i is in this cluster

    #Returns the probability that the given nodes comes from this cluster
    def fromCluser(self, node):
        print("setting prob")


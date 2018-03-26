#Cluster class
from random import random

class Cluster:
    def __init__(self, id):
        #set the mean
        mean = random() * 150.0
        mean = mean - 75.0

        #set the variance
        variance = random() * 10

        #
        self.mean = mean
        self.variance = variance
        self.id = id
        self.member = 0



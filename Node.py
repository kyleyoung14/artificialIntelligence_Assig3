import math

#The class node holds info about the data points
class Node:
    def __init__(self, coordinates, clusterNum):
        self.coordinates = coordinates
        self.probabilities = [0] * clusterNum
        self.cluster = 0

    #Does the math to check what is the probability that this nodes belongs to the given cluster
    def probFrom(self, clusters):
        # print("Checking the probability this node comes from cluster " + str(cluster.id))
        for cluster in clusters:
            dist = 0
            for i in xrange(cluster.numDim):
                dist += (cluster.mean[i] - self.coordinates[i])**2

            probMath = math.exp(-1 / (2*cluster.variance) * dist**2)
            self.probabilities[cluster.id] = probMath
        # Take the summation of all of the probabilities
        #FORMULA BASed on the pos,
        sumN = 0.0
        for prob in self.probabilities:
            sumN += prob

        # Normalize all of the probabilities
        for i in xrange(len(self.probabilities)):
            self.probabilities[i] = self.probabilities[i]/sumN


    #Gets the cluster id with highest probability and sets it
    def bestCluster(self):
        highest = self.probabilities[0]
        id = 0



        #Get the highest id
        for i, prob in enumerate(self.probabilities):
            if prob > highest :
                highest = prob
                id = i

        #Set to the cluster with the highest probability
        self.cluster = id




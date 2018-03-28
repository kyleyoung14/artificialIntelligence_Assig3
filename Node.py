import math
from scipy.stats import norm

#The class node holds info about the data points
class Node:
    def __init__(self, coordinates, clusterNum, numDim):
        self.coordinates = coordinates
        self.probabilities = [0] * clusterNum
        for cluster in self.probabilities:
            cluster = [0] * numDim
        self.cluster = 0

    #Does the math to check what is the probability that this nodes belongs to the given cluster
    def probFrom(self, clusters):
        # print("Checking the probability this node comes from cluster " + str(cluster.id))
        for n, cluster in enumerate(clusters):
            for i in xrange(cluster.numDim):
                # calculate probability for this cluster for this dimension
                mean = cluster.meanList[i]
                stddev = math.sqrt(cluster.varianceList[i])
                p = (self.coordinates[i] - mean)/stddev
                # normalize
                p_norm = norm.ppf(p,loc=mean,scale=stddev)
                # update probabilities list
                self.probabilities[n][i] = p_norm


    """
            # OLD MATH
            # dist = 0
            # for i in xrange(cluster.numDim):
            #     dist += (cluster.mean[i] - self.coordinates[i])**2
            #
            # probMath = math.exp(-1 / (2*cluster.variance) * dist**2)
            # probMath = 0
            # self.probabilities[cluster.id] = probMath

        # Take the summation of all of the probabilities
        #FORMULA BASed on the pos,
        sumN = 0.0
        for prob in self.probabilities:
            sumN += prob

        # Normalize all of the probabilities
        for i in xrange(len(self.probabilities)):
            self.probabilities[i] = self.probabilities[i]/sumN
    """

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




import math
from scipy.stats import norm

#The class node holds info about the data points
class Node:
    def __init__(self, coordinates, clusterNum, numDim):
        self.coordinates = coordinates
        self.probabilities = [[] for x in xrange(clusterNum)]
        for i in xrange(clusterNum):
            for j in xrange(numDim):
                self.probabilities[i].append(0)
            # cluster = [0] * numDim
        self.probabilities_unorm = [0] * clusterNum
        self.probabilities_norm = [0] * clusterNum
        self.L = 0
        self.logL = 0

    #Does the math to check what is the probability that this nodes belongs to the given cluster
    def probFrom(self, clusters):

        # calculate probability that node is in this cluster per dimension
        for cluster in clusters:
            for i in xrange(cluster.numDim):
                # calculate probability for this cluster for this dimension
                mean = cluster.mean[i]
                print"COORD: ",self.coordinates[i]
                print"MEAN CALC: ",mean," CLUSTER",cluster.id
                stddev = math.sqrt(cluster.variance[i])
                # calculate Z value
                # z = (self.coordinates[i] - mean)/stddev
                # calculate prob from z value, mean, and stddev
                p_norm = norm(mean,stddev).cdf(self.coordinates[i])
                if self.coordinates[i] > mean:
                    p_norm = 1 - p_norm
                if p_norm == 0.0:
                    p_norm = 1*10**-300
                # update probabilities list
                self.probabilities[cluster.id][i] = p_norm
                print "PNORM: ",p_norm
            print "PNORMS: ",self.probabilities[cluster.id]

        # calculate probability that node is from cluster (unorm)
        for cluster in clusters:
            probability = 1
            for i in xrange(cluster.numDim):
                probability *= self.probabilities[cluster.id][i]
            probability *= cluster.probability
            if probability == 0.0:
                probability = 1 * 10 ** -300
            self.probabilities_unorm[cluster.id] = probability
        print"PROB UNORM: ",self.probabilities_unorm

        # normalize probabilities
        sumP = 0
        self.probabilities_norm = []
        for prob in self.probabilities_unorm:
            sumP += prob
        for prob in self.probabilities_unorm:
            prob_norm = prob/sumP
            self.probabilities_norm.append(prob_norm)
        print"PROB NORM: ",self.probabilities_norm

    def calculateNodeL(self):
        likelihood = 0
        log_likelihood = 0
        #calculate likelihood
        for prob in self.probabilities_unorm:
            likelihood += prob
        self.L = likelihood
        #calculate log likelihood
        self.logL = math.log(self.L)






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






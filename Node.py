import math
from scipy.stats import norm

#The class node holds info about the data points
class Node:
    def __init__(self, coordinates, clusterNum, numDim):
        self.coordinates = coordinates
        self.probabilities = [0] * clusterNum
        for cluster in self.probabilities:
            cluster = [0] * numDim
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
                mean = cluster.meanList[i]
                stddev = math.sqrt(cluster.varianceList[i])
                p = (self.coordinates[i] - mean)/stddev
                # normalize
                p_norm = norm.ppf(p,loc=mean,scale=stddev)
                # update probabilities list
                self.probabilities[cluster.id][i] = p_norm

        # calculate probability that node is from cluster (unorm)
        probability = 1
        for cluster in clusters:
            for i in xrange(cluster.numDim):
                probability *= self.probabilities[cluster.id][i]
            probability *= cluster.probability
            self.probabilities_unorm.append(probability)

        # normalize probabilities
        sumP = 0
        for prob in self.probabilities_unorm:
            sumP += prob
        for prob in self.probabilities_unorm:
            prob_norm = prob/sumP
            self.probabilities_norm.append(prob_norm)

    def calculateNodeL(self):
        likelihood = 0
        log_likelihood = 0
        #calculate likelihood
        for prob in self.probabilities_unorm:
            likelihood += prob
        self.L = likelihood
        #calculate log likelihood
        self.logL = math.log10(self.L)






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






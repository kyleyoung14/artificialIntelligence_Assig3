#Cluster class
import random

class Cluster:
    def __init__(self, id, numDim, meanList, varianceList, probability):
        #set the mean
        self.mean = meanList
        variance = []
        self.probability = probability

        #set the variance
        for i in xrange(numDim):
            val = varianceList[i]
            scale = random.uniform(0.8, 1.2)

            curVar = val * scale
            variance.append(curVar)


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
        # print"Old Means: ","cluster",self.id," :",self.mean
        for i in xrange(self.numDim):
            mean = 0.0
            prob = 0.0
            for j in xrange(len(nodes)):
                mean += nodes[j].coordinates[i] * nodes[j].probabilities_norm[self.id]
                prob += nodes[j].probabilities_norm[self.id]

            mean = mean/prob
            meanList.append(mean)
        self.mean = meanList

        # print"New Means: ","cluster",self.id," :",self.mean

        # calculate new variance
        for i in xrange(self.numDim):
            square_diff = 0
            var_sum = 0
            c_psum = 0
            for j in xrange(len(nodes)):
                square_diff = (nodes[j].coordinates[i] - self.mean[i])**2
                prob = nodes[j].probabilities_norm[self.id]
                c_psum += prob
                var_sum += square_diff * prob

            # variance = square_diff * mean / prob
            variance = var_sum / c_psum
            varianceList.append(variance)

            self.variance = varianceList

        # calculate new cluster probability
        c_probsum = 0
        for node in nodes:
            c_probsum += node.probabilities_norm[self.id]
        c_prob = c_probsum / len(nodes)
        self.probability = c_prob


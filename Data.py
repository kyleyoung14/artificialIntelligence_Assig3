import numpy as np

# Holds all the information to perform EM data points and clusters
class Data:
    def __init__(self, nodes, clusters):
        self.nodes = nodes
        self.clusters = clusters
        self.L = []
        self.L.append(-1000000)
        self.logL = []
        self.logL.append(-1000000)


    #Loops through all the nodes and sets their probability of being in part in all clusters (EXPECTATION)
    def setAllNodeProb(self):
        print("setting all clusters nodes")

        # calculate probabilities
        for node in self.nodes:
            node.probFrom(self.clusters)


    #This will update our initial guesses (MAXIMIZATION)
    def updateClusters(self):
        print("Updating clusters' mean and variance")
        for cluster in self.clusters:
            cluster.maximize(self.nodes)


    #Calculate the newest log LL
    def updateLikelihood(self):
        likelihood = 0
        log_likelihood = 0

        # calculate node likelihoods
        for node in self.nodes:
            node.calculateNodeL()

        # calculate overall likelihoods
        for node in self.nodes:
            likelihood += node.L
            log_likelihood += node.logL

        # append to data's L and logL arrays
        self.logL.append(log_likelihood)
        self.L.append(likelihood)



    #This runs EM
    def ExpectedMax(self):
        print("running EM")
        #Runs until the new log likelihood is at least 0.1 better than before
        thresh = 3 # threshold for when to stop EM
        first = True
        size = len(self.logL)
        while(first or self.logL[size-1]-self.logL[size-2] > thresh):
            self.setAllNodeProb()
            self.updateClusters()
            self.updateLikelihood()
            size = len(self.logL)
            print('Last Log Likelihood = ' + str(self.logL[size-2]) + ', New Log Likelihood = ' + str(self.logL[size-1]))
            first = False
        return self


# Holds all the information to perform EM data points and clusters
class Data:
    def __init__(self, nodes, clusters):
        self.nodes = nodes
        self.clusters = clusters
        self.logLL = []


    #Loops through all the nodes and sets their probability of being in part in all clusters
    def setAllNodeProb(self):
        print("setting all clusters nodes")

        #
        for cluster in self.clusters:
            for node in self.nodes:
                node.probFrom(cluster)


    #This will update our initial guesses (MAXIMIZATION)
    def updateClusters(self):
        print("Updating clusters")


    #This runs EM
    def ExpectedMax(self):
        print("running EM")
        #Runs until the new log likelihood is at least 0.1 better than before


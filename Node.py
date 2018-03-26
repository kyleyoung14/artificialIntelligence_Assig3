#The class node holds info about the data points
class Node:
    def __init__(self, coordinates, clusterNum):
        self.coordinates = coordinates
        self.probabilities = [0] * clusterNum
        self.cluster = 0

    #Does the math to check what is the probability that this nodes belongs to the given cluster
    def probFrom(self, cluster):
        print("Checking the probability this node comes from cluster " + str(cluster.id))
        math = 1
        self.probabilities[cluster.id] = math


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




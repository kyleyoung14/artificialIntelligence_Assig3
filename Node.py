#The class node
class Node:
    def __init__(self, coordinates, clusterSize):
        self.coordinates = coordinates
        self.clusterSize = clusterSize
        self.probability = [0] * clusterSize               #list of Probabilities of size cluster

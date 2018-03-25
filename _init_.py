from Node import Node
from Cluster import Cluster
from Data import Data

import csv


#Main Function
def main():
    print("Running EM")

    #Take in input
    #dataFile = raw_input("Input data file name: ")
    dataFile = "sample_EM_data.csv"
    clusterCnt = int(raw_input("Number of clusters: "))

    #Extract from CSV file
    file = open(dataFile)
    csv_file = csv.reader(file)

    #Create the list of nodes
    nodes = []
    for row in csv_file:
        nodes.append(Node(row))

    #Create the list of clusters
    clusters = []
    numNodes = len(nodes)
    for i in xrange(clusterCnt):
        clusters.append(Cluster(numNodes))

    print(nodes[0].coordinates[0])
    print(clusters[0].mean)

    #Create the Data Class
    Data(nodes,clusters)



#Run the main function
if __name__ == "__main__":
    main()

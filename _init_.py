from Node import Node
from Cluster import Cluster
from Data import Data

import csv

#Returns a list with the biggest coordinate value for each dimension
def getMaxList(nodes):
    maxList = []

    #Loops and appends the max for the specific coordinate dimension
    coordSize = len(nodes[0].coordinates)

    for i in xrange(coordSize):
        currMax =nodes[0].coordinates[i]
        for j in xrange(len(nodes)) :
            curr = nodes[j].coordinates[i]

            if(curr > currMax):
                currMax = curr

        #Get the current Max for the coordinate
        maxList.append(currMax)

    return maxList

#Returns a list with the lowest coordinate value for each dimension
def getMinList(nodes):
    minList = []

    #Loops and appends the max for the specific coordinate dimension
    coordSize = len(nodes[0].coordinates)
    for i in xrange(coordSize):
        currMin = nodes[0].coordinates[i]
        for node in nodes:
            curr = node.coordinates[i]
            if(curr < currMin):
                currMin = curr

        #Get the current Max for the coordinate
        minList.append(currMin)

    return minList

#Returns a list for the variance
def getVarList(nodes):
    varList = []
    return varList




#Main Function
def main():
    print("Running EM")

    #Take in input
    #dataFile = raw_input("Input data file name: ")
    dataFile = "sample_EM_data2.csv"
    clusterCnt = int(raw_input("Number of clusters: "))

    #Extract from CSV file
    file = open(dataFile)
    csv_file = csv.reader(file)

    #Create the list of nodes
    nodes = []
    for row in csv_file:
        coordinates = []

        #Convert the strings to floats
        for i in row:
            coordinates.append(float(i))

        nodes.append(Node(coordinates,clusterCnt))
        print(coordinates)

    #Get the max and min from the nodes
    maxList = getMaxList(nodes)
    minList = getMinList(nodes)

    #Get a list of variance for each dimension
    varianceList = getVarList(nodes)



    # #Create the list of clusters
    # clusters = []
    # for id in xrange(clusterCnt):
    #     clusters.append(Cluster(id, len(nodes[0].coordinates), maxList,minList, varianceList))
    #
    # #Create the Data Class
    # allData = Data(nodes,clusters)
    #
    # allData.ExpectedMax()



#Run the main function
if __name__ == "__main__":
    main()

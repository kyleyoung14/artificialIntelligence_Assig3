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

    #Get the sampleMean of all the coordinates to their respective slot
    sampleMeanList = []
    coordSize = len(nodes[0].coordinates)
    numNodes = len(nodes)
    for i in xrange(coordSize):
        sum = 0
        for node in nodes:
            sum += node.coordinates[i]

        #Get the sample mean for the respective coordinate
        sampleMean = sum/numNodes
        sampleMeanList.append(sampleMean)

    print(sampleMeanList)

    #get (x-xMean)^2
    dateMinusSampleMS= [[0 for x in range(numNodes)] for y in range(coordSize)]
    for i in xrange(coordSize):

        for j in xrange(numNodes):
            #Get x-xMean squared
            val = nodes[j].coordinates[i] - sampleMeanList[i]
            dateMinusSampleMS[i][j] = (val**2)

    #Get the sum for each coord E((x-xMean)^2)
    sumECoord = []
    for i in xrange(coordSize):
        sum = 0
        for j in xrange(numNodes):
            sum += dateMinusSampleMS[i][j]

        sumECoord.append(sum)

    #Set the variance for each coordinate
    for i in xrange(coordSize):
        variance = (sumECoord[i]/(numNodes-1))

        varList.append(variance)

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
    numDim = 0
    for row in csv_file:

        #Convert the strings to floats
        for i in row:
            coordinates.append(float(i))

        numDim = len(row)

        nodes.append(Node(coordinates,clusterCnt,numDim))
        print(coordinates)

    #Get the max and min from the nodes
    maxList = getMaxList(nodes)
    minList = getMinList(nodes)

    #Get a list of variance for each dimension
    varianceList = getVarList(nodes)



    # #Create the list of clusters
    # clusters = []
    # for id in xrange(clusterCnt):
    #     clusters.append(Cluster(id, numDim), maxList,minList, varianceList))
    #
    # #Create the Data Class
    # allData = Data(nodes,clusters)
    #
    # allData.ExpectedMax()



#Run the main function
if __name__ == "__main__":
    main()

from Node import Node
from random import randint
from Cluster import Cluster
from Data import Data
import copy
import csv
import numpy as np

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

#Returns a list of initial cluster centers or means
def getInitialCenters(maxList,minList,numDim,clusterCnt):
    # Get 'average intervals' for each dimension
    # used for cluster mean initialization
    dim_intervals = []
    for i in xrange(numDim):
        if clusterCnt == 1:
            interval = 0
        else:
            interval = (maxList[i] - minList[i]) / (clusterCnt - 1)
        #print "interval ", i, "= ", interval
        dim_intervals.append(interval)

    # calculate initial 'means' or cluster centers
    cluster_centers = []
    print "INITIAL CENTERS"
    for i in xrange(clusterCnt):
        if i == 0:
            cur_center = copy.deepcopy(minList)
            print i, ":", cur_center
        else:
            for x, center in enumerate(cur_center):
                cur_center[x] += dim_intervals[x]
            print i, ":", cur_center
        cluster_centers.append(copy.deepcopy(cur_center))
    #print "initial centers: ", cluster_centers
    return cluster_centers


#Returns a list of random centers or means for clustes
def getNextCenters(maxList,minList,numDim,clusterCnt):
    cluster_center = []

    #Create a list of means for each dimension for every cluster
    for i in xrange(clusterCnt):
        mean = []
        for j in xrange(numDim):
            max = int(maxList[j])
            min = int(minList[j])

            #Random center between ranges
            cur_center = randint(min,max)
            mean.append(cur_center)

        cluster_center.append(mean)
    print "INITIAL CENTERS: ",cluster_center
    return cluster_center


# PART 2 Code
def calculateBIC(n, k, Lhat):
    result = np.log(n)*k - 2 * Lhat  # Lhat is already the log of the likelihood
    return result






############## Main Function ##################
def main():
    print("Running EM")

    # Input
    dataFile = raw_input("Input data file name: ")
    #dataFile = "sample_EM_data.csv"
    clusterCnt = raw_input("Number of clusters: ")
    restartNum = 10

    #Extract from CSV file
    file = open(dataFile)
    csv_file = csv.reader(file)

    #Create the list of nodes
    nodes = []

    numDim = 0

    data = []


    ###### BIC OR NOT #######
    if clusterCnt == 'X':
        # RUN BIC
        currentResult = 999999999  # very large number to start
        clusterCount = 1
        newIteration = True

        while (newIteration == True):
            # RUN EM
            clusterCnt = clusterCount
            # Random restarts
            for xx in xrange(restartNum):
                # Create Nodes
                for row in csv_file:
                    coordinates = []

                    # Convert the strings to floats
                    for i in row:
                        coordinates.append(float(i))

                    numDim = len(row)

                    nodes.append(Node(coordinates, clusterCnt, numDim))
                    # print(coordinates)

                # Get the max and min from the nodes
                maxList = getMaxList(nodes)
                minList = getMinList(nodes)

                # Get a list of variance for each dimension
                varianceList = getVarList(nodes)

                # Calculate initial centers or means
                if xx == 0:
                    initial_centers = getInitialCenters(maxList, minList, numDim, clusterCnt)
                else:
                    initial_centers = getNextCenters(maxList, minList, numDim, clusterCnt)

                # calculate initial cluster probability
                probability = 1 / float(clusterCnt)

                # Create the list of clusters
                clusters = []
                for id in xrange(clusterCnt):
                    meanList = initial_centers[id]
                    clusters.append(Cluster(id, numDim, meanList, varianceList, probability))

                # Create the Data Class
                allData = Data(nodes, clusters)

                newData = allData.ExpectedMax()

                # if(len(data) < 1 or ):
                data.append(newData)

            maxLogL = -1000000
            for i in xrange(len(data)):
                if maxLogL < data[i].logL[len(data[i].logL) - 1]:
                    maxInd = i
                    maxLogL = data[i].logL[len(data[i].logL) - 1]

            finalData = data[maxInd]
            #print"\n---------RESULTS----------"
            #print('There were ' + str(len(finalData.clusters)) + ' clusters.')
            #print('Run ' + str(maxInd) + ' had the greatest log likelihood at ' + str(maxLogL))
            #for i in xrange(len(finalData.clusters)):
                #print "CLUSTER ", i, ":", "Mean =", finalData.clusters[i].mean, "  Variance =", finalData.clusters[
                    #i].variance

            # BIC CALCULATION
            Lhat = maxLogL
            newResult = calculateBIC(len(nodes), clusterCount, Lhat)

            if (currentResult - newResult > 2):  # Hey, Keep going
                currentResult = newResult
                newIteration = True
                clusterCount = clusterCount + 1
            else:  # currentResult - newResult < 2, this means that it's not worth to continue
                currentResult = newResult
                newIteration = False

        print"\n---------RESULTS----------"
        print('There were ' + str(len(finalData.clusters)) + ' clusters.')
        print('Run ' + str(maxInd) + ' had the greatest log likelihood at ' + str(maxLogL))
        for i in xrange(len(finalData.clusters)):
            print "CLUSTER ", i, ":", "Mean =", finalData.clusters[i].mean, "  Variance =", finalData.clusters[i].variance
        print"BIC = ",currentResult


    else:
        # NORMAL EM
        clusterCnt = int(clusterCnt)

        # Random restarts
        for xx in xrange(restartNum):
            #Create Nodes
            for row in csv_file:
                coordinates = []

                #Convert the strings to floats
                for i in row:
                    coordinates.append(float(i))

                numDim = len(row)

                nodes.append(Node(coordinates,clusterCnt,numDim))
                # print(coordinates)

            #Get the max and min from the nodes
            maxList = getMaxList(nodes)
            minList = getMinList(nodes)

            #Get a list of variance for each dimension
            varianceList = getVarList(nodes)

            # Calculate initial centers or means
            if xx == 0:
                initial_centers = getInitialCenters(maxList,minList,numDim,clusterCnt)
            else:
                initial_centers = getNextCenters(maxList,minList,numDim,clusterCnt)

            # calculate initial cluster probability
            probability = 1/float(clusterCnt)

            #Create the list of clusters
            clusters = []
            for id in xrange(clusterCnt):
                meanList = initial_centers[id]
                clusters.append(Cluster(id, numDim,meanList, varianceList, probability))

            #Create the Data Class
            allData = Data(nodes,clusters)

            newData = allData.ExpectedMax()

            # if(len(data) < 1 or ):
            data.append(newData)



        maxLogL = -1000000
        for i in xrange(len(data)):
            if maxLogL < data[i].logL[len(data[i].logL)-1]:
                maxInd = i
                maxLogL = data[i].logL[len(data[i].logL)-1]

        finalData = data[maxInd]
        print"\n---------RESULTS----------"
        print('There were ' + str(len(finalData.clusters)) + ' clusters.')
        print('Run ' + str(maxInd) + ' had the greatest log likelihood at ' + str(maxLogL))
        for i in xrange(len(finalData.clusters)):
            print "CLUSTER ",i, ":", "Mean =", finalData.clusters[i].mean, "  Variance =", finalData.clusters[i].variance




#Run the main function
if __name__ == "__main__":
    main()

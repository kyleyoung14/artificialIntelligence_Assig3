import np

#Hey, this will not work. A bunch of these variables need to be replaced with actual shit

class BIC:
    #BIC is equal to:
    # ln(n)k - 2ln(Lhat)
    #
    # n    is the number of data points
    # k    is the number of clusters
    # Lhat is the resulting likelihood of the model with k clusters

    def calculateBIC(self, n, k, Lhat):
        result = np.log(n)*k - 2 * Lhat  # Lhat is already the log of the likelihood
        return result

    def findSmallestBIC(self):
        currentResult = 999999999  # very large number to start
        clusterCount = 1
        newIteration = True

        while(newIteration == True):
            Lhat = WhateverTheEMFunctionIs(clusterCount) #THIS NEEDS TO BE UPDATED WITH THE REAL FUNCTION CALL
            #newResult = np.log(n)*k - 2*LHat
            newResult = calculateBIC(n, k, Lhat)

            if(currentResult - newResult > 2):  # Hey, Keep going
                currentResult = newResult
                newIteration = True
                clusterCount = clusterCount + 1
            else: # currentResult - newResult < 2, this means that it's not worth to continue
                currentResult = newResult
                newIteration = False
        return clusterCount
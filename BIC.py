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
        result = np.log(n)*k - 2 * np.log(Lhat)
        return result

    def findSmallestBIC(self):
        Lhat = (insertwhateverEMfunctionis)(1)
        current = calculateBIC(n, 1, Lhat) #replace these variables later
        currentClusters = n

        for i in range (2, n / 2):
            Lhat = (insertwhateverEMfunctionis)(i)
            new = calculateBIC(n, i, Lhat)
            if (new < current):
                current = new
                currentClusters = i

        return currentClusters
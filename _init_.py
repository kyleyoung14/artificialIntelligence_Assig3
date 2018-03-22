import csv

#Main Function
def main():
    print("Running EM")

    #Take in input
    dataFile = raw_input("Input data file name: ")
    clusterCnt = int(raw_input("Number of clusters: "))

    #Extract from CSV file
    file = open(dataFile)
    csv_file = csv.reader(file)

    points = []
    for row in csv_file:
        points.append(row)

    print points



#Run the main function
if __name__ == "__main__":
    main()

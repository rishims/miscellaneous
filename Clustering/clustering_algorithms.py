# -*- coding: utf-8 -*-
"""
@author: Rishi Shah
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Helper Methods

def calcAverages(groups):
    averages = []
    for group in groups:
        total = 0
        for name in group:
            total += data[name]
        average = total / len(group)
        averages.append(average)
    return averages

def makeDistanceMatrix(data):
    distanceTriangle = [] #This will look like a lower diagonal matrix
    for i in range(1,len(data)): #for each instance but the first
        distances = [] #this will be a list of distances to location i
        for j in range(0,i): #only need to measure distance for objects before i
            distances.append(np.abs(data[i] - data[j]))
        distanceTriangle.append(distances)
    return distanceTriangle

def updateMatrix_Single(distances, i, j):
    #create a new row
    row = []
    n = len(distances)+1
    for col in range(n):
        if col == i+1 or col == j:
            continue
        if col > i+1:
            row.append(min(distances[col - 1][i+1], distances[col-1][j]))
        elif col > j:
            row.append(min(distances[i][col], distances[col-1][j]))
        else:
            row.append(min(distances[i][col], distances[j-1][col]))        
    #delete old cols
    for r in range(i+1,n-1):
        del distances[r][i+1]
    for r in range(j,n-1):
        del distances[r][j]
    #delete old rows
    del distances[i]
    del distances[max(j-1,0)]    
    #Add row to Table
    distances.append(row)
    return distances

def updateMatrix_Complete(distances, i, j):
    #create a new row
    row = []
    n = len(distances)+1
    for col in range(n):
        if col == i+1 or col == j:
            continue
        if col > i+1:
            row.append(max(distances[col - 1][i+1], distances[col-1][j]))
        elif col > j:
            row.append(max(distances[i][col], distances[col-1][j]))
        else:
            row.append(max(distances[i][col], distances[j-1][col]))        
    #delete old cols
    for r in range(i+1,n-1):
        del distances[r][i+1]
    for r in range(j,n-1):
        del distances[r][j]
    #delete old rows
    del distances[i]
    del distances[max(j-1,0)]    
    #Add row to Table
    distances.append(row)
    return distances

def updateGroups(groups, i, j):
    #Combine two groups
    #because table excludes first row add one to i when accessing groups which doesn't exclude first row
    newGroup = groups[i+1]+groups[j]
    #remove the old groups, start with higher number
    del groups[i+1]
    del groups[j]
    #add in the new group
    groups.append(newGroup)
    #print(groups)
    return groups

# Define a function to initialize k centroids
def initialize1D(data, k):
    centroids = []    
    # Get x range of values as arrays
    x_range = np.linspace(min(data), max(data), int(max(data) - min(data) + 1))    
    # Create k centroids as tuples
    for i in range(k):
        x = np.random.choice(x_range)
        centroid = x
        centroids.append(centroid)        
    # Return initialized centroids
    return centroids

# Define a function to assign each data point to its closest centroid
def assignment1D(data, centroids):
    # Notes which cluster each point has been assigned to (0,1,2,3,4)
    clusters = []
    distances = []
    # Find closest cluster for each point:
    for i in range(len(data)):
        x = data[i]
        # Find closest cluster and calculate the distance from the point to the cluster
        cluster = np.argmin([np.sqrt( (x - centroid) ** 2) for centroid in centroids])
        distance = np.min([np.sqrt((x - centroid) ** 2) for centroid in centroids])
        clusters.append(cluster)
        distances.append(distance)    
    # Calculate total squared distance
    tot_sqdist = sum([x ** 2 for x in distances])    
    # Return closest clusters and the total squared distance
    return clusters, tot_sqdist

# Define a function to update centroid positions
def update1D(data, clusters, old_centroids, k):
    # Store new centroid calculations
    centroids = []    
    # Calculate x positions of center of each centroid (0,1,2,3,4)
    for i in range(k):
        # Cardinality of cluster k
        cardinality = clusters.count(i)        
        # Obtain x-coords for all points assigned to cluster k
        x_coords = []        
        for j in range(len(clusters)):
            if clusters[j] == i:
                x_coords.append(data[j])                
        # Calculate x positions of each cluster centroid
        # Account for centroids that may not have any assigned points 
        if cardinality > 0:
            x = sum(x_coords) / cardinality
            centroid = x
            centroids.append(centroid)
        else:
            centroid = old_centroids[i]
            centroids.append(centroid)    
    return centroids

def initialize2D(attribute2, attribute1, k):
    centroids = []    
    # Get x and y range of values as arrays
    x_range = np.linspace(min(attribute2), max(attribute2), int(max(attribute2) - min(attribute2) + 1))
    y_range = np.linspace(min(attribute1), max(attribute1), int(max(attribute1) - min(attribute1) + 1))    
    # Create k centroids as tuples
    for i in range(k):
        x = np.random.choice(x_range)
        y = np.random.choice(y_range)
        centroid = (x, y)
        centroids.append(centroid)        
    # Return initialized centroids
    return centroids

# Define a function to assign each data point to its closest centroid
def assignment2D(attribute2, attribute1, centroids):
    # Notes which cluster each point has been assigned to (0,1,2,3,4)
    clusters = []
    distances = []
    # Find closest cluster for each point:
    for i in range(len(attribute2)):
        x = attribute2[i]
        y = attribute1[i]
        # Find closest cluster and calculate the distance from the point to the cluster
        cluster = np.argmin( [np.sqrt( (x - centroid[0]) ** 2 + (y - centroid[1]) ** 2) for centroid in centroids] )
        distance = np.min( [np.sqrt( (x - centroid[0]) ** 2 + (y - centroid[1]) ** 2) for centroid in centroids] )
        clusters.append(cluster)
        distances.append(distance)    
    # Calculate total squared distance
    tot_sqdist = sum([x ** 2 for x in distances])    
    # Return closest clusters and the total squared distance
    return clusters, tot_sqdist

# Define a function to update centroid positions
def update2D(attribute2, attribute1, clusters, old_centroids, k):
    # Store new centroid calculations
    centroids = []    
    # Calculate x and y positions of center of each centroid (0,1,2,3,4)
    for i in range(k):
        # Cardinality of cluster k
        cardinality = clusters.count(i)        
        # Obtain x- and y-coords for all points assigned to cluster k
        x_coords = []
        y_coords = []
        for j in range(len(clusters)):
            if clusters[j] == i:
                x_coords.append(attribute2[j])
                y_coords.append(attribute1[j])                
        # Calculate x and y positions of each cluster centroid
        # Account for centroids that may not have any assigned points 
        if cardinality > 0:
            x = sum(x_coords) / cardinality
            y = sum(y_coords) / cardinality
            centroid = (x, y)
            centroids.append(centroid)
        else:
            centroid = old_centroids[i]
            centroids.append(centroid)
    
    return centroids

# Clustering Methods

def singleLinkage(data, k):
    groups = [[name] for name in data.index]
    distances = makeDistanceMatrix(data)
    n = len(groups)
    while n > k:
        #find the index of the minimum distance from table
        minRow = min(distances,key = min)
        i = distances.index(minRow)
        minValue = min(minRow)
        j = minRow.index(minValue)
        groups = updateGroups(groups, i, j)
        distances = updateMatrix_Single(distances, i, j)                
        n = len(groups)
    return groups

def completeLinkage(data, k):
    groups = [[name] for name in data.index]
    distances = makeDistanceMatrix(data)
    #print(distances)
    n = len(groups)
    while n > k:
        #find the index of the minimum distance from table
        minRow = min(distances,key = min)
        #print(minRow)
        i = distances.index(minRow)
        #print(i)
        minValue = min(minRow)
        #print(minValue)
        j = minRow.index(minValue) #Here is where the min distance is found
        #print(j)
        groups = updateGroups(groups, i, j)
        #print(groups)
        distances = updateMatrix_Complete(distances, i, j)
        #print(distances)
                
        n = len(groups)
    return groups

def averageLinkage(data, k):
    # Make sure data is sorted
    data = data.sort_values()
    groups = [[d] for d in data.index]
    while len(groups) > k:
        averages = calcAverages(groups)
        # Calculate distances between centroids
        distances = []
        for i in range(len(groups)-1):
            distance = averages[i+1] - averages[i]
            distances.append(distance)
        # Find minimum distances between centroids
        minValue = min(distances)
        index = distances.index(minValue)
        # Combine groups with closest centroids
        groups[index].extend(groups[index+1])
        groups.pop(index+1)    
    return groups

# Define a function to execute the K-means 1D algorithm
# Returns the centroids and clusters for the best run
def kmeans1D(data, k, numtrials):
    # Initialize vars to hold the data for our best run (run that minimizes tot_sqdist)
    min_dist = float('inf')
    best_clusters = []
    best_centroids = []
    
    for i in range(numtrials):
        # Step 1: initialization of centroids
        centroids = initialize1D(data, k)
        
        # Create dummy cluster lists for first iteration
        old_clusters = [0] * len(data)
        clusters = [1] * len(data)
        old_centroids = [0] * k
        
        # Keep updating centroids until no cluster assignments change
        while clusters != old_clusters:
            # Update clusters and centroids
            old_clusters = list(clusters)
            old_centroids = list(centroids)
            
            # Step 2: assignment of points to centroids
            clusters, tot_sqdist = assignment1D(data, centroids)
            
            # Step 3: update the positions of the centroids
            centroids = update1D(data, clusters, old_centroids, k)
            
        # Save information of the trial that minimizes tot_sqdist:
        if tot_sqdist < min_dist:
            best_clusters = clusters
            best_centroids = centroids
            min_dist = tot_sqdist
    
    return best_clusters, best_centroids

# Define a function to execute the K-means 2D algorithm
# Returns the centroids and clusters for the best run
def kmeans2D(attribute2, attribute1, k, numtrials):
    # Initialize vars to hold the data for our best run (run that minimizes tot_sqdist)
    min_dist = float('inf')
    best_clusters = []
    best_centroids = []
    
    for i in range(numtrials):
        # Step 1: initialization of centroids
        centroids = initialize2D(attribute2, attribute1, k)
        
        # Create dummy cluster lists for first iteration
        old_clusters = [0] * len(attribute2)
        clusters = [1] * len(attribute2)
        old_centroids = [(0,0)] * k
        
        # Keep updating centroids until no cluster assignments change
        while clusters != old_clusters:
            # Update clusters and centroids
            old_clusters = clusters
            old_centroids = centroids
            
            # Step 2: assignment of points to centroids
            clusters, tot_sqdist = assignment2D(attribute2, attribute1, centroids)
            
            # Step 3: update the positions of the centroids
            centroids = update2D(attribute2, attribute1, clusters, old_centroids, k)
            
        # Save information of the trial that minimizes tot_sqdist:
        if tot_sqdist < min_dist:
            best_clusters = clusters
            best_centroids = centroids
            min_dist = tot_sqdist
    
    return best_clusters, best_centroids

# Start Program and open file

print("\nRishi's Clustering Program.\n")
filename = input("Please enter the data-file's name: ")
dataFile = pd.read_csv(filename, index_col = 0)
### Allow User to select attribute
print("\nHere is a list of attributes:\n")
for name in dataFile.columns:
    print(name, end = "    ")
attribute = input("\nWhich attribute would you like to cluster?  ")
#attribute = 'Value'
data = dataFile.loc[:][attribute]
dimension = int(input("\nPlease enter the number of dimensions (1 or 2(only available for k-means)): "))
if dimension == 2:
    attribute2 = input("Please enter the second attribute that you wish to cluster: ")
    data2 = dataFile.loc[:][attribute2]
### Potentially plot data
toPlot = input("Would you like to plot this data? (y,n)  ")

if toPlot.lower()[0] == 'y' and dimension == 1:
    plt.hist(data)
    plt.show()
elif toPlot.lower()[0] == 'y' and dimension == 2:
    plt.scatter(data, data2)
    plt.xlabel(attribute)
    plt.ylabel(attribute2)
    plt.show()

 
### Select the Clustering Technique
"\nWhich clustering technique would you like to use?"
print("\n(S)ingle linkage\n(C)omplete linkage\n(A)verage linkage\n(K)-means")
clusterTechnique = input("\nWhich clustering technique would you like to use? ").lower()
#clusterTechnique = 's'
k = int(input("How many clusters? "))
#k = 4
if clusterTechnique == 's':
    groups = singleLinkage(data, k)
elif clusterTechnique == 'c':
    groups = completeLinkage(data, k)
elif clusterTechnique == 'a':
    groups = averageLinkage(data, k)
elif clusterTechnique == 'k':
    numTrials = 100
    if dimension == 1:
        best_clusters, best_centroids = kmeans1D(data, k, numTrials)
    elif dimension == 2:
        best_clusters, best_centroids = kmeans2D(data, data2, k, numTrials)
print("\nThe groups are:")
if clusterTechnique == 'k':
    for i in range(k):
        print("\n")
        for j in range(len(data)):
            if(best_clusters[j] == i and dimension == 1):
                print(str(data.index[j]) + ": " +str(round(data[j],5)))
            elif(best_clusters[j] == i and dimension == 2):
                print(str(data.index[j]) + ": " +str(round(data[j],5)) + ", ", str(round(data2[j],5)))
else:
    for g in groups:
        print()
        for name in g:
            print(name + ":", data[name])
toPlot = input("Would you like to plot the groups? (y/n)  ")
toPlot = toPlot.lower()[0]
temp = []
if toPlot == 'y' and clusterTechnique == 'k' and dimension == 1:
    for i in range(k):
        for j in range(len(data)):
            if(best_clusters[j] == i):
                temp.append(data[j])
        plt.hist(temp)
        temp.clear()
    plt.show()
elif toPlot == 'y' and clusterTechnique == 'k' and dimension == 2:
    plt.scatter(data, data2, marker = 'o', c = best_clusters, cmap = 'Set1', alpha = 0.75)
    # Plot each centroid
    for centroid in best_centroids:
        x = centroid[0]
        y = centroid[1]
        plt.scatter(x, y, s=300, c='black', marker=(5,1))
    plt.xlabel(attribute)
    plt.ylabel(attribute2)
elif toPlot == 'y':
    for g in groups:
        groupData = [data[name] for name in g]
        plt.hist(groupData)
    plt.show()

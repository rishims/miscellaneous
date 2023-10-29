# Miscellaneous
This repository contains code for some miscellaneous projects I have conducted either for class or for fun! 

Note: this is not a complete collection of my work and I am still in the process of adding more projects to this repository!

## Password Generator
This is a random password generator I programmed in Java that creates a random password based on user provided specifications. A good way to get comfortable with ASCII!

## Spotify Listens
This was my final project for my Data Analysis & Exploration class, where I looked at relationships between variables such as track length, danceability, energy, and more and determined if these variables could be used to predict the popularity or number of listens for a track on Spotify. I used statistical techniques such as bootstrapping, ANOVAS, linear models, and regression to accomplish this.

## Clustering
In this project, the main task I attempted was to cluster a set of data according to an attribute. This was achieved through a variety of clustering algorithms, from agglomerative hierarchical clustering methods to k-means clustering. The methodology of my main and helper functions is explained below.

Note: The purpose of the program is to cluster data. As such, minimal error checking is implemented in the program as this may crowd the code and slow the clustering process. It is assumed the user will obey the provided instructions when entering input in the terminal.

You can try the program using the students.csv file in the folder!

Clustering Methods:

singleLinkage Clustering:
	Summary: clusters data according to the single linkage algorithm. Distance is measured as nearest points between groups
	input: data, k
		data is a pandas series, this data will be clustered
		k is the number of clusters
	output: groups
		groups is a list of index values, these can be used to access the data in a pandas dataframe
		
completeLinkage Clustering:
	Summary: clusters data according to the complete linkage algorithm. Distance is measured as farthest two data points within groups
	input: data, k
		data is a pandas series, this data will be clustered
		k is the number of clusters
	output: groups
		groups is a list of index values, these can be used to access the data in a pandas dataframe
		
averageLinkage Clustering:
	Summary: clusters data according to the average linkage algorithm. Distance is measured between the averages of two groups
	input: data, k
		data is a pandas series, this data will be clustered
		k is the number of clusters
	output: groups
		groups is a list of index values, these can be used to access the data in a pandas dataframe
		
kMeans1D Clustering: 
	Summary: iterates through the k-means algorithm until no data changes. Uses Euclidean distance to group data according
		to nearest centroid, then updates centroids to mean of group. 
	input: data, k, numTrials
		data is a pandas series, this data will be clustered
		k is the number of clusters
		numTrials is the number of iteration of the k-means algorithm to complete. Although the algorithm will continue until
		the centroids and clusters no longer change this is a safety precaution introduced to reduce waiting time or to prevent possible errors
	output: best_clusters, best_centroids
		best_clusters is a list of indices assigned to a specific cluster. best_centroids is a list of the optimal centroids 
		found when clustering the data, used when plotting

kMeans2D Clustering: 
	Summary: iterates through the k-means algorithm until no data changes. Uses Euclidean distance to group data according
		to nearest centroid, then updates centroids to mean of group. 
	input: attribute1, attribute2, k, numTrials
		attribute1 is a pandas series, this is one set of data that will be clustered
		attribute2 is a pandas series, this the other set of data that will be clustered in conjunction with attribute1
		k is the number of clusters
		numTrials is the number of iteration of the k-means algorithm to complete. Although the algorithm will contiue until
		the centroids and clusters no longer change this is a safety precaution introduced to reduce waiting time or to prevent possible errors
	output: best_clusters, best_centroids
		best_clusters is a list of indices assigned to a specific cluster. best_centroids is a list of the optimal centroids 
		found when clustering the data, used when plotting		
		
Helper Functions:

makeDistanceMatrix:
	Summary: Creates a lower triangular matrix of distances
	input: data
		data is a pandas series. The distance matrix is calculated according to the distances between each data point in data
	output: distanceTriangle
		A lower triangular matrix of distances
		
updateMatrix_Single
	Summary: Updates a distance matrix after joining two groups
	input distances, i, j
		distances is a lower triangular distance matrix that needs to be updated
		i and j are indices of the two groups to be joined, i must be greater than or equal to j or errors will occur
	output: distances
		distances is returned after joining the two groups

updateMatrix_Complete
	Summary: Updates a distance matrix after joining two groups, utilizing the max distances instead of the min distances, in accordance with the complete linkage algorithm.
	input distances, i, j
		distances is a lower triangular distance matrix that needs to be updated
		i and j are indices of the two groups to be joined, i must be greater than or equal to j or errors will occur
	output: distances
		distances is returned after joining the two groups
		
updateGroups
	Summary: A list of groups is kept, this function updates this list
	input: groups, i, j
		groups is a list of lists, the inner lists are index names. Each inner list is a group
	output: groups
		after updating groups, it is returned

calcAverages
	Summary: Calculates the averages of each new group or cluster created by the average linkage method
	input: groups
		groups is a list of the lists, with the inner lists being the index names. In other words, groups is the list of clusters created so far
	output: averages
		averages is a list that contains the average of each group passed into calcAverages

initialize1D
	Summary: Initializes "k" centroids randomly within the set of provided points in the passed data
	input: data, k
		data is a pandas series, containing the data that is to be clustered
		k is the number of clusters the data is to be clustered into
	output: centroids
		centroids is a list of the randomly chosen centroids within data. These centroids are actual values within data

assignment1D
	Summary: Assigns the values of data to its nearest centroid, calculating the distance from each point to its nearest cluster via a Euclidean approach (sum of squared distances)
	input: data, centroids
		data is a pandas series, containing the data that is to be clustered
		centroids is a list of randomly chosen centroids within data. These centroids are actual values within data
	output: clusters, tot_sqdist
		clusters is a list of the created groups based on proximity of a point to a centroid. tot_sqdist is the total squared distance,
		used to determine the clusters and centroids that minimize this distance
  
update1D
	Summary: Updates the centroid values based on the average of the clusters and the k-means algorithm
	input: data, clusters, old_centroids, k
		data is a pandas series, containing the data that is to be clustered
		clusters is a list of the created groups based on proximity of a point to a centroid
		old_centroids is a list of the centroids created on the last iteration, used to check for any changes
		k is the number of clusters the data is to be clustered into
	output: centroids
		centroids is the updated list of centroids, recalculated using the 1D k-means algorithm

initialize2D
	Summary: Initializes "k" centroids randomly within the set of provided points in the passed data
	input: attribute1, attribute2, k
		attribute1 is a pandas series, this is one set of data that will be clustered
		attribute2 is a pandas series, this the other set of data that will be clustered in conjunction with attribute1
		k is the number of clusters the data is to be clustered into
	output: centroids
		centroids is a list of the randomly chosen centroids within data. These centroids are actual values within data

assignment2D
	Summary: Assigns the values of data to its nearest centroid, calculating the distance from each point to its nearest cluster via a Euclidean approach (sum of squared distances)
	input: attribute1, attribute2, centroids
		attribute1 is a pandas series, this is one set of data that will be clustered
		attribute2 is a pandas series, this the other set of data that will be clustered in conjunction with attribute1
		centroids is a list of randomly chosen centroids within data. These centroids are actual values within data
	output: clusters, tot_sqdist
		clusters is a list of the created groups based on proximity of a point to a centroid. tot_sqdist is the total squared distance,
		used to determine the clusters and centroids that minimize this distance

update2D
	Summary: Updates the centroid values based on the average of the clusters and the 2D k-means algorithm
	input: attribute1, attribute2, clusters, old_centroids, k
		attribute1 is a pandas series, this is one set of data that will be clustered
		attribute2 is a pandas series, this the other set of data that will be clustered in conjunction with attribute1
		clusters is a list of the created groups based on proximity of a point to a centroid
		old_centroids is a list of the centroids created on the last iteration, used to check for any changes
		k is the number of clusters the data is to be clustered into
	output: centroids
		centroids is the updated list of centroids, recalculated using the 2D k-means algorithm

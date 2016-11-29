'''Python DBSCAN clustering algorithm implementation.

Supports a sorted history list of tuples, clustering on the first two values 
in the tuple. These values are interpreted as (time, price). 

To use:
1. Build history list sorted by time. Ex:
history = [(1, 20.00, ...), (2, 20.01, ...), (10, 20.10, ...), 
           (11, 20.08, ...)]
2. Call detect_clusters(history, timeDist, priceDist, minPoints) with desired 
constraints. 
3. detect_clusters returns a list of lists, where each sublist is a cluster.
'''

def detect_clusters(history, timeDist, priceDist, minPoints):
    '''Finds clusters in a list of tuples.
    
    history is a list of tuples of length >= 2, sorted by index 0 of each 
    tuple, and the indices of each tuple is interpreted as (time, price, ...)
    
	timeDist is the maximum distance in time a point can be to remain in a 
    cluster
    
	priceDist is the maximum distance in price a point can be to remain in a 
    cluster
    
	minPoints is the minimum number of points in a cluster
    '''
    
    def get_neighbors(point):
        #Point can be a tuple of length >= 2
        pTime = point[0]
        pPrice = point[1]
        minTime = pTime - timeDist
        maxTime = pTime + timeDist
        minPrice = pPrice - priceDist
        maxPrice = pPrice + priceDist
        neighbors = []
        for neighbor in history:
            nTime = neighbor[0]
            nPrice = neighbor[1]
            if (minTime <= nTime <= maxTime) 
            and (minPrice <= nPrice <= maxPrice):
                neighbors.append(neighbor)
        return neighbors
    
    def grow_cluster(cluster, neighbors):
        for neighbor in neighbors:
            #Only work on neighbors not yet added to the cluster
            if neighbor not in cluster:
                cluster.append(neighbor)
                extendedNeighbors = get_neighbors(neighbor)
                #Only add more neighbors if cluster density is satisfied
                if len(extendedNeighbors) >= minPoints:
                    grow_cluster(cluster, extendedNeighbors)
    
    clusterList = []
    for point in history:
        #Flatten the known clusters in clusterList to check if point has been 
        #clustered already
        flatClusterList = [point for cluster in clusterList for point in cluster]
        if point not in flatClusterList:
            #Check if this point has enough neighbors to be in a cluster
            neighbors = get_neighbors(point)
            if len(neighbors) >= minPoints:
                cluster = [point]
                grow_cluster(cluster, neighbors)
                clusterList.append(cluster)
    return clusterList

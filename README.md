# Clustering
Python DBSCAN clustering algorithm implementation.

Supports a sorted history list of tuples, clustering on the first two values in the tuple. These values are interpreted as (time, price). 

To use:
1. Build history list sorted by time. Ex: history = [(1, 20.00, ...), (2, 20.01, ...), (10, 20.10, ...), (11, 20.08, ...)]
2. Call detect_clusters(history, timeDist, priceDist, minPoints) with desired constraints. 
3. detect_clusters returns a list of lists, where each sublist is a cluster.

Written in Python 3.5.2

from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

if __name__ == "__main__":
    """
    Do something
    """
    # Create graph
    g = Graph()
    g.addEdge('u', 'v', 2)
    g.addEdge('u', 'w', 5)
    g.addEdge('u', 'x', 1)
    g.addEdge('v', 'x', 2)
    g.addEdge('v', 'w', 3)
    g.addEdge('x', 'w', 3)
    g.addEdge('x', 'y', 1)
    g.addEdge('y', 'w', 1)
    g.addEdge('y', 'z', 1)
    g.addEdge('z', 'w', 5)
    # run Dijkstra algorithm
    dijkstra(g, g.getVertex('u'))
    # Print shortest paths
    print(g)

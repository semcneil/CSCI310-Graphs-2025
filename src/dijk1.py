from pythonds.graphs import PriorityQueue, Graph, Vertex
from pdb import set_trace

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

def printPaths(aGraph):
    """
    Prints the shortest paths found by Dijkstra starting at start
    """
    # Cycle through all the vertices
    for v in aGraph:
        print(f'{v.getId()}:{v.getDistance()} p = ', end='')
    # Trace path to starting vertex, starting vertex will have dist of 0 and own predecessor
        # Cycle through v.getPred() to list path
        w = v.getPred()
        while w:
            print(f'{w.getId()} - ', end='')
            w = w.getPred()
        print()


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
    printPaths(g)

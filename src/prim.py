from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys
from pdb import set_trace

class BiGraph(Graph):
    """
    Adds a method to create edges in both directions
    """
    def __init__(self):
        super().__init__()
    
    def addBiEdge(self,f,t,cost=0):
        self.addEdge(f,t,cost)
        self.addEdge(t,f,cost)
    

def prim(G,start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
          newCost = currentVert.getWeight(nextVert)
          if nextVert in pq and newCost<nextVert.getDistance():
              nextVert.setPred(currentVert)
              nextVert.setDistance(newCost)
              pq.decreaseKey(nextVert,newCost)

def printPrim(myGraph):
    """
    Prints the shortest paths from Dijkstra's algorithm
    """
    # Find path from each vertex to starting vertex and distance
    for v in myGraph:
      print(f'{v.getId()}:{v.getDistance()}', end='')
      w = v.getPred()
      while w:
          print(f'->{w.getId()}', end='')
          w = w.getPred()
      print()
    #   set_trace() 


if __name__ == "__main__":
    """
    Do something
    """
    # Create graph
    g = BiGraph()
    # g.addBiEdge('u', 'v', 2)
    # g.addBiEdge('u', 'w', 5)
    # g.addBiEdge('u', 'x', 1)
    # g.addBiEdge('v', 'x', 2)
    # g.addBiEdge('v', 'w', 3)
    # g.addBiEdge('x', 'w', 3)
    # g.addBiEdge('x', 'y', 1)
    # g.addBiEdge('y', 'w', 1)
    # g.addBiEdge('y', 'z', 1)
    # g.addBiEdge('z', 'w', 5)
    g.addBiEdge('A', 'B', 2)
    g.addBiEdge('A', 'C', 3)
    g.addBiEdge('B', 'C', 1)
    g.addBiEdge('B', 'D', 1)
    g.addBiEdge('B', 'E', 4)
    g.addBiEdge('C', 'F', 5)
    g.addBiEdge('D', 'E', 1)
    g.addBiEdge('E', 'F', 1)
    g.addBiEdge('F', 'G', 1)
    # run Prim's Spanning Tree algorithm
    prim(g, g.getVertex('A'))
    # Print shortest paths
    printPrim(g)

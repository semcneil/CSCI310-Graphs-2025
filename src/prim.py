from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys
from pdb import set_trace


class myVertex(Vertex):
    """Adds a routing table to the vertex
    """
    def __init__(self, num):
        super().__init__(num)
        self.route = []

    def addRoute(self, nextVert):
        self.route.append(nextVert)

    def printRoute(self):
        for v in self.route:
            print(v.getId(), end=",")
        print()

class BiGraph(Graph):
    """
    Add bidirectional edge creation
    """
    def __init__(self):
        super().__init__()
    
    def addBiEdge(self,f,t,cost=0):
        """
        Adds a bidirectional edge
        """
        self.addEdge(f, t, cost)
        self.addEdge(t, f, cost)

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = myVertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def createRoutes(self):
        """
        Populate routes for all nodes assuming prim has been run
        """


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
    Prints the shortest paths from Prim's algorithm
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
    # g.addBiEdge('A', 'B', 2)
    g.addBiEdge('B', 'C', 1)
    g.addBiEdge('B', 'D', 1)
    g.addBiEdge('B', 'E', 4)
    g.addBiEdge('C', 'F', 5)
    g.addBiEdge('D', 'E', 1)
    g.addBiEdge('E', 'F', 1)
    g.addBiEdge('F', 'G', 1)
    # run Prim's algorithm algorithm
    prim(g, g.getVertex('A'))
    # Print Prim's results
    printPrim(g)

    for n in g:
        print(f'{n.getId()}: ', end='')
        n.printRoute()
    # myV = g.getVertex('A')
    # myV.printRoute()

    # v1 = myVertex('Z')
    # v1.addRoute(g.getVertex('A'))
    # v1.addRoute(g.getVertex('B'))
    # v1.addRoute(g.getVertex('C'))
    # v1.printRoute()
    set_trace()

"""
graphs1.py
====================================
This plays with the graph data structures from:
https://runestone.academy/ns/books/published/pythonds/Graphs/Implementation.html

| Author: Seth McNeill
| Date: 2025 November 06
"""

# import pdb

class Vertex:
    """
    The class for a vertex of a graph.
    
    Parameters
    ----------
    key 
        Typically a string for the name of the Vertex
    
    Attributes
    ----------
    id
        The vertex's name

    connectedTo : dict
        A dictionary of vertices that self is connected to and the weight of each connection
        
    """
    def __init__(self,key):
        """
        Initialize a new Vertex instance.
        
        Parameters
        ----------
        key
            The vertex's name
        """
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        """
        What type should nbr be?
        Is there a way to tell?
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library

       to import this file as a library: 
       from src.graphs1 import Vertex, Graph
    """
    v1 = Vertex('One')
    print(v1)
    v1.addNeighbor('two',2)
    v1.addNeighbor('three',3)
    v1.getConnections()
    v1.getId()
    print(v1.id)
    print(v1.connectedTo)
    print(v1)  # what do the errors tell us?

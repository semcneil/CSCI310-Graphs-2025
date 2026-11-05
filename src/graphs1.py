"""
graphs1.py
====================================
This plays with the graph data structures from:
https://runestone.academy/ns/books/published/pythonds/Graphs/Implementation.html

| Author: Seth McNeill
| Date: 2025 November 06
"""

import matplotlib.pyplot as plt
import networkx as nx
import pdb

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
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        retStr = ''
        for v in self:
            for w in v.getConnections():
                retStr += f"Vertex {v.getId()} is connected to {w.getId()} with weight {v.getWeight(w)}\n"
                # retStr += "( %s , %s )\n" % (v.getId(), w.getId())
        return retStr

def plot_graph(graph_obj):
    """
    Converts a pythonds Graph object to a NetworkX DiGraph and plots it with Matplotlib.
    Edges are truncated so arrowheads land precisely at the node borders.

    Written by Gemini 2026 October 27.
    """
    nx_graph = nx.DiGraph()

    # Add vertices and weighted edges
    for vertex in graph_obj:
        v_id = vertex.getId()
        nx_graph.add_node(v_id)
        for nbr in vertex.getConnections():
            nbr_id = nbr.getId()
            weight = vertex.getWeight(nbr)
            nx_graph.add_edge(v_id, nbr_id, weight=weight)

    pos = nx.circular_layout(nx_graph)
    node_size = 1200  # Store node size to share between nodes and edges

    plt.figure(figsize=(8, 6))

    # 1. Draw nodes
    nx.draw_networkx_nodes(
        nx_graph,
        pos,
        node_color="skyblue",
        node_size=node_size
    )

    # 2. Draw labels
    nx.draw_networkx_labels(
        nx_graph,
        pos,
        font_size=12,
        font_family="sans-serif"
    )

    # 3. Draw edges with node_size specified so arrowheads stop at node boundaries
    nx.draw_networkx_edges(
        nx_graph,
        pos,
        edgelist=nx_graph.edges(),
        arrowstyle="-|>",
        arrowsize=20,
        edge_color="gray",
        node_size=node_size,          # Ensures arrows don't clip under nodes
        connectionstyle="arc3,rad=0.15"  # Curved edges for bidirectional links
    )

    # 4. Draw edge weight labels
    edge_labels = nx.get_edge_attributes(nx_graph, "weight")
    nx.draw_networkx_edge_labels(
        nx_graph,
        pos,
        edge_labels=edge_labels,
        font_size=11,
        label_pos=0.3
    )

    plt.title("Directed Weighted Graph (Figure 2)")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library

       to import this file as a library: 
       from src.graphs1 import Vertex, Graph
    """
    # v1 = Vertex('One')
    # print(v1)
    # v1.addNeighbor('two',2)   # incorrect since needs to be a Vertex added
    # v1.addNeighbor('three',3)
    # # print(v1)
    # v1.getConnections()
    # v1.getId()
    # print(v1.id)
    # print(v1.connectedTo)
    # print(v1)  # what do the errors tell us?
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    print('*'*20)
    print(g)
    plot_graph(g)
    pdb.set_trace()

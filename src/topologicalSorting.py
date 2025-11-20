

from pythonds.graphs import Graph
from pdb import set_trace

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
    
    def __str__(self):
        retStr = ''
        for v in self:
            for w in v.getConnections():
                retStr += f"Vertex {v.getId()} ({v.getDiscovery()}/{v.getFinish()}) is connected to {w.getId()} with weight {v.getWeight(w)}\n"
                # retStr += "( %s , %s )\n" % (v.getId(), w.getId())
        return retStr

if __name__ == "__main__":
    """
    Runs if script
    """
    # create graph
    pk = DFSGraph()
    # pk.addVertex('milk')
    # pk.addVertex('mix')
    # pk.addVertex('pour')
    # pk.addVertex('bubble')
    # pk.addVertex('eat')
    pk.addEdge('milk', 'mix')
    pk.addEdge('mix', 'pour')
    pk.addEdge('pour', 'bubble')
    pk.addEdge('bubble', 'eat')
    pk.addEdge('egg', 'mix')
    pk.addEdge('oil', 'mix')
    pk.addEdge('mix', 'syrup')
    pk.addEdge('griddle', 'pour')
    pk.addEdge('syrup', 'eat')
    pk.dfs()


    print(pk)
    set_trace()
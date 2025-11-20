from pythonds.graphs import Graph

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
                retStr += f"Vertex {v.getId()} ({v.getDiscovery()}/{v.getFinish()}) is connected to {w.getId()} ({w.getDiscovery()}/{w.getFinish()})\n"
                # retStr += "( %s , %s )\n" % (v.getId(), w.getId())
        return retStr
    
    def orderByFinish(self):
        resList = []
        for v in self:
            c = v.getFinish()
            resList.append((c,v))
        resList.sort(key=lambda x: x[0])
        resList.reverse()
        return [[y[1].getId(),y[1].getFinish()] for y in resList]


if __name__ == "__main__":
    """
    Run as script
    """

    pk = DFSGraph() # created the empty graph
    pk.addEdge('griddle', 'pour')
    pk.addEdge('milk', 'mix')
    pk.addEdge('eggs', 'mix')
    pk.addEdge('oil', 'mix')
    pk.addEdge('mix', 'syrup')
    pk.addEdge('mix', 'pour')
    pk.addEdge('syrup', 'eat')
    pk.addEdge('pour', 'bubble')
    pk.addEdge('bubble', 'eat')

    pk.dfs()

    print(pk)

    print(pk.orderByFinish())
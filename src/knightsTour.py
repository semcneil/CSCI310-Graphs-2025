# from https://runestone.academy/ns/books/published/pythonds/Graphs/ImplementingKnightsTour.html

from pythonds.graphs import Graph, Vertex
from pdb import set_trace
from datetime import datetime

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
       for col in range(bdSize):
           nodeId = posToNodeId(row,col,bdSize)
           newPositions = genLegalMoves(row,col,bdSize)
           for e in newPositions:
               nid = posToNodeId(e[0],e[1],bdSize)
               ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row, column, board_size):
    return (row * board_size) + column

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
backTrackCount = 0
def knightTour(n,path,u,limit):
        """

        Parameters
        ----------
        n : int
            The current depth in the search tree, initially 0
        path : list
            A list of the vertices visited up to this point, initially []
        u : Vertex
            The vertex in the graph that we wish to explore, start with a node from KnightGraph
        limit : int
            The maximum number of nodes in a complete graph
        """
        global backTrackCount
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done: # prepare to backtrack
                path.pop()
                backTrackCount += 1
                u.setColor('white')
        else:
            done = True
        return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    # set_trace()
    return [y[1] for y in resList]


backTrackCount = 0
def knightTourH(n,path,u,limit):
        """

        Parameters
        ----------
        n : int
            The current depth in the search tree, initially 0
        path : list
            A list of the vertices visited up to this point, initially []
        u : Vertex
            The vertex in the graph that we wish to explore, start with a node from KnightGraph
        limit : int
            The maximum number of nodes in a complete graph
        """
        global backTrackCount
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = orderByAvail(u)
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTourH(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done: # prepare to backtrack
                path.pop()
                backTrackCount += 1
                u.setColor('white')
        else:
            done = True
        return done

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    boardSize = 5
    kg = knightGraph(boardSize)
    v1 = kg.getVertex(1)  # get the Vertex named 0
    for conn in v1.getConnections():
        print(conn.getId())
    
    # path search (try different starting nodes and board sizes)
    # are the paths always the same from the same starting point?
    path = []
    startTime = datetime.now()
    knightTourH(0,path,v1,boardSize*boardSize - 1)
    endTime = datetime.now()
    print(f'Path found in {endTime - startTime}')
    pathIDs = []
    for v in path:
        print(v.getId(), end=',')
        pathIDs.append(v.getId())
    print()
    pathIDs.sort()
    print(pathIDs)
    print(f'Back tracked times: {backTrackCount}')
    # set_trace()
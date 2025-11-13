from pythonds.graphs import Graph

from pdb import set_trace

def buildDict(wordFile):
    d = {}
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        # print(d)
        # set_trace()
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    return d


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    edgeCount = 0
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
                    edgeCount += 1
    print(f'{g.numVertices} vertices')
    print(f"{edgeCount} edges created")
    return g

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    # myD = buildDict('./src/four.txt')
    myG = buildGraph('./src/four.txt')
    myV = myG.getVertex('TOME')
    print(myV.getConnections())
    for conn in myV.getConnections():
        print(conn.getId())
    set_trace()
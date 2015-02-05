from heapq import heappush, heappop

def euler107():

    edges = open('p107_network.txt').read().split('\n')
    graph = []
    for line in edges:
        graph.append(line.split(','))
    graph.pop()

    vertices, presum = set(), 0

    for i in xrange(len(graph)):
        for j in xrange(len(graph[0])):
            if graph[i][j] == '-':
                graph[i][j] = 0
            else:
                graph[i][j] = int(graph[i][j])
                presum += graph[i][j]
                vertices.add(i)

    presum /= 2

    Edges = []
    a = vertices.pop()
    edgepush(a, Edges, graph)

    postsum = 0
    while vertices:
        weight, x, y = heappop(Edges)
        if y in vertices:
            vertices.discard(y)
            edgepush(y, Edges, graph)
            postsum += weight

    print "Saved: ", presum-postsum


def edgepush(edge, Edges, Graph):
        for i in xrange(len(Graph[edge])):
            if Graph[edge][i] > 0:
                heappush(Edges, (Graph[edge][i], edge, i))



if __name__ == "__main__":
    euler107()

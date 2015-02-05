def euler83():
	grid = getgrid()
	graph, seed = makegraphdict(grid), grid[0][0]
	d = dijkstra(graph, seed)
	print d[79,79]

def getgrid():
	tmp, Grid = open('matrix83.txt').read().split('\n'), []
	for line in tmp:
		if line: Grid.append([int(i) for i in line.split(',')])
	return Grid


def getneighbors(sx, sy, sqlength):
    neighbors = [(sx+1, sy), (sx-1, sy), (sx, sy+1), (sx, sy-1)]
    return [(x, y) for x, y in neighbors if (0 <= x < sqlength) and (0 <= y < sqlength)]
    
	
def makegraphdict(matrix):
    gdict = {}
    for x, line in enumerate(matrix):
        for y, col in enumerate(line):
            gdict[x,y] = {}
            neighbors = getneighbors(x,y, len(matrix))
            for nx, ny in neighbors:
                gdict[x,y][nx, ny] = matrix[nx][ny]
    return gdict


# Takes a dict-of-dicts style Graph and returns the shortest path from (0,0) to the 
def dijkstra(Graph, seed=0):
	from heapq import heappush, heappop
	Dist, Pqueue, Visited = {(0,0):seed}, [(seed, (0,0))], set()
	while Pqueue:
		_, node = heappop(Pqueue)
		if node in Visited: continue
		Visited.add(node)
		for neighbor in Graph[node]:
			relax(Graph, node, neighbor, Dist)
			heappush(Pqueue, (Dist[neighbor], neighbor))
	return Dist

def relax(Graph, start, end, Distance):
    d = Distance.get(start, float('inf')) + Graph[start][end]
    if d < Distance.get(end, float('inf')):
        Distance[end] = d
        return True

if __name__ == "__main__":
	euler83()

'''
Alternative implementation using just the matrix from getgrid() and the Bellman-Ford algorithm. Runs much slower than Dijkstra.

def seeddistance(Graph): return [[float('inf') for entry in row] for row in Graph]

# uses Bellman-Ford to produce a matrix of the distance of (x, y) from (0,0) for a nxn graph. Does not check for negative cycles. 
def bfdist(graph):
    dimension, dist, counter = len(graph), seeddistance(graph), 0
    dist[0][0] = graph[0][0]
    while counter < dimension-1:
        counter += 1
        for x, row in enumerate(graph):
            for y, col in enumerate(row):
                for neighbor in getneighbors(x,y, dimension):
                    relax(graph, (x,y), neighbor, dist)
    return dist

	
def relax(Graph, (sx, sy), (ex, ey), Distance):
    d = Distance[sx][sy] + Graph[ex][ey]
    if d < Distance[ex][ey]:
        Distance[ex][ey] = d
        return True

	relax(Graph, (x, y), neighbor, Distance)
'''


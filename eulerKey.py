import collections

def getKeys():
	j = open("keylog.txt")
	keystr = []
	for line in j:
		keystr.append(line.strip())
#keystr[0] = keystr[0].strip()	


# If I can put this into a tree, I can do a topological sort of it.


graph = collections.defaultdict(set)
toplen = []
for num in keystr:
	for i in range(len(num)):
		graph[num[i]].update(set(num[:i]))
for key, value in graph.iteritems():
	toplen.append((key, len(value)))
toplen.sort(lambda x,y: x[1]-y[1])
print ''.join([g[0] for g in toplen])

# ans = 73162890

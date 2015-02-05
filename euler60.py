### How the fuck did 0,1,2, or 18 end up in graph!!!!!!!

import collections, isprime as ip, itertools

primes = list(ip.primes_sieve2(10000))
edges = []
for a in primes:
	for b in primes:
		if a < b: 
			# I'm pretty sure Python is not lazy, and will do this comparison even if a > b, if I join 
			# these two conditionals on one line.
			if iscatprime(a,b):
				edges.append((a,b))
graph = {}
for (a, b) in edges:
	if a not in graph:
		graph[a] = set()
	graph[a].add(b)
	if b not in graph:
		graph[b] = set()
	graph[b].add(a)
edgeset = set(edges)

four_cliques = []
for (a, b) in edges:
	for (c, d) in edges:
		if len(set([a,b,c,d])) == 4:
			if ( tuple(sorted([a,c])) in edgeset and tuple(sorted([a,d])) and tuple(sorted([b,c])) in edgeset and tuple(sorted([b,d])) in edgeset):
				 four_cliques.append([a,b,c,d])

answerset = []
for four_clique in four_cliques:
	candidates = set(graph[four_clique[0]]) & set(graph[four_clique[1]]) & set(graph[four_clique[2]]) & set(graph[four_clique[3]])
	candidates = candidates - set(four_clique)
	if candidates:
		for candidate in candidates:
			answerset.append(sorted([a,b,c,d,candidate]))



def iscatprime(a,b):
	return ip.isprime(int(str(a) + str(b))) and ip.isprime(int(str(b) + str(a)))

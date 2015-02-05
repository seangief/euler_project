def euler61():
	figurative, figuredict = [(tri, 3), (squ, 4), (pent, 5), (hexa, 6), (hept, 7), (octa, 8)], {}
	for function in figurative:
		seeddict(function, figuredict)
	Answers = {}
	for prefix in figuredict.keys():
		for candidate in figuredict[prefix]:
			findans(figuredict, [], candidate, [], Answers)
	for value, (answer, searched) in Answers.iteritems():
		print answer, ": sum =", value

def findans(Graph, History, (node, magnitude), Searched, Answers):
	prefix = node%100
	History, Searched = [num1 for num1 in History], [num2 for num2 in Searched]
	History.append(node)
	Searched.append(magnitude)
	if prefix in Graph:
		if len(Searched) == 6:
			if History[-1] % 100 == History[0] / 100:
				Answers[sum(History)] = (History, Searched)
 		else:
			neighbors = [(node, magnitude) for node, magnitude in Graph[prefix] if magnitude not in Searched] 
			if len(neighbors) > 0:
				for neighbor in neighbors:
					findans(Graph, History, neighbor, Searched, Answers)

def seeddict((funct, magnitude), numdict):
	entries = [funct(n) for n in xrange(1,141) if funct(n) > 999 and funct(n) < 10000]
	for entry in entries:
		pref = entry / 100
		if pref not in numdict:
			numdict[pref] = set()
		numdict[pref].add((entry, magnitude))


def tri(n): return n*(n+1)/2

def squ(n): return n**2

def pent(n): return n*(3*n-1)/2

def hexa(n): return n*(2*n-1)

def hept(n): return n*(5*n-3)/2

def octa(n): return n*(3*n-2)



if __name__ == "__main__":
	euler61()


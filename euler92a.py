import collections as c

def euler92():
	ify = c.defaultdict(int)
	t, ans = 1, 0
	while t < 10000000:
		for i in range(t, t+1000000):
			if int(dictify(str(i), ify)) == 89:
				ans += 1
		t += 1000000
	print ans

###

def squarechain(n):
	return str(sum([int(x)**2 for x in n])) 

###


def dictify(g, chain):
	if int(chain[g]) != 0:
		ans = chain[g]
	elif int(g) == 1 or int(g) == 89:
		ans = g
	else:
		ans = dictify(squarechain(g), chain)
	chain[g] = ans
	return ans

if __name__ == "__main__":
	euler92()

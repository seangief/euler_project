from isprime import rational

def euler93():
	a = arithdict()
	ans, longest = '', 0
	for key, val in a.iteritems():
		j = longestseq(val)
		if  j > longest:
			longest = j
			ans = key
	print ans


def arithdict():
	ops = operators()
	digs = digits()
	ans = {}
	for d in digs:
		a = set()
		for tree in get_trees(d, ops):
			k = (evaluate(0, tree)).intVal()
			if k: a.add(k)
		ans[d] = a
	return ans

def evaluate(idx, atree):
	case = atree[idx]
	if case.isdigit():
		return rational(int(atree[idx]), 1)
	else:
		children = [evaluate(2*idx+1, atree), evaluate(2*idx+2, atree)]
		if case == '+':
			return children[0] + children[1]
		elif case == '-':
			return children[0] - children[1]
		elif case == '*':
			return children[0] * children[1]
		elif case == '/':
			return children[0] - children[1]	

def operators():
	j = ['*', '+', '-', '/']
	ops = []
	for a in j:
		for b in j:
			for c in j:
				ops.append((a,b,c))
	return ops

def digits():
	digits = []
	for a in xrange(1, 10):
		for b in xrange(a+1, 10):
			for c in xrange(b+1, 10):
				for d in xrange(c+1, 10):
					digits.append((str(a), str(b), str(c), str(d)))
	return digits

def get_trees(digits, operators):
	from itertools import permutations
	trees = []

	# These are lists of indices: the first list are indices of the digits
	# in the arithemtic tree, the second list are the indices of the operators.
	# These represent every possible binary arithemtic tree with 4 variables
	# and 3 operators.
	dgram = [([2,4,7,8], [0,1,3]),
			([2,3,9,10], [0,1,4]),
			([3,4,5,6], [0,1,2]),
			([1,6,11,12], [0,2,5]),
			([1,5,13,14], [0,2,6])]
	for d in permutations(digits):
		for operator in operators:
			for dig, opt in dgram:
				t = ['#' for _ in xrange(15)]
				for i, idx in enumerate(dig):
					t[idx] = d[i]
				for i, idx in enumerate(opt):
					t[idx] = operator[i]
				trees.append(t)
	return trees

def longestseq(aset):
	start, count = 1, True
	while count:
		if start in aset:
			start+=1
		else: count = False
	return start

if __name__ == "__main__":
	euler93()

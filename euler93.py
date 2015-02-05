# 3,870,720 expressions to be evaluated ((4!*126)*(5*4^4))

def makesets():
	ret = []
	for x in xrange(1, 10):
		for y in xrange(x+1, 10):
			for z in xrange(y+1, 10):
				for a in xrange(z+1, 10):
					ret.append((x,y,z,a))
	return ret

# Clever but doesn't work. Does integer division and throws ZeroDivisionError.
def evaluate_digits(digits):
	from itertools import permutations
	trees =  [
	'(({0} {{0}} {1}) {{1}} {2}) {{2}} {3}',
	'({0} {{0}} ({1} {{1}} {2})) {{2}} {3}',
	'({0} {{0}} {1}) {{1}} ({2} {{2}} {3})',
	'{0} {{0}} (({1} {{1}} {2}) {{2}} {3})',
	'{0} {{0}} ({1} {{1}} ({2} {{2}} {3}))']

	operators = list(permutations(['+', '-', '/', '*'], 3))
	ans = set()

	for perm in permutations(digits):
		for operator in operators:
			for tree in trees:
				t = tree.format(*perm)
				t = t.format(*operator)
				try:
					ans.add(eval(t))
				except ZeroDivisionError:
					continue
	return ans

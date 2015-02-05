from math import factorial

def diff(degree, n, List):
	if degree == 0: return List[n]
	else: return diff(degree-1, n+1, List) - diff(degree-1, n, List)


def polynomial(maxDegree, ans, List):
	coeff = diff(maxDegree, 1, List) / factorial(maxDegree)
	ans.append(coeff)
	List = [List[i] - coeff*i**maxDegree for i in range(len(List))]
	if maxDegree > 0:
		return polynomial(maxDegree-1, ans, List)
	else:
		return ans

def euler101():
	values = [n**10-n**9+n**8-n**7+n**6-n**5+n**4-n**3+n**2-n+1 for n in range(20)]
	size, difer = 10, []
	for i in range(size):
		ans, coeffs = 0, polynomial(i, [], values)
		for n in range(i+1):
			ans += coeffs[n]*(i+2)**(i-n)
		difer.append(ans)
	print sum(difer)

if __name__ == "__main__":
	euler101()

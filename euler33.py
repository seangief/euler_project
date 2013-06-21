import isprime as ip

def euler33():
	ans = []
	for d in range(10,100):
		for n in range(10, d):
			val = float(n)/d
			try:
				n1 = int("".join(set(str(n))-set(str(d))))
				d1 = int("".join(set(str(d))-set(str(n))))
				val1 = float(n1)/d1
				if d1 < 10 and ip.almostEq(val, val1) and n%11 != 0 and n%10 != 0:
					ans.append([n,d])
			except:
				continue
	a = reduce(int.__mul__, [i[0] for i in ans])
	b = reduce(int.__mul__, [i[1] for i in ans])
	print a, b, b / ip.gcd(a,b)

if __name__ == "__main__":
	euler33()

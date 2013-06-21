import itertools as it

def euler43():
	perms = it.permutations('0123456789')
	ans = []
	primes = [3, 5, 7, 11, 13, 17]
	for perm in perms:
		test = "".join(perm)
		if int(test[3]) % 2 == 0:
			candidate = True
			count = 2
			while count < 8:
				if not int(test[count:count+3]) % primes[count-2] == 0:
					candidate = False
					break
				count += 1
			if candidate and len(str(int(test))) == 10:
				ans.append(int(test))
	print ans
	print sum(ans)

if __name__ == "__main__":
	euler43()

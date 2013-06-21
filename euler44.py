import sys

def euler44():
	pent = [(3*i-1)*i /2 for i in range(1,5000)]
	pentset = set(pent)
	candidate = ()
	mindif = sys.maxint
	for i in range(1, len(pent)):
		for j in range(i+1, len(pent)):
			diff = abs(pent[j]-pent[i])
			if diff in pentset:
				if pent[i] + pent[j] in pentset:
					if diff < mindif:
						mindif = diff
						candidate = (pent[i], pent[j], diff)
	print candidate[0], " - ", candidate[1], " = ", candidate[2]
	print candidate[0], " + ", candidate[1], " = ", candidate[0] + candidate[1]



if __name__ == "__main__":
	euler44()

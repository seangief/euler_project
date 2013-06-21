# we'll call this "naive"

def euler44():
	pent, found, dist, count = [n*(3*n-1)/2 for n in range(1,10000)][::-1], False, 1000, 1
	while not found:
		for i in range(len(pent)-count):
			if pent[i]-pent[i+count] in pent and pent[i]+pent[i+count] in pent:
				found = True
				if dist > pent[i]-pent[i+count]:
					dist = pent[i]-pent[i+count]
		count+=1	
	print dist


if __name__ == "__main__":
	euler44()

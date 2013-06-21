def getMatrix():
	g = open('matrix.txt')
	data = g.read().split()
	for i in range(len(data)):
		data[i] = data[i].split(',')
		for j in range(len(data[i])):
			data[i][j] = int(data[i][j])
	g.close()
	return data

def findMin(a,b, data, d):
	if (a,b) not in d:
		if a == 0 and b == 0:
			d[a,b] = data[0][0]
		elif a==0:
			d[a,b] = data[a][b] + findMin(a,b-1, data, d)		
		elif b==0:
			d[a,b] = data[a][b] + findMin(a-1,b, data, d)
		else:
			d[a,b] = data[a][b] + min(findMin(a-1,b, data, d), findMin(a,b-1, data, d))
	return d[a,b]

def main():
	data = getMatrix()
	d = dict()
	print findMin(len(data)-1,len(data[0])-1, data, d)

if __name__ == "__main__":
	main()

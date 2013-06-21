def euler82():
	# Objective: create a matrix with shortest path length from each point

	# render data as matrix
	# last column of new matrix is the same as old matrix

	o = getMatrix()
	j = len(o)-1
	n = [[0 for i in range(len(o))] for j in range(len(o[0]))]

	for i in range(len(o)):
		n[i][j] = o[i][j]

	for c in range(len(o[0])-1)[::-1]:
		for r in range(len(o)):
			val = o[r][c]
			minimum = val + n[r][c+1]

			upwalk = 0
			for i in range(0, r)[::-1]:
				upwalk += o[i][c]
				if minimum > val+upwalk+n[i][c+1]:
					minimum = val+upwalk+n[i][c+1]

			downwalk = 0
			for i in range(r+1, len(o)):
				downwalk += o[i][c]
				if minimum > val+downwalk+n[i][c+1]:
					minimum = val+downwalk+n[i][c+1]

			n[r][c] = minimum

	print min([n[i][0] for i in range(len(n))])

def getMatrix():
	g = open('e82matrix.txt')
	data = g.read().split()
	for i in range(len(data)):
		data[i] = data[i].split(',')
		for j in range(len(data[i])):
			data[i][j] = int(data[i][j])
	g.close()
	return data

if __name__ == "__main__":
               euler82()

def main():
	g = open('testmatrix.txt')
	text = g.read().split()
	for i in range(len(text)):
		text[i] = text[i].split(',')
	g.close()
	matrix = []
	for i in range(len(text)):
		matrix.append(text[i])
		for j in range(len(text[0])):
			matrix[i][j] = int(text[i][j])
	print check(0,0,matrix)
	
	G = dict()
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			G[i,j] = dict()
			if i+1 < len(matrix):
				G[i,j][i+1, j] = matrix[i+1][j]
			if j+1 < len(matrix[0]):
				G[i,j][i,j+1] = matrix[i][j+1]


if __name__ == "__main__":
	main()

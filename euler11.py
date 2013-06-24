def main():
	f = open('euler11.txt')
	matrix, ans = [], 0
	for line in f:
		matrix.append(line.split())

	for h in range(len(matrix)):
		for k in range(len(matrix[h])):
			matrix[h][k] = int(matrix[h][k])

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			a, b = 0,0
			try:
				a = reduce(int.__mul__,	[matrix[i+di][j+di] for di in range(4)])
			except:
				pass
			try:
				b = reduce(int.__mul__,	[matrix[i+di][j-di] for di in range(4)])
			except:
				pass
			if max(a,b) > ans:
				ans = max(a,b)
	print ans

if __name__ == "__main__":
	main()

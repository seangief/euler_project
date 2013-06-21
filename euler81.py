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
	

# good so far as I can tell
def check(x,y, source):
	rpath, dpath = 0, 0
	val = source[x][y]
	if x == len(source)-1 and y == len(source[0])-1:
		return val
	else:
		if x < len(source)-1:
			rpath = check(x+1, y, source)
		if y < len(source[0])-1:
			dpath = check(x, y+1, source)
		return val + min(rpath, dpath)

if __name__ == "__main__":
	main()

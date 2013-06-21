import sys
# d[row][column]
def getMatrix():
	g = open('e82testmatrix.txt')
	data = g.read().split()
	for i in range(len(data)):
		data[i] = data[i].split(',')
		for j in range(len(data[i])):
			data[i][j] = int(data[i][j])
	g.close()
	return data

def findMin(row,column, data, d):
	if (row, column) not in d:
		if column == len(data[0])-1:
			d[row,column] = data[row][column]
		else:
			neighborValues = [findMin(row, column+1, data, d)]
			neighborValues.extend([findMin(i,column,data,d) for i in [j for j in range(len(data)) if j != row]])
			d[row,column] = data[row][column] + min(neighborValues)
	return d[row,column]

def main():
	data = getMatrix()
	d = dict()
	print min( [findMin(0,i,data,d) for i in range(len(data[0]))] )

if "__name__" == "__main__":
	main()

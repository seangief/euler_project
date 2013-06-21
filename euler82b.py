columns = []
for column in range(len(f[0])):
	columns.append([data[i][column] for i in range(len(f))])	

	for column in range(len(data[0])):
	# number in matrix, counting from top right ( i.e., [0][len(matrix}-1]
		for neighbor in range(len(neighbors)):
			distance = 0	
			if index >= neighbor:
				for i in range(neighbor, index):
					distance += neighbors[i]
			else:
				for j in range(index, neighbor):
					distance += neighbors[j]
			distance+= data[column][neighbor]


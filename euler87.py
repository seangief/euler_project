triplets = 0
sq = [i**2 for i in range(1,7072)]
cub = [j**3 for j in range(1,367)]
quad = [k**4 for k in range(1,85)]

for x in quad:
	for y in cub:
		for z in sq:
			if x+y+z < 50000000:
				triplets+=1
			else:
				continue
print len(triplets)

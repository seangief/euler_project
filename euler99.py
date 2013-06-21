import math

f = open("base_exp.txt")
g = f.read()
f.close()
pairs = g.split('\n')

for i in range(len(pairs)):
	pairs[i] = pairs[i].split(',')

for i in range(len(pairs)):
	for j in range(len(pairs[i])):
		pairs[i][j] = int(pairs[i][j])

ans = []
for i,j in pairs:
	ans.append(j*log(i))
print ans.index(max(ans))+1

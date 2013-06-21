#creates set of #s to do this to [x**y for x in range(100) for y in range(100)]
#returns sum of 1 number: sum([int(char) for char in str(j)])

print max([sum([int(char) for char in str(power)]) for power in [x**y for x in range(100) for y in range(100)]])

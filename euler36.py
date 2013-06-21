print sum([i for i in range (1, 1000000) if i == int(str(i)[::-1]) and int(bin(i)[:1:-1]) == int(bin(i)[2:])])

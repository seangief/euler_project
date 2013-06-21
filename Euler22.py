def euler22():
	f = open("names.txt")
	names = f.read()
	f.close()
	names = names.strip('\"')
	names = names.split('\",\"')
	names.sort()
	order = []
	for name in names:
		total = 0
		for letter in name:
			total += ord(letter)-64
		order.append(total)
	product = []
	for t in range(len(order)):
		product.append((t+1) * order[t])
        testn = names.index("COLIN")
        print(str(testn) +" " + str(order[testn]) + " " +str(product[testn]) + "\n")
	return sum(product)
    

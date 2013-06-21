def euler38():
	answers = []
	digitset = set('123456789')
	for i in range(2, 50000):
		numstring = str(i)
		old = ""
		count = 2
		while len(numstring) < 10:
			old = numstring
			numstring += str(count*i)
			count+=1
		if len(set(old)) == len(old) and not('0' in old):
			answers.append(int(old))
	print max(answers)

if __name__ == "__main__":
	euler38()

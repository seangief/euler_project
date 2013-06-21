def splitByDigit(source):
	ans = []
	i = 0
	while source:
		try:
			if source[i] != source[i+1]:
				ans.append(source[0:i+1])
				source = source[i+1:]
				i = 0
			else:
				i+=1
		except IndexError:
			ans.append(source)
			source = None
	return ans


def euler419():
	source = "1"
	ans = []
	seeSay = ""
	while len(seeSay) < 25:
		ans = splitByDigit(source)
		for i in ans:
			seeSay+=str(i[0])
			seeSay+=str(len(i)) 	
		source = seeSay
		print seeSay
	print seeSay

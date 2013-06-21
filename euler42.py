triangle =[.5*(i**2 +i) for i in range(0,5000)]
j = open("words.txt")
words = j.read().rstrip('\"').lstrip('\"').split('\",\"')
answer = []
j.close()
for word in words:
	val = 0
	for letter in word:
		val += ord(letter)-64
	if val in triangle:
		answer.append(word)
print len(answer)

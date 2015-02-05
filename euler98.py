def euler98():
	from collections import defaultdict
	sort = defaultdict(list)
	for word in open('p098_words.txt').read().split('\",\"'):
		word = word.strip('\"')
		pat = ''.join(sorted(list(word)))
		sort[pat].append(word)
	print "Done writing dictionary!"

	anagrams, maxlen = {}, 0
	for key in sort.keys():
		if len(sort[key]) > 1:
			anagrams[key] = sort[key]
			if len(key) > maxlen:
				maxlen = len(key)
	print "Done thinning dictionary!"

	# Convert the squares into easy to understand patterns
	square_patterns, squareset = defaultdict(list), set()
	for n in xrange(10**((maxlen+1)/2)):
		squareset.add(str(n**2))
		square_patterns[getPattern(str(n**2))].append(str(n**2))
	print "Finished calculating and hashing squares!"

	answer = []

	for pair in anagrams.values():
		# pair is a two value list of words which are anagams of each other
		anagram, test = pair[0], pair[1]
		k = square_patterns[getPattern(anagram)]
		for square in k:
			candidate = replace_char(test, anagram, square)
			if candidate in squareset:
				answer.extend([int(square), int(candidate)])

	print max(answer)


def replace_char(buf, old_val, new_val):
	buf = list(buf)
	if len(old_val) != len(new_val):
		raise
	d = {}
	for i in xrange(len(old_val)):
		d[old_val[i]] = new_val[i]
	if len(buf) != len(new_val):
		raise
	for i in xrange(len(new_val)):
		if buf[i] in d:
			buf[i] = d[buf[i]]
	return ''.join(buf)


def getPattern(word):
	d, count = {}, 1
	buf = list(word)
	for i in xrange(len(buf)):
		if buf[i] not in d:
			d[buf[i]] = str(count)
			count = (count +1)%10
		buf[i] = d[buf[i]]
	pattern = ''.join(buf)
	return pattern


if __name__ == "__main__":
	euler98()



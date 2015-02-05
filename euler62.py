def euler62():
	perms = dict()
	for value in xrange(316, 10000):
		permset = ''.join(sorted(str(value**3)))
		if permset not in perms:
			perms[permset] = [0, []]
		perms[permset][0] += 1
		perms[permset][1].append(value)

	minimum = 10000
	for key, value in perms.iteritems():
		if value[0] == 5:
			thismin = min(value[1])
			if thismin < minimum:
				minimum = thismin
	print minimum**3

def euler68():
	from itertools import permutations
	centers = permutations(range(1,10), 5)
	answers = []
	for center in centers:
		answers.extend(process(list(center)))
	print max([answer for answer in answers if len(answer) == 16])


def process(centerlist):
	ans = []
	for total in xrange(14,20):
		remaining = set(range(1,11)) - set(centerlist)
		good = True
		digitstring = []
		for index, number in enumerate(centerlist):
			second, third = number, centerlist[(index+1) % len(centerlist)]
			first = total - (second + third)
			if not ((first != second != third) and (0 < first < 11) and first in remaining):
				good = False
			if first in remaining: remaining.remove(first)
			digitstring.append(str(first) + str(second) + str(third))
		if good:
			if min([int(i) for i in digitstring]) == int(digitstring[0]):
				ans.append(''.join(digitstring))
	return ans


if __name__ == "__main__":
	euler68()

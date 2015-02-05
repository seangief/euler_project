from functools import wraps

def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap

# see Slomson, An Introduction to Combinitorics, p. 32 for explanation.
def euler76():
	@memo
	def partition(number, max_parts):
		if number <= 1: return 1
		elif max_parts > number: return partition(number, number)
		elif max_parts == 2: return int(number/2 +1)
		elif max_parts == 1: return 1
		else: return partition(number, max_parts-1) + partition(number-max_parts, max_parts)
	print partition(100,99)

if __name__ == "__main__":
	euler76()

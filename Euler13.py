def Euler13():
	nums = open("euler13.txt").read()
	nums = nums.split()
	nums = [number[:12] for number in nums]
	sum=0
	for number in nums:
		sum += int(number)
	print str(sum)[:-4]

if __name__ == "__main__":
	Euler13()

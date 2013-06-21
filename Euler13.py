euler = open("c:\\euler13.txt","r")
nums = euler.read()
euler.close()
nums = nums.split()
nums = [number[:12] for number in nums]
sum=0
for number in nums:
	sum += int(number)
print sum

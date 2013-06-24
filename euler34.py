def euler34(bound):
    factorials = [1,1,2,6,24,120,720,5040,40320,362880]
    factn = []
    for i in range(1,bound):
        istring = str(i)
        total = 0
        for j in range(0,len(istring)):
            total += factorials[int(istring[j])]
        if total == i:
            factn.append(i)
    print sum(factn) - (1 + 2) #  1! and 2! don't count

if __name__ == "__main__":
	euler34(1000000) # shamless guess about the bound

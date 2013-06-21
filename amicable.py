def amicable():
        from getDivs import getDivs
        divisors = []
        divisors.append(0)
        for i in range (2,10001):
                divisors.append(sum(getDivs(i)))
        amicable = []
        for j in range (0,9999):
                if divisors[j] > 1 and divisors[j] < 10000:
                        if divisors[divisors[j]-1] == j+1 and divisors[j]-1 != j:
                                amicable.append(divisors[j])
        print sum(amicable)
        

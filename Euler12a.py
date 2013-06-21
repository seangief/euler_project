def findLPrime(test):
    import math
    prime = -1
    if test < 0:
        return -1
    else:
        bound = int(math.sqrt(test))
        for integer in range(2,bound+1):
                if test%integer == 0:
                    prime = integer
                    break
        return prime

def listFactors(number):
    if findLPrime(number) < 0:
        return [1, number]
    else:
        factors = []
        factor = findLPrime(number)
        while findLPrime(number) > 0:
            factors.append(factor)
            number = number/factor
            factor = findLPrime(number)
        factors.append(number)
        return factors

def euler12():
    index, divisors, triangle = 1, 3, 0
    while divisors < 500:
        triangle = index*(index+1)/2
        g = count(listFactors(triangle))
        for i in range(len(g)):
            g[i] += 1
        divisors = reduce(lambda x,y: x*y, g)
        index +=1
    return triangle


def count(list):
    d = dict()
    for k in list:
        if k not in d:
            d[k] =1
        else:
            d[k] += 1
    return d.values()

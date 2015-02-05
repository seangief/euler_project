from collections import Counter, defaultdict

def euler108():
    Factors, Radix = {}, []
    Factors[1] = {1:1}
    for n in xrange(1, 100001):
        dfactor(n, Factors)

    for key, value in Factors.iteritems():
        l = reduce(int.__mul__, value.keys())
        Radix.append((l, key))

    Radix.sort()

    print Radix[9999][1]

def getfactor(n):
    from math import sqrt
    mf, rem = int(sqrt(n)), 2
    while rem <= mf:
        if n % rem == 0:
            return rem
        rem+=1
    return 1

def dfactor(n, Factors):
    if n not in Factors:
        f = getfactor(n)
        if f == 1:
            Factors[n] = {n:1}
        else:
            Factors[n] = Counter(dfactor(n/f, Factors))
            Factors[n][f]+=1
    return Factors[n]

if __name__ == "__main__":
    euler108()

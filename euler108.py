from isprime import primefact
from collections import Counter

def euler108():
    Factors, n, maxfact = {}, 1260, 2
    Factors[1] = {1:1}
    while maxfact <= 1000:
        n += 1
        dfact = dfactor(n, Factors)
        dfact  = reduce(int.__mul__, [(2*f)+1 for f in dfact.values()])
        maxfact = (dfact+1)/2
    print n, maxfact

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

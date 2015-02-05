def euler88():
    Bests = [0, 0, 4, 6, 8, 8, 12] + [2*i for i in xrange(7, 12001)]
    for j in xrange(2, 12001):
        tryval(1, 1, 0, j, Bests)
    print sum(set(Bests[2:]))


def tryval(count, pprev, sprev, val, Bests):
    prod, ssum = pprev * val, sprev + val
    candidate = prod - ssum + count
    if candidate <= 12000:
        if Bests[candidate] > prod:
            Bests[candidate] = prod
        for n in xrange(val, 12001/val):
            tryval(count+1, prod, ssum, n, Bests)

if __name__ == "__main__":
    euler88()

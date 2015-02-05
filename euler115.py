def euler115():
    k, n, Ref = 0, 49, {}
    while k <= 1000000:
        n += 1
        k = recur(50, n, Ref)
    print n

def recur(m, n, Ref):
    if n not in Ref:
        if n < m:
            Ref[n] = 1
        else:
            total = 1
            for tile in xrange(m, n+1):
                for pos in xrange(0, n-tile+1):
                    total += recur(m, n-(pos+tile)-1, Ref)
            Ref[n] = total
    return Ref[n]

if __name__ == "__main__":
    euler115()

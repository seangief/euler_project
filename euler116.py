def euler116():
    n, Red, Green, Blue = 50, {}, {} , {}
    print recur(2, n, Red)-1 + recur(3, n, Green)-1 + recur(4, n, Blue)-1

def recur(m, n, Ref):
    if n not in Ref:
        if n < m:
            Ref[n] = 1
        else:
            total = 1
            for pos in xrange(0, (n-m)+1):
                total += recur(m, n-(pos+m), Ref)
            Ref[n] = total
    return Ref[n]

if __name__ == "__main__":
    euler116()

def euler114():
    print recur(50, {})
    


def recur(n, Ref):
    if n not in Ref:
        if n < 3:
            Ref[n] = 1
        else:
            total = 1
            for tile in xrange(3, n+1):
                for pos in xrange(0, n-tile+1):
                    total += recur(n-(pos+tile)-1, Ref)
            Ref[n] = total
    return Ref[n]

if __name__ == "__main__":
    euler114()


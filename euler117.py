def euler117():
    print recur(50, {})

def recur(n, Ref):
    if n not in Ref:
        if n < 2:
            Ref[n] = 1
        else:
            total = 1
            for tile in xrange(2, 5):
                for pos in xrange(0, (n-tile)+1):
                    total += recur(n-(pos+tile), Ref)
            Ref[n] = total
    return Ref[n]

if __name__ == "__main__":
    euler117()

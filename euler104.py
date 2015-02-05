# http://fusharblog.com/solving-linear-recurrence-for-programming-contest/

from functools import wraps

def euler104():
    found, n, gf = False, 2, getfib()
    while not found:
        frontfib, backfib = gf.next()
        if is_pandigital(str(frontfib)[:9]) and is_pandigital(str(backfib)[-9:]):
            found = True
            break
        else:
            n += 1
    print "The answer is: ", n +1

def getfib():
    cfront, cprev, bfront, bprev = 1, 1, 1, 1
    while True:

        cfront, cprev = cfront + cprev, cfront
        if cfront > 10**50:
            cprev /= 10
            cfront /= 10

        bfront, bprev = bfront + bprev, bfront
        if bfront > 10**10:
            bfront = bfront % 10**10
            bprev = bprev % 10**10

        yield cfront, bfront


def is_pandigital(string):
    arr = [False] *10
    for char in string:
        arr[int(char)] = True
    return (reduce(bool.__and__, arr[1:]))


if __name__ == "__main__":
    euler104()

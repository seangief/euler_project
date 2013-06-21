def collatz(base, count=0):
    count += 1
    if base == 1 or base == 0:
        return count
    elif base%2 == 0:
        base /= 2
    else:
        base = base*3 +1
    count = collatz(base, count)
    return count

def euler13():
    colCount = []
    max = 0
    for i in range(0,1000001):
        colCount.append(collatz(i))
    for i in range(0,1000001):
        if colCount[i] > colCount[max]:
            max = i

    return i

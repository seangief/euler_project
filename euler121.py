from itertools import combinations
from math import factorial, floor

def euler121():
    j = float(factorial(16))/winning(15)
    print floor(j)
    

def winning(x):
    discs = x+1
    dice, total = range(2, discs+1), 1
    for n in range(1, ((x-1)/2)+1):
        for combo in combinations(dice, n):
            combo = [n-1 for n in combo]
            total += reduce(int.__mul__, combo)
    return total


if __name__ == "__main__":
    euler121()

# http://fusharblog.com/solving-linear-recurrence-for-programming-contest/

def getfib(n, mode = ''):
    return dot(mat_power(((0, 1), (1, 1)), n, mode), ((0,), (1,)))[1][0]

def is_pandigital(string):
    arr = [False] *10
    for char in string:
        arr[int(char)] = True
    return (reduce(bool.__and__, arr[1:]))


def dot(mat1, mat2, mode = ''):
    from math import log
    if len(mat1[0]) != len(mat2):
        raise Exception
    mdot = [[0] * len(mat2[0]) for _ in xrange(len(mat1))]
    for i in xrange(len(mat1)):
        for j in xrange(len(mat2[0])):
            mdot[i][j] = sum([mat1[i][a]*mat2[a][j] for a in xrange(len(mat1[0]))])

    base = log(10)
    size = int(log(mdot[0][0])/base)

    if mode == 'front':
        if size > 100:
            for i in xrange(len(mdot)):
                for j in xrange(len(mdot[0])):
                    mdot[i][j] /= 10**(size-100)

    elif mode == 'back':        
        for i in xrange(len(mdot)):
            for j in xrange(len(mdot[0])):
                mdot[i][j]  = mdot[i][j] % 10**11
        
            
    return mdot


def mat_power(matrix, power, mode):
    if power == 1:
        return matrix
    elif power % 2 == 0:
        rooted_matrix = mat_power(matrix, power/2, mode)
        return dot(rooted_matrix, rooted_matrix, mode)
    else:
        return dot(matrix, mat_power(matrix, power-1, mode), mode)

def first_hundred(num):
    from math import log
    base = log(10)
    size = int(log(num)/base)
    if size > 100:
        return num / 10**(size-100)
    else:
        return num

def last_hundred(num):
    return num % 100


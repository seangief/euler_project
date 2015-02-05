# 40 squares

def euler84():
    position = initialpos()
    initial_matrix = stoc_mat(4)
    late_matrix = stoc_mat(4, False)
    for i in xrange(40):
        if i < 3:
            position = dot(initial_matrix, position)
        else:
            position = dot(late_matrix, position)
    return position


def dot(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        raise Exception
    mdot = [[0] * len(mat2[0]) for _ in xrange(len(mat1))]
    for i in xrange(len(mat1)):
        for j in xrange(len(mat2[0])):
            mdot[i][j] = sum([mat1[i][a]*mat2[a][j] for a in xrange(len(mat1[0]))])
    return mdot

def dicedist(pos, die=4):
    dice, c = {}, 0
    for i in xrange(2, 2*die+1):
        if i <= die+1:
            c += 1
        else:
            c -= 1
        dice[(pos+i) % 40] = float(c)/(die**2)
    return dice


def stoc_mat(die, initial=True):
    # Construct the probability matrix
    GO = 0
    JAIL = 10
    GO2JAIL = 30
    CHANCE = set([7, 22, 36])
    COMMUNITY = set([2, 17, 33])
    
    #Markov matrix has unit-column vectors
    stomat = [[0] *40 for _ in xrange(40)]
    for i in xrange(len(stomat[0])):
        if i == GO2JAIL:
            stomat[JAIL][i] = 1.0
        else:
            for roll, chance in dicedist(i, die).iteritems():
                if roll %2 == 0 and not initial:
                    chance -= 1.0/(die**4)
                    stomat[JAIL][i] += 1.0/(die**4)
                if roll == GO2JAIL:
                    stomat[JAIL][i] += chance
                elif roll in COMMUNITY:
                    for pos, cond in communitydist(roll).iteritems():
                        stomat[pos][i] += chance * cond
                elif roll in CHANCE:
                    for pos, cond in chancedist(roll).iteritems():
                        stomat[pos][i] += chance * cond
                else:
                    stomat[roll][i] = chance
    return stomat


def chancedist(pos):
    GO = 0
    JAIL = 10
    GO2JAIL = 30

    railway = getrail(pos)
    utility = getutil(pos)
    dist = {}
    dist[GO] = 1.0/16
    dist[JAIL] = 1.0/16
    dist[11] = 1.0/16
    dist[24] = 1.0/16
    dist[39] = 1.0/16
    dist[5] = 1.0/16
    dist[railway] = 2.0/16 
    dist[utility] = 1.0/16
    dist[(pos-3)%40] = 1.0/16
    dist[pos] = 6.0/16
    return dist

def communitydist(pos):
    GO = 0
    JAIL = 10
    GO2JAIL = 30

    dist = {}
    dist[pos] = 14.0/16
    dist[GO] = 1.0/16
    dist[JAIL] = 1.0/16
    return dist



def getutil(pos):
    if pos == 7: 
        return 15
    elif pos == 22:
        return 25
    elif pos == 36:
        return 5

def getrail(pos): 
    if pos == 7:
        return 12
    elif pos == 22:
        return 28
    elif pos == 36:
        return 12

def initialpos():
    return [[1]] + [[0] for _ in xrange(39)]


def verify(g):
    t = []
    for col in xrange(len(g[0])):
        total = 0
        for row in g:
            total += row[col]
        t.append(total)
    return t

def euler96():
	text = open('sudoku.txt').read().split('\n')
	gameset, game = [], []
	for line in text:
		try:
			_ = int(line)
			game.append(list(line))
		except ValueError:
			if game: gameset.append(game)
			game = []
	else:
		gameset.append(game)

	ans = 0
	for game in gameset:
		ans += int(''.join(solve(game)[0][:3]))
	print ans

def getneighbors(board):
    imp = {}
    for rownum, row in enumerate(board):
        for colnum, cell in enumerate(row):
            excluded = set([x for x in board[rownum] if x != '0'])
            excluded |= set([board[y][colnum] for y in xrange(len(board)) if board[y][colnum] != '0'])
            excluded |= set([board[y][x] for y, x in getsquare(rownum, colnum) if board[y][x] != '0'])
            imp[rownum, colnum] = excluded
    return imp
    
def getsquare(rownum, colnum):
    from itertools import product
    x, y = rownum / 3, colnum / 3
    return product(xrange(3*x, 3*x+3),xrange(3*y, 3*y+3))

def updateboard(rownum, colnum, newdigit, impossible, board):
    board[rownum][colnum] = newdigit
    for x,y in getsquare(rownum, colnum):
        impossible[x,y].add(newdigit)
    for i in xrange(len(board)):
        impossible[rownum, i].add(newdigit)
        impossible[i, colnum].add(newdigit)
    
    
def findexcluded(row, col, neighbors, board):
    value, digits = board[row][col], set('123456789')    

    possible4 = digits-neighbors[row, col]
    if len(possible4) == 1:
        return possible4.pop()
    else:
        possible1, possible2, possible3 = set('123456789'), set('123456789'), set('123456789')
        for i in xrange(len(board)):
            if i != col:
                if board[row][i] == '0': possible1 &= neighbors[row, i]
            if i != row:
                if board[i][col] == '0': possible2 &= neighbors[i, col]
        possible1 -= neighbors[row, col]
        possible2 -= neighbors[row, col]
    	
        for x, y in getsquare(row, col):
            if (x,y) !=(row, col):
                if board[x][y] == '0': possible3 &= neighbors[x,y]
        possible3 -= neighbors[row, col]
	
    for pos in [possible1, possible2, possible3, possible4]:
        if len(pos) == 1:
            value = pos.pop()
    return value
    
def fillin(board):
    neighbors, complete = getneighbors(board), False
    while not complete:
        complete = True
        for ridx, row in enumerate(board):
            for cidx, col in enumerate(row):
                if col == '0':
                    val = findexcluded(ridx, cidx, neighbors, board)
                    if val != '0':
                        complete = False
                        updateboard(ridx, cidx, val, neighbors, board)
    return neighbors
    
    
def copyboard(board):
    return [[cell for cell in row] for row in board]
	
	
def solve(board):
	neighbors = fillin(board)
	choices, cx, cy, choicestack, digits, filled = 10, 0, 0, [], set('123456789'), True
	for ridx, row in enumerate(board):
		for cidx, col in enumerate(row):
			if col == '0':
				filled = False
				if (9-len(neighbors[ridx, cidx])) < choices:
					choices, cx, cy, choicestack = 9-len(neighbors[ridx, cidx]), ridx, cidx, digits-neighbors[ridx, cidx]
	if filled: return board
	elif choices == 0: return False
	else:
		for choice in choicestack:
			copy = copyboard(board)
			copy[cx][cy] = choice
			tmp = solve(copy)
			if tmp:
				return tmp
		return False

# this function isn't used but helps for solving random problems
def process(ans):
	ans, board = ans.split('\n'),  []
	for line in ans:
		board.append(list(line))
	return board


if __name__ == "__main__":
	euler96()


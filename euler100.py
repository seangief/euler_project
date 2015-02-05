# http://math.stackexchange.com/questions/531833/generating-all-solutions-for-a-negative-pell-equation
# these solutions are defined by y**2-2*x**2 = -1, where y = 2*t-1, and 
# x = 2*b-1, where b is the number of blue chips, and t is the total chips
# This is a negative pell equation.

def euler100():
	b, t = 15, 21
	x, y = b*2-1, t*2-1 
	while t < 1000000000000:
		y, x = neg_pell_eq(y, x)
		b, t = (x+1)/2, (y+1)/2
	print b, "/", t

def neg_pell_eq(xn, yn):
	return (3*xn+4*yn, 2*xn+3*yn)

if __name__ == "__main__":
	euler100()

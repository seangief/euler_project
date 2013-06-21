from decimal import *

getcontext().prec = 100
b = Decimal(10**12)
f = 1+2*Decimal(b**2-b).sqrt()
while f-f.to_integral_value() != 0:
	print f-f.to_integral_value()
	b+=1
	f = 1+2*Decimal(b**2-b).sqrt()
print b

#-1000000000000

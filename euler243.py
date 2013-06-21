# totient of 94745 = 64944
# factors of 94745 = 5, 7, 2707
# 603,912,399,090 definitely works

import isprime as ip

def euler243():
	ansbound = float(15499)/94744
	totients = ip.totrange(7000000)
	numfactr = 94744+1
	numtotient = ip.totient(numfactr)
	found = False
	i = 2
	try:
		while not found:
			temp = i/ip.gcd(numfactr, i)
			if totients[temp] != 0:
				if numtotient*totients[temp]/float(i*(numfactr-1)) < ansbound:
					found = True
					print numtotient*totients[temp]/float(i*(numfactr-1)), " < ", ansbound
					print i
			i+=1

		print numfactr*i
	except:
		print i

if __name__ == "__main__":
	euler243()



'''
def euler243():
	ansbound = float(15499)/94744
	numfactr = 94744+1
	found = False
	i = 2
	candidate = numfactr
	while not found:
		if ip.gcd(candidate, i) == 1:
			candidate*= i
			if ip.totient(candidate)/float(candidate-1) < ansbound:
				found = True
		i+= 1
	print candidate

def euler243():
	ansbound = float(15499)/94744
	numfactr = 94744+1
	found = False
	i = 2
	candidate = numfactr
	try:
		while not found:
			candidate = numfactr * i
			if ip.totient(candidate)/float(candidate-1) < ansbound:
				found = True
			i+=1

		print candidate
	except:
		print candidate

'''

import isprime as ip

def euler12():
    index, divisors, triangle = 1, 3, 0
    while divisors < 500:
        triangle = index*(index+1)/2
        divisors = len(ip.allfacts(triangle))
	index+=1
    print triangle


if __name__ == "__main__":
	euler12()

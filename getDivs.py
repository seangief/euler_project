def getDivs(number):
   divisors = []
   for i in range(1,number-1):
      if number%i == 0:
         divisors.append(i)
   return divisors

def getNDivs(number):
   divisors = []
   for i in range(1,number-1):
      if number%i == 0:
         divisors.append(i)
   return len(divisors)

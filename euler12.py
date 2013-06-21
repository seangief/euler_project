def euler12():
    divs = 0
    count = 1
    triangle = (count**2+count)/2
    
    while divs < 500:
        triangle = (count**2+count)/2
        divs = getNDivs(triangle)
        count+=1 
    return triangle

def getNDivs(number):
   divisors = []
   for i in range(1,number-1):
      if number%i == 0:
         divisors.append(i)
   return len(divisors)

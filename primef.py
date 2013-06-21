def findLPrime(test):
    import math
    prime = -1
    if test < 0:
        return -1
    else:
        bound = int(math.sqrt(test))
        for integer in range(2,bound+1):
                if test%integer == 0:
                    prime = integer
                    break
        return prime

def listFactors(number):
    if findLPrime(number) < 0:
        return []
    else:
        factors = []
        factor = findLPrime(number)
        while findLPrime(number) > 0:
            factors.append(factor)
            number = number/factor
            factor = findLPrime(number)
        factors.append(number)
        return factors

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number*factorial(number-1)

def permu(elements,total):
    return (factorial(total))/(factorial(elements)*factorial(total-elements))

def combin(elements,total):
    return (factorial(total))/(factorial(elements))

def thin(list1,list2):
    for item in list1:
        if item in list2:
            list1.remove(item)
            list2.remove(item)

def duplicates(factors):
    duplicate = []
    for item in factors:
       count = 0
       for t in range(1,len(factors)):
          if factors[t] == item:
             count+=1
       duplicate.append(count)
    return duplicate


def divisorCalc(factors, duplicates):
    n = len(factors)
    for t in range(1,len(duplicate)):
       n -= duplicate[t]-1
       k += duplicate[t]-1
    total = (2**(n)-1) + (k*n)
    return total

def euler12():
    number, count = 0
    while divisors < 500:
        number = count*(count+1) /2
        factors = listFactors(number)
        divisors = divisorCalc(factors,divisorCalc(factors))
        count+=1
    return number

"""
list1 = range(1,n)   // list1 is a set of items
list2 = range(n-k,n)  // list2 is the number of elements to be combined in list1
list3 = range(1,k) // list3 are the elements that are duplicated. We don't use
                    //  these in permutations, only in combinations
    I think these ranges are a little messed up...
    
thin(list1,list2)
thin(list1,list3)
for all items in list1, list2
count *= (list1.pop(item)/list2.pop(item))
count /= list3.pop(item)
return count

// Will prevent overflow, but this may result in rounding errors!

For extensive thinning, it might be best to make new lists factors1,
factors2, then

for all n in range:
   factors1.extend(listFactors(n))
   factors2.extend(listFactors(n))
   factors3.extend(listFactors(n))
divisors = factors2+factors3

then thin(factors1, divisors)
then product of factors1/product of divisors

def bestFact(element,base):
    list1 = range(1,element)-range(1,base)+range(1,element-base)
    list2 = range(1,base)+range(1,element-base) - range(1,element) " This syntax only works on set!"
    if len(list1) > len(list2):
        list2.append(1)*(len(list1)-len(list2)) " This syntax only works on set!"
    elif len(list2) > len(list1):
        list1.append(1)*(len(list2)-len(list1)) " This syntax only works on set!"
    float total
    for i in range(1,len(list1)):
        total *= list1.pop(i) / list2.pop(i)
    return total


def unique(list1):
    unique = []
    for item in list1:
        unique.append(item)
    return unique

def // function that returns # of duplicates, i.e.:
for input
[1,2,2,4,7,3,21,11,13,4]
it returns
[3,2]
- meaning that there are 2 dulicate items, one appearing 3 times, one
appearing twice.

def // function that 
for i in range(1,len(list3)):
	if list3[i] in list2:
		list2.remove(list3[i])
		del list3[i]
"""


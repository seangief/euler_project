from decimal import *
from bigfloat import *

print sum([sum(Decimal(str(sqrt(i, precision(400)))).as_tuple().digits[0:100]) for i in {x for x in range(1,100) if x not in [i**2 for i in range(0,10)]}])


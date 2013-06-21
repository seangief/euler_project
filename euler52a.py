import sys

i = int(sys.argv[1])
s = sorted(str(i))
print i
print s
if s != sorted(str(2*i)):
	print "Fails on 2!"
elif s != sorted(str(3*i)):
	print "Fails on 3!"
elif s != sorted(str(4*i)):
	print "Fails on 4!"
elif s != sorted(str(5*i)):
	print "Fails on 5!"
elif s != sorted(str(6*i)):
	print "Fails on 6!"
else:
	print "Nothing succeeds like success!"

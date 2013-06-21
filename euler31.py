#73682

tup = range(0,101)
fivep =  range(0,41)
tenp = range(0,21)
twentyp = range(0,11)
fiftyp= range(0,5)
oned = range(0,3)

counter =0
for a in tup:
	for b in fivep:
		for c in tenp:
			for d in twentyp:
				for e in fiftyp:
					for f in oned:
						sansPence = (a*2)+(b*5)+(c*10)+(d*20)+(e*50)+(f*100)
						if sansPence  <= 200:
							counter +=1

counter +=1  ## for 2d.
print counter

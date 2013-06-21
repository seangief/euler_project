f = open("keylog.txt")
keylog = f.read().split('\n')
keylog = keylog[:len(keylog)-2]
firsts = set([i[0] for i in keylog])
mids  = set([i[1] for i in keylog])
lasts = set([i[2] for i in keylog])
firsts-(mids|lasts) # = 7... first digit 7
lasts-(firsts|mids) # = 0... last digit 0

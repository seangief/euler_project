def euler55():
    lyrichal = []
    for i in range(1,10001):
        if palindrome(i):
            lyrichal.append(i)
        else for k in range(0,50):
            i = temp
            temp += backwards(temp)
            if palindrome(temp):
                lyrichal.append(i)
                break
    return len(lyrichal)
        
def backwards{forewards}:
    str(forewards)
    backwards = ''
    for i in range(len(forewards)):
        backwards += forewards[-i-1]
    return int(forewards)

def palindrome(test):
    if test == backwards(test):
        return true
    else return false
    

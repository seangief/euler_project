def euler55(bound):
    ly = []
    for number in range(1,bound+1):
        if lyrichaln(number):
            ly.append(number)
    return len(ly)
        
def backwards(fore):
    fore = str(fore)
    back = ''
    for i in range(len(fore)):
        back += fore[-i-1]
    return int(back)

def palindrome(test):
    if test == backwards(test):
        return 1
    else:
        return 0
    
def lyrichaln(i):
    lyrichal = 1
    for number in range(0,50):
        i += backwards(i)
        if palindrome(i):
            lyrichal = 0
            break
    return lyrichal

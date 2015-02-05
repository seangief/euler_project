def euler125():
    ans = set()

    for i in xrange(1, 10001):
        count = i**2
        for j in xrange(i+1, 10001):
            count += j**2
            if count > 10**8:
                break
            else:
                if palindrome(count):
                    ans.add(count)
    print sum(ans)


def palindrome(n):
    r = str(n)
    if not (r == r[::-1]):
        return False
    return True

if __name__ == "__main__":
    euler125()

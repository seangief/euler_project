from isprime import primes_sieve2

def euler123():
    primes, power, rem = primes_sieve2(1000000), 0, 1

    while rem < 10**10:
        power += 1
        prime = primes.next()
        mod = prime**2
        rem = (mod_power(prime-1, mod, power) + mod_power(prime+1, mod, power)) % mod
    print power

def mod_power(n, mod, power):
    if power == 1:
        return n % mod
    elif power % 2 == 0:
        p = mod_power(n, mod, power/2)
        return (p * p) % mod
    else:
        return (n * mod_power(n, mod, power-1)) % mod

if __name__ == "__main__":
    euler123()


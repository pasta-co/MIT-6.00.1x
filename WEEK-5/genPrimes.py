def genPrimes():
    x, primes = 2, []
    while True:
        if all([x % p != 0 for p in primes]):
            yield x
            primes.append(x)
        x += 1

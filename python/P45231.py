def fibs():
    a = 0
    yield a
    b = 1
    while (True):
        yield b
        a, b = b, a + b


def roots(n):
    a = n
    yield a
    b = 0.5 * (a + (n/a))
    while (True):
        yield b
        a, b = b, 0.5 * (b + (n/b))


def isPrime(x):
    if x == 1 or x == 0:
        return False
    primo = True
    for i in range(2, x):
        primo = primo and (x % i) != 0
    return primo


def primes():
    res = 2
    yield res
    while (True):
        res += 1
        if isPrime(res):
            yield res


def isHamming(n):
    if (n == 1):
        return True
    elif (n % 2 == 0):
        return isHamming(n/2)
    elif (n % 3 == 0):
        return isHamming(n/3)
    elif (n % 5 == 0):
        return isHamming(n/5)
    else:
        return False


def hammings():
    res = 1
    yield res
    while (True):
        res += 1
        if (isHamming(res)):
            yield res

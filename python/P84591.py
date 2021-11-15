def absValue(x):
    if x < 0:
        return -x
    else:
        return x


def power(x, p):
    return x ** p


def isPrime(x):
    if x == 1 or x == 0:
        return False
    primo = True
    for i in range(2, x):
        primo = primo and (x % i) != 0
    return primo


def slowFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = 2
        anterior = 0
        actual = 1
        while i <= n:
            temp = actual
            actual = actual + anterior
            anterior = temp
            i += 1
        return actual


def fib(n):
    if n < 2:
        return (0, n)
    (f2, f1) = fib(n - 1)
    return (f1, f1+f2)


def quickFib(x): return fib(x)[1]

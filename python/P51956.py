from functools import reduce


def myLength(L):
    def sumaUno(x, y): return x + 1
    return reduce(sumaUno, L, 0)


def myMaximum(L):
    def max(x, y):
        if x < y:
            return y
        else:
            return x

    return reduce(max, L)


def average(L):
    def suma(x, y): return x + y
    acumulador = reduce(suma, L, 0)
    return acumulador/myLength(L)


def buildPalindrome(L):
    def fusion(x, y):
        lista = [y]
        return lista + x

    inversa = reduce(fusion, L, [])
    return inversa + L


def flatten(L):
    acumulador = []
    for lista in L:
        if isinstance(lista, list):
            acumulador = acumulador + flatten(lista)
        else:
            acumulador.append(lista)
    return acumulador


def remove(L1, L2):
    return [x for x in L1 if x not in L2]


def oddsNevens(L):
    L1 = [x for x in L if x % 2 != 0]
    L2 = [x for x in L if x % 2 == 0]
    return L1, L2


def isPrime(x):
    if x == 1 or x == 0:
        return False
    primo = True
    for i in range(2, x):
        primo = primo and (x % i) != 0
    return primo


def primeDivisors(n):
    if n > 0:
        result = []
        for i in range(2, n + 1):
            if isPrime(i) and n % i == 0:
                result.append(i)

        return result
    return []

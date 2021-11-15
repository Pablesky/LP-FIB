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

        #fusion = lambda x, y: [y] + x

    inversa = reduce(fusion, L, [])
    return inversa + L

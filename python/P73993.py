from functools import reduce


def evens_product(L):
    def multiplica(x, y): return x * y

    def my_filter(f, L):
        return [x for x in L if f(x)]

    def par(x): return x % 2 == 0

    return reduce(multiplica, my_filter(par, L), 1)


def reverse(L):
    def invertir(x, y): return [y] + x
    return reduce(invertir, L, [])


def zip_with(f, L1, L2):
    return [f(x, y) for (x, y) in zip(L1, L2)]


def count_if(f, L):
    def my_filter(f1, L1):
        return [x for x in L1 if f1(x)]

    return len(my_filter(f, L))

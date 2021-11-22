from functools import reduce


def count_unique(L):
    return len(set(L))


def remove_duplicates(L):
    return set(L)


"""
def flatten(L):
    acumulador = []
    for lista in L:
        acumulador = acumulador + lista

    return acumulador
"""


def flatten(L):
    def concat(L1, L2): return L1 + L2
    return reduce(concat, L)


def flatten_rec(L):
    acumulador = []
    for lista in L:
        if isinstance(lista, list):
            acumulador = acumulador + flatten_rec(lista)
        else:
            acumulador.append(lista)
    return acumulador

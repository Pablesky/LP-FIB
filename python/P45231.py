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

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def division(n1, n2):
    return n1 // n2


def multiplicacion(n1, n2):
    return n1 * n2


def potencia(n1, n2):
    return n1 ** n2


def igual(n1, n2):
    print(type(n1))
    print(type(n2))
    print(n1)
    print(n2)
    return n1 == n2


def menor(n1, n2):
    return n1 < n2


def mayor(n1, n2):
    return n1 > n2


def menorigual(n1, n2):
    return n1 <= n2


def mayorigual(n1, n2):
    return n1 >= n2


diccionario = {'+': suma, '-': resta,
               '*': multiplicacion, '/': division, '^': potencia,
               '=': igual, '<': menor, '>': mayor,
               '>=': menorigual, '<=': mayorigual}


class TreeVisitor(ExprVisitor):
    taulaSimbols = {}

    def __init__(self):
        self.nivell = 0

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        valor = self.visit(l[0])
        if valor != None:
            print(valor)

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            if (l[0].getText().isnumeric()):
                return int(l[0].getText())
            else:
                return int(self.taulaSimbols[l[0].getText()])

        elif len(l) == 2:
            print(self.visit(l[1]))

        elif l[0].getText() == "(":
            return self.visit(l[1])

        else:  # len(l) == 3
            if l[1].getText() == ":=":
                self.taulaSimbols[l[0].getText()] = self.visit(l[2])

            else:
                #print(len(list(l[0].getChildren())))
                return diccionario[l[1].getText()](self.visit(l[0]),
                                                   self.visit(l[2]))

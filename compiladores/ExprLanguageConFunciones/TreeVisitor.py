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
               '*': multiplicacion, '/': division, '^': potencia}
comparaciones = {'=': igual, '<': menor,
                 '>': mayor, '<=': menorigual, '>=': mayorigual}


class TreeVisitor(ExprVisitor):

    def __init__(self): _
        self.taulaSimbols = {}

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            resultat = l[0].getText()
            if resultat.isnumeric():
                return int(resultat)
            else:
                return self.taulaSimbols[resultat]

        else:  # len(l) == 3
            return diccionario[l[1].getText()](self.visit(l[0]),
                                               self.visit(l[2]))

    def visitAssignation(self, ctx):
        l = list(ctx.getChildren())
        self.taulaSimbols[l[0].getText()] = self.visit(l[2])

    def visitImprimir(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[1]))

    def visitCondition(self, ctx):
        l = list(ctx.getChildren())
        return comparaciones[l[1].getText()](self.visit(l[0]), self.visit(l[2]))

    def visitIfcondition(self, ctx):
        l = list(ctx.getChildren())
        if (self.visit(l[1])):
            for i in range(3, len(l)-1):
                self.visit(l[i])

    def visitBucle(self, ctx):
        l = list(ctx.getChildren())
        while (self.visit(l[1])):
            for i in range(3, len(l)-1):
                self.visit(l[i])

    def visitFuncion(self, ctx):
        l = list(ctx.getChildren())
        self.taulaFuncions[l[1].getText()] = ctx

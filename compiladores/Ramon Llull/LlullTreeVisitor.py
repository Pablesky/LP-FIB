if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor


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


def modulo(n1, n2):
    return n1 % n2


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


taulaOperacions = {'+': suma, '-': resta,
                   '*': multiplicacion, '/': division, '^': potencia,
                   '%': modulo}

comparaciones = {'=': igual, '<': menor,
                 '>': mayor, '<=': menorigual, '>=': mayorigual}


class LlullTreeVisitor(llullVisitor):

    def __init__(self):
        self.taulaSimbols = {}

    def visitInstru(self, ctx):
        llistaFills = list(ctx.getChildren())
        retorno = self.visit(llistaFills[0])
        if (retorno is not None):
            print(retorno)

    def visitExpr(self, ctx):
        llistaFills = list(ctx.getChildren())
        if (len(llistaFills) == 1):
            contingut = llistaFills[0].getText()
            if (contingut.isnumeric()):
                return int(contingut)
            else:
                return self.taulaSimbols[contingut]

        else:
            if (llistaFills[0].getText() == "("):
                return self.visit(llistaFills[1])

            else:
                return taulaOperacions[llistaFills[1].getText()](self.visit(llistaFills[0]), self.visit(llistaFills[2]))

    def visitAssigancio(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.taulaSimbols[llistaFills[0].getText()] = self.visit(
            llistaFills[2])

    def visitLectura(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.taulaSimbols[llistaFills[2].getText()] = int(input())

    def visitEscriptura(self, ctx):
        llistaFills = list(ctx.getChildren())
        llistaPerImprimir = self.visit(llistaFills[2])
        for impresion in llistaPerImprimir:
            print(impresion, end=" ")

        print("\n")

    def visitBlocStrings(self, ctx):
        llistaFills = list(ctx.getChildren())
        resultado = []
        for contenidoHijo in llistaFills:
            contenido = contenidoHijo.getText()
            if (contenido != ","):
                if (contenido.startswith("\"") and contenido.endswith("\"")):
                    resultado.append(contenido[1:-1])
                else:
                    result = str((self.visit(contenidoHijo)))
                    if (result is not None):
                        resultado.append(result)
        return resultado

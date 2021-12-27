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
    return int(n1 == n2)


def diferente(n1, n2):
    return int(n1 != n2)


def menor(n1, n2):
    return int(n1 < n2)


def mayor(n1, n2):
    return int(n1 > n2)


def menorigual(n1, n2):
    return int(n1 <= n2)


def mayorigual(n1, n2):
    return int(n1 >= n2)


taulaOperacions = {'+': suma, '-': resta,
                   '*': multiplicacion, '/': division, '^': potencia,
                   '%': modulo}

taulaComparacions = {'==': igual, '<': menor, '<>': diferente,
                     '>': mayor, '<=': menorigual, '>=': mayorigual}


class LlullTreeVisitor(llullVisitor):

    def __init__(self):
        self.taulaSimbols = [{}]
        self.taulaFuncions = {}

    def empieza0(self, func):
        ejecuto = self.taulaFuncions[func]
        cuerpo = ejecuto[1]
        self.visit(cuerpo)

    def empieza1(self, func, values):

        ejecuto = self.taulaFuncions[func]
        cuerpo = ejecuto[1]
        asignaciones = ejecuto[0]

        for i in range(0, len(asignaciones)):
            self.taulaSimbols[-1][asignaciones[i]] = int(values[i])

        self.visit(cuerpo)

    def visitExpr(self, ctx):
        llistaFills = list(ctx.getChildren())
        if (len(llistaFills) == 1):
            contingut = llistaFills[0].getText()
            if (contingut.isnumeric()):
                return int(contingut)
            else:
                return self.taulaSimbols[-1][contingut]

        else:
            if (llistaFills[0].getText() == "("):
                return self.visit(llistaFills[1])

            else:
                return taulaOperacions[llistaFills[1].getText()](self.visit(llistaFills[0]), self.visit(llistaFills[2]))

    def visitAssigancio(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.taulaSimbols[-1][llistaFills[0].getText()] = self.visit(
            llistaFills[2])

    def visitLectura(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.taulaSimbols[-1][llistaFills[2].getText()] = int(input())

    def visitEscriptura(self, ctx):
        llistaFills = list(ctx.getChildren())
        llistaPerImprimir = self.visit(llistaFills[2])
        for impresion in llistaPerImprimir:
            print(impresion, end="")
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

    def visitBloc(self, ctx):
        llistaFills = list(ctx.getChildren())
        for instru in llistaFills:
            self.visit(instru)

    def visitBucleWhile(self, ctx):
        llistaFills = list(ctx.getChildren())
        while (self.visit(llistaFills[2])):
            self.visit(llistaFills[5])

    def visitBucleFor(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.visit(llistaFills[2])
        while (self.visit(llistaFills[4])):
            self.visit(llistaFills[9])
            self.visit(llistaFills[6])

    def visitAsigParametros(self, ctx):
        llistaFills = list(ctx.getChildren())
        variables = []
        for variable in llistaFills:
            contenido = variable.getText()
            if (contenido != ','):
                variables.append(contenido)

        return variables

    def visitAsignacionFuncion(self, ctx):
        llistaFills = list(ctx.getChildren())
        nameFuncio = llistaFills[1].getText()
        variables = self.visit(llistaFills[3])
        ejecucion = llistaFills[6]
        self.taulaFuncions[nameFuncio] = [variables, ejecucion]

    def visitEjecParametros(self, ctx):
        llistaFills = list(ctx.getChildren())
        variables = []
        for variable in llistaFills:
            contenido = variable.getText()
            if (contenido != ','):
                variables.append(self.visit(variable))

        return variables

    def visitEjecutarFuncion(self, ctx):
        llistaFills = list(ctx.getChildren())
        contenido = self.visit(llistaFills[2])

        nameFuncio = llistaFills[0].getText()
        tuplaFuncion = self.taulaFuncions[nameFuncio]
        asigancionesFuturas = tuplaFuncion[0]
        cuerpo = tuplaFuncion[1]

        self.taulaSimbols.append({})

        for i in range(0, len(asigancionesFuturas)):
            self.taulaSimbols[-1][asigancionesFuturas[i]
                                  ] = contenido[i]

        self.visit(cuerpo)
        self.taulaSimbols.pop()

    def visitIfCondicion(self, ctx):
        llistaFills = list(ctx.getChildren())
        if (self.visit(llistaFills[2])):
            self.visit(llistaFills[5])

        else:
            if (len(llistaFills) == 8):
                self.visit(llistaFills[7])

    def visitElseCondicion(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.visit(llistaFills[2])

    def visitCondicion(self, ctx):
        llistaFills = list(ctx.getChildren())
        return taulaComparacions[llistaFills[1].getText()](self.visit(llistaFills[0]),
                                                           self.visit(
                                                                   llistaFills[2]))

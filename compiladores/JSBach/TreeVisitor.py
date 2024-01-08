from antlr4 import *
import subprocess

if __name__ is not None and "." in __name__:
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachVisitor import jsbachVisitor


def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def division(n1, n2):
    if (n2 == 0):
        raise Exception("El segon argument es un 0 i no es pot dividir per 0")
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

taulaComparacions = {'=': igual, '<': menor, '/=': diferente,
                     '>': mayor, '<=': menorigual, '>=': mayorigual}

taulaNotas = {'A0': 0, 'B0': 1, 'C1': 2, 'D1': 3, 'E1': 4, 'F1': 5, 'G1': 6,
              'A1': 7, 'B1': 8, 'C2': 9, 'D2': 10, 'E2': 11, 'F2': 12, 'G2': 13,
              'A2': 14, 'B2': 15, 'C3': 16, 'D3': 17, 'E3': 18, 'F3': 19, 'G3': 20,
              'A3': 21, 'B3': 22, 'C4': 23, 'D4': 24, 'E4': 25, 'F4': 26, 'G4': 27,
              'A4': 28, 'B4': 29, 'C5': 30, 'D5': 31, 'E5': 32, 'F5': 33, 'G5': 34,
              'A5': 35, 'B5': 36, 'C6': 37, 'D6': 38, 'E6': 39, 'F6': 40, 'G6': 41,
              'A6': 42, 'B6': 43, 'C7': 44, 'D7': 45, 'E7': 46, 'F7': 47, 'G7': 48,
              'A7': 49, 'B7': 50, 'C8': 51}

taulaNumeros = {0: 'a\'0', 1: 'b\'0', 2: 'c\'1', 3: 'd\'1', 4: 'e\'1', 5: 'f\'1', 6: 'g\'1',
                7: 'a\'1', 8: 'b\'1', 9: 'c\'2', 10: 'd\'2', 11: 'e\'2', 12: 'f\'2', 13: 'g\'2',
                14: 'a\'2', 15: 'b\'2', 16: 'c\'3', 17: 'd\'3', 18: 'e\'3', 19: 'f\'3', 20: 'g\'3',
                21: 'a\'3', 22: 'b\'3', 23: 'c\'4', 24: 'd\'4', 25: 'e\'4', 26: 'f\'4', 27: 'g\'4',
                28: 'a\'4', 29: 'b\'4', 30: 'c\'5', 31: 'd\'5', 32: 'e\'5', 33: 'f\'5', 34: 'g\'5',
                35: 'a\'5', 36: 'b\'5', 37: 'c\'6', 38: 'd\'6', 39: 'e\'6', 40: 'f\'6', 41: 'g\'6',
                42: 'a\'6', 43: 'b\'6', 44: 'c\'7', 45: 'd\'7', 46: 'e\'7', 47: 'f\'7', 48: 'g\'7',
                49: 'a\'7', 50: 'b\'7', 51: 'c\'8'}


def reproduir(notas):
    print(notas)
    partitura = ""
    if len(notas) != 0:
        for nota in notas:
            partitura = partitura + taulaNumeros[nota] + ' '

    texto = """
                \\version "2.20.0"
                \\score {
                    \\absolute {
                        \\tempo 4 = 120
                        %s
                    }
                    \\layout {}
                    \\midi {}
                    }
            """ % partitura
    with open('notas.lily', 'w+') as f:
        f.write(texto)

    subprocess.call('lilypond notas.lily', shell=True, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

    subprocess.call('timidity -Ow -o notas.wav notas.midi', shell=True, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

    subprocess.call('ffmpeg -i notas.wav -codec:a libmp3lame -qscale:a 2 notas.mp3 -y', shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

    #subprocess.call('mpg123 notas.mp3', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.STDOUT)


class JSTreeVisitor(jsbachVisitor):
    def __init__(self):
        self.taulaSimbols = [{}]
        self.taulaFuncions = {}
        self.notes = []

    def comenca0(self, func):
        executo = self.taulaFuncions[func]
        cos = executo[1]
        self.visit(cos)
        reproduir(self.notes)

    def comenca1(self, func, values):
        executo = self.taulaFuncions[func]
        cos = executo[1]
        assignacions = executo[0]

        for i in range(0, len(assignacions)):
            self.taulaSimbols[-1][assignacions[i]] = int(values[i])

        self.visit(cos)
        reproduir(self.notes)

    def visitExpr(self, ctx):
        llistaFills = list(ctx.getChildren())
        if (len(llistaFills) == 1):
            contingut = llistaFills[0].getText()

            if (contingut.isnumeric()):
                return int(contingut)
            else:
                if llistaFills[0].getText() in 'ABCDEFG':
                    return taulaNotas[llistaFills[0].getText() + '4']

                elif '[' in llistaFills[0].getText():
                    return self.visit(llistaFills[0])

                elif llistaFills[0].getText() in list(taulaNotas.keys()):
                    return taulaNotas[llistaFills[0].getText()]

                elif '#' in llistaFills[0].getText():
                    return self.visit(llistaFills[0])

                else:
                    return self.taulaSimbols[-1][contingut]

        else:
            if (llistaFills[0].getText() == "("):
                return self.visit(llistaFills[1])

            else:
                numero1 = self.visit(llistaFills[0])
                numero2 = self.visit(llistaFills[2])

                if not isinstance(numero1, int) or not isinstance(numero2, int):
                    raise Exception("No es poden operar les arrays")

                return taulaOperacions[llistaFills[1].getText()](
                    numero1, numero2)

    # Visit a parse tree produced by jsbachParser#condicio.
    def visitCondicio(self, ctx):
        llistaFills = list(ctx.getChildren())
        return taulaComparacions[llistaFills[1].getText()](
            self.visit(llistaFills[0]), self.visit(llistaFills[2]))

    # Visit a parse tree produced by jsbachParser#lectura.
    def visitLectura(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.taulaSimbols[-1][llistaFills[1].getText()] = int(input())

    # Visit a parse tree produced by jsbachParser#escriure.
    def visitEscriure(self, ctx):
        llistaFills = list(ctx.getChildren())
        llistaImprimir = self.visit(llistaFills[1])
        for impresion in llistaImprimir:
            print(impresion, end="")
        print("\r")

    # Visit a parse tree produced by jsbachParser#blocStrings.
    def visitBlocStrings(self, ctx):
        llistaFills = list(ctx.getChildren())
        retorn = []
        for paraula in llistaFills:
            contingut = paraula.getText()
            if contingut.startswith('"'):
                retorn.append(contingut[1:-1])
            else:
                resultat = str(self.visit(paraula))
                if (resultat is not None):
                    retorn.append(resultat)

        return retorn

    # Visit a parse tree produced by jsbachParser#bucleWhile.
    def visitBucleWhile(self, ctx):
        llistaFills = list(ctx.getChildren())
        while (self.visit(llistaFills[1])):
            self.visit(llistaFills[3])

    def visitBloc(self, ctx):
        llistaFills = list(ctx.getChildren())
        for instru in llistaFills:
            self.visit(instru)

    # Visit a parse tree produced by jsbachParser#assigancio.
    def visitAssigancio(self, ctx):
        llistaFills = list(ctx.getChildren())
        if llistaFills[1] == '[':
            lista = self.taulaSimbols[-1][llistaFills[0].getText()]
            lista[self.visit(llistaFills[2])] = self.visit(llistaFills[5])
        else:
            self.taulaSimbols[-1][llistaFills[0].getText()] = self.visit(llistaFills[2])

    def visitCrearFuncio(self, ctx):
        llistaFills = list(ctx.getChildren())
        nameFuncio = llistaFills[0].getText()

        if nameFuncio in self.taulaFuncions:
            raise Exception("La funcio ja ha sigut declarada")

        variables = self.visit(llistaFills[1])
        setVariables = set(variables)
        if len(variables) != len(setVariables):
            raise Exception("Hi ha dos parametres formals amb el mateix nom")

        execucio = llistaFills[3]
        self.taulaFuncions[nameFuncio] = [variables, execucio]

    # Visit a parse tree produced by jsbachParser#executarFuncio.
    def visitExecutarFuncio(self, ctx):
        llistaFills = list(ctx.getChildren())
        nameFuncio = llistaFills[0].getText()
        if nameFuncio not in self.taulaFuncions:
            raise Exception("La funcio no existeix")

        contenido = self.visit(llistaFills[1])
        tuplaFuncion = self.taulaFuncions[nameFuncio]
        asigancionesFuturas = tuplaFuncion[0]
        cuerpo = tuplaFuncion[1]

        self.taulaSimbols.append({})

        if len(asigancionesFuturas) != len(contenido):
            raise Exception("Els parametres de la funcio no son els correctes")

        for i in range(0, len(asigancionesFuturas)):
            self.taulaSimbols[-1][asigancionesFuturas[i]
            ] = contenido[i]

        self.visit(cuerpo)
        self.taulaSimbols.pop()

    # Visit a parse tree produced by jsbachParser#executarParametres.
    def visitExecutarParametres(self, ctx):
        llistaFills = list(ctx.getChildren())
        variables = []
        for variable in llistaFills:
            variables.append(self.visit(variable))

        return variables

    # Visit a parse tree produced by jsbachParser#crearParametres.
    def visitCrearParametres(self, ctx):
        llistaFills = list(ctx.getChildren())
        variables = []
        for variable in llistaFills:
            contenido = variable.getText()
            variables.append(contenido)

        return variables

    # Visit a parse tree produced by jsbachParser#condicioIf.
    def visitCondicioIf(self, ctx):
        llistaFills = list(ctx.getChildren())
        if (self.visit(llistaFills[1])):
            self.visit(llistaFills[3])

        else:
            if (len(llistaFills) == 6):
                self.visit(llistaFills[5])

    # Visit a parse tree produced by jsbachParser#condicioElse.
    def visitCondicioElse(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.visit(llistaFills[2])

    # Visit a parse tree produced by jsbachParser#agafarValorLLista.
    def visitAgafarValorLLista(self, ctx):
        llistaFills = list(ctx.getChildren())
        return self.taulaSimbols[-1][llistaFills[0].getText()][self.visit(llistaFills[2]) - 1]

    # Visit a parse tree produced by jsbachParser#afegirFinalLLista.
    def visitAfegirFinalLLista(self, ctx):
        llistaFills = list(ctx.getChildren())
        anadir = self.visit(llistaFills[2])
        if not isinstance(anadir, list):
            anadir = [anadir]
        self.taulaSimbols[-1][llistaFills[0].getText()].extend(anadir)

    # Visit a parse tree produced by jsbachParser#retallarLlista.
    def visitRetallarLlista(self, ctx):
        llistaFills = list(ctx.getChildren())
        lista = self.taulaSimbols[-1][llistaFills[1].getText()]
        del self.taulaSimbols[-1][llistaFills[1].getText()][self.visit(llistaFills[3]) - 1]

    # Visit a parse tree produced by jsbachParser#longitudLlista.
    def visitLongitudLlista(self, ctx):
        llistaFills = list(ctx.getChildren())
        return len(self.taulaSimbols[-1][llistaFills[1].getText()])

    # Visit a parse tree produced by jsbachParser#crearLlista.
    def visitCrearLlista(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.taulaSimbols[-1][llistaFills[0].getText()] = []
        if len(llistaFills) > 4:
            lista = llistaFills[3:-1]
            for numero in lista:
                afegir = self.visit(numero)
                self.taulaSimbols[-1][llistaFills[0].getText()].append(afegir)

    # Visit a parse tree produced by jsbachParser#notas.
    def visitNotas(self, ctx):
        llistaFills = list(ctx.getChildren())
        if len(llistaFills) == 2:
            contingut = llistaFills[1].getText()
            variable = self.taulaSimbols[-1][contingut]
            if not isinstance(variable, list):
                variable = [variable]
            self.notes.extend(variable)

        else:
            hijos = llistaFills[2:-1]
            for nota in hijos:
                letra = nota.getText()
                if letra in 'ABCDEFG':
                    letra = letra + '4'
                numero = taulaNotas[letra]
                self.notes.append(numero)

if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor

from colorama import Fore, init

init()


class beatVisitor(llullVisitor):

    def __init__(self):
        self.tabs = 0

    def visitExpr(self, ctx):
        llistaFills = list(ctx.getChildren())
        if (len(llistaFills) == 1):
            contingut = llistaFills[0].getText()
            if (contingut.startswith("get")):
                return self.visit(llistaFills[0])

            elif (contingut.isnumeric()):
                print(Fore.BLUE + contingut, end='')
            else:
                print(Fore.WHITE + contingut, end='')

        else:
            if (llistaFills[0].getText() == "("):
                print(Fore.WHITE + '(', end='')
                self.visit(llistaFills[1])
                print(Fore.WHITE + ')', end='')

            else:
                self.visit(llistaFills[0])
                print(' ', end='')
                print(Fore.WHITE + llistaFills[1].getText(), end=' ')
                self.visit(llistaFills[2])

    def visitAssigancio(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.WHITE
              + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end=' ')
        self.visit(llistaFills[2])

    def visitLectura(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.GREEN
              + llistaFills[0].getText(), end='')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        print(Fore.WHITE + llistaFills[2].getText(), end='')
        print(Fore.WHITE + llistaFills[3].getText(), end='')

    def visitBlocStrings(self, ctx):
        llistaFills = list(ctx.getChildren())
        for fill in llistaFills:
            paraula = fill.getText()
            if paraula == ',':
                print(Fore.WHITE + ',', end=' ')
            elif (paraula.startswith("\"") and paraula.endswith("\"")):
                print(Fore.BLUE + paraula, end='')
            else:
                self.visit(fill)

    def visitEscriptura(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.GREEN
              + llistaFills[0].getText(), end='')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print(Fore.WHITE + llistaFills[3].getText(), end='')

    def visitBloc(self, ctx):
        llistaFills = list(ctx.getChildren())
        for elem in llistaFills:
            print('    ' * self.tabs, end='')
            self.visit(elem)
            print('\r')

    def visitCondicion(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.visit(llistaFills[0])
        print(Fore.WHITE + ' ' + llistaFills[1].getText(), end=' ')
        self.visit(llistaFills[2])

    def visitBucleWhile(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.RED
              + llistaFills[0].getText(), end=' ')
        self.tabs += 1
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print(Fore.WHITE + llistaFills[3].getText(), end=' ')
        print(Fore.WHITE + llistaFills[4].getText(), end='')
        print('\r')
        self.visit(llistaFills[5])
        self.tabs -= 1
        print('   ' * self.tabs + Fore.WHITE
              + llistaFills[6].getText(), end='')

    def visitBucleFor(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.RED
              + llistaFills[0].getText(), end=' ')
        self.tabs += 1
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print(Fore.WHITE + llistaFills[3].getText(), end=' ')
        self.visit(llistaFills[4])
        print(Fore.WHITE + llistaFills[5].getText(), end=' ')
        self.visit(llistaFills[6])
        print(Fore.WHITE + llistaFills[7].getText(), end=' ')
        print(Fore.WHITE + llistaFills[8].getText(), end='')
        print('\r')
        self.visit(llistaFills[9])
        self.tabs -= 1
        print('   ' * self.tabs + Fore.WHITE
              + llistaFills[10].getText(), end='')

    def visitAsigParametros(self, ctx):
        llistaFills = list(ctx.getChildren())
        for fill in llistaFills:
            paraula = fill.getText()
            if paraula == ',':
                print(Fore.WHITE + ',', end=' ')
            else:
                print(Fore.WHITE + paraula, end='')

    def visitAsignacionFuncion(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.tabs += 1
        print(Fore.YELLOW + llistaFills[0].getText(), end=' ')
        print(Fore.LIGHTMAGENTA_EX + llistaFills[1].getText(), end=' ')
        print(Fore.WHITE + llistaFills[2].getText(), end='')
        self.visit(llistaFills[3])
        print(Fore.WHITE + llistaFills[4].getText(), end=' ')
        print(Fore.WHITE + llistaFills[5].getText(), end='')
        print('\r')
        self.visit(llistaFills[6])
        self.tabs -= 1
        print('   ' * self.tabs + Fore.WHITE
              + llistaFills[7].getText(), end='')
        print('\r')

    def visitIfCondicion(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.tabs += 1
        print(Fore.RED + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print(Fore.WHITE + llistaFills[3].getText(), end=' ')
        print(Fore.WHITE + llistaFills[4].getText(), end='')
        print('\r')
        self.visit(llistaFills[5])
        self.tabs -= 1
        print('   ' * self.tabs + Fore.WHITE
              + llistaFills[6].getText(), end=' ')
        if len(llistaFills) == 8:
            self.visit(llistaFills[7])

    def visitElseCondicion(self, ctx):
        llistaFills = list(ctx.getChildren())
        self.tabs += 1
        print(Fore.RED + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        print('\r')
        self.visit(llistaFills[2])
        self.tabs -= 1
        print('   ' * self.tabs + Fore.WHITE
              + llistaFills[3].getText(), end='')

    def visitEjecParametros(self, ctx):
        llistaFills = list(ctx.getChildren())
        for fill in llistaFills:
            paraula = fill.getText()
            if paraula == ',':
                print(Fore.WHITE + ',', end=' ')
            else:
                print(Fore.WHITE + paraula, end='')

    def visitEjecutarFuncion(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.LIGHTMAGENTA_EX + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print(Fore.WHITE + llistaFills[3].getText(), end='')

    def visitArrayCrear(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.GREEN + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        print(Fore.BLUE + llistaFills[2].getText(), end='')
        print(Fore.WHITE + llistaFills[3].getText(), end=' ')
        self.visit(llistaFills[4])
        print(Fore.WHITE + llistaFills[5].getText(), end='')

    def visitArrayGet(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.GREEN + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        print(Fore.BLUE + llistaFills[2].getText(), end='')
        print(Fore.WHITE + llistaFills[3].getText(), end=' ')
        self.visit(llistaFills[4])
        print(Fore.WHITE + llistaFills[5].getText(), end='')

    def visitArraySet(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.GREEN + llistaFills[0].getText(), end=' ')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        print(Fore.BLUE + llistaFills[2].getText(), end='')
        print(Fore.WHITE + llistaFills[3].getText(), end=' ')
        self.visit(llistaFills[4])
        print(Fore.WHITE + llistaFills[5].getText(), end=' ')
        self.visit(llistaFills[6])
        print(Fore.WHITE + llistaFills[7].getText(), end=' ')

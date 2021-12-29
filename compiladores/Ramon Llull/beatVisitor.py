if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor

from colorama import Fore, init

init()


class beatVisitor(llullVisitor):

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
                return self.visit(llistaFills[1])
                print(Fore.WHITE + ')', end='')

            else:
                self.visit(llistaFills[0])
                print(Fore.WHITE + llistaFills[1].getText(), end='')
                self.visit(llistaFills[2])

    def visitAssigancio(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.WHITE + llistaFills[0].getText(), end='')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print("\r")

    def visitLectura(self, ctx):
        llistaFills = list(ctx.getChildren())
        print(Fore.BLUE + llistaFills[0].getText(), end='')
        print(Fore.WHITE + llistaFills[1].getText(), end='')
        self.visit(llistaFills[2])
        print(Fore.WHITE + llistaFills[3].getText(), end='')
        print("\r")

# Generated from llull.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
else:
    from llullParser import llullParser

# This class defines a complete generic visitor for a parse tree produced by llullParser.

class llullVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by llullParser#root.
    def visitRoot(self, ctx:llullParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#bloc.
    def visitBloc(self, ctx:llullParser.BlocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#instru.
    def visitInstru(self, ctx:llullParser.InstruContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#expr.
    def visitExpr(self, ctx:llullParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#condicion.
    def visitCondicion(self, ctx:llullParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#lectura.
    def visitLectura(self, ctx:llullParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#bucleWhile.
    def visitBucleWhile(self, ctx:llullParser.BucleWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#bucleFor.
    def visitBucleFor(self, ctx:llullParser.BucleForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#escriptura.
    def visitEscriptura(self, ctx:llullParser.EscripturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#assigancio.
    def visitAssigancio(self, ctx:llullParser.AssigancioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#blocStrings.
    def visitBlocStrings(self, ctx:llullParser.BlocStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#asignacionFuncion.
    def visitAsignacionFuncion(self, ctx:llullParser.AsignacionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ejecutarFuncion.
    def visitEjecutarFuncion(self, ctx:llullParser.EjecutarFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#asigParametros.
    def visitAsigParametros(self, ctx:llullParser.AsigParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ejecParametros.
    def visitEjecParametros(self, ctx:llullParser.EjecParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ifCondicion.
    def visitIfCondicion(self, ctx:llullParser.IfCondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#elseCondicion.
    def visitElseCondicion(self, ctx:llullParser.ElseCondicionContext):
        return self.visitChildren(ctx)



del llullParser
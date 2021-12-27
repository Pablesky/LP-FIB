# Generated from Expr.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#instru.
    def visitInstru(self, ctx:ExprParser.InstruContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcion.
    def visitFuncion(self, ctx:ExprParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bucle.
    def visitBucle(self, ctx:ExprParser.BucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignation.
    def visitAssignation(self, ctx:ExprParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#imprimir.
    def visitImprimir(self, ctx:ExprParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condition.
    def visitCondition(self, ctx:ExprParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifcondition.
    def visitIfcondition(self, ctx:ExprParser.IfconditionContext):
        return self.visitChildren(ctx)



del ExprParser
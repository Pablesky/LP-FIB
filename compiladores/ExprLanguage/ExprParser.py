# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3")
        buf.write("\5\3\5\3\5\3\5\6\58\n\5\r\5\16\59\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6B\n\6\3\7\3\7\3\7\5\7G\n\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\6\tQ\n\t\r\t\16\tR\3\t\3\t\3\t\2\3\6\n\2")
        buf.write("\4\6\b\n\f\16\20\2\6\3\2\24\25\3\2\4\5\3\2\6\7\3\2\r\21")
        buf.write("\2[\2\25\3\2\2\2\4 \3\2\2\2\6\"\3\2\2\2\b\63\3\2\2\2\n")
        buf.write("=\3\2\2\2\fC\3\2\2\2\16H\3\2\2\2\20L\3\2\2\2\22\24\5\4")
        buf.write("\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31\3")
        buf.write("\3\2\2\2\32!\5\b\5\2\33!\5\20\t\2\34!\5\16\b\2\35!\5\6")
        buf.write("\4\2\36!\5\n\6\2\37!\5\f\7\2 \32\3\2\2\2 \33\3\2\2\2 ")
        buf.write("\34\3\2\2\2 \35\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\5\3\2")
        buf.write("\2\2\"#\b\4\1\2#$\t\2\2\2$\60\3\2\2\2%&\f\6\2\2&\'\7\3")
        buf.write("\2\2\'/\5\6\4\6()\f\5\2\2)*\t\3\2\2*/\5\6\4\6+,\f\4\2")
        buf.write("\2,-\t\4\2\2-/\5\6\4\5.%\3\2\2\2.(\3\2\2\2.+\3\2\2\2/")
        buf.write("\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\7\3\2\2\2\62")
        buf.write("\60\3\2\2\2\63\64\7\b\2\2\64\65\5\16\b\2\65\67\7\t\2\2")
        buf.write("\668\5\4\3\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2")
        buf.write("\2\2:;\3\2\2\2;<\7\n\2\2<\t\3\2\2\2=>\7\25\2\2>A\7\13")
        buf.write("\2\2?B\5\6\4\2@B\5\16\b\2A?\3\2\2\2A@\3\2\2\2B\13\3\2")
        buf.write("\2\2CF\7\f\2\2DG\5\6\4\2EG\5\16\b\2FD\3\2\2\2FE\3\2\2")
        buf.write("\2G\r\3\2\2\2HI\5\6\4\2IJ\t\5\2\2JK\5\6\4\2K\17\3\2\2")
        buf.write("\2LM\7\22\2\2MN\5\16\b\2NP\7\23\2\2OQ\5\4\3\2PO\3\2\2")
        buf.write("\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\7\n\2\2U")
        buf.write("\21\3\2\2\2\n\25 .\609AFR")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "'while'", 
                     "'do'", "'end'", "':='", "'write'", "'='", "'<'", "'>'", 
                     "'>='", "'<='", "'if'", "'then'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "VAR", "WS" ]

    RULE_root = 0
    RULE_instru = 1
    RULE_expr = 2
    RULE_bucle = 3
    RULE_assignation = 4
    RULE_imprimir = 5
    RULE_condition = 6
    RULE_ifcondition = 7

    ruleNames =  [ "root", "instru", "expr", "bucle", "assignation", "imprimir", 
                   "condition", "ifcondition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    NUM=18
    VAR=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def instru(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstruContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstruContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__5) | (1 << ExprParser.T__9) | (1 << ExprParser.T__15) | (1 << ExprParser.NUM) | (1 << ExprParser.VAR))) != 0):
                self.state = 16
                self.instru()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bucle(self):
            return self.getTypedRuleContext(ExprParser.BucleContext,0)


        def ifcondition(self):
            return self.getTypedRuleContext(ExprParser.IfconditionContext,0)


        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def assignation(self):
            return self.getTypedRuleContext(ExprParser.AssignationContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(ExprParser.ImprimirContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_instru

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstru" ):
                return visitor.visitInstru(self)
            else:
                return visitor.visitChildren(self)




    def instru(self):

        localctx = ExprParser.InstruContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instru)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.bucle()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.ifcondition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.condition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.assignation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 29
                self.imprimir()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not(_la==ExprParser.NUM or _la==ExprParser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(ExprParser.T__0)
                        self.state = 37
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.T__1 or _la==ExprParser.T__2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.T__3 or _la==ExprParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(3)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BucleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def instru(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstruContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstruContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bucle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle" ):
                return visitor.visitBucle(self)
            else:
                return visitor.visitChildren(self)




    def bucle(self):

        localctx = ExprParser.BucleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bucle)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(ExprParser.T__5)
            self.state = 50
            self.condition()
            self.state = 51
            self.match(ExprParser.T__6)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.instru()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__5) | (1 << ExprParser.T__9) | (1 << ExprParser.T__15) | (1 << ExprParser.NUM) | (1 << ExprParser.VAR))) != 0)):
                    break

            self.state = 57
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignation" ):
                return visitor.visitAssignation(self)
            else:
                return visitor.visitChildren(self)




    def assignation(self):

        localctx = ExprParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ExprParser.VAR)
            self.state = 60
            self.match(ExprParser.T__8)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 61
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 62
                self.condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImprimirContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_imprimir

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = ExprParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ExprParser.T__9)
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 66
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 67
                self.condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ExprParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.expr(0)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__10) | (1 << ExprParser.T__11) | (1 << ExprParser.T__12) | (1 << ExprParser.T__13) | (1 << ExprParser.T__14))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 72
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfconditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def instru(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstruContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstruContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ifcondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfcondition" ):
                return visitor.visitIfcondition(self)
            else:
                return visitor.visitChildren(self)




    def ifcondition(self):

        localctx = ExprParser.IfconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifcondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ExprParser.T__15)
            self.state = 75
            self.condition()
            self.state = 76
            self.match(ExprParser.T__16)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.instru()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__5) | (1 << ExprParser.T__9) | (1 << ExprParser.T__15) | (1 << ExprParser.NUM) | (1 << ExprParser.VAR))) != 0)):
                    break

            self.state = 82
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





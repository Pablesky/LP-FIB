# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("E\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\5\3\23\n\3\3\4\3\4\3\4\3\4\3\4\7\4\32\n\4")
        buf.write("\f\4\16\4\35\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\'\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\62\n\4")
        buf.write("\f\4\16\4\65\13\4\3\5\3\5\3\5\3\5\6\5;\n\5\r\5\16\5<\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b\n\2\5\3\2\7")
        buf.write("\b\3\2\t\n\3\2\17\23\2J\2\f\3\2\2\2\4\22\3\2\2\2\6&\3")
        buf.write("\2\2\2\b\66\3\2\2\2\n@\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2")
        buf.write("\3\16\3\3\2\2\2\17\23\5\n\6\2\20\23\5\b\5\2\21\23\5\6")
        buf.write("\4\2\22\17\3\2\2\2\22\20\3\2\2\2\22\21\3\2\2\2\23\5\3")
        buf.write("\2\2\2\24\25\b\4\1\2\25\26\7\25\2\2\26\27\7\3\2\2\27\33")
        buf.write("\5\6\4\2\30\32\5\6\4\2\31\30\3\2\2\2\32\35\3\2\2\2\33")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\'\3\2\2\2\35\33\3\2\2\2\36")
        buf.write("\37\7\4\2\2\37 \5\6\4\2 !\7\5\2\2!\'\3\2\2\2\"#\7\13\2")
        buf.write("\2#\'\5\6\4\5$\'\7\25\2\2%\'\7\24\2\2&\24\3\2\2\2&\36")
        buf.write("\3\2\2\2&\"\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'\63\3\2\2\2(")
        buf.write(")\f\b\2\2)*\7\6\2\2*\62\5\6\4\b+,\f\7\2\2,-\t\2\2\2-\62")
        buf.write("\5\6\4\b./\f\6\2\2/\60\t\3\2\2\60\62\5\6\4\7\61(\3\2\2")
        buf.write("\2\61+\3\2\2\2\61.\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\7\3\2\2\2\65\63\3\2\2\2\66\67\7\f\2")
        buf.write("\2\678\5\n\6\28:\7\r\2\29;\5\6\4\2:9\3\2\2\2;<\3\2\2\2")
        buf.write("<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\16\2\2?\t\3\2\2\2@")
        buf.write("A\5\6\4\2AB\t\4\2\2BC\5\6\4\2C\13\3\2\2\2\b\22\33&\61")
        buf.write("\63<")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "')'", "'^'", "'*'", "'/'", 
                     "'+'", "'-'", "'write'", "'if'", "'then'", "'end'", 
                     "'='", "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "VAR", "WS" ]

    RULE_root = 0
    RULE_value = 1
    RULE_expr = 2
    RULE_ifcondition = 3
    RULE_conditional = 4

    ruleNames =  [ "root", "value", "expr", "ifcondition", "conditional" ]

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

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.value()
            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(ExprParser.ConditionalContext,0)


        def ifcondition(self):
            return self.getTypedRuleContext(ExprParser.IfconditionContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.conditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.ifcondition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.expr(0)
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

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

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
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 19
                self.match(ExprParser.VAR)
                self.state = 20
                self.match(ExprParser.T__0)
                self.state = 21
                self.expr(0)
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 22
                        self.expr(0) 
                    self.state = 27
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 2:
                self.state = 28
                self.match(ExprParser.T__1)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(ExprParser.T__2)
                pass

            elif la_ == 3:
                self.state = 32
                self.match(ExprParser.T__8)
                self.state = 33
                self.expr(3)
                pass

            elif la_ == 4:
                self.state = 34
                self.match(ExprParser.VAR)
                pass

            elif la_ == 5:
                self.state = 35
                self.match(ExprParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 39
                        self.match(ExprParser.T__3)
                        self.state = 40
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.T__4 or _la==ExprParser.T__5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 45
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.T__6 or _la==ExprParser.T__7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(5)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class IfconditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(ExprParser.ConditionalContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ifcondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfcondition" ):
                return visitor.visitIfcondition(self)
            else:
                return visitor.visitChildren(self)




    def ifcondition(self):

        localctx = ExprParser.IfconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifcondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ExprParser.T__9)
            self.state = 53
            self.conditional()
            self.state = 54
            self.match(ExprParser.T__10)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.expr(0)
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__1) | (1 << ExprParser.T__8) | (1 << ExprParser.NUM) | (1 << ExprParser.VAR))) != 0)):
                    break

            self.state = 60
            self.match(ExprParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = ExprParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.expr(0)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__12) | (1 << ExprParser.T__13) | (1 << ExprParser.T__14) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            self.expr(0)
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         





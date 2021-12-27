# Generated from llull.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\7\3\27\n\3\f\3\16\3\32\13")
        buf.write("\3\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5(\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\63\n\5")
        buf.write("\f\5\16\5\66\13\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\5\tH\n\t\3\t\3\t\3\t\5\t")
        buf.write("M\n\t\7\tO\n\t\f\t\16\tR\13\t\3\t\2\3\b\n\2\4\6\b\n\f")
        buf.write("\16\20\2\5\4\2\16\16\20\20\3\2\6\7\3\2\b\t\2V\2\22\3\2")
        buf.write("\2\2\4\30\3\2\2\2\6\37\3\2\2\2\b\'\3\2\2\2\n\67\3\2\2")
        buf.write("\2\f<\3\2\2\2\16A\3\2\2\2\20G\3\2\2\2\22\23\5\4\3\2\23")
        buf.write("\24\7\2\2\3\24\3\3\2\2\2\25\27\5\6\4\2\26\25\3\2\2\2\27")
        buf.write("\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32")
        buf.write("\30\3\2\2\2\33 \5\b\5\2\34 \5\16\b\2\35 \5\n\6\2\36 \5")
        buf.write("\f\7\2\37\33\3\2\2\2\37\34\3\2\2\2\37\35\3\2\2\2\37\36")
        buf.write("\3\2\2\2 \7\3\2\2\2!\"\b\5\1\2\"#\7\3\2\2#$\5\b\5\2$%")
        buf.write("\7\4\2\2%(\3\2\2\2&(\t\2\2\2\'!\3\2\2\2\'&\3\2\2\2(\64")
        buf.write("\3\2\2\2)*\f\6\2\2*+\7\5\2\2+\63\5\b\5\6,-\f\5\2\2-.\t")
        buf.write("\3\2\2.\63\5\b\5\6/\60\f\4\2\2\60\61\t\4\2\2\61\63\5\b")
        buf.write("\5\5\62)\3\2\2\2\62,\3\2\2\2\62/\3\2\2\2\63\66\3\2\2\2")
        buf.write("\64\62\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\64\3\2\2")
        buf.write("\2\678\7\n\2\289\7\3\2\29:\7\16\2\2:;\7\4\2\2;\13\3\2")
        buf.write("\2\2<=\7\13\2\2=>\7\3\2\2>?\5\20\t\2?@\7\4\2\2@\r\3\2")
        buf.write("\2\2AB\7\16\2\2BC\7\f\2\2CD\5\b\5\2D\17\3\2\2\2EH\5\b")
        buf.write("\5\2FH\7\17\2\2GE\3\2\2\2GF\3\2\2\2HP\3\2\2\2IL\7\r\2")
        buf.write("\2JM\5\b\5\2KM\7\17\2\2LJ\3\2\2\2LK\3\2\2\2MO\3\2\2\2")
        buf.write("NI\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\21\3\2\2\2R")
        buf.write("P\3\2\2\2\n\30\37\'\62\64GLP")
        return buf.getvalue()


class llullParser ( Parser ):

    grammarFileName = "llull.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'^'", "'*'", "'/'", "'+'", 
                     "'-'", "'read'", "'write'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "STRING", "NUM", "WS" ]

    RULE_root = 0
    RULE_bloc = 1
    RULE_instru = 2
    RULE_expr = 3
    RULE_lectura = 4
    RULE_escriptura = 5
    RULE_assigancio = 6
    RULE_blocStrings = 7

    ruleNames =  [ "root", "bloc", "instru", "expr", "lectura", "escriptura", 
                   "assigancio", "blocStrings" ]

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
    ID=12
    STRING=13
    NUM=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloc(self):
            return self.getTypedRuleContext(llullParser.BlocContext,0)


        def EOF(self):
            return self.getToken(llullParser.EOF, 0)

        def getRuleIndex(self):
            return llullParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = llullParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.bloc()
            self.state = 17
            self.match(llullParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instru(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llullParser.InstruContext)
            else:
                return self.getTypedRuleContext(llullParser.InstruContext,i)


        def getRuleIndex(self):
            return llullParser.RULE_bloc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloc" ):
                return visitor.visitBloc(self)
            else:
                return visitor.visitChildren(self)




    def bloc(self):

        localctx = llullParser.BlocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << llullParser.T__0) | (1 << llullParser.T__7) | (1 << llullParser.T__8) | (1 << llullParser.ID) | (1 << llullParser.NUM))) != 0):
                self.state = 19
                self.instru()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self):
            return self.getTypedRuleContext(llullParser.ExprContext,0)


        def assigancio(self):
            return self.getTypedRuleContext(llullParser.AssigancioContext,0)


        def lectura(self):
            return self.getTypedRuleContext(llullParser.LecturaContext,0)


        def escriptura(self):
            return self.getTypedRuleContext(llullParser.EscripturaContext,0)


        def getRuleIndex(self):
            return llullParser.RULE_instru

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstru" ):
                return visitor.visitInstru(self)
            else:
                return visitor.visitChildren(self)




    def instru(self):

        localctx = llullParser.InstruContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instru)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.assigancio()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.lectura()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.escriptura()
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llullParser.ExprContext)
            else:
                return self.getTypedRuleContext(llullParser.ExprContext,i)


        def NUM(self):
            return self.getToken(llullParser.NUM, 0)

        def ID(self):
            return self.getToken(llullParser.ID, 0)

        def getRuleIndex(self):
            return llullParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = llullParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [llullParser.T__0]:
                self.state = 32
                self.match(llullParser.T__0)
                self.state = 33
                self.expr(0)
                self.state = 34
                self.match(llullParser.T__1)
                pass
            elif token in [llullParser.ID, llullParser.NUM]:
                self.state = 36
                _la = self._input.LA(1)
                if not(_la==llullParser.ID or _la==llullParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = llullParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(llullParser.T__2)
                        self.state = 41
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = llullParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        _la = self._input.LA(1)
                        if not(_la==llullParser.T__3 or _la==llullParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = llullParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        _la = self._input.LA(1)
                        if not(_la==llullParser.T__5 or _la==llullParser.T__6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(3)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LecturaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(llullParser.ID, 0)

        def getRuleIndex(self):
            return llullParser.RULE_lectura

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura" ):
                return visitor.visitLectura(self)
            else:
                return visitor.visitChildren(self)




    def lectura(self):

        localctx = llullParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(llullParser.T__7)
            self.state = 54
            self.match(llullParser.T__0)
            self.state = 55
            self.match(llullParser.ID)
            self.state = 56
            self.match(llullParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscripturaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocStrings(self):
            return self.getTypedRuleContext(llullParser.BlocStringsContext,0)


        def getRuleIndex(self):
            return llullParser.RULE_escriptura

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriptura" ):
                return visitor.visitEscriptura(self)
            else:
                return visitor.visitChildren(self)




    def escriptura(self):

        localctx = llullParser.EscripturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_escriptura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(llullParser.T__8)
            self.state = 59
            self.match(llullParser.T__0)
            self.state = 60
            self.blocStrings()
            self.state = 61
            self.match(llullParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigancioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(llullParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(llullParser.ExprContext,0)


        def getRuleIndex(self):
            return llullParser.RULE_assigancio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigancio" ):
                return visitor.visitAssigancio(self)
            else:
                return visitor.visitChildren(self)




    def assigancio(self):

        localctx = llullParser.AssigancioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assigancio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(llullParser.ID)
            self.state = 64
            self.match(llullParser.T__9)
            self.state = 65
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlocStringsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llullParser.ExprContext)
            else:
                return self.getTypedRuleContext(llullParser.ExprContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(llullParser.STRING)
            else:
                return self.getToken(llullParser.STRING, i)

        def getRuleIndex(self):
            return llullParser.RULE_blocStrings

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocStrings" ):
                return visitor.visitBlocStrings(self)
            else:
                return visitor.visitChildren(self)




    def blocStrings(self):

        localctx = llullParser.BlocStringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blocStrings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [llullParser.T__0, llullParser.ID, llullParser.NUM]:
                self.state = 67
                self.expr(0)
                pass
            elif token in [llullParser.STRING]:
                self.state = 68
                self.match(llullParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==llullParser.T__10:
                self.state = 71
                self.match(llullParser.T__10)
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [llullParser.T__0, llullParser.ID, llullParser.NUM]:
                    self.state = 72
                    self.expr(0)
                    pass
                elif token in [llullParser.STRING]:
                    self.state = 73
                    self.match(llullParser.STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[3] = self.expr_sempred
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
         





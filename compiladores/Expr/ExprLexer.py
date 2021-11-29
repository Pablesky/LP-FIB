# Generated from Expr.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\6\20J\n\20\r")
        buf.write("\20\16\20K\3\21\6\21O\n\21\r\21\16\21P\3\22\6\22T\n\22")
        buf.write("\r\22\16\22U\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23\3\2\5\3\2\62;\4\2C\\c|\4\2\f\f\"\"\2[\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'")
        buf.write("\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13.\3\2\2\2\r\61\3\2\2")
        buf.write("\2\17\64\3\2\2\2\21\66\3\2\2\2\238\3\2\2\2\25:\3\2\2\2")
        buf.write("\27<\3\2\2\2\31>\3\2\2\2\33@\3\2\2\2\35B\3\2\2\2\37I\3")
        buf.write("\2\2\2!N\3\2\2\2#S\3\2\2\2%&\7?\2\2&\4\3\2\2\2\'(\7>\2")
        buf.write("\2(\6\3\2\2\2)*\7@\2\2*\b\3\2\2\2+,\7>\2\2,-\7?\2\2-\n")
        buf.write("\3\2\2\2./\7@\2\2/\60\7?\2\2\60\f\3\2\2\2\61\62\7<\2\2")
        buf.write("\62\63\7?\2\2\63\16\3\2\2\2\64\65\7*\2\2\65\20\3\2\2\2")
        buf.write("\66\67\7+\2\2\67\22\3\2\2\289\7`\2\29\24\3\2\2\2:;\7,")
        buf.write("\2\2;\26\3\2\2\2<=\7\61\2\2=\30\3\2\2\2>?\7-\2\2?\32\3")
        buf.write("\2\2\2@A\7/\2\2A\34\3\2\2\2BC\7y\2\2CD\7t\2\2DE\7k\2\2")
        buf.write("EF\7v\2\2FG\7g\2\2G\36\3\2\2\2HJ\t\2\2\2IH\3\2\2\2JK\3")
        buf.write("\2\2\2KI\3\2\2\2KL\3\2\2\2L \3\2\2\2MO\t\3\2\2NM\3\2\2")
        buf.write("\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\"\3\2\2\2RT\t\4\2\2")
        buf.write("SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\b")
        buf.write("\22\2\2X$\3\2\2\2\6\2KPU\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    NUM = 15
    VAR = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'<'", "'>'", "'<='", "'>='", "':='", "'('", "')'", "'^'", 
            "'*'", "'/'", "'+'", "'-'", "'write'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "NUM", "VAR", "WS" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



# Generated from Expr.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("p\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\6\23a\n\23\r")
        buf.write("\23\16\23b\3\24\6\24f\n\24\r\24\16\24g\3\25\6\25k\n\25")
        buf.write("\r\25\16\25l\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26\3\2\5\3\2\62;\4\2C\\c|\4\2\f\f\"\"\2")
        buf.write("r\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5-\3\2\2\2")
        buf.write("\7/\3\2\2\2\t\61\3\2\2\2\13\63\3\2\2\2\r\65\3\2\2\2\17")
        buf.write(";\3\2\2\2\21>\3\2\2\2\23B\3\2\2\2\25E\3\2\2\2\27K\3\2")
        buf.write("\2\2\31M\3\2\2\2\33O\3\2\2\2\35Q\3\2\2\2\37T\3\2\2\2!")
        buf.write("W\3\2\2\2#Z\3\2\2\2%`\3\2\2\2\'e\3\2\2\2)j\3\2\2\2+,\7")
        buf.write("`\2\2,\4\3\2\2\2-.\7,\2\2.\6\3\2\2\2/\60\7\61\2\2\60\b")
        buf.write("\3\2\2\2\61\62\7-\2\2\62\n\3\2\2\2\63\64\7/\2\2\64\f\3")
        buf.write("\2\2\2\65\66\7y\2\2\66\67\7j\2\2\678\7k\2\289\7n\2\29")
        buf.write(":\7g\2\2:\16\3\2\2\2;<\7f\2\2<=\7q\2\2=\20\3\2\2\2>?\7")
        buf.write("g\2\2?@\7p\2\2@A\7f\2\2A\22\3\2\2\2BC\7<\2\2CD\7?\2\2")
        buf.write("D\24\3\2\2\2EF\7y\2\2FG\7t\2\2GH\7k\2\2HI\7v\2\2IJ\7g")
        buf.write("\2\2J\26\3\2\2\2KL\7?\2\2L\30\3\2\2\2MN\7>\2\2N\32\3\2")
        buf.write("\2\2OP\7@\2\2P\34\3\2\2\2QR\7@\2\2RS\7?\2\2S\36\3\2\2")
        buf.write("\2TU\7>\2\2UV\7?\2\2V \3\2\2\2WX\7k\2\2XY\7h\2\2Y\"\3")
        buf.write("\2\2\2Z[\7v\2\2[\\\7j\2\2\\]\7g\2\2]^\7p\2\2^$\3\2\2\2")
        buf.write("_a\t\2\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c&\3")
        buf.write("\2\2\2df\t\3\2\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2")
        buf.write("\2h(\3\2\2\2ik\t\4\2\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2l")
        buf.write("m\3\2\2\2mn\3\2\2\2no\b\25\2\2o*\3\2\2\2\6\2bgl\3\b\2")
        buf.write("\2")
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
    T__14 = 15
    T__15 = 16
    T__16 = 17
    NUM = 18
    VAR = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'^'", "'*'", "'/'", "'+'", "'-'", "'while'", "'do'", "'end'", 
            "':='", "'write'", "'='", "'<'", "'>'", "'>='", "'<='", "'if'", 
            "'then'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "NUM", "VAR", "WS" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


